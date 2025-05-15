from email.policy import default

from odoo import models, fields,api

class Apartment(models.Model):
    _name = 'society.apartment'
    _description = 'Society_Apartment'
    _rec_name = 'apart_num'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    apart_num=fields.Char("Apartment Number",tracking=True)
    apart_area = fields.Integer("Apartment area(sqft)")
    l_apart_area = fields.Char("Apartment area(sqft)",compute="area")
    apart_status = fields.Selection([('unsold','Unsold'),('availabe_for_rent','Available For Rent'),('occupied','Occupied')],"Apartment status",default='unsold')
    apart_type_id = fields.Many2one("apartment.type.settings","Apartment type")
    tower_id =fields.Many2one("society.tower","Tower_Name")
    parking_id=fields.Many2one("society.parking","Parking_code")
    floor_id=fields.Many2one("society.floor","Floors")
    owner_id=fields.Many2one("society.owner","Select Owner")

    tenant_id = fields.Many2one("society.tenant", string="Current Tenant", compute="_compute_tenant", store=True)

    def _compute_tenant(self):
        for rec in self:
            rent = self.env['society.rent'].search(
                [('r_apart_id', '=', rec.id), ('r_tenant_id', '!=', False)],
                order='id desc', limit=1
            )
            rec.tenant_id = rent.r_tenant_id if rent else False

    def area(self):
        settings = self.env['maintenance.settings'].search([], limit=1)
        unit = settings.unit_name or '' # if we dont use --(or '') then if unit name not given it returns false
        for i in self:
            if i.apart_area:
                i.l_apart_area=f"{i.apart_area} {unit}"
            else:
                i.l_apart_area = unit or ''

    def action_unsold(self):
        for record in self:
            record.apart_status = 'unsold'

    def action_occupied(self):
        for record in self:
            record.apart_status = 'occupied'
            if record.parking_id:
                record.parking_id.parking_status = 'allocated'

    def action_availabe_for_rent(self):
        for record in self:
            record.apart_status = 'availabe_for_rent'

