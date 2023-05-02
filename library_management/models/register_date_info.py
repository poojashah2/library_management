from odoo import models,fields,api
from datetime import date,timedelta

class RegisterDateInfo(models.Model):
	_name = 'register.date.info'

	entry_id = fields.Integer(string="Entry id")
	customer_name = fields.Char(string="Customer Name")
	book_code = fields.Integer(string="Book Code",readonly=True)
	books_name = fields.Char(string="Book name")
	late_charges = fields.Integer(compute="_compute_book_charges",string="Book Charges")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)
	submission_deadline= fields.Date(compute="_compute_submission_deadline",string="Submission Deadline")
	final_charge = fields.Integer(string="Charge")
	demo_id = fields.Many2one('issue.book.info')





	def _compute_submission_deadline(self):
		for rec in self:
			if rec.outgoing_date:
				rec.submission_deadline = rec.outgoing_date + timedelta(days=15)
			else:
				rec.submission_deadline = False

	def _compute_book_charges(self):
		for rec in self:
			rec.late_charges = 0
			model_rec = self.env['book.details.info'].search([('name','=',rec.books_name)]).book_charges
			if not rec.incoming_date and str(date.today()) > str(rec.submission_deadline):
				rec.late_charges += model_rec + (model_rec * (date.today() - rec.submission_deadline).days // 5)
				rec.final_charge = rec.late_charges
				