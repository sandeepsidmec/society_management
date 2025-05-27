# models/society_dashboard.py
from odoo import models, fields, api

class SocietyDashboard(models.TransientModel):
    _name = 'society.dashboard'
    _description = 'Society Dashboard'
    _rec_name = 'name'

    name = fields.Char(string="Name", compute="_compute_name", readonly=True)
    tower_count = fields.Integer(compute="_compute_counts")
    owner_count = fields.Integer(compute="_compute_counts")
    tenant_count = fields.Integer(compute="_compute_counts")
    apartment_count = fields.Integer(compute="_compute_counts")
    maintenance_due_count = fields.Integer(compute="_compute_counts")
    amenities_ids = fields.Many2many('society.book_amenities', string='Amenities', compute='_compute_amenities')
    rent_ids = fields.Many2many('society.rent', string='Rent Payments', compute='_compute_rents')
    ticket_ids = fields.Many2many('society.ticket', string='', compute='_compute_tickets')
    bill_ids = fields.Many2many('society.utility', string='', compute='_compute_bills')
    cbill_ids = fields.Many2many('society.common_area', string='', compute='_compute_common_bills')
    clock_ids = fields.Many2many('society.clock', string='', compute='_compute_clock')

    @api.depends()
    def _compute_name(self):
        for record in self:
            record.name = "Dashboard"

    def _compute_amenities(self):
        for rec in self:
            # Get all amenities (or filter as needed)
            amenities = self.env['society.book_amenities'].search([])
            rec.amenities_ids = amenities.ids

    def _compute_rents(self):
        for rec in self:
            # Get recent rent payments
            rents = self.env['society.rent'].search([], limit=10, order='id desc')
            rec.rent_ids = rents.ids

    def _compute_tickets(self):
        for rec in self:
            # Get recent tickets
            tickets = self.env['society.ticket'].search([], limit=10, order='id desc')
            rec.ticket_ids = tickets.ids

    def _compute_bills(self):
        for rec in self:
            # Get recent bills
            bills = self.env['society.utility'].search([], limit=10, order='id desc')
            rec.bill_ids = bills.ids


    def _compute_common_bills(self):
        for rec in self:
            # Get recent bills
            cbills = self.env['society.common_area'].search([], limit=10, order='id desc')
            rec.cbill_ids = cbills.ids

    def _compute_clock(self):
        for rec in self:
            # Get recent bills
            clock = self.env['society.clock'].search([], limit=10, order='id desc')
            rec.clock_ids = clock.ids

    @api.depends()
    def _compute_counts(self):
        for rec in self:
            rec.tower_count = self.env['society.tower'].search_count([])
            rec.owner_count = self.env['society.owner'].search_count([])
            rec.tenant_count = self.env['society.tenant'].search_count([])
            rec.apartment_count = self.env['society.apartment'].search_count([])
            rec.maintenance_due_count = self.env['society.maintenance'].search_count([])



    def action_open_towers(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'society.tower',
            'view_mode': 'list,form',
            'target': 'current',
        }

    def action_open_owners(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'society.owner',
            'view_mode': 'list,form',
            'target': 'current',
        }

    def action_open_tenants(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'society.tenant',
            'view_mode': 'list,form',
            'target': 'current',
        }

    def action_open_apartments(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'society.apartment',
            'view_mode': 'list,form',
            'target': 'current',
        }

    def action_open_maintenance(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'society.maintenance',
            'view_mode': 'list,form',
            'target': 'current',
        }