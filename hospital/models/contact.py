from odoo import fields, models

class Contact(models.Model):
    _inherit = 'res.partner'

    
    # instructor = fields.Boolean("Instructor", default=False)

    # session_ids = fields.Many2many('openacademy.session',
    #     string="Attended Sessions", readonly=True)

    patient = fields.Many2one('hospital.patient', ondelete='set null', string="Patient")
    # instructor = fields.Boolean("Instructor", default=False)