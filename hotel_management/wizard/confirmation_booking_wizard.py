from odoo import models, fields, api

class ConfirmationBookingWizard(models.TransientModel):
	_name = 'confirmation.booking.wizard'

	select_terms = fields.Selection(selection=[('cancel_mail','Cancel booking and send mail'), ('cancel','Cancel booking' )],string="Select terms")


	def action_confirm(self):
		model_rec = self.env['hotel.room.booking'].search([('id','=',self._context['active_id'])])
		model_rec.write({'state':'cancel'})
		for rec in self:
			if rec.select_terms == 'cancel_mail':
				template = self.env.ref('hotel_management.cancel_booking_mail_id').id
				template_id = self.env['mail.template'].browse(template)
				template_id.send_mail(self._context.get('active_id'), force_send=True)
