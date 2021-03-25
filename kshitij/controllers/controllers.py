# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request
import json
from odoo.addons.website_form.controllers.main import WebsiteForm
import logging

_logger  = logging.getLogger(__name__)

class SubmissionTest(WebsiteForm):
    # @http.route('/website_form', type='http', auth="public", methods=['POST'], multilang=False)
    # def website_form_empty(self, **kwargs):
    #     print(kwargs)
    #     return ""

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def website_form(self, model_name, **kwargs):
        data = {
            "x_studio_opening_balance_so":1000
        }
        request.env['sale.order'].sudo().create(data)
        return ""