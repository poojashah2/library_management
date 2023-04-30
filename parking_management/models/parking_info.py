from odoo import fields,models,api

class ParkingInfo(models.Model):
    _name = 'parking.info'

    security_name_id = fields.Many2one('security.info',string="Security_guide_name")
    area_name_id = fields.Many2one('area.info',string="Area")



