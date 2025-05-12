from odoo import models, fields,api

class IssueReport(models.Model):
    _name = 'society.issue_report'
    _description = 'Society_Issue_Report'
    _rec_name = 'issue_title'

    asset=fields.Many2one("society.assets","Select Asset")
    issue_title=fields.Char("Issue Title")
    state=fields.Selection([('pending','Pending'),('process','Process'),('resolved','Resolved')],default='pending',string="Issue Status")
    priority=fields.Selection([('low','Low'),('medium','Medium'),('high','High')],string='Priority')
    description=fields.Text("Issue Description")
    image=fields.Binary("Browse Image")