from odoo import fields, models, api


class ProductInformation(models.Model):
    _inherit = 'product.template'

    # General Information Tab
    retail_price = fields.Float(string="Retail Price",readonly=True)
    wholesales_price = fields.Float(string="Wholesales Price",readonly=True)
    item_category = name = fields.Char(string="Item Category", readonly=True)

    # Unit of Measures Tab
    @api.model
    def _default_sales_unit_of_measure(self):
        return self.env['uom.uom'].search([], limit=1)
    sales_unit_of_measure = fields.Many2one('uom.uom', ondelete='set null', 
                                            string="Sales Unit of Measure", required=True, 
                                            default=_default_sales_unit_of_measure,
                                            readonly=True, defauel="xxx", index=True)#,required=True,readonly=True


    uom = fields.One2many('uom.uom','product_information', ondelete='set null', string="UoM",readonly=True)
    
    # Sales Tab
    thai_discription = fields.Text(default='C1302 ซิดนีย์45 พร้อมฝา C91005 (Test)',readonly=True)
    eng_product_name = fields.Text(default='C1302 ซิดนีย์45 พร้อมฝา C91005 (Test)',readonly=True)
    eng_discription = fields.Text(default='C1302 ซิดนีย์45 พร้อมฝา C91005 (Test)',readonly=True)
