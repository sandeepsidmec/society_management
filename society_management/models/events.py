from email.policy import default

from odoo import models, fields, api


class Events(models.Model):
    _name = 'society.events'
    _description = 'Society_Events'
    _rec_name = 'event_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    event_name=fields.Char("Event Name")
    where=fields.Char("Where")
    e_desc=fields.Text("Description")
    start=fields.Datetime("Starts On")
    end= fields.Datetime("Ends  On")
    s_date=fields.Char("Start Date & Time",compute="date_time")
    e_date = fields.Char("End Date & Time", compute="date_time")
    e_status=fields.Selection([('pending','Pending'),('completed','Completed'),('cancelled','Cancelled')],"Status")
    role = fields.Selection(selection=[('role', 'Role'),('user', 'User')],default='role')
    group_ids = fields.Many2many(
            'res.groups',
            string='Role',
            domain="[('name', 'in', ['Society_Admin','Owner', 'Tenant'])]"
        )
    e_users=fields.Many2one("society.user","Name")


    def date_time(self):
        for i in self:
            if i.start:
                i.s_date = i.start.strftime("%d %B %Y, %I:%M %p")
            else:
                i.s_date = False
            if i.end:
                i.e_date = i.end.strftime("%d %B %Y, %I:%M %p")
            else:
                i.e_date = False



    def action_pending(self):
        for record in self:
            record.e_status = 'pending'

    def action_completed(self):
        for record in self:
            record.e_status = 'completed'

    def action_cancelled(self):
        for record in self:
            record.e_status = 'cancelled'


