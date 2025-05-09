
from odoo import models, fields

class Apartment(models.Model):
    _name = 'society.apartment'
    _description = 'Society_Apartment'
    _rec_name = 'apart_num'

    apart_num=fields.Char("Apartment Number")
    apart_area = fields.Integer("Apartment area(sqft)")
    apart_status = fields.Selection([('unsold','Unsold'),('occupied','Occupied'),('available for rent','Available For Rent'),('rented','Rented')],"Apartment status")
    apart_type = fields.Many2one("apartment.type.settings","Apartment type")
    tower_id=fields.Many2one("society.tower","Tower_Name")
    parking_id=fields.Many2one("society.parking","Parking_code")
    floor_id=fields.Many2one("society.floor","Floors")
    owner_id=fields.Many2one("society.owner","Select Owner")