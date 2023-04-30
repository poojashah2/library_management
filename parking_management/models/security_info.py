from odoo import fields,models,api

class SecurityInfo(models.Model):
    _name = 'security.info'

    name = fields.Char(string="Name")
    phone_num = fields.Char(string="Phone number")
    address = fields.Char(string="Address")
