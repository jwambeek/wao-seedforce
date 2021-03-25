# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo import fields
from odoo.http import request
import json
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging

_logger  = logging.getLogger(__name__)

class WebsiteFormTest(WebsiteForm):
    # @http.route('/website_form', type='http', auth="public", methods=['POST'], multilang=False)
    # def website_form_empty(self, **kwargs):
    #     print(kwargs)
    #     return ""

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def website_form(self, model_name, **kwargs):
        data = {
            "x_studio_opening_balance_so":1000,

        }
        request.env['sale.order'].sudo().create(data)
        # sale.order ki sari required values chahiyae
        return ""

class WebsiteSaleTest(WebsiteSale):
    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        _logger.debug(kw)
        _logger.info(kw)

    @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart_hook(self,**post):
        _logger.info("=================================================")
        res_super=super(WebsiteSaleTest, self).cart(post)
        _logger.debug(res_super)
        _logger.info("--------------------------------------")
        _logger.info(self,post)
        return res_super
        _logger.info("================================")
