from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):

    @http.route('/harvest_webform', type='http', auth="public", website=True)
    def harvest_webform(self, **post):
        return "Thanks for submission"
        #return http.render('custom_seedforce.sale_order_view', {})


    @http.route('/harvest_webform/submit', type='http', auth="public", website=True)
    def sale_order(self, **post):
        #request.env['sale.order'].sudo().create(kw)
        #return request.render("custom_seedforce.harvest_success", {})

        partner = request.env['sale.order'].create({
            'partner_id': post.get('partner_id')

        })
        vals = {
            'partner': partner,
        }

        #return request.render("custom_seedforce.harvest_success", vals)
