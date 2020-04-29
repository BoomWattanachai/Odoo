from odoo import fields, models


class ProductUnitOfMeasure(models.Model):
    _inherit = "uom.uom"

    product_uom = fields.Many2one('uom.uom', string='Product UoM', index=True)
    # bigger_ration = fields.Float(string="Bigger Ration",default=1.00)

    product_information = fields.Many2one('product.template', ondelete='set null', string="Uom2", index=True)