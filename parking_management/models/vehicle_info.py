from odoo import models,fields,api,_

class VehicleInfo(models.Model):
    _name = 'vehicle.info'

    name = fields.Char(string="Vehicle Type")