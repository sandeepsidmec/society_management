
from odoo import models, fields

class Apartment(models.Model):
    _name = 'society.apartment'
    _description = 'Society_Apartment'
    _rec_name = 'apart_num'

    apart_num=fields.Char("Apartment Number")
    apart_area = fields.Integer("Apartment area(sqft)")
    l_apart_area = fields.Char("Apartment area(sqft)",compute="area")
    apart_status = fields.Selection([('unsold','Unsold'),('occupied','Occupied'),('available for rent','Available For Rent'),('rented','Rented')],"Apartment status")
    apart_type = fields.Many2one("apartment.type.settings","Apartment type")
    tower_id=fields.Many2one("society.tower","Tower_Name")
    parking_id=fields.Many2one("society.parking","Parking_code")
    floor_id=fields.Many2one("society.floor","Floors")
    owner_id=fields.Many2one("society.owner","Select Owner")

    def area(self):
        settings = self.env['maintenance.settings'].search([], limit=1)
        unit = settings.unit_name or '' # if we dont use --(or '') then if unit name not given it returns false
        for i in self:
            if i.apart_area:
                i.l_apart_area=f"{i.apart_area} {unit}"
            else:
                i.l_apart_area = unit or ''

