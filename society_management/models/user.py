
from odoo import models, fields,api

class User(models.Model):
    _name = 'society.user'
    _description = 'Society_User'
    _rec_name = "user_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    user_id= fields.Many2one("res.users",string=" Full Name", required=True)
    email= fields.Char(string=" Email_address", required=True)
    phone= fields.Char(string=" Phone Number")
    role= fields.Char(string="Role")
    status= fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],string="Status")
    photo=fields.Binary("photo_upload")

    @api.onchange('user_id')
    def mail(self):
        for i in self:
            if i.user_id:
                i.email = i.user_id.login

    def action_active(self):
        for record in self:
            record.status = 'active'

    def action_inactive(self):
        for record in self:
            record.status = 'inactive'


