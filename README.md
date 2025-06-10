# Module `edrive_downloader`
## `Odoo`: `18`

## README Translation
- [English](README.md)
- [Spanish](README.es.md)
- [Portuguese](README.pt.md)
- [French](README.fr.md)

## Purpose

This model enables file downloads from Google Drive or public URLs.

## Functionality

For Google Drive integration, you need a service account with JSON credentials. If you don't know how to obtain these:
[Follow this guide to get the JSON credentials](https://developers.google.com/workspace/guides/create-credentials)

Once you have the JSON, create a system parameter:
> - `service.account.credential.json`
Containing your credentials JSON content.


## Usage Examples

### 1. Download from Google Drive
```python
# Initialize the service
drive_service = self.env['service.account']._initialize_drive_service()

# Download file by URL
file_url = 'your_google_drive_file_url'
base64_data, mimetype = self.env['service.account'].download_file_from_url(file_url,drive_service)
```

### 2. Download from Public URL
```python
url = 'https://example.com/file.pdf'
base64_data, mimetype = self.env['service.account'].download_file_from_url(url)
```
## Important Notes
- For private drives, it is necessary to include the service account as a reader to the file.

- The service account requires https://www.googleapis.com/auth/drive.readonly scope

- All methods return a tuple of (base64_data, mimetype)

- Methods raise UserError on failure with descriptive messages

