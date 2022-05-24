# -*- coding: utf-8 -*-

from odoo.addons.web.controllers.main import Home
from odoo import http


class HomeWithCors(Home):
   
    @http.route('/web/login', type='http', auth="none", cors='*')
    def web_login(self, redirect=None, **kw):
        return super().web_login(redirect=redirect, **kw)
