from odoo import models,fields,api,_

class AreaInfo(models.Model):
    _name = 'area.info'

    name = fields.Char(string="Location name")