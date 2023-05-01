from odoo import models, fields, api

class BookAuthorInfo(models.Model):
	_name = 'book.author.info'

	name = fields.Char(String="Author name")
	email = fields.Char(String="Email")
	address = fields.Char(String="Address")
	contact_no = fields.Char(String="Contact no")

class SaleOrder(models.Model):
	_inherit = "sale.order"

	p_name = fields.Char(string="products")
	l_name = fields.Char(string="Last name")


class ResPartner(models.Model):
	_inherit = 'res.partner'

	company_type = fields.Selection(string='Company Type',
		selection=[('person', 'Individual'), ('company', 'Company'),('other','Other')],
		compute='_compute_company_type', inverse='_write_company_type')
	new_selection = fields.Selection(selection=[("yes", "Visible"), ("no", "Invisible")])
	is_author = fields.Boolean(string="Author ?")
	

	@api.onchange("new_selection")
	def onchange_new_selectioon(self):
		for rec in self:
			if rec.new_selection == "yes":
				print("\n\n\n\n\n\n YES VISIBLE IS SELECTED")
			else:
				print("\n\n\n\n NO INVISIBLE IS SELECTED")


	# @api.depends('is_company')
	# def _compute_company_type(self):
	# 	for partner in self:
	# 		if partner.is_company:
	# 			partner.company_type = 'company'
	# 		else:
	# 			partner.company_type = 'person'

	