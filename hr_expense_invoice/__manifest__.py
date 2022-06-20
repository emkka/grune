# -*- coding: utf-8 -*-

{
    'name': 'Gastos unidos a facturas',
    'version': '1.0',
    'category': 'Accounting/Expenses',
    'sequence': 6,
    'summary': 'Gastos unidos a facturas',
    'description': """ Cambios a gastos para unirlas a facturas """,
    'website': 'http://aquih.com',
    'author': 'Rodrigo Fernandez',
    'depends': ['hr_expense'],
    'data': [
        'views/hr_expense_views.xml',
        'views/account_move_views.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}