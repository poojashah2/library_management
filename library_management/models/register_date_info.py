from odoo import models,fields,api
from datetime import date

class RegisterDateInfo(models.Model):
	_name = 'register.date.info'

	entry_id = fields.Integer(string="Entry id")
	customer_name = fields.Char(string="Customer Name")
	book_code = fields.Integer(string="Book Code",readonly=True)
	books_name = fields.Char(string="Book name")
	book_charges = fields.Integer(string="Book Charges")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)

	
	def return_button(self):
		model_rec = self.env['issue.book.info'].search([])
		one_book_name = self.env["book.details.info"].search([("name", "=", self.books_name)])
		for rec in self:
			rec.incoming_date = date.today()
		for record in model_rec:
			record.return_date = self.incoming_date
			if str(rec.incoming_date) >  str(record.submission_deadline):
				rec.book_charges = 
			# if rec.incoming_date:
			# 	record.charges = 0 
			# 	for records in record.books_line_ids:
			# 		if records.book == rec.books_name:

					print("<<<<<<<<<<",records)



		print("><<><<<<><><>>")