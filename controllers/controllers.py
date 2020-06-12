# -*- coding: utf-8 -*-
from odoo import http, api


class Study(http.Controller):
    @http.route("/report/sales/", auth='user')
    def print_sales_order(self):
        res= http.request.env['sale.order']
        sales_orders = res.search([])
        return http.request.render(
            'study.play_ground_template', {'sales':sales_orders}
        )

