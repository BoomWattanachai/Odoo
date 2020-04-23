from odoo import fields, models


class Product(models.Model):
    _inherit = 'product.template'

    retail_price = fields.Float(string="Retail Price",readonly=True)
    wholesales_price = fields.Float(string="Wholesales Price",readonly=True)
    cost_price = fields.Float(string="Cost Price",readonly=True)
    sales_unit_of_measure = fields.Integer(string="Sales Unit of Measure")
    # instructor = fields.Boolean(default=False,string="InstructorAAAA")

    # session_ids = fields.Many2many('openacademy.session',
    #     string="Attended Sessions", readonly=True)

    # patient = fields.Many2one('hospital.patient', ondelete='set null', string="Patient")
    # instructor = fields.Boolean("Instructor", default=False)
