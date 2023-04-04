from odoo import models, fields, api

class BookDeatailsInfo(models.Model):
	_name = 'book.details.info'

	book_no = fields.Char(string="Book ID", readonly=True , copy=False)
	name = fields.Char(string="Book name")
	price = fields.Integer(string="Price")
	pages = fields.Integer(string="Pages")
	author_name_id = fields.Many2one('book.author.info',string="Author name")
	book_quantity = fields.Integer(string="Books Quantity")

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
