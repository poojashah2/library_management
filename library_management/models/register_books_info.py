from odoo import models, fields, api
from datetime import datetime

class RegisterBooksInfo(models.Model):
	_name = 'register.books.info'

	book_name_id = fields.Many2one('book.details.info',string="Book name")
	issue_quantity = fields.Integer(string="Book Quantity")
	books_line_id = fields.Many2one('issue.book.info')
