from odoo import models, fields
from datetime import date

class IssueDateWizard(models.TransientModel):
	_name = 'issue.date.wizard'

	def action_confirm(self):
		issue = self.env["issue.book.info"].search([("id", "=", self._context.get("active_id"))])
		issue.write({'state':"issue"})
		issue.issue_date = date.today()
		for line in issue.books_line_ids:
			for _ in range(line.issue_quantity):
				register_id = [{
					"entry_id": self._context.get("active_id"),
					"outgoing_date": issue.issue_date,
					"book_code": line.book_name_id.id,
					"books_name":line.book_name_id.name,
					"customer_name":issue.user_name_id.name,
				}]
				create_data = self.env["register.date.info"].create(register_id)

