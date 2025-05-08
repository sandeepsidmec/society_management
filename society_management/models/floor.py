
from odoo import models, fields

class Floor(models.Model):
    _name = 'society.floor'
    _description = 'Society_Floor'

    floor=fields.Char("Floors")
    tower_id=fields.Many2one("society.tower","Tower_name")