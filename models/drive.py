import base64
import json
import requests
import io
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import mimetypes
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

class Drive(models.AbstractModel):
    _name = "service.account"
    _description = "Download service for Google Drive"
    
    @api.model
    def _initialize_drive_service(self):
        """Initialize Google Drive service with service account."""
        config = self.env['ir.config_parameter'].sudo()
        service_account_info = config.get_param('service.account.credential.json')

        if not service_account_info:
            raise UserError(_("The service account JSON needs to be configured in System Parameters. (service.account.credential.json)."))

        try:
            credentials = json.loads(service_account_info)
            creds = service_account.Credentials.from_service_account_info(
                credentials,
                scopes=['https://www.googleapis.com/auth/drive.readonly']
            )
            service = build('drive', 'v3', credentials=creds)
            return service
        except Exception as e:
            raise UserError(f"Could not initialize Google Drive: {str(e)}")

    def download_public_file_from_url(self,url):
        def _get_filename(response:requests.Response,url:str):
            filename = None
            try:
                content_disposition = response.headers.get('Content-Disposition')
                if content_disposition:
                    parts = content_disposition.split('filename=')
                    if len(parts) > 1:
                        filename = parts[1].strip('"\'')  
                
                if not filename:
                    filename = url.split('/')[-1].split('?')[0]
            except:
                return filename
        try:
            response = requests.get(url, timeout=1)
            response.raise_for_status()
            mimetype = response.headers.get('Content-Type')
            if not mimetype:
                mimetype = mimetypes.guess_type(url)[0] or 'application/octet-stream'
            filename = _get_filename(response,url)
            base64_data = base64.b64encode(response.content)
            return (base64_data,filename,mimetype)
        except:
            raise UserError(_("Invalid URL."))

    @api.model
    def download_file_from_drive(self, file_id , drive_service = None):
        """Download a file from Drive using its ID and return it as base64.
        
        Args:
            file_id (str): File ID in Google Drive.
            
        Returns:
            tuple: (base64_data, mimetype) or None if there's an error.
        """
        try:
            if not drive_service:
                drive_service = self._initialize_drive_service()
            
            # Get metadata for MIME type
            file_metadata = drive_service.files().get(
                fileId=file_id,
                fields='mimeType'
            ).execute()
            mimetype = file_metadata.get('mimeType', 'application/octet-stream')

            # Download content
            request = drive_service.files().get_media(fileId=file_id)
            file_stream = io.BytesIO()
            downloader = MediaIoBaseDownload(file_stream, request)
            
            done = False
            while not done:
                _, done = downloader.next_chunk()

            file_stream.seek(0)
            base64_data = base64.b64encode(file_stream.read())
            return (base64_data,False, mimetype)

        except Exception as e:
            raise UserError(f"Error downloading file: {str(e)}")

    @api.model
    def download_file_from_url(self, url,drive_service = None):
        """Download an image from a Drive URL."""
        drive_file_id = self._check_drive_and_extract_file_id_from_url(url)
        if not drive_file_id:
            return self.download_public_file_from_url(url)
        return self.download_file_from_drive(drive_file_id,drive_service)

    def _check_drive_and_extract_file_id_from_url(self, url):
        """Extract file ID from a Drive URL."""
        patterns = [
            r'/file/d/([^/]+)',
            r'id=([^&]+)',
            r'/([^/]+)/view',
            r'/([^/]+)/edit'
        ]
        import re
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None