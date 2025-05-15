from odoo import models, fields, api
from datetime import datetime

class NoticeBoard(models.Model):
    _name = 'society.notice_board'
    _description = 'Society_Notice_Board'
    _rec_name = 'title'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title=fields.Char("Title")
    desc=fields.Text("Description")
    # role=fields.Many2many("",string="Role")
    date=fields.Char("Date & Time",compute="date_time")

    def date_time(self):
        for i in self:
            i.date = str(datetime.now().strftime("%d %B %Y, %I:%M %p"))