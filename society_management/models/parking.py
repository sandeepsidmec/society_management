
from odoo import models, fields

class Parking(models.Model):
    _name = 'society.parking'
    _description = 'Society_Parking'
    _rec_name = 'parking_code'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    parking_code=fields.Char("Parking Code")
    apart_id=fields.Many2one("society.apartment","Apartment Number")
    parking_status=fields.Selection([('allocated','Allocated'),('not_allocated','Not Allocated')],"Status",default="not_allocated")

    tenant_id = fields.Many2one("society.tenant", string="Current Tenant", compute="_compute_tenant", store=True)

    def _compute_tenant(self):
        for rec in self:
            rent = self.env['society.rent'].search(
                [('r_apart_id', '=', rec.id), ('r_tenant_id', '!=', False)],
                order='id desc', limit=1
            )
            rec.tenant_id = rent.r_tenant_id if rent else False

    def action_allocated(self):
        for record in self:
            record.parking_status = 'allocated'

    def action_not_allocated(self):
        for record in self:
            record.parking_status = 'not_allocated'
