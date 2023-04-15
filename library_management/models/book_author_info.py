from odoo import models, fields, api

class BookAuthorInfo(models.Model):
	_name = 'book.author.info'

	name = fields.Char(String="Author name")
	email = fields.Char(String="Email")
	address = fields.Char(String="Address")
	contact_no = fields.Char(String="Contact no")
