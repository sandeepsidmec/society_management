from odoo import models, fields


class MaintenanceSettings(models.Model):
    _name = 'maintenance.settings'
    _rec_name = "cost_type"


    cost_type = fields.Selection([('fixed','fixed_value'),('unit','unit_type')],"Cost Type")
    apartment_type = fields.Many2one("apartment.type.settings", "Apartment Type")
    unit_value = fields.Float("Unit Value ($)")
    unit_name = fields.Char("Unit Name")
    unit_value2 = fields.Char("Unit Value (₹)")






