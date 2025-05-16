from odoo import models, fields, api
from datetime import datetime

class Report(models.Model):
    _name = 'society.reports'
    _description = 'Society_Reports'
    _rec_name = 'report'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    report = fields.Selection(selection=[('monthly', 'Monthly'), ('yearly', 'Yearly')])
    month = fields.Selection([
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ], string='Rent For Month')
    year = fields.Selection([
        (str(y), str(y)) for y in range(2020, 2026)])

    def pdf_report(self):
        pass