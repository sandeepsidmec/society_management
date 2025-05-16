from odoo import models, fields, api
from datetime import datetime

class NoticeBoard(models.Model):
    _name = 'society.notice_board'
    _description = 'Society_Notice_Board'
    _rec_name = 'title'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title=fields.Char("Title")
    desc=fields.Text("Description")
    date=fields.Char("Date & Time",compute="date_time")
    group_ids = fields.Many2many(
            'res.groups',
            string='Role',
            domain="[('name', 'in', ['Society_Admin','Owner', 'Tenant'])]"
        )


    def date_time(self):
        for i in self:
            i.date = str(datetime.now().strftime("%d %B %Y, %I:%M %p"))