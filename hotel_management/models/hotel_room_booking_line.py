from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelRoomBookingLine(models.Model):
	_name = 'hotel.room.booking.line'

	hotel_room_id = fields.Many2one('hotel.room',string="Room name",required=True)
	num_of_adults = fields.Integer(string="Number of adults")
	num_of_children = fields.Integer(string="Number of children")
	price = fields.Integer(string="Price")
	hotel_room_booking_id = fields.Many2one('hotel.room.booking')


	@api.constrains('num_of_adults')
	def check_num_of_adults(self):
		for rec in self:
			if rec.num_of_adults > 8:
				raise ValidationError("Limit of adults is 8")

	@api.constrains('num_of_children')
	def check_num_of_children(self):
		for rec in self:
			if rec.num_of_children > 6:
				raise ValidationError("Limit of children is 6")

	
	@api.onchange('hotel_room_id')
	def _onchange_hotel_room_id(self):
		for rec in self:
			for record in rec.hotel_room_id:
				rec.price = record.room_price


