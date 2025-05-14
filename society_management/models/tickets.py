from odoo import models, fields,api

class Tickets(models.Model):
    _name = 'society.ticket'
    _description = 'Society_Ticket'
    _rec_name = 'tenant_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    name = fields.Char("Ticket sequence", default="New")
    tenant_id= fields.Many2one("res.partner",string="Requested By", required=True)
    ticket_type_id= fields.Many2one("ticket.type.settings","Type")
    owner_id= fields.Many2one("society.owner","Agent")
    status = fields.Selection([('open','Open'),('pending','Pending'),('resolved','Resolved'),('closed','Closed')],"Status",default='open')
    subject = fields.Char("Subject")
    description =fields.Text("Description")
    file = fields.Binary("File Upload ")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('society.ticket') or 'New'
        return super(Tickets,self).create(vals)

    # def compute_name(self):
    #     for rec in self:
    #         rec.name = self.env['ir.sequence'].next_by_code('society.ticket')

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


