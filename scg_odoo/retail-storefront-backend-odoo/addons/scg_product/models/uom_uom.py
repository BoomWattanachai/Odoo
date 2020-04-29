# -*- coding: utf-8 -*-
from odoo import fields, models, api

class UomUoM(models.Model):
    _inherit = 'uom.uom'

    uom_label = fields.Char(string='UoM Label', required=True)
    name = fields.Char(string='Unit of Measure', compute='_uom_name', store=True)

    #Product information at General information tab
    product_template_id = fields.Many2one('product.template', ondelete='set null', string="Uom2", index=True)

    @api.depends('uom_label', 'factor_inv')
    def _uom_name(self):
        self.name = self.uom_label
        for r in self:
            if r.uom_type == 'bigger' and r.factor_inv > 0:
                r.name = '%s-%.0f' % (r.uom_label, r.factor_inv)

    @api.model
    def create(self, vals):
        vals['name'] = vals['uom_label']
        if vals['uom_type'] == 'bigger' and vals['factor_inv'] > 0:
            vals['name'] = '%s-%.0f' % (vals['uom_label'], vals['factor_inv'])
        res = super(UomUoM, self).create(vals)
        return res
