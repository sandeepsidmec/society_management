from odoo import models, fields


class ApartmentTypeSettings(models.Model):
    _name = 'apartment.type.settings'
    _rec_name = "apartment_type"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    apartment_type = fields.Char("Apartment Type")