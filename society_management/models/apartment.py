
from odoo import models, fields

class Apartment(models.Model):
    _name = 'society.apartment'
    _description = 'Society_Apartment'

    apart_num=fields.Integer("Apartment Number")
    apart_area = fields.Integer("Apartment area(sqft)")
    apart_status = fields.Selection([('unsold','Unsold'),('occupied','Occupied'),('available for rent','Available For Rent'),('rented','Rented')],"Apartment Number")
    # apart_type = fields.
    tower_id=fields.Many2one("society.tower","Tower_Name")
    parking_id=fields.Many2one("society.parking","Parking_code")
    floor_id=fields.Many2one("society.floor","Floors")
    # owner_id