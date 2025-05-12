
from odoo import models, fields

class User(models.Model):
    _name = 'society.user'
    _description = 'Society_User'

    name= fields.Many2one("res.users",string=" Full Name", required=True)
    email= fields.Char(string=" Email_address", required=True)
    phone= fields.Char(string=" Phone Number")
    role= fields.Char(string="Role")
    status= fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],string="Status")
    photo=fields.Binary("photo_upload")

