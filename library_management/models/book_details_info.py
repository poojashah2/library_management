from odoo import models, fields, api

class BookDeatailsInfo(models.Model):
	_name = 'book.details.info'

	book_no = fields.Char(string="Book ID", readonly=True , copy=False)
	name = fields.Char(string="Book name")
	price = fields.Integer(string="Price")
	pages = fields.Integer(string="Pages")
	author_name_id = fields.Many2one('book.author.info',string="Author name")
	book_quantity = fields.Integer(string="Books Quantity")
	book_count =fields.Integer(string="Book count")

	@api.model
	def create(self, vals):
		if not vals.get('book_no'):
			seq = self.env["ir.sequence"].next_by_code('book.details')
			vals['book_no'] = seq
		return super(BookDeatailsInfo,self).create(vals)


	def name_get(self):
		result = []
		for rec in self:
			name = rec.book_no + ' '+rec.name+' '+ rec.author_name_id.name
			result.append((rec.id,name))
		return result


	@api.model
	def _name_search(self, name, args=None,  operator='ilike',limit=100, name_get_uid=None):
		args = args or []
		if name:
			args = ['|','|',('book_no',operator,name),('name',operator,name),('author_name_id',operator,name)]
		return self._search(args, limit=limit, access_rights_uid=name_get_uid)

	def action_book_count(self):
		print(":::::::::::::::")
		issue = self.env['issue.book.info'].search([])
		for rec in issue.books_line_ids:
			if rec.book_name_id.name in self.name:
				self.book_count = self.book_quantity - rec.issue_quantity
			print("::::::::::::",rec.book_name_id)
		# 	print("\n\n\n::::::::::",rec.books_line_ids.issue_quantity)
		# # for rec in self: