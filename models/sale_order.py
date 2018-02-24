# -*- coding: utf-8 -*-

from openerp import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_delivery_methods(self, order):
        sql = ("SELECT id"
               " FROM delivery_carrier"
               " WHERE website_published=true"
               " AND zip_from <= '" + order.partner_shipping_id.zip +
               "' AND zip_to >= '" + order.partner_shipping_id.zip + "'")
        self.env.cr.execute(sql)

        delivery_carriers_ids = [dc[0] for dc in self.env.cr.fetchall() if dc]

        carrier = order._get_delivery_carrier_id(
            delivery_carriers_ids)
        if carrier and carrier.id:
            return [carrier.id]
        return []
