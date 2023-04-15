from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

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
			issue_book_read = self.env['issue.book.info']._read_group_raw([('user_email','!=',False)],['user_email','quantity'],['user_email'])
			print(":::::::>>>>>>issue_book_read",issue_book_read)
			for record in book_type:
				if record.id == self.book_name_id.id:
					rec.update({
						'book_types_ids':[(6,0,record.book_type_ids.ids)]
						})
	# def unlink(self):
	# 	model_rec = self.env['issue.book.info'].search([]).books_line_ids.book_name_id
	# 	for rec in model_rec:
	# 		for record in self.book_name_id:
	# 			print(">>>>>>>>>>")
	# 			if rec.id != record.id:
	# 				return super (RegisterBooksInfo,self).unlink()
					# raise ValidationError("YOU CANONOT DELETE THIS RECORD")
			
	# 	# model_rec = self.env['issue.book.info'].search([('books_line_ids','=',self.id)]).id
	# 	print("\n\n\n rfgugh",model_rec)
	# 	# for rec in model_rec:
		# 	if rec:

	# @api.model
	# def create(self, vals):
	# 	search_rec = self.env['book.details.info'].search(['name','=',self.book_name_id])
	# 	vals.update({
	# 		'book_types_ids':[(4,booktype) for booktype in search_rec.book_type_ids]
	# 		})