from odoo import models, fields, api
from datetime import timedelta

class BookAmenities(models.Model):
    _name = 'society.book_amenities'
    _description = 'Society_Book_Amenities'
    _rec_name = 'b_amenity_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    b_amenity_id = fields.Many2one("society.amenities", "Amenity Name", tracking=True)
    booking_date = fields.Date("Booking Date")
    b_no_of_per = fields.Integer("Number of Persons")
    booking_time = fields.Selection([], string="Booking Time")  # Empty for now
    start = fields.Char("Start Time", compute="_compute_times")
    end = fields.Char("End Time", compute="_compute_times")

    @api.depends('b_amenity_id')
    def _compute_times(self):
        for i in self:
            if i.b_amenity_id:
                i.start = i.b_amenity_id.start_time.strftime("%I:%M %p") if i.b_amenity_id.start_time else ''
                i.end = i.b_amenity_id.end_time.strftime("%I:%M %p") if i.b_amenity_id.end_time else ''
            else:
                i.start = ''
                i.end = ''

    @api.onchange('b_amenity_id')
    def _onchange_b_amenity_id(self):
        if self.b_amenity_id and self.b_amenity_id.start_time and self.b_amenity_id.end_time:
            start = self.b_amenity_id.start_time
            end = self.b_amenity_id.end_time
            slot_minutes = self.b_amenity_id.slot_time or 30  # Default 30 min

            time_slots = []
            while start + timedelta(minutes=slot_minutes) <= end:
                slot_str = start.strftime('%I:%M %p')
                time_slots.append((slot_str, slot_str))
                start += timedelta(minutes=slot_minutes)

            # Manually set selection field dynamically
            self.fields_get()['booking_time']['selection'] = time_slots
        else:
            self.fields_get()['booking_time']['selection'] = []