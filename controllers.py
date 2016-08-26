# -*- coding: utf-8 -*-
from openerp import http

# class Instalador(http.Controller):
#     @http.route('/instalador/instalador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instalador/instalador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('instalador.listing', {
#             'root': '/instalador/instalador',
#             'objects': http.request.env['instalador.instalador'].search([]),
#         })

#     @http.route('/instalador/instalador/objects/<model("instalador.instalador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instalador.object', {
#             'object': obj
#         })