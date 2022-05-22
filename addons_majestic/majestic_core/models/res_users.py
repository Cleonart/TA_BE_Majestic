# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def do_login(self, payload: dict={}) -> None:
        username: str = payload.get('login')
        password: str = payload.get('password')

        access: models.Model = self.search([
            ('login', '=', username),
            ('password', '=', password),
        ], limit=1)

        if not access:
            msg: str = 'Username atau password salah'
            raise ValidationError(msg)
        
        return True