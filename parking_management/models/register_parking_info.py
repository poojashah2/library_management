from odoo import models,fields,api,_

class RegisterParkingInfo(models.Model):
    _name = 'register.parking.info'

    register_name_id = fields.Many2one('res.partner',string="Customer Name")
    # vehicle_num_plate = fields.Char(string="Vehicle Number Plate")
    register_slot_ids = fields.Many2many('slot.detail',string="Slots")
    # location_id = fields.Many2one('area.info',string="Location")
    # basement = fields.Many2one('basement.info',string="Select Basement")
    # vehicle_type_ids = fields.Many2many("vehicle.info", "vehicle_type_id", string="Vehicle type")
    