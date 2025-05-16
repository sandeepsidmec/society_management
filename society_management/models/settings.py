from odoo import models, fields


class AppSettings(models.Model):
    _name = 'society.settings'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char("name")
    country_id = fields.Many2one(comodel_name="res.country", string="Country")
    timezone_id = fields.Many2one(comodel_name="res.country", string="Time Zone")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")


class SocietySettings(models.Model):
    _name = 'society_society.settings'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'


    name = fields.Char("Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone Number")
    address = fields.Text("Address")
