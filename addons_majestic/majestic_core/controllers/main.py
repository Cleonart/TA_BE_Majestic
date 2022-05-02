# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.api import call_kw
from odoo.models import check_method_name


class ControllerMain(http.Controller):
    '''User Authentication API'''

    @http.route(['/api/v1/model/<string:model_name>/search_read'],
                method=['POST'], cors='*', csrf=False, csrf_token=False, type='json', auth='public')
    def core_read_api(self, model_name, **kwargs):

        # Parameter pass from xmlrpc
        domain = kwargs.get('domain') or []
        offset = kwargs.get('offset') or 0
        limit = kwargs.get('limit') or None
        fields = kwargs.get('fields') or []

        # Do a search read to data
        model = request.env[model_name].sudo().search(
            domain, offset=offset, limit=limit)

        # Return the data
        return {
            'length': len(model.read()),
            'records': model.read(fields),
            'status': 'success',
            'msg': 'API Called Successfully'
        }

    def _call_kw(self, model, method, args, kwargs):
        check_method_name(method)
        return call_kw(request.env[model], method, args, kwargs)

    @http.route(['/api/v1/model/<string:model>/<string:method>'],
                cors='*', csrf=False, csrf_token=False, type='json', auth='public')
    def call_kw(self, model, method, *args, **kwargs):
        request.session.authenticate('TA_BE_MAJESTIC', 'admin', 'admin')
        return self._call_kw(model, method, *args, **kwargs)
