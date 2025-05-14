from odoo import models, fields


class BillTypeSettings(models.Model):
    _name = 'bill.type.settings'
    _rec_name = "bill_type"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    bill_type = fields.Char("Bill Type")
    bill_type_category = fields.Selection([
        ('utility', 'Utility Bills'),
        ('common_area', 'Common Area Bills')
    ], string="Bill Type Category")
