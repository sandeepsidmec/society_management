from odoo import fields, models


class Clock(models.Model):
    _name = 'society.clock'
    _description = 'Society_Clock'
    _rec_name = 'provider_id'

    service_id = fields.Many2one("service.type.settings", String="Service Person")
    provider_id = fields.Many2one("society.add.services", "Service Provider")
    clock_in = fields.Datetime("Clock_In")
    clock_out = fields.Datetime("Clock_Out")