from odoo import fields, models


class Product(models.Model):
    # _name = 'inheritmodule.product'
    _inherit = 'product.template'

    # General Information Tab
    retail_price = fields.Float(string="Retail Price",readonly=True)
    wholesales_price = fields.Float(string="Wholesales Price",readonly=True)
    cost_price = fields.Float(string="Cost Price",readonly=True)

    # Unit of Measures Tab
    sales_unit_of_measure = fields.Integer(string="Sales Unit of Measure") #required=True
    
    # Sales Tab
    thai_discription = fields.Text(default='C1302 ซิดนีย์45 พร้อมฝา C91005 (Test)',readonly=True)
    eng_product_name = fields.Text(default='C1302 ซิดนีย์45 พร้อมฝา C91005 (Test)',readonly=True)
    eng_discription = fields.Text(default='C1302 ซิดนีย์45 พร้อมฝา C91005 (Test)',readonly=True)
    