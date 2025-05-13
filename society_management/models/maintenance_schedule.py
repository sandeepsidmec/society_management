from email.policy import default

from odoo import models, fields,api


class MaintenanceSchedule(models.Model):
    _name = 'society.m_schedule'
    _description = 'Society_Maintenance_Schedule'
    _rec_name = 'm_asset_name'

    m_asset_name=fields.Many2one("society.assets","Select Asset")
    m_date= fields.Date("Maintenance Date")
    # m_schedule
    m_status= fields.Selection([('pending', 'Pending'), ('completed', 'Completed'), ('overdue', 'OverDue')], "Status",default="pending")
    m_amt=fields.Float("Amount")
#   provider
    notes=fields.Text("Notes:")


    def action_pending(self):
        for record in self:
            record.m_status = 'pending'

    def action_completed(self):
        for record in self:
            record.m_status = 'completed'

    def action_overdue(self):
        for record in self:
            record.m_status = 'overdue'
