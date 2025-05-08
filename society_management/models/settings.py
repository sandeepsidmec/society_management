from odoo import models, fields


class SocietySettings(models.Model):
    _name = 'society.settings'
    _rec_name = "name"

    name = fields.Char("name")