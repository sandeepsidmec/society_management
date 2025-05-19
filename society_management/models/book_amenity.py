from odoo import models, fields, api
from datetime import timedelta

class BookAmenities(models.Model):
    _name = 'society.book_amenities'
    _description = 'Society Book Amenities'
    _rec_name = 'b_amenity_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    b_amenity_id = fields.Many2one("society.amenities", "Amenity Name", tracking=True)
    booking_date = fields.Date("Booking Date")
    b_no_of_per = fields.Integer("Number of Persons")
    booking_time = fields.Char("Booking Time")
    available_times = fields.Selection([], string="Available Time Slots", compute="_compute_available_times", store=False)
    start = fields.Char("Start Time", compute="_compute_times")
    end = fields.Char("End Time", compute="_compute_times")

    @api.depends('b_amenity_id')
    def _compute_times(self):
        for rec in self:
            if rec.b_amenity_id:
                rec.start = rec.b_amenity_id.start_time.strftime("%I:%M %p") if rec.b_amenity_id.start_time else ''
                rec.end = rec.b_amenity_id.end_time.strftime("%I:%M %p") if rec.b_amenity_id.end_time else ''
            else:
                rec.start = ''
                rec.end = ''

    @api.depends('b_amenity_id')
    def _compute_available_times(self):
        for rec in self:
            times = []
            if rec.b_amenity_id and rec.b_amenity_id.start_time and rec.b_amenity_id.end_time:
                start = rec.b_amenity_id.start_time
                end = rec.b_amenity_id.end_time
                slot_minutes = rec.b_amenity_id.slot_time or 30

                while start < end:
                    time_str = start.strftime('%I:%M %p')
                    times.append((time_str, time_str))
                    start += timedelta(minutes=slot_minutes)

            rec.available_times = False  # Required to clear previous values
            rec._fields['available_times'].selection = times

    @api.onchange('available_times')
    def _onchange_available_times(self):
        self.booking_time = self.available_times
