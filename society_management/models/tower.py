
from odoo import models, fields,api

class Tower(models.Model):
    _name = 'society.tower'
    _description = 'Society_Tower'
    _rec_name = 'tower_name'

    tower_name=fields.Char("Tower_name")
    no_of_apart=fields.Integer("No of Apartment", compute='_compute_apartment_count')

    @api.depends('tower_name')
    def _compute_apartment_count(self):
        for record in self:
            record.no_of_apart = self.env['society.apartment'].search_count([('tower_id', '=', record.id)])