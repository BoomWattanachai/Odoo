from odoo import fields, models


class ProductUnitOfMeasure(models.Model):
    _name = "scg_product.product_unit"

    name = fields.Integer(string="Sales Unit of Measure") #required=True
    unit_of_measure = fields.Many2many('product.template',string="Unit of Measure", readonly=True)
