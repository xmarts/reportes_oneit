# -*- coding: utf-8 -*-
from odoo import http

# class ReportOne(http.Controller):
#     @http.route('/report_one/report_one/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_one/report_one/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_one.listing', {
#             'root': '/report_one/report_one',
#             'objects': http.request.env['report_one.report_one'].search([]),
#         })

#     @http.route('/report_one/report_one/objects/<model("report_one.report_one"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_one.object', {
#             'object': obj
#         })