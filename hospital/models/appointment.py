from odoo import fields, models, api


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital Appointment"

   
    start_date_time = fields.Datetime('Date Time', default=lambda self: fields.datetime.now(),required=True)

    # @api.onchange('start_date_time')
    # def _get_end_date_time(self):
    #     for r in self:
    #         if not (r.start_date_time):
    #             r.end_date_time = r.start_date_time
    #             continue

    #         # Add duration to start_date, but: Monday + 5 days = Saturday, so
    #         # subtract one second to get on Friday instead
    #         # duration = timedelta(days=r.duration, seconds=-1)
    #         r.end_date_time = r.start_date_time

    # end_date_time = fields.Datetime('To', default=_get_end_date_time,required=True)
    # name = fields.Char(string="Doctor name",required=True)
    # age = fields.Integer(required=True,default=1)
    # gender = fields.Selection((('male','Male'),('female','Female')),required=True)
    # # 1 patient 1 doctor / 1 doctor many patient
    patient = fields.Many2one('hospital.patient', ondelete='set null', string="Patient", index=True,required=True)
    patient_code = fields.Char(string="Patient Id",compute='_patient_code')
    doctor = fields.Many2one('hospital.doctor', ondelete='set null', string="Doctor", index=True,required=True)
    doctor_code = fields.Char(string="Doctor Id",compute='_doctor_code')

    doctor_code_name = fields.Char(compute='_doctor_code_name',string="Doctor")
    patient_code_name = fields.Char(compute='_patient_code_name',string="Patient")


    # user_ref = fields.Many2one('res.users', ondelete='set null', string="User", index=True,required=True)

    # doctor_code = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='DRXXX')
    

    
    @api.onchange('patient')
    def _patient_code(self):
        for r in self:
            r.patient_code = r.patient.patient_code

    @api.onchange('doctor')
    def _doctor_code(self):
        for r in self:
            r.doctor_code = r.doctor.doctor_code

    @api.depends('doctor')
    def _doctor_code_name(self):
        for r in self:
            r.doctor_code_name = r.doctor.doctor_code + ':' + r.doctor.name

    @api.depends('patient')
    def _patient_code_name(self):
        for r in self:
            r.patient_code_name = r.patient.patient_code + ':' + r.patient.name