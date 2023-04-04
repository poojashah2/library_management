from odoo import models, fields, api

class IssueBookInfo(models.Model):
	_name = 'issue.book.info'

	user_name_id = fields.Many2one('res.partner',string="User name")
	books_line_ids = fields.One2many('register.books.info','books_line_id',string="Books")
	user_contact_no = fields.Char(string='User Contact No')
	user_email = fields.Char(string="User Email Id")
	user_address = fields.Text(string="User Address")
	issue_date = fields.Datetime(string="Issue Date")
	return_date = fields.Datetime(string="Return Date")


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