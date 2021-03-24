from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):

    @http.route('/harvest_webform', type='http', auth="public", website=True)
    def harvest_webform(self, **kw):
        #return "Thanks for submission"
        return http.request.render('custom_seedforce.sale_order_view', {})


    @http.route('/harvest_webform/submit', type='http', auth="public", website=True)
    def sale_order(self, **post):
        #request.env['res.partner'].sudo().create(kw)
        #return request.render("custom_seedforce.harvest_success", {})

        partner = request.env['res.partner'].create({
            'name': post.get('name')

        })
        vals = {
             'partner': partner
        }
        #return request.render("custom_seedforce.harvest_success", {})
        return request.render("custom_seedforce.harvest_success", vals)
