from odoo import models, fields


class VisitorTypeSettings(models.Model):
    _name = 'visitor.type.settings'
    _rec_name = "visitor_type"

    visitor_type = fields.Char("Visitor Type")