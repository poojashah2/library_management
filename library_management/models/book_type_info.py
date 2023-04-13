from odoo import models, fields,api

class BookTypeInfo(models.Model):
	_name = "book.type.info"

	name = fields.Char(string="Book type")

	_sql_constraints = [('unique_name','unique(name)',"""invalid name""")]

	def copy(self, default=None):
		if default is None:
			default = {}
		default['name'] = self._get_copy_name()
		return super(BookTypeInfo, self).copy(default)
	
	def _get_copy_name(self):
		parts = self.name.split(' - ')
		name = parts[0]
		if len(parts) > 1:
			number = int(parts[1]) + 1
		else:
			number = 1
		return '%s - %s' % (name, number)

	