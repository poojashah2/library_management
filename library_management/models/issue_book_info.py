from odoo import models, fields, api
from datetime import date

class IssueBookInfo(models.Model):
	_name = 'issue.book.info'

	user_name_id = fields.Many2one('res.partner',string="User name")
	books_line_ids = fields.One2many('register.books.info','books_line_id',string="Books")
	user_contact_no = fields.Char(string='User Contact No')
	user_email = fields.Char(string="User Email Id")
	user_address = fields.Text(string="User Address")
	issue_date = fields.Date(string="Issue Date", readonly=True)
	return_date = fields.Date(string="Return Date",readonly=True)
	state = fields.Selection(selection=[('draft','Draft'),('issue','Issued'),('return','Return')],string="Status",required=True,copy=False,tracking=True,default='draft',readonly=True)



	def issued_book_view(self):
		register = self.env['register.date.info']
		for rec in self:
			rec.write({'state':"issue"})
			rec.issue_date = date.today()
			for line in rec.books_line_ids:
				for _ in range(line.issue_quantity or 1):
					register.create({
							'book_code': line.book_name_id.book_no,
							'incoming_date': rec.issue_date
						})
			# incoming_date = rec.books_line_ids.book_name_id
			# model_rec = self.env['register.date.info'].create(incoming_date)
			# print(incoming_date)

	def return_book_view(self):
		print("\n\n\n\n", self.books_line_ids.id)
		register = self.env['register.date.info'].search([])
		for rec in self:
			rec.write({'state':"return"})
			rec.return_date = date.today()
			for line in register:
				register.write({'outgoing_date':rec.return_date})


	@api.onchange("user_name_id")
	def _onchange_field_fill(self):
		for rec in self:
			rec.user_email = ""
			if rec.user_name_id:
				res_data = self.env["res.partner"].search([("id", "=", rec.user_name_id.id)])
				rec.user_email = res_data.email
				rec.user_contact_no = res_data.phone
				if not res_data.street2:
					rec.user_address = str(res_data.street)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)
				else:
					rec.user_address = str(res_data.street)+"\n"+str(res_data.street2)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)