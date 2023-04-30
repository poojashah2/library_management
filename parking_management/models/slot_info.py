from odoo import models,fields,api,_

class SlotDetail(models.Model):
    _name = 'slot.detail'

    name = fields.Char(string='Slot name')
    # slot_ids = fields.One2many('slot.detail','slot_id',string="Slots")

    def copy(self,default=None):
        if default is None:
            default = {}
        default['name'] = self._get_copy_name()
        return super(SlotDetail,self).copy(default)

    def _get_copy_name(self):
        parts = self.name.split(' - ')
        name = parts[0]
        if len(parts) > 1:
            number = int(parts[1]) + 1
        else:
            number = 1
        return '%s - %s' % (name, number)