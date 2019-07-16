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

	marca=fields.Char(string="Marca")
	modelo=fields.Char(string="Modeo")
	
	
class campos_purchase(models.Model):
	_inherit='purchase.order.line'

	marca=fields.Char(string="Marca")
	modelo=fields.Char(string="Modeo")

class stock(models.Model):
	_inherit='stock.move'

	marca=fields.Char(string="Marca")
	modelo=fields.Char(string="Modeo")

class razon_salida(models.Model):
	_name = 'motivo.salida'
	name = fields.Char(string='Nombre')

class stock(models.Model):
	_inherit='stock.picking'

	nombre_pro=fields.Char(string="Nombre del Proyecto")
	nombre_salida=fields.Char(string="Quien entrega")
	motivo = fields.Many2one('motivo.salida', string='Razon')
	empleado=fields.Many2one('hr.employee',string='Quien entrega')

class img(models.Model):
	_inherit='res.company'	

	upload_image = fields.Binary("Marca de agua en reporte",
									attachment=True,
									help="This field holds the image used for" +
									"the badge, limited to 256x256")