from odoo import models, fields
from datetime import date

class IssueBookWizard(models.TransientModel):
	_name = 'issue.date.wizard'

	# issued_date = fields.Date(string = "Issued Date")

	def action_confirm(self):
		# self.issued_date = date.today()
		issue = self.env["issue.book.info"].search([("id", "=", self._context.get("active_id"))])
		if issue:
			issue.issue_date = date.today()
			issue.state = "issue"