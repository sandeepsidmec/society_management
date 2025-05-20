from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import timedelta

class BookAmenities(models.Model):
    _name = 'society.book_amenities'
    _description = 'Society_Book_Amenities'
    _rec_name = 'b_amenity_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    b_amenity_id = fields.Many2one("society.amenities", "Amenity Name", tracking=True)
    booking_date = fields.Date("Booking Date")
    b_no_of_per = fields.Integer("Number of Persons")
    booking_time = fields.Datetime("Booking Time")
    start = fields.Char("Start Time")
    end = fields.Char("End Time")

    @api.constrains('booking_time', 'b_amenity_id')
    def _check_slot_overlap(self):
        for rec in self:
            if not rec.booking_time or not rec.b_amenity_id or not rec.b_amenity_id.slot_time:
                continue

            slot_duration = timedelta(minutes=rec.b_amenity_id.slot_time)
            new_start = rec.booking_time
            new_end = new_start + slot_duration

            overlapping = self.env['society.book_amenities'].search([
                ('id', '!=', rec.id),
                ('b_amenity_id', '=', rec.b_amenity_id.id),
                ('booking_time', '!=', False),
            ])

            for existing in overlapping:
                existing_start = existing.booking_time
                existing_end = existing_start + timedelta(minutes=existing.b_amenity_id.slot_time)

                if (new_start < existing_end and new_end > existing_start):
                    raise ValidationError("Selected time slot overlaps with an existing booking.")
