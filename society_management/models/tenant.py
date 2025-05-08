
from odoo import models, fields

class Tenant(models.Model):
    _name = 'society.tenant'
    _description = 'Society_Tenant'

    t_name= fields.Many2one("res.partner",string=" Full Name", required=True)
    t_email= fields.Char(string=" Email_address", required=True)
    t_phone= fields.Integer(string=" Phone Number")
    t_status= fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],string="Status")
    t_photo=fields.Binary("photo_upload")


class Rent(models.Model):
    _name="society.rent"
    _description = 'Society_Rent'

    # apart_number=fields.Many2one("Apartment Number")
    # tenant_name=fields.