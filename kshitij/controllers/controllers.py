# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    @http.route('/website_form',type="http",auth="public",website=True)
    def website_form_empty(self, **kwargs):
        print(kwargs)

