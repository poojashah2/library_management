from odoo import models,fields,api,_

class BasementInfo(models.Model):
    _name = 'basement.info'

    name = fields.Char(string="Basement")