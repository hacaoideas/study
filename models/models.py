# -*- coding: utf-8 -*-
from odoo import models, fields

class Exercise1(models.Model):
    _inherit = 'sale.order'
    type = fields.Selection(
        [('commercial','Commercial'),
         ('residential','Residential')],
        string='Type')


    def print_pdf(self):
        if self.type == 'commercial':
            return self.env.ref('study.action_sale_report_commercial').report_action(self)
        else:
            return self.env.ref('study.action_sale_report_residential').report_action(self)
