from odoo import models, fields


class ServiceTypeSettings(models.Model):
    _name = 'service.type.settings'
    _rec_name = "service_type"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    service_type = fields.Char("Service Type")