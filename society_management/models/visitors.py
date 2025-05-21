from odoo import models, fields, api
from datetime import datetime

class Visitors(models.Model):
    _name = 'society.visitors'
    _description = 'Society_Visitors'
    _rec_name = 'visitor_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    visitor_name=fields.Char("Visitor Name")
    v_tower_id=fields.Many2one("society.tower","Select Tower")
    v_floor_id = fields.Many2one("society.floor","Select Floor")
    v_apart_id = fields.Many2one("society.apartment","Select Apartment")
    address=fields.Text("Visitor Address")
    mobile=fields.Char("Mobile Number")
    v_type=fields.Many2one("visitor.type.settings","Visitor Type")
    purpose=fields.Char("Purpose of Visit")
    date_visit=fields.Datetime("Date of Visit")
    date_exit = fields.Datetime("Date of Exit")
    v_photo=fields.Binary("Upload Photo")
    v_status=fields.Selection([("allow","Allow"),("deny","Deny")],"Status")

    tenant_id = fields.Many2one("society.tenant", string="Current Tenant", compute="_compute_tenant", store=True)

    # def _compute_tenant(self):
    #     for rec in self:
    #         rent = self.env['society.rent'].search(
    #             [('r_apart_id', '=', rec.id), ('r_tenant_id', '!=', False)],
    #             order='id desc', limit=1
    #         )
    #         rec.tenant_id = rent.r_tenant_id if rent else False

    @api.depends('v_apart_id.tenant_id')
    def _compute_tenant(self):
        for rec in self:
            rec.tenant_id = rec.v_apart_id.tenant_id if rec.v_apart_id else False


    def action_allow(self):
        for record in self:
            record.v_status = 'allow'

    def action_deny(self):
        for record in self:
            record.v_status = 'deny'



