# -*- coding: utf-8 -*-
from odoo import models, fields

class Exercise1(models.Model):
    _inherit = 'sale.order'
    type = fields.Selection(
        [('commercial','Commercial'),
         ('residential','Residential')],
        string='Type')

    def print_pdf(self):
        return self.env.ref('sale.action_report_saleorder').report_action(self)