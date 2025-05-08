from odoo import models, fields


class SocietySettings(models.Model):
    _name = 'society.settings'

    name = fields.Char("name")
    country = fields.Many2one(comodel_name="res.country", string="Country")
    timezone = fields.Many2one(comodel_name="res.country", string="Time Zone")
    currency = fields.Many2one(comodel_name="res.currency", string="Currency")


class AppSettings(models.Model):
    _name = 'society_society.settings'


    name = fields.Char("Name")
    email = fields.Char(string="Email")
    phone = fields.Integer(string="Phone Number")
    address = fields.Text("Address")
