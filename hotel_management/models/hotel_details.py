from odoo import models, fields, api

class HotelDetails(models.Model):
	_name = 'hotel.details'

	name = fields.Char(string="Hotel name",required=True)
	email = fields.Char(string="Email")
	address = fields.Char(string="Address")
	contact_no = fields.Char(string="Contact no")
	website = fields.Char(string="Website")