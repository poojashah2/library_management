from odoo import models,fields,api
from datetime import date

class RegisterDateInfo(models.Model):
	_name = 'register.date.info'

	entry_id = fields.Integer(string="Entry id")
	customer_name = fields.Char(string="Customer Name")
	book_code = fields.Integer(string="Book Code",readonly=True)
	books_name = fields.Char(string="Book name")
	book_charges = fields.Integer(compute="_compute_book_charges",string="Book Charges")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)

	
	def return_button(self):
		self.incoming_date = date.today()
		# model_rec = self.env['book.details.info'].search([('name','=',self.books_name)])
		# for rec in model_rec:
		# 	self.book_charges = rec.charges
		# model_rec = self.env['issue.book.info'].search([])
		# one_book_name = self.env["book.details.info"].search([("name", "=", self.books_name)])
		# for rec in self:
		# 	rec.incoming_date = date.today()
		# for record in model_rec:
		# 	record.return_date = self.incoming_date
		# 	if str(rec.incoming_date) >  str(record.submission_deadline):
		# 		rec.book_charges = 
		# 	# if rec.incoming_date:
		# 	# 	record.charges = 0 
		# 	# 	for records in record.books_line_ids:
		# 	# 		if records.book == rec.books_name:

		# 			print("<<<<<<<<<<",records)



		print("><<><<<<><><>>")
	def _compute_book_charges(self):
		for record in self:
			record.book_charges = 0
			model_rec = self.env['book.details.info'].search([('name','=',record.books_name)])
			for rec in model_rec:
				if record.incoming_date:
					record.book_charges = rec.book_charges
				else:
					record.book_charges = 0