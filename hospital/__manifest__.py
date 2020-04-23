# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Hospital""",

    'description': """
        Manage patient, ...
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hospital',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],
    # 'depends': ['base','mail','uom','product'],

    # always loaded
    'data': [
        'security/security.xml',
        "security/ir.model.access.csv",
        "wizards/create_appointment_view_wizards.xml",
        # "views/course_view.xml",
        # "views/session_view.xml",
        "views/patient_view.xml",
        "views/doctor_view.xml",
        "views/appointment_view.xml",
        "views/contact_view.xml",
        # "views/product_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
}
