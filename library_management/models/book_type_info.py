from odoo import models, fields,api

class BookTypeInfo(models.Model):
	_name = "book.type.info"

	name = fields.Char(string="Book type")