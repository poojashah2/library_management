from odoo import models, fields, api
from datetime import date

class IssueBookWizard(models.TransientModel):
	_name = 'return.book.wizard'

	books_ids = fields.One2many('issued.books.wizard','books_id',string="Books line")

	def action_confirm(self):
		for rec in self.books_ids:
			print("\n\n\n rec.return_quantity",rec.return_quantity)
			issue = self.env["register.date.info"].search([('book_code','=',rec.books_name_id.id),('incoming_date','=',False),("entry_id", "=", self._context.get("active_id"))])
			for record in issue:
				for i in range(rec.return_quantity):
					print("\n\n\n\n record",record)
					issue[i].incoming_date = date.today()
			register_date_lines = self.env["register.date.info"].search([('entry_id','=',self._context["active_id"])])
			for res in register_date_lines:
				date_list = []
				if res.incoming_date:
					date_list.append(True)
				else:
					date_list.append(False)
			if all(date_list):
				self.env["issue.book.info"].search([('id','=',self._context["active_id"])]).write({"state":"return"})


	# def default_get(self,fields):
	# 	res = super(IssueBookWizard,self).default_get(fields)
	# 	issue = self.env["issue.book.info"].search([("id", "=", self._context.get("active_id"))])
	# 	print("\n\n\n guhuthg",issue)
	# 	lst1 = []
	# 	for rec in issue.books_line_ids:
	# 		lst1.append((0,0,{'books_name_id' : rec.book_name_id,'quantity':rec.issue_quantity}))
	# 	print("\n\n\n tftvgrtgtr",lst1)
	# 	if issue:
	# 		res['books_ids'] = lst1
	# 	# model_rec = self.env['issue.book.info'].search([]).books_line_ids
	# 	# for record in model_rec:
	# 		# res['books_ids'] = ([0,0,])
	# 	return res

class IssuedBooksWizard(models.TransientModel):
	_name = 'issued.books.wizard'

	books_id = fields.Many2one('return.book.wizard',string="Book date line")
	quantity = fields.Integer(string="Issued Quantity")
	return_quantity = fields.Integer(string="Return Quantity")
	books_name_id = fields.Many2one('book.details.info',string="Book name")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)