from odoo import models, fields, api
from odoo.osv import expression

class HotelRoom(models.Model):
	_name = 'hotel.room'
	description = '''This model is for hotel room'''
	_rec_name = 'room_code'

	room_code = fields.Char(string="Room code",readonly=True)
	hotel_name_id = fields.Many2one('hotel.details',String="Hotel name",required=True)
	num_of_rooms = fields.Integer(string="Number of rooms")
	room_type = fields.Selection(selection=[('ac','AC'),('non-ac','NON-AC')],String="Room type")
	discount_percentage = fields.Float(string="Discount percentage")
	discount_valid_from = fields.Date(string="Discount valid from")
	discount_valid_to = fields.Date(string="Discount valid to")
	room_price = fields.Integer(string="Room price")


	@api.model
	def create(self,vals):
		if not vals.get('room_code'):
			seq = self.env['ir.sequence'].next_by_code('hotel.room')
			vals['room_code'] = seq
		return super(HotelRoom,self).create(vals)

	

	def name_get(self):
		result = []
		for rec in self:
			n = str(rec.hotel_name_id.name)+ '/' + str(rec.room_code)
			result.append((rec.id,n))
		return result

	@api.model
	def _name_search(self, name, args=None,  operator='ilike',limit=100, name_get_uid=None):
		args = args or []
		print(":::::::: _name_search",self._context.get('record'))
		print(":::::::::::\n\n\n name",name)
		if self.env.context.get('record'):
			args = expression.AND([[('hotel_name_id', '=', self._context.get('record'))], args])

		return super(HotelRoom,self)._name_search(name,args, limit=limit, name_get_uid=None)