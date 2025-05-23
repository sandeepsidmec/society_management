from odoo import models, fields


class MaintenanceSettings(models.Model):
    _name = 'maintenance.settings'
    _rec_name = "cost_type"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    cost_type = fields.Selection([('fixed','fixed_value'),('unit','unit_type')],"Cost Type")
    apartment_type = fields.Many2one("apartment.type.settings", "Apartment Type")
    unit_value = fields.Float("Unit Value ($)")
    unit_name = fields.Char("Unit Name")
    unit_value2 = fields.Char("Unit Value (₹)")
    maintenance_lines = fields.One2many("maintenance.settings.lines", "maintenance", "Order lines")


class MaintenanceSettingsLines(models.Model):
    _name = 'maintenance.settings.lines'
    _rec_name = "apartment_type"

    apartment_type = fields.Many2one("apartment.type.settings", "Apartment Type")
    unit_value = fields.Float("Unit Value ($)")

    maintenance = fields.Many2one("maintenance.settings", "maintenance")







