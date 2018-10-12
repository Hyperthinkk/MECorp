# -*- coding: utf-8 -*-
from odoo import api, fields, models

class DeliveryNoteTemplate(models.AbstractModel):
    _name = 'report.delivery_note_report.deliverynotereport'


    def get_invoice_address(self,obj):
        picking_obj = self.env['stock.picking']
        if obj:
            picking_id = picking_obj.browse(obj)
            if picking_id:
                origin = picking_id.origin
                sale_id = self.env['sale.order'].search([('name','=',origin)])
                if sale_id:
                    address = sale_id.partner_invoice_id
                    return address

    def get_delivery_address(self,obj):
        picking_obj = self.env['stock.picking']
        if obj:
            picking_id = picking_obj.browse(obj)
            if picking_id:
                origin = picking_id.origin
                sale_id = self.env['sale.order'].search([('name','=',origin)])
                if sale_id:
                    address = sale_id.partner_shipping_id
                    return address

    def get_total_net_weight(self,obj):
        picking_obj = self.env['stock.picking']
        if obj:
            picking_id = picking_obj.browse(obj)
            if picking_id:
                origin = picking_id.origin
                if origin:
                    pick_ids = picking_obj.search([('origin','=',origin)])
                    total = 0.0
                    if pick_ids:
                        for pick_id in pick_ids:
                            for moveline in pick_id.move_lines:
                                total += moveline.product_id.net_weight
                        return str(total)


    @api.model
    def render_html(self, docids, data=None):
        delivery_address = self.get_delivery_address(docids[0])
        invoice_address = self.get_invoice_address(docids[0])
        total = self.get_total_net_weight(docids[0])
        docargs = {
            'doc_ids': docids,
            'doc_model': 'stock.picking',
            'docs': self.env['stock.picking'].browse(docids),
            'get_delivery': delivery_address,
            'get_invoice': invoice_address,
            'get_total': total,
            'data': data,
        }
        return self.env['report'].render('delivery_note_report.deliverynotereport', docargs)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
