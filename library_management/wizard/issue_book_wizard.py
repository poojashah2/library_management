from odoo import models, fields, api
from datetime import date

class IssueBookWizard(models.TransientModel):
	_name = 'issue.book.wizard'

	books_ids = fields.One2many('issued.books.wizard','books_id',string="Books line")

	def action_confirm(self):
		print("shg7fudtgevfyfdevcftfrtwrtgrtg")

	@api.model
	def default_get(self,fields):
		res = super(IssueBookWizard,self).default_get(fields)
		issue = self.env["issue.book.info"].search([("id", "=", self._context.get("active_id"))])
		print("\n\n\n guhuthg",issue)
		lst1 = []
		for rec in issue.books_line_ids:
			lst1.append((0,0,{'books_name_id' : rec.book_name_id,'quantity':rec.issue_quantity}))
		print("\n\n\n tftvgrtgtr",lst1)
		if issue:
			res['books_ids'] = lst1
		# model_rec = self.env['issue.book.info'].search([]).books_line_ids
		# for record in model_rec:
			# res['books_ids'] = ([0,0,])
		return res

class IssuedBooksWizard(models.TransientModel):
	_name = 'issued.books.wizard'

	books_id = fields.Many2one('register.date.info',string="Book date line")
	entry_id = fields.Integer(string="Entry id")
	customer_name = fields.Char(string="Customer Name")
	quantity = fields.Integer(string="Quantity")
	# book_code = fields.Integer(string="Book Code",readonly=True)
	books_name_id = fields.Many2one('book.details.info',string="Book name")
	# late_charges = fields.Integer(compute="_compute_book_charges",string="Book Charges")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)
	# submission_deadline= fields.Date(compute="_compute_submission_deadline",string="Submission Deadline")
	final_charge = fields.Integer(string="Charge")

		# 	vals={
		# 		'books_ids':([0,0,record.ids])
		# 	}
		# 	return super(IssueBookWizard,self).create(vals)
