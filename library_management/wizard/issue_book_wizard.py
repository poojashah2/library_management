from odoo import models, fields, api
from datetime import date

class IssueBookWizard(models.TransientModel):
	_name = 'issue.book.wizard'

	books_ids = fields.One2many('issued.books.wizard','books_id',string="Books line")

	def action_confirm(self):
		for rec in self.books_ids:
			print("\n\n\n rec.return_quantity",rec.return_quantity)
			issue = self.env["register.date.info"].search([('incoming_date','=',False),("entry_id", "=", self._context.get("active_id"))])
			for record in issue:
				for i in range(rec.return_quantity):
					print("\n\n\n\n record",record)
					issue[i].incoming_date = date.today()
					# if record.incoming_date == True:
					# 	print("\n\n\n incoming_date",record)

		# data_get = self.env["register.date.info"].search([('incoming_date','!=',False),("entry_id", "=", self._context.get("active_id"))])
		# for data in data_get:
		# 	self.env['issue.book.info'].write({'state':'return'})
		# 	print("\n\n\n data_get",data)
					# new_data = self.env['issue.book.info'].search([])
					# 	if data:
					# 		issue.write({
					# 			'state':'return'
					# 			})


			# book_data_search = self.env['register.data']. \
            #     search([('', '=', lines.book_name_id.id), ('incoming_time', '=', False), ('trans_id', '=', self._context.get('active_id'))])
            # for i in range(lines.selected_book_quantity):
            #     book_data_search[i].incoming_time = date.today()
		# data_list = []
		# for rec in self.books_ids:
		# 	for record in issue.books_line_ids:
		# 		if rec.books_name_id.name == record.book_name_id.name:
		# 			vals = {
		# 				'issue_quantity' : record.issue_quantity - rec.return_quantity
		# 			}
		# 			print('valsssssssssssssssssss', vals)
		# 			issue.write({
		# 				"books_line_ids": [(1, record.id, vals)]
		# 				})
					# if all(record.issue_quantity) == 0:
					# 	issue.write({'state':'return'})
					# print("\n\n\n\n issue_quantity",record.issue_quantity)
			# data_list.append(record.issue_quantity)
			# if all(data_list)
			# # if sum(data_list) == 0:
			# 	issue.write({
			# 		"state": "return"
			# 		})
			# else:
			# 	print("------------------------------------------------------------------------")
			# print("\n\n\n\n data_list",data_list)
	

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

	books_id = fields.Many2one('issue.book.wizard',string="Book date line")
	quantity = fields.Integer(string="Issued Quantity")
	return_quantity = fields.Integer(string="Return Quantity")
	books_name_id = fields.Many2one('book.details.info',string="Book name")
	# customer_name = fields.Char(string="Customer Name")
	# entry_id = fields.Integer(string="Entry id")
	# book_code = fields.Integer(string="Book Code",readonly=True)
	# late_charges = fields.Integer(compute="_compute_book_charges",string="Book Charges")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)
	# submission_deadline= fields.Date(compute="_compute_submission_deadline",string="Submission Deadline")
	# final_charge = fields.Integer(string="Charge")

		# 	vals={
		# 		'books_ids':([0,0,record.ids])
		# 	}
		# 	return super(IssueBookWizard,self).create(vals)
