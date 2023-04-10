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

	def unlink(self):
		model_rec = self.env['register.books.info'].search([('id','=',self.books_line_ids.ids)])
		for rec in model_rec:
			rec.unlink()
			print("ncfbbcfedfbcvd",rec)
		return super(IssueBookInfo,self).unlink()


	# def unlink(self):
	# 	for rec in self.books_line_ids:
	# 		self.env["register.books.info"].search([('id','=',rec.id)]).unlink()
	# 	return super(IssueBookInfo,self).unlink()

	def issued_book_view(self):
		for rec in self:
			rec.write({'state':"issue"})
			rec.issue_date = date.today()
			for line in self.books_line_ids:
				for _ in range(line.issue_quantity):
					register_id = [{
						"entry_id": line.id,
						"outgoing_date": self.issue_date,
						"book_code": line.book_name_id.id,
					}]
					create_data = self.env["register.date.info"].create(register_id)
		vals = {
			"book_name_id" : "33",
			"issue_quantity" : 2,
		}
		self.write({'books_line_ids' : [(0,0,vals)]})


	def return_book_view(self):
		for rec in self:
			rec.write({'state':"return"})
			rec.return_date = date.today()
		for line in self.books_line_ids:
			register = self.env['register.date.info'].search([("entry_id",'=',line.id)])
			register.incoming_date = rec.return_date

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