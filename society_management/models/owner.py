from odoo import models, fields

class Owner(models.Model):
    _name = 'society.owner'
    _description = 'Society_Owner'
    _rec_name = "o_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']



    o_name= fields.Char(string=" Full Name", required=True)
    o_email= fields.Char(string=" Email_address", required=True)
    o_phone= fields.Char(string=" Phone Number")
    o_status= fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],string="Status")
    o_tower_id=fields.Many2one("society.tower","Select_Tower")
    o_floor_id=fields.Many2one("society.floor","Select_Floor")
    owner_apart_ids=fields.Many2many("society.apartment",string="Apartment Number")
    o_photo=fields.Binary("photo_upload")


    def action_active(self):
        for record in self:
            record.o_status = 'active'

    def action_inactive(self):
        for record in self:
            record.o_status = 'inactive'
