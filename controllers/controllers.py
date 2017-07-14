# -*- coding: utf-8 -*-
from odoo import http

# class Geselle-wunsch(http.Controller):
#     @http.route('/geselle-wunsch/geselle-wunsch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/geselle-wunsch/geselle-wunsch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('geselle-wunsch.listing', {
#             'root': '/geselle-wunsch/geselle-wunsch',
#             'objects': http.request.env['geselle-wunsch.geselle-wunsch'].search([]),
#         })

#     @http.route('/geselle-wunsch/geselle-wunsch/objects/<model("geselle-wunsch.geselle-wunsch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geselle-wunsch.object', {
#             'object': obj
#         })