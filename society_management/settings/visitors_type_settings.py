from odoo import models, fields


class VisitorTypeSettings(models.Model):
    _name = 'visitor.type.settings'
    _rec_name = "visitor_type"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    visitor_type = fields.Char("Visitor Type")