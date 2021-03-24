# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm


class Hospital(WebsiteForm):
    @http.route('/website_form', type='http', auth="public", methods=['POST'], multilang=False)
    def website_form_empty(self, **kwargs):
        return ""
