{
    'name': 'edrive_downloader',
    'version': '0.1',
    'summary': '',
    'description': """
        
    """,
    'author': """acevedoesteban999@gmail.com""",
    'depends': [],
    
    'data': [
        'data/credential.xml',
    ],
    
    'external_dependencies': {
        'python': [
            'requests',
            'google-api-python-client',
            'google-auth',
            'google-auth-oauthlib',
            'google-auth-httplib2'
        ]
    },

    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
