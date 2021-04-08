from odoo import http
from odoo.http import request

class GetData(http.Controller):
     @http.route('/shop/address', type='http', website=True, auth='public')
     def index(self, **kw):
         return "Hello, world"
       




		


