{
    'name': "study",
    'version': '1.0',
    'depends': ['base','sale'],
    'author': "Tam Nguyen",
    'category': 'Uncategorized',
    'description': """
    This is just a test
    """,
    # data files always loaded at installation
    'data': [
        'views/views.xml',
        'views/actions.xml',
        'views/templates.xml',
        'views/play_ground_template.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo.xml',
    ],
}