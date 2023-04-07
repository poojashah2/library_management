from odoo import models,fields,api

class RegisterDateInfo(models.Model):
	_name = 'register.date.info'

	entry_id = fields.Integer(string="Entry id")
	book_code = fields.Integer(string="Book Code",readonly=True)
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)


	
