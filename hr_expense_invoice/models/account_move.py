# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import logging

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def crear_gasto(self, empleado_id):
        Expense = self.env['hr.expense']
        
        for f in self:
            if f.state == 'posted' and f.invoice_date:
                anteriores = Expense.search([('factura_id','=',f.id)])
            
                if len(anteriores) > 0:
                    raise ValidationError('La factura {} ya fue utilizada en otro gasto, no se puede utilizar en otro gasto.'.format(f.name))
                
                productos = self.env['product.product'].search([('can_be_expensed', '=', True), '|', ('company_id', '=', False), ('company_id', '=', f.company_id.id)])
                
                if len(productos) == 0:
                    raise ValidationError('No existe productos para gastos.')
                
                values = {
                    'name': f.name,
                    'date': f.invoice_date,
                    'employee_id': empleado_id,
                    'factura_id': f.id,
                    'product_id': productos[0].id,
                    'unit_amount': 0,
                    'product_uom_id': self.env['uom.uom'].search([], limit=1, order='id').id,
                };
                
                exp = Expense.create(values);
                exp._onchange_factura_id()
            
class HRExpenseInvoiceCrearGasto(models.TransientModel):
    _name = 'hr.expense.invoice.crear_gasto'
    _description = 'Crear gastos desde factura'
    
    empleado_id = fields.Many2one('hr.employee', required=True)
    
    def action_crear_gasto(self):
        active_ids = self.env.context.get('active_ids')

        for f in self.env['account.move'].browse(active_ids):
            f.crear_gasto(self.empleado_id.id)
