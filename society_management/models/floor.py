
from odoo import models, fields

class Floor(models.Model):
    _name = 'society.floor'
    _description = 'Society_Floor'
    _rec_name = 'floor'

    floor=fields.Char("Floors")
    tower_id=fields.Many2one("society.tower","Tower_name")