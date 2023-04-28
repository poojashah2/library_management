from odoo import models, fields, api
from datetime import date

class PassContextWizard(models.TransientModel):
	_name = 'pass.context.wizard'

	f_name = fields.Char(string="First Name")
	m_name = fields.Char(string="Middle Name")
	l_name = fields.Char(string="Last Name")

	def action_confirm(self):
		pass