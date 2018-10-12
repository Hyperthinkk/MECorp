# -*- coding: utf-8 -*-

from odoo import SUPERUSER_ID, api,fields, models, _
        
class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    picking_code = fields.Selection('stock.picking.type', related='picking_type_id.code', string='Code')

    @api.multi
    def print_deliveryorder(self, data):
        return self.env['report'].get_action(self, 'delivery_note_report.deliverynotereport')

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    net_weight = fields.Float(string='Net Weight')

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def print_invoiceyorder(self, data):
        return self.env['report'].get_action(self, 'delivery_note_report.invoicereportview')