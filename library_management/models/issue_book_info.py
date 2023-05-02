from odoo import models, fields, api, _
from datetime import date,timedelta
from odoo.exceptions import ValidationError

class IssueBookInfo(models.Model):
	_name = 'issue.book.info'
	_inherit = 'mail.thread'

	user_name_id = fields.Many2one('res.partner',string="User name")
	books_line_ids = fields.One2many('register.books.info','books_line_id',string="Books")
	user_contact_no = fields.Char(string='User Contact No')
	user_email = fields.Char(string="User Email Id")
	user_address = fields.Text(string="User Address")
	book_names_id = fields.Many2one('book.details.info',string="Book name")
	quantity = fields.Integer(string="Quantity")
	submission_deadline = fields.Date(compute="_compute_submission_deadline",string="Return Book Deadline")
	charges = fields.Integer(compute="_compute_book_charges",string="Total charges")
	issue_date = fields.Date(string="Issue Date", readonly=True)
	return_date = fields.Date(string="Return Date",readonly=True)
	state = fields.Selection(selection=[('draft','Draft'),('issue','Issued'),('return','Return')],string="Status",required=True,copy=False,tracking=True,default='draft',readonly=True)
	nationality = fields.Selection(selection=[('india','India'),('pakistan','Pakistan')],string="Nationality")
	color = fields.Integer(string="Color",compute="_compute_get_color")
	user_image = fields.Image(string="User Image")

	def pass_context_button(self):
		# if 'aaaa' in self._context:
			# context = dict(self.env.context or {})
			# context['pass'] = 'india'
			return {
				"type" : "ir.actions.act_window",
				"res_model" : "pass.context.wizard",
				"name" : ("pass_context"),
				"view_mode" : "form",
				"target" : "new",
				# "context" : context,
			}

	def _compute_get_color(self):
		for rec in self:
			if rec.state == 'draft':
				rec.color = 4
			elif rec.state == 'issue':
				rec.color = 1
			else:
				rec.color = 10

	def unlink(self):
		model_rec = self.env['register.books.info'].search([('id','=',self.books_line_ids.ids)])
		for rec in model_rec:
			rec.unlink()
			print("ncfbbcfedfbcvd",rec)
		return super(IssueBookInfo,self).unlink()

	def _compute_submission_deadline(self):
		for rec in self:
			if rec.issue_date:
				rec.submission_deadline = rec.issue_date + timedelta(days=15)
			else:
				rec.submission_deadline = False

	def action_return_book_mail(self):
		model_rec = self.env['issue.book.info'].search([])
		for rec in model_rec:
			template = self.env.ref('library_management.issue_book_mail_id').id
			template_id = self.env['mail.template'].browse(template)
			template_id.send_mail(rec.id, force_send=True)
			# if not rec.incoming_date:
			# 	print("\n\n\n",rec.outgoing_date)
				# return IssueBookInfo.issue_book_mail(self)
		# if not model_rec.incoming_date:
		# 	print("incoming_date is not available")
		# 	self.issue_book_mail()
	# def unlink(self):
	# 	for rec in self.books_line_ids:
	# 		self.env["register.books.info"].search([('id','=',rec.id)]).unlink()
	# 	return super(IssueBookInfo,self).unlink()

	def issued_book_view(self):
		new_data = self.env['book.author.info'].search_read([('id','>',0)])
		print(">>:L:LDGETFrtg",new_data)
		# for rec in self:
		# 	# rec.write({'state':"issue"})
		# 	# rec.issue_date = date.today()
		# 	for line in self.books_line_ids:
		# 		for _ in range(line.issue_quantity):
		# 			register_id = [{
		# 				"entry_id": line.id,
		# 				"outgoing_date": self.issue_date,
		# 				"book_code": line.book_name_id.id,
		# 				"books_name":line.book_name_id.name,
		# 				"customer_name":self.user_name_id.name,
		# 			}]
		# 			create_data = self.env["register.date.info"].create(register_id)
		return {
			"type" : "ir.actions.act_window",
			"res_model" : "issue.date.wizard",
			"name" : ("issue_date"),
			"view_mode" : "form",
			"target" : "new",
		}
		# vals = {
		# 	"book_name_id" : "33",
		# 	"issue_quantity" : 2,
		# }
		# self.write({'books_line_ids' : [(0,0,vals)]})

	def issue_book_mail(self):
		return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
        }
		# template = self.env.ref('library_management.issue_book_mail_id').id
		# template_id = self.env['mail.template'].browse(template)
		# template_id.send_mail(self.id, force_send=True)
	


	def return_book_view(self):
		for rec in self:
			print("hfyegf")
			# register = self.env['register.date.info'].search([("entry_id",'=',rec.id),('incoming_date','!=',False)])
			# for record in register:
			# 	rec.write({'state':"return"})
			# rec.return_date = date.today()
		data_list = []
		for line in self.books_line_ids:
			# model_rec = self.env['issue.book.wizard'].search([])
			data_list.append((0,0,{'books_name_id':line.book_name_id.id,
				'quantity':line.issue_quantity}))

		return {
			"type" : "ir.actions.act_window",
			"res_model" : "return.book.wizard",
			"name" : ("issue_book"),
			"view_mode" : "form",
			"target" : "new",
			"context" : {
				'default_books_ids' : data_list
			}
		}

	@api.onchange("user_name_id")
	def _onchange_field_fill(self):
		for rec in self:
			rec.user_email = ""
			if rec.user_name_id:
				model_rec = self.env['res.partner'].search_read([("id", "=", rec.user_name_id.id)],['email','phone','street','street2'])
				print("\n\n\n>>>>>>>>>>>>",model_rec)
				res_data = self.env["res.partner"].search([("id", "=", rec.user_name_id.id)])
				rec.user_email = res_data.email
				rec.user_contact_no = res_data.phone
				rec.user_image = res_data.image_1920
				if not res_data.street2:
					rec.user_address = str(res_data.street)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)
				else:
					rec.user_address = str(res_data.street)+"\n"+str(res_data.street2)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)


	@api.constrains("books_line_ids")
	def check_book_number(self):
		for rec in self.books_line_ids:
			if self.env["register.books.info"].search_count([("book_name_id", "=", rec.book_name_id.id), ("books_line_id", "=", self.id)]) > 1:
				raise ValidationError("Selected book already added in the list.")
				# data_rec = self.env['register.books.info'].search([]).book_
				# for data in model_rec:
				# 	print("sngsygsag")
				# 	if record in data:
				# 		raise ValidationError("you cannot make same data")
				# if record.book_name_id.name not in record.book_name_id.name:
				# 	print("dgcedcrfyuescdgf")
				# else:
				# 	raise ValidationError("something went wrong")

	def _compute_book_charges(self):
		value_list = []
		for rec in self:
			rec.charges = 0
			if rec.issue_date:
				single_charge = self.env["register.date.info"].search([("entry_id", "=", rec.id)])
				for book in single_charge:
					rec.charges += book.final_charge
					