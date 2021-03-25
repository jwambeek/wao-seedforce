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
        print(kwargs)
        _logger.info("kshitij ",kwargs,self)
        _logger.debug("kshitij ",kwargs,self)
        return ""