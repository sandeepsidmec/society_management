from odoo import models, fields


class TicketTypeSettings(models.Model):
    _name = 'ticket.type.settings'
    _rec_name = "ticket_type"

    ticket_type = fields.Char("Ticket Type")
