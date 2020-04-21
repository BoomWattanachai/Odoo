from odoo import fields, models, api


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'


    start_date_time = fields.Datetime('Date Time', default=lambda self: fields.datetime.now(),required=True)

    def _default_patient_name(self):
        return self.env['hospital.patient'].browse(self._context.get('active_id'))

    
    doctor = fields.Many2one('hospital.doctor', ondelete='set null', string="Doctor", index=True,required=True)
    doctor_code = fields.Char(string="Doctor Id",compute='_doctor_code')
    doctor_code_name = fields.Char(compute='_doctor_code_name')

    
    patient = fields.Many2one('hospital.patient', ondelete='set null', string="Patient", index=True,required=True
                                ,default=_default_patient_name,readonly=True)
    patient_code = fields.Char(string="Patient Id",compute='_patient_code')
    patient_code_name = fields.Char(compute='_patient_code_name')
    
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

    @api.multi
    def create_appointment(self):
        vals = {
            'start_date_time': self.start_date_time,
            'doctor': self.doctor.id,
            'doctor_code': self.doctor_code,
            'doctor_code_name': self.doctor_code_name,
            'patient': self.patient.id,
            'patient_code': self.patient_code,
            'patient_code_name': self.patient_code_name
        }
        self.env['hospital.appointment'].create(vals)
