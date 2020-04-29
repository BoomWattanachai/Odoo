# -*- coding: utf-8 -*-
{
    'name': "scg_product_information",

    'summary': """
        Product Information""",

    'description': """
        scg product information
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'product information',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product',],

    # always loaded
    'data': [
        "views/product_information_view.xml",

    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}
