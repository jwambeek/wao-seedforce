# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    @http.route('/website/ksh',type="http",auth="public",website=True)
    def patient_web(self,**kwargs):
        print(kwargs)

