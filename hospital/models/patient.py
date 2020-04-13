from odoo import fields, models, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread'
    _description = "Hospital Patient"

    # name = fields.Char(string="Titlessssssssss", required=True)
    # description = fields.Text()
    # responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    # session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    
    name = fields.Char(string="Patient name",required=True,track_visibility='always')
    note = fields.Text(track_visibility='onchange')
    age = fields.Integer(required=True,default=1,track_visibility='onchange')
    gender = fields.Selection((('male','Male'),('female','Female')),required=True,track_visibility='onchange')
    age_group = fields.Char(compute='_age_group',store=True,track_visibility='onchange')
    # 1 patient 1 doctor / 1 doctor many patient
    doctor_name = fields.Many2one('hospital.doctor', ondelete='set null', string="Doctor", index=True,track_visibility='onchange')
    color = fields.Integer()

    @api.depends('age')
    def _age_group(self):
        for r in self:
            if r.age > 20 :
                r.age_group = "Major"
            else:
                r.age_group = "Minor"