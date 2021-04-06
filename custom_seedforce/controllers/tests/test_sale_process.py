import odoo.tests

from odoo import api
from odoo.addons.base.tests.common import HttpCaseWithUserDemo, TransactionCaseWithUserDemo
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website.tools import MockRequest



@odoo.tests.tagged('post_install', '-at_install')
class TestWebsiteSaleCheckoutAddress(TransactionCaseWithUserDemo):
    ''' The goal of this method class is to test the address management on
        the checkout (new/edit billing/shipping, company_id, website_id..).
    '''

    def _create_so(self, partner_id=None):
        return self.env['sale.order'].create({
            'partner_id': partner_id,
            'website_id': self.website.id,
            'order_line': [(0, 0, {
                'product_id': self.env['product.product'].create({'name': 'Product A', 'list_price': 200}).id,
                'name': 'Product A',
            })]
        })
