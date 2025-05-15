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

