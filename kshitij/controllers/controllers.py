from odoo import http
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging

_logger = logging.getLogger(__name__)

class WebsiteFormTest(WebsiteForm):
    # @http.route('/website_form', type='http', auth="public", methods=['POST'], multilang=False)
    # def website_form_empty(self, **kwargs):
    #     print(kwargs)
    #     return ""

    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def website_form(self, model_name, **kwargs):
        super_website = super(WebsiteFormTest,self).website_form("res.partner",**kwargs)
        
        _logger.info(kwargs)
        return super_website

class WebsiteSaleTest(WebsiteSale):
    @http.route()
    def checkout(self, **post):
        sup=super(WebsiteSaleTest,self).checkout(**post)
        _logger.info("==========")
        _logger.info(post)
        _logger.info(sup)
        _logger.info("==============================")
        return sup

    @http.route()
    def cart(self):
        res_super=super(WebsiteSaleTest, self).cart()
        return res_super

    @http.route()
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        updated_cart = super(WebsiteSaleTest,self).cart_update_json(product_id, line_id, add_qty, set_qty)
        _logger.info(product_id,line_id,add_qty,set_qty)
        return updated_cart

    @http.route()
    def confirm_order(self, **post):
        confirm_order_hook = super(WebsiteSaleTest,self).confirm_order(**post)
        
        return confirm_order_hook
