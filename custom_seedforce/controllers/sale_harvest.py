from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class Sale(http.Controller):

    @http.route('/my_sale_details', type='http', auth='public', website=True)
    def sale_details(self , **kwargs):
        sale_details = request.env['sale.order'].sudo().search([])
        return  request.render('custom_seedforce.sale_details_page', {'my_details': sale_details})

        return request.redirect('/my_filtered_orders')

