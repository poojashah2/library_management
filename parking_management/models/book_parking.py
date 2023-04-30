from odoo import models,fields,api,_

class Bookparking(models.Model):
    _name = 'book.parking'

    customer_name_id = fields.Many2one('res.partner',string="Customer Name")
    vehicle_num_plate = fields.Char(string="Vehicle Number Plate")
    slot_ids = fields.Many2many('slot.detail',string="Slots")
    location_id = fields.Many2one('area.info',string="Location")
    basement = fields.Many2one('basement.info',string="Select Basement")
    vehicle_type_ids = fields.Many2many("vehicle.info", "vehicle_type_id", string="Vehicle type")
    
    def book_parking(self):
        for rec in self.slot_ids:
            # print(len(rec.slot_ids))
            for _ in range(len(rec)):
                create_values = [{
                'register_name_id':self.customer_name_id.id,
                'register_slot_ids':rec,
                }]
                create_data = self.env['register.parking.info'].create(create_values)