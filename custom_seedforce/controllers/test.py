from odoo import http
from odoo.http import request

class PartnerForm(http.Controller):
    #mention class name
    @http.route(['/customer/form'], type='http', auth="public", website=True)
    #mention a url for redirection.
    #define the type of controller which in this case is ‘http’.
    #mention the authentication to be either public or user.
    def partner_form(self, **post):
    #create method
    #this will load the form webpage
        return request.render("custom_seedforce.tmp_customer_form", {})

    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        partner = request.env['sale.order'].create({
            'partner_shipping_id': post.get('partner_shipping_id'),
            #'email': post.get('email'),
            #'phone': post.get('phone')
        })
        vals = {
            'partner': partner,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("custom_seedforce.tmp_customer_form_success", vals)
     