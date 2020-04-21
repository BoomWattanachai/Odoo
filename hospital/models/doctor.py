from odoo import fields, models, api


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Hospital Doctor"

   
    
    name = fields.Char(string="Doctor name",required=True)
    age = fields.Integer(required=True,default=1)
    gender = fields.Selection((('male','Male'),('female','Female')),required=True)
    # 1 patient 1 doctor / 1 doctor many patient
    patient_name = fields.One2many('hospital.patient', 'doctor_name', ondelete='set null', string="Sessions")
    user_ref = fields.Many2one('res.users', ondelete='set null', string="User", index=True,required=True)

    doctor_code = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='DRXXX')

    @api.model
    def create(self, vals):
        vals['doctor_code'] = self.env['ir.sequence'].next_by_code(
                'hospital.doctor') or '/'
        result = super(Doctor, self).create(vals)
        return result



      