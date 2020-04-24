from odoo import fields, models


    

class Notebook(models.Model):
    _name = 'inheritmodule.notebook'

    # Unit of Measures Tab
    product_uom = fields.Char(string="Product UoM")
    bigger_ration = fields.Float(string="Bigger Ration",default=1.0)

    # product_ids = fields.One2many('inheritmodule.product', 'unit_of_measures', string="Unit of Measures")
    # unit_of_measures = fields.Many2one('inheritmodule.product', ondelete='cascade', string="Unit of Measures")
    