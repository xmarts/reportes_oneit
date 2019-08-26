# -*- coding: utf-8 -*-
{
    'name': "report_one",

    'summary': """
        Modificacion en el diseño de los reportes de ventas, compras, inventario y facturacion""",

    'description': """
        Modificacion de diseño de reportes
    """,

    'author': "Xmarts",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','stock','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/sale_report_templete.xml',
        'report/purchase_report_template.xml',
        'report/report_stock.xml',        
        'report/factura.xml',
        'report/account_receipt.xml',
        'report/solicitud_purchase.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}