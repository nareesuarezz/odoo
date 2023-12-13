# -*- coding: utf-8 -*-
{
    'name': "nareme",

    'summary': """
        Módulo de fin de curso de nareme""",

    'description': """
        Módulo de apoyo a una empresa de desarrollo de software, donde empresas crean proyectos, con tareas
    """,

    'author': "Nareme",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/project_tags_data.xml',
        'reports/projects_report.xml',
        'reports/projects_report_view.xml',    
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': 'True',

    # assets
    'assets': {
        'web.assets_common': [
            'nareme/static/src/scss/style1.scss'
        ],

    }
}
