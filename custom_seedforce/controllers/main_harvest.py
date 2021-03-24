from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):

    @http.route('/harvest_webform', type='http', auth="public", website=True)
    def harvest_webform(self, **kw):
        #return "Thanks for submission"
        return http.request.render('custom_seedforce.sale_order_view', {})


    @http.route('/harvest_webform/submit', type='http', auth="public", website=True)
    def sale_order(self, **kw):
        #request.env['res.partner'].sudo().create(kw)
        #return request.render("custom_seedforce.harvest_success", {})

        partner = request.env['res.partner'].create({
            'name': kw.get('name')

        })
        # vals = {
        #      'partner_id': kw.get('partner_id')
        # }
        return request.render("custom_seedforce.harvest_success", partner)
        #return request.render("custom_seedforce.harvest_success", vals)
