
from odoo import models, fields

class Tower(models.Model):
    _name = 'society.tower'
    _description = 'Society_Tower'

    tower_name=fields.Char("Tower_name")
    # no_of_apart=fields.Integer("No of Apartment")--compute