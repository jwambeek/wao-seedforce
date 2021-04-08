from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):
    @http.route('/shop/payment',website=True, auth='public')
    def get_data(self, **kw):
        return "Hello, world"
        #return request.render("recently_purchased.test_page" , {})




        




  #  @http.route('/harvest_webform', type='http', auth="public", website=True)
   # def harvest_webform(self, **kw):
        #return "Thanks for submission"
      #  return http.request.render('custom_seedforce.sale_order_view', {})


   # @http.route('/harvest_webform/submit', type='http', auth="public", website=True)
   # def sale_order(self, **kw):
    #    request.env['res.partner'].sudo().create(kw)
        #return request.render("custom_seedforce.harvest_success", {})

        # partner = request.env['res.partner'].create({
        #     'partner_id': kw.get('partner_id')

        # })
        # vals = {
        #      'partner_id': kw.get('partner_id')
        # }
     #   return request.render("custom_seedforce.harvest_success", {})
        #return request.render("custom_seedforce.harvest_success", vals)
