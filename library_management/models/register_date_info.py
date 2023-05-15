from odoo import models,fields,api
from datetime import date,timedelta

class RegisterDateInfo(models.Model):
	_name = 'register.date.info'

	entry_id = fields.Integer(string="Entry id")
	customer_name = fields.Char(string="Customer Name")
	book_code = fields.Integer(string="Book Code",readonly=True)
	books_name = fields.Char(string="Book name")
	book_charges = fields.Integer(string="Book Charges")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)
	submission_deadline= fields.Date(compute="_compute_submission_deadline",string="Submission Deadline")

	
	def return_button(self):
		self.incoming_date = date.today()
		model_rec = self.env['book.details.info'].search([('name','=',self.books_name)])
		for rec in model_rec:
			if str(self.incoming_date) > str(self.submission_deadline):
				total_days = (self.incoming_date - self.submission_deadline).days
				self.book_charges = rec.book_charges
				if (total_days // 5) == 0:
					self.book_charges = self.book_charges
				else:
					for i in range((total_days // 5) - 1):
						self.book_charges += rec.book_charges
						
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


	def _compute_submission_deadline(self):
		for rec in self:
			if rec.outgoing_date:
				rec.submission_deadline = rec.outgoing_date + timedelta(days=15)
			else:
				rec.submission_deadline = False


		print("><<><<<<><><>>")
	# def _compute_book_charges(self):
	# 	for record in self:
	# 		record.book_charges = 0
	# 		model_rec = self.env['book.details.info'].search([('name','=',record.books_name)])
	# 		for rec in model_rec:
	# 			if record.incoming_date:
	# 				if str(record.incoming_date) > str(record.submission_deadline):
	# 					total_days = (record.incoming_date - record.submission_deadline).days
	# 					if (total_days // 5) == 0:
	# 						record.book_charges = self.book_charges
	# 					else:
	# 						for i in range((total_days // 5) - 1):
	# 							record.book_charges += self.book_charges

	# 			else:
	# 				record.book_charges = 0