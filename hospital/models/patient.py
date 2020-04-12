from odoo import fields, models, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patient"

    # name = fields.Char(string="Titlessssssssss", required=True)
    # description = fields.Text()
    # responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    # session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    
    name = fields.Char(string="Patient name",required=True)
    note = fields.Text()
    age = fields.Integer(required=True,default=1)
    gender = fields.Selection((('male','Male'),('female','Female')),required=True)
    # gender = fields.selection(('male','Male'),('female','Female'))
    age_group = fields.Char(compute='_age_group',store=True)
    # age(int)
    # age_group(char) display major when age > 20 other display minor
    # gender(selector)

    @api.depends('age')
    def _age_group(self):
        for r in self:
            if r.age > 20 :
                r.age_group = "Major"
            else:
                r.age_group = "Minor"