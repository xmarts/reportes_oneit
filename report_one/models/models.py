# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import amount_to_text


class amount_to_texts(models.Model):
	_inherit='sale.order'
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
								help='Amount of the invoice in letter')
	duracion_ser=fields.Char(string='duración del servicio ')
	entrega=fields.Char(string='tiempos de entrega')
	ingeniero_pre=fields.Many2one('res.users', string="Ing Preventa")
	administrador_venta=fields.Char(string="Administrador de venta")


	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)

class amount_to_texts(models.Model):
	_inherit='purchase.order'
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
								help='Amount of the invoice in letter')
	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)

class amount_to_texts(models.Model):
	_inherit='account.invoice'
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
								help='Amount of the invoice in letter')
	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)

class campos_purchase(models.Model):
	_inherit='sale.order.line'

	marca = fields.Many2one(related='product_id.categ_id',string='Marca/Modelo')
	
	
class campos_purchase(models.Model):
	_inherit='purchase.order.line'

	marca = fields.Many2one(related='product_id.categ_id',string='Marca/Modelo')

class stock(models.Model):
	_inherit='stock.move'

	marca = fields.Many2one(related='product_id.categ_id',string='Marca/Modelo')


	
class razon_salida(models.Model):
	_name = 'motivo.salida'
	name = fields.Char(string='Nombre')




class stock(models.Model):
	_inherit='stock.picking'

	nombre_pro=fields.Char(string="Nombre del Proyecto")
	nombre_salida=fields.Char(string="Quien entrega")
	motivo = fields.Many2one('motivo.salida', string='Razon')
	empleado=fields.Many2one('hr.employee',string='Quien entrega')

	
			# self.partner_id = self.picking_id.partner_id.id
			# self.partner_phone = self.picking_id.partner_id.phone
			# self.email_from = self.picking_id.partner_id.email
			# self.sale_id = self.picking_id.sale_id.id
			# claim_lines = [
			# 	(0, 0, {'product_id': move.product_id.id,'marca': move.marca.id, 'modelo':move.modelo.id, 'series':move.series,'observaciones':move.observaciones, 'quantity': move.product_uom_qty, 'move_id': move.id}) for
			# 	move in self.picking_id.move_lines]
			# self.claim_line_ids = claim_lines


class pagos_pagos(models.Model):
    _inherit = 'account.payment'

    @api.model
    def l10n_mx_edi_get_pago_etree(self, cfdi):
        if not hasattr(cfdi, 'Complemento'):
            return None
        attribute = 'pago10:Pagos[1]'
        namespace = {'pago10': 'http://www.sat.gob.mx/Pagos'}
        node = cfdi.Complemento.xpath(attribute, namespaces=namespace)
        return node[0] if node else None

