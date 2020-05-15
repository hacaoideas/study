# -*- coding: utf-8 -*-
from odoo import models, fields

class Exercise1(models.Model):
    _inherit = 'sale.order'
    type = fields.Selection(
        [('commercial','Commercial'),
         ('residential','Residential')],
        string='Type')