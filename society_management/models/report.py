from odoo import models, fields, api
from datetime import datetime

class Report(models.Model):
    _name = 'society.reports'
    _description = 'Society_Reports'
    _rec_name = 'report'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    society_id=fields.Many2one(comodel_name="society_society.settings", string="society_id")
    r_month=fields.Many2one(comodel_name="society.rent", string="r_month")
    tower_id=fields.Many2one(comodel_name="society.tower", string="Tower")
    report = fields.Selection(selection=[('monthly', 'Monthly'), ('yearly', 'Yearly')],default="monthly")
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
    ], string='Month')
    year = fields.Selection([
        (str(y), str(y)) for y in range(2020, 2026)])

    def pdf_report(self):
        return self.env.ref('society_management.report_maintenance_pdf').report_action(self)

    def mon_pdf_report(self):
        return self.env.ref('society_management.report_monthly_maintenance_pdf').report_action(self)

    def get_yearly_summary(self):
        if not self.year:
            return {}
        # Prepare months
        payment_records = self.env['society.rent'].search([('r_year', '=', self.year)])
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Create dictionary for each month
        summary = {month: {'count': 0, 'amount': 0,'pending':0} for month in months}

        for record in payment_records:
            if record.r_month:
                month = record.r_month[:3].capitalize()  # e.g., 'May'
                if month in summary:
                    summary[month]['count'] += 1
                    if record.r_status=='paid':
                        summary[month]['amount'] += record.rent_amt
                    else:
                        summary[month]['pending'] += record.rent_amt


        return summary
    def get_monthly_summary(self):
        if not self.year:
            return {}
        # Prepare months
        payment_records = self.env['society.rent'].search([('r_year', '=', self.year)])
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Create dictionary for each month
        summary = {month: {'amount': 0,'pending':0} for month in months}

        for record in payment_records:
            if record.r_month:
                month = record.r_month[:3].capitalize()  # e.g., 'May'
                if month in summary:
                    if record.r_status=='paid':
                        summary[month]['amount'] += record.rent_amt
                    else:
                        summary[month]['pending'] += record.rent_amt


        return summary