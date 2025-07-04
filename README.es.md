# Módulo`edrive_downloader`

## `Odoo`:`18`

## Traducción de lectura

-   [Inglés](README.md)
-   [Español](README.es.md)
-   [portugués](README.pt.md)
-   [Francés](README.fr.md)

## Objetivo

Este modelo habilita las descargas de archivos de Google Drive o URL públicas.

## Funcionalidad

Para la integración de Google Drive, necesita una cuenta de servicio con credenciales JSON. Si no sabe cómo obtener estos:[Siga esta guía para obtener las credenciales JSON](https://developers.google.com/workspace/guides/create-credentials)

Una vez que tenga el JSON, cree un parámetro del sistema:

> `service.account.credential.json`Que contiene sus credenciales JSON Content.

## Ejemplos de uso

### 1. Descargar desde Google Drive

```python
# Initialize the service
drive_service = self.env['service.account']._initialize_drive_service()

# Download file by URL
file_url = 'your_google_drive_file_url'
base64_data, filename, mimetype = self.env['service.account'].download_file_from_url(file_url,drive_service)
```

### 2. Descargar desde URL pública

```python
url = 'https://example.com/file.pdf'
base64_data, filename, mimetype = self.env['service.account'].download_file_from_url(url)
```

## Notas importantes

-   Para unidades privadas, es necesario incluir la cuenta de servicio como lector del archivo.

-   La cuenta de servicio requiere<https://www.googleapis.com/auth/drive.readonly>alcance

-   Todos los métodos devuelven una tupla de (base64_data, nombre de archivo, mimetype)

-   Los métodos elevan el usuario de User en falla con mensajes descriptivos
