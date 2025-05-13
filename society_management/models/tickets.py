from odoo import models, fields,api

class Tickets(models.Model):
    _name = 'society.ticket'
    _description = 'Society_Ticket'
    _rec_name = 't_name'


    t_name= fields.Many2one("res.partner",string="Requested By", required=True)
    type= fields.Many2one("ticket.type.settings","Type")
    owner= fields.Many2one("society.owner","Agent")
    status = fields.Selection([('open','Open'),('pending','Pending'),('resolved','Resolved'),('closed','Closed')],"Status",default='open')
    subject = fields.Char("Subject")
    description =fields.Text("Description")
    file = fields.Binary("File Upload ")

    def action_open(self):
        for record in self:
            record.status = 'open'

    def action_pending(self):
        for record in self:
            record.status = 'pending'

    def action_resolved(self):
        for record in self:
            record.status = 'resolved'

    def action_closed(self):
        for record in self:
            record.status = 'closed'


