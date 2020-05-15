# -*- coding: utf-8 -*-
from odoo import models, fields

class SalesOrderInherited(models.Model):
    _inherit = 'sale.order'
    type = fields.Selection(
        [('commercial','Commercial'),
         ('residential','Residential')],
        string='Type')