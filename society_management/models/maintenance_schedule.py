from odoo import models, fields,api


class MaintenanceSchedule(models.Model):
    _name = 'society.m_schedule'
    _description = 'Society_Maintenance_Schedule'
    _rec_name = 'm_asset_name'

    m_asset_name=fields.Many2one("society.assets","Select Asset")
    m_date= fields.Date("Maintenance Date")
    # m_schedule
    m_status= fields.Selection([('pending', 'Pending'), ('completed', 'Completed'), ('overdue', 'OverDue')], "Status")
    m_amt=fields.Float("Amount")
#   provider
    notes=fields.Text("Notes:")
