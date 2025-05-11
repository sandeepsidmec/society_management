from odoo import models, fields

class Tenant(models.Model):
    _name = 'society.tenant'
    _description = 'Society_Tenant'
    _rec_name = 't_name'

    t_name= fields.Many2one("res.partner",string=" Full Name", required=True)
    t_email= fields.Char(string=" Email_address", required=True)
    t_phone= fields.Char(string=" Phone Number")
    t_status= fields.Selection([('active', 'Active'), ('inactive', 'Inactive')],string="Status")
    t_photo=fields.Binary("photo_upload")

