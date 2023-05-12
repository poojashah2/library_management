from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class HotelRoomBooking(models.Model):
	_name = 'hotel.room.booking'

	hotel_names_id = fields.Many2one('hotel.details',string="Hotel name",required=True)
	customer_name_id = fields.Many2one('res.partner',string="Customer name",required=True)
	customer_address = fields.Char(string="Customer address")
	customer_email = fields.Char(string="Customer email")
	check_in_date = fields.Datetime(string="Check in")
	check_out_date = fields.Datetime(string="Check out")
	state = fields.Selection(selection=[('draft','Draft'),('booked','Booked'),('cancel','Cancel')],string="Status",required=True,copy=False,tracking=True,default='draft',readonly=True)
	hotel_room_book_line_ids = fields.One2many('hotel.room.booking.line','hotel_room_booking_id',string="Rooms")



	@api.onchange("hotel_names_id")
	def _onchange_hotel_names_id(self):
		model_rec = self.env['hotel.room'].search([('hotel_name_id','=',self.hotel_names_id.id)])
		print("::::::: model_rec",model_rec)
		# your_many2one_value = self.hotel_names_id
		# self.hotel_room_book_line_ids.write({'hotel_room_id':})
			# print(":::::: hotel_room_book_line_ids",rec)
			# 	# print(":::::::: hotel_names_id",rec.hotel_names_id)


	@api.onchange("customer_name_id")
	def _onchange_field_fill(self):
		for rec in self:
			rec.customer_address = ""
			if rec.customer_name_id:
				model_rec = self.env['res.partner'].search_read([("id", "=", rec.customer_name_id.id)],['email','street','street2'])
				print("\n\n\n>>>>>>>>>>>>",model_rec)
				res_data = self.env["res.partner"].search([("id", "=", rec.customer_name_id.id)])
				rec.customer_email = res_data.email
				if not res_data.street2:
					rec.customer_address = str(res_data.street)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)
				else:
					rec.customer_address = str(res_data.street)+"\n"+str(res_data.street2)+"\n"+str(res_data.zip)+"\n"+str(res_data.city)

	def booked_room(self):
		for rec in self:
			template = self.env.ref('hotel_management.room_booked_mail_id').id
			template_id = self.env['mail.template'].browse(template)
			template_id.send_mail(rec.id, force_send=True)
		self.write({'state':'booked'})
	

	def cancel_room(self):
		return {
	        'type': 'ir.actions.act_window',
	        'view_mode': 'form',
	        'res_model': 'confirmation.booking.wizard',
	        'views': [(False, 'form')],
	        'view_id': False,
	        'target': 'new',
	    }
	

	def send_booking_email(self):
		template = self.env.ref('hotel_management.room_booked_mail_id')
		template_id = self.env['mail.template'].browse(template.id)
		ctx = dict(
			default_template_id = template and template.id
			)
		return {
	        'type': 'ir.actions.act_window',
	        'view_mode': 'form',
	        'res_model': 'mail.compose.message',
	        'views': [(False, 'form')],
	        'view_id': False,
	        'target': 'new',
	        'context': ctx,
	    }

	def action_email_reminder_check_out(self):
		model_rec = self.env['hotel.room.booking'].search([])
		for rec in model_rec:
			if rec.check_out_date:
				if (rec.check_out_date.hour - datetime.now().hour) == 1:
					template = self.env.ref('hotel_management.reminder_check_out_mail_id').id
					template_id = self.env['mail.template'].browse(template)
					template_id.send_mail(rec.id, force_send=True)
	
	@api.constrains('check_in_date','check_out_date')
	def check_in_out_date(self):
		if self.check_out_date < self.check_in_date:
			raise ValidationError("check_out_date should be grater than check_in_date")

