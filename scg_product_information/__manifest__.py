# -*- coding: utf-8 -*-
{
    'name': "Product Information",

    'summary': """
        Product Information""",

    'description': """
        Manage product, ...
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ProductInformation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['base','product'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/product_information_view.xml",
        "views/product_unit_of_measure_view.xml",
        "views/menu_item.xml",
        
    ],
    # only loaded in demonstration mode
    'demo': [],
}


