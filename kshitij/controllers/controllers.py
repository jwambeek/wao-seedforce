# -*- coding: utf-8 -*-
# from odoo import http


# class Kshitij(http.Controller):
#     @http.route('/kshitij/kshitij/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kshitij/kshitij/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kshitij.listing', {
#             'root': '/kshitij/kshitij',
#             'objects': http.request.env['kshitij.kshitij'].search([]),
#         })

#     @http.route('/kshitij/kshitij/objects/<model("kshitij.kshitij"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kshitij.object', {
#             'object': obj
#         })
