from odoo import models, fields, api
from datetime import datetime

class RegisterBooksInfo(models.Model):
	_name = 'register.books.info'

	book_name_id = fields.Many2one('book.details.info',string="Book name")
	issue_quantity = fields.Integer(string="Book Quantity")
	books_line_id = fields.Many2one('issue.book.info') #empty field
	book_types_ids = fields.Many2many('book.type.info',string="Book Type")


	@api.onchange('book_name_id')
	def _onchange_book_type(self):
		for rec in self:
			book_type = self.env['book.details.info'].search([('id', '=', self.book_name_id.id)])
			print(":::::::::;>>>>>>>>>>>",book_type.id,self.book_name_id.id)
			for record in book_type:
				if record.id == self.book_name_id.id:
					rec.update({
						'book_types_ids':[(6,0,record.book_type_ids.ids)]
						})
	# @api.model
	# def create(self, vals):
	# 	search_rec = self.env['book.details.info'].search(['name','=',self.book_name_id])
	# 	vals.update({
	# 		'book_types_ids':[(4,booktype) for booktype in search_rec.book_type_ids]
	# 		})