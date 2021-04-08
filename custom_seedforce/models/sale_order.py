from odoo import api, fields, models

class SalesOrderLine(models.Model):
    _inherit = "sale.order.line"

    opening_balance = fields.Float(string = 'Opening Balance (MT)')
    seed_purchased = fields.Float(string = 'Seed Purchased (MT)')
    tonnes_harvested = fields.Float(string = 'Tonnes Harvested (MT)')
    qty_retained = fields.Float(string = 'Qty Retained (MT)')
    auto_deduct = fields.Float(string = 'Auto-Deduct')
    non_auto_deduct = fields.Char(string = 'Non-Auto Deduct')
    closing_balance = fields.Float(string = 'Closing Balance')
    #epr_amt_payable_excl_gst = fields.Float(string = 'Closing Balance')
