from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):
    @http.route('/shop/payment',website=True, auth='public')
    def get_data(self, **kw):
        return "Hello, world!"
