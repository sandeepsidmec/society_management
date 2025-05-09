
from odoo import models, fields

class Parking(models.Model):
    _name = 'society.parking'
    _description = 'Society_Parking'
    _rec_name = 'parking_code'

    parking_code=fields.Integer("Parking Code")
    apart_id=fields.Many2one("society.apartment","Apartment Name")
    parking_status=fields.Selection([('allocated','Allocated'),('not allocated','Not Allocated')])