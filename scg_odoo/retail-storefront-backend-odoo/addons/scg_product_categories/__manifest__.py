# -*- coding: utf-8 -*-
{
    'name': "scg_product_categories",

    'summary': """
        Product Categories""",

    'description': """
        scg product categories
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product',],

    # always loaded
    'data': [
        "views/product_categories_view.xml",

    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}
