# -*- coding: utf-8 -*-
{
    'name': "Inherit",

    'summary': """
        Inherit""",

    'description': """
        Manage patient, ...
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inherit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['base','product'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/menu_item.xml",
        "views/product_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
}
