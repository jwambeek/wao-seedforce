from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):

    @http.route('/harvest_webform', type='http', auth="public", website=True)
    def harvest_webform(self, **kw):
        return http.render('custom_seedforce.sale_order_view', {})


    @http.route('/harvest_webform/submit', type='http', auth="public", website=True)
    def sale_order(self, **kw):
        request.env['sale.order'].sudo().create(kw)
        return request.render("custom_seedforce.harvest_success", {})
