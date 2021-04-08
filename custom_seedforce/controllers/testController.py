from odoo import http
from odoo.http import request

class RecentlyPurchased(http.Controller):
     @http.route('/shop/payment',website=True, auth='public')
     def index(self, **kw):
         return "Hello, world"
        #return request.render("recently_purchased.test_page" , {})




		


