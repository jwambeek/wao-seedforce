from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):
    @http.route('/shop/cart', type='http', auth="public", website=True)
    def get_data(self, **kw):
        return "world!"
