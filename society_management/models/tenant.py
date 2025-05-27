from odoo import models, fields,api

class Tenant(models.Model):
    _name = 'society.tenant'
    _description = 'Society_Tenant'
    _rec_name = 'tenant_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    tenant_id= fields.Many2one("res.partner",string=" Full Name", required=True)
    t_email= fields.Char(string=" Email_address", required=True)
    t_phone= fields.Char(string=" Phone Number")
    t_status= fields.Selection([('inactive', 'Inactive'), ('active', 'Active')],string="Status", default="inactive")
    t_photo=fields.Binary("photo_upload")
    apartment_id=fields.Many2one("society.apartment","Apartment ID")

    owner_id = fields.Many2one("society.owner", string="Apartment Owner", compute="_compute_owner", store=True)


    def action_active(self):
        for record in self:
            record.t_status = 'active'

    def action_inactive(self):
        for record in self:
            record.t_status = 'inactive'

    @api.onchange('tenant_id')
    def mail(self):
        for i in self:
            if i.tenant_id:
                i.t_email=i.tenant_id.email
