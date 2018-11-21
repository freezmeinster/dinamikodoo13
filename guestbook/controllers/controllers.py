# -*- coding: utf-8 -*-
from odoo import http

# class Guestbook(http.Controller):
#     @http.route('/guestbook/guestbook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/guestbook/guestbook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('guestbook.listing', {
#             'root': '/guestbook/guestbook',
#             'objects': http.request.env['guestbook.guestbook'].search([]),
#         })

#     @http.route('/guestbook/guestbook/objects/<model("guestbook.guestbook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('guestbook.object', {
#             'object': obj
#         })