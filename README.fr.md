# Module`edrive_downloader`

## `Odoo`:`18`

## Traduction de réadme

-   [Anglais](README.md)
-   [Espagnol](README.es.md)
-   [portugais](README.pt.md)
-   [Français](README.fr.md)

## But

Ce modèle permet les téléchargements de fichiers depuis Google Drive ou URL publics.

## Fonctionnalité

Pour l'intégration Google Drive, vous avez besoin d'un compte de service avec JSON Identials. Si vous ne savez pas comment les obtenir:[Suivez ce guide pour obtenir les informations d'identification JSON](https://developers.google.com/workspace/guides/create-credentials)

Une fois que vous avez le JSON, créez un paramètre système:

> `service.account.credential.json`Contenant votre contenu JSON d'identification.

## Usage Examples

### 1. Télécharger depuis Google Drive

```python
# Initialize the service
drive_service = self.env['service.account']._initialize_drive_service()

# Download file by URL
file_url = 'your_google_drive_file_url'
base64_data, filename, mimetype = self.env['service.account'].download_file_from_url(file_url,drive_service)
```

### 2. Télécharger à partir de l'URL publique

```python
url = 'https://example.com/file.pdf'
base64_data, filename, mimetype = self.env['service.account'].download_file_from_url(url)
```

## Notes importantes

-   Pour les disques privés, il est nécessaire d'inclure le compte de service en tant que lecteur dans le fichier.

-   Le compte de service nécessite<https://www.googleapis.com/auth/drive.readonly>portée

-   Toutes les méthodes renvoient un tuple de (base64_data, nom de fichier, mimetype)

-   Les méthodes augmentent la doctorat de l'utilisateur en échec avec des messages descriptifs
