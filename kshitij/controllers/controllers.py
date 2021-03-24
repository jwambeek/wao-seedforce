# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm

def ksh(t):
    print("Khs")

class SubmissionTest(WebsiteForm):
    @http.route('/website_form', type='http', auth="public", methods=['POST'], multilang=False)
    def website_form_empty(self, **kwargs):
        print(kwargs)
        return ksh("noting")

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def website_form(self, model_name, **kwargs):
        print(kwargs)
        return ksh("kshitij")