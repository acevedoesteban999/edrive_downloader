# Módulo`edrive_downloader`

## `Odoo`:`18`

## Readme Tradução

-   [Inglês](README.md)
-   [Espanhol](README.es.md)
-   [Português](README.pt.md)
-   [Francês](README.fr.md)

## Propósito

Este modelo permite downloads de arquivos do Google Drive ou URLs públicos.

## Funcionalidade

Para integração do Google Drive, você precisa de uma conta de serviço com as credenciais JSON. Se você não sabe como obtê -los:[Siga este guia para obter as credenciais JSON](https://developers.google.com/workspace/guides/create-credentials)

Depois de ter o JSON, crie um parâmetro do sistema:

> `service.account.credential.json`Contendo suas credenciais JSON Conteúdo.

## Exemplos de uso

### 1. Download do Google Drive

```python
# Initialize the service
drive_service = self.env['service.account']._initialize_drive_service()

# Download file by URL
file_url = 'your_google_drive_file_url'
base64_data, filename, mimetype = self.env['service.account'].download_file_from_url(file_url,drive_service)
```

### 2. Download do URL público

```python
url = 'https://example.com/file.pdf'
base64_data, filename, mimetype = self.env['service.account'].download_file_from_url(url)
```

## Notas importantes

-   Para unidades particulares, é necessário incluir a conta de serviço como leitor no arquivo.

-   A conta de serviço exige<https://www.googleapis.com/auth/drive.readonly>escopo

-   Todos os métodos retornam uma tupla de (base64_data, nome do arquivo, mimetype)

-   Methods raise UserError on failure with descriptive messages
