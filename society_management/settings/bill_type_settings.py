from odoo import models, fields


class BillTypeSettings(models.Model):
    _name = 'bill.type.settings'
    _rec_name = "bill_type"

    bill_type = fields.Char("Bill Type")
    bill_type_category = fields.Char("Bill Type Category")