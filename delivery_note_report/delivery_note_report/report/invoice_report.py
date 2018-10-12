# -*- coding: utf-8 -*-
from odoo import api, fields, models

class InvoiceReportTemplate(models.AbstractModel):
    _name = 'report.delivery_note_report.invoicereportview'


    def get_total_net_weight(self,obj):
        invoice_obj = self.env['account.invoice']
        if obj:
            invoice_id = invoice_obj.browse(obj)
            if invoice_id:
                origin = invoice_id.origin
                if origin:
                    invoice_ids = invoice_obj.search([('origin','=',origin)])
                    if invoice_ids:                        
                        for invoice_id in invoice_ids:
                            total = 0.0
                            for line in invoice_id.invoice_line_ids:
                                total += line.product_id.net_weight
                            return total

    @api.model
    def render_html(self, docids, data=None):
        total = self.get_total_net_weight(docids[0])
        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': self.env['account.invoice'].browse(docids),
            'get_total': total,
            'data': data,
        }
        return self.env['report'].render('delivery_note_report.invoicereportview', docargs)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
