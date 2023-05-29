from odoo import models, fields, api

class BookDeatailsInfo(models.Model):
	_name = 'book.details.info'

	book_no = fields.Char(string="Book ID", readonly=True , copy=False)
	name = fields.Char(string="Book name")
	price = fields.Integer(string="Price")
	pages = fields.Integer(string="Pages")
	author_name_id = fields.Many2one('book.author.info',string="Author name")
	book_quantity = fields.Integer(string="Books Quantity")
	book_charges = fields.Integer(string="Book Charges")
	book_type_ids = fields.Many2many('book.type.info',string="Book Type")
	book_count =fields.Integer(string="Book count",compute="_compute_available_book_count")
	
	@api.model
	def create(self, vals):
		if not vals.get('book_no'):
			seq = self.env["ir.sequence"].next_by_code('book.details')
			vals['book_no'] = seq
		return super(BookDeatailsInfo,self).create(vals)


	def name_get(self):
		result = []
		for rec in self:
			n = str(rec.book_no) + ' '+str(rec.name)+' '+ str(rec.author_name_id.name)
			result.append((rec.id,n))
		return result


	@api.model
	def _name_search(self, name, args=None,  operator='ilike',limit=100, name_get_uid=None):
		args = args or []
		if name:
			args = ['|','|',('book_no',operator,name),('name',operator,name),('author_name_id',operator,name)]
		return self._search(args, limit=limit, access_rights_uid=name_get_uid)

	def _compute_available_book_count(self):
		# model_rec = self.env['register.date.info'].search([])
		search_rec = self.env['register.date.info'].search_count([('book_code','=',self.id),('incoming_date','=',False)])
		# model_rec = self.env['register.date.info'].search_count([('book_code','=',self.book_no),('incoming_date','!=',False),('outgoing_date','')])
		print("::::",search_rec)
		self.book_count = self.book_quantity - int(search_rec)
		# elif model_rec:
		# 	self.book_count += model_rec
		# if search_rec:

	def action_book_count(self):
		print(":::::::::::::::")
		# counting = 0 
		# issue = self.env['issue.book.info'].search([])
		# for rec in issue.books_line_ids:
		# 	if self.env["issue.book.info"].search([("issue_date", "=", datetime.date.today())]):
		# 		if rec.book_name_id.name in self.name:
		# 			counting += rec.issue_quantity
		# 			self.book_count = self.book_quantity - counting
		# 		print("::::::::::::",rec.book_name_id)
		# 	print("\n\n\n::::::::::",rec.books_line_ids.issue_quantity)
		# # for rec in self: