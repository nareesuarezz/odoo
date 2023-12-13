# -*- coding: utf-8 -*-
# from odoo import http


# class Nareme(http.Controller):
#     @http.route('/nareme/nareme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nareme/nareme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nareme.listing', {
#             'root': '/nareme/nareme',
#             'objects': http.request.env['nareme.nareme'].search([]),
#         })

#     @http.route('/nareme/nareme/objects/<model("nareme.nareme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nareme.object', {
#             'object': obj
#         })
