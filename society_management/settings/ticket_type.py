from odoo import models, fields


class TicketTypeSettings(models.Model):
    _name = 'ticket.type.settings'
    _rec_name = "ticket_type"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ticket_type = fields.Char("Ticket Type")
