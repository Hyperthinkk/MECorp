# -*- coding: utf-8 -*-

{
    'name' : "Delivery Report",
    'version' : "1.0",
    'author' : "Caret Consulting Services",
    'website': 'www.caretcs.com',
    'description' : 'Generate Delivery Note Report & Invoice Report',
    'depends' : ['base','product','purchase','sale_stock'],
    'data' : [
		'views/stock_picking_view.xml',
        'report/delivery_note_report_view.xml',
        'report/invoice_report_view.xml',
        'report/custom_layouts_hf.xml',
 		'report_menu.xml',
 	],
    'demo' : [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

