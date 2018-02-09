# -*- coding: utf-8 -*-

from openerp import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_delivery_methods(self, order):

        available_carrier_ids = super(
            SaleOrder, self)._get_delivery_methods(order)
        carrier = order._get_delivery_carrier_id()

        if carrier and carrier.id in available_carrier_ids:
            return [carrier.id]
        return []
