# -*- coding: utf-8 -*-
{
    'name': "Guest Book",
    'summary': """
        Guest Book Apps""",

    'description': """
        Guest Book apps for Dinamik 13 Event
    """,
    'author': "Bramandityo Prabowo",
    'website': "https://blog.armsolusi.com/author/bram/",
    'category': 'Uncategorized',
    'version': '0.9',
    'depends': ['base'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'data/programing_language.xml',
    ],
}