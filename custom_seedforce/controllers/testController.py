import logging
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale 


_logger = logging.getLogger(__name__)


class WebsiteSaleData(WebsiteSale):
     @http.route(['/shop/payment'], type='http', auth="public", website=True, sitemap=False)
     def payment(self, **post):
      res = super(WebsiteSaleData,self).payment(**post)
      _logger.info("Test String")
      return "testTheMethod"
      #return "Odoo"
      #return request.render("custom_seedforce.get_data_form" , {})

#class GetData(http.Controller):
 #    @http.route('/shop/payment', type='http', website=True, auth='public')
  #   def index(self, **kw):
         #return "Hello, world"
   #     return request.render("custom_seedforce.get_data_form" , {})
