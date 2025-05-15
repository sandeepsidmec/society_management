from odoo import models, fields, api


class BookAmenities(models.Model):
    _name = 'society.book_amenities'
    _description = 'Society_Book_Amenities'
    _rec_name = 'b_amenity_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # bid=fields.Char("")
    b_amenity_id = fields.Many2one("society.amenities", "Amenity Name", tracking=True)
    # booked_by=
    booking_date = fields.Date("Booking Date")
    # booking_time = fields.Selection([
    #     (str(i), str(i)) for i in range(b_amenity_id.start_time,b_amenity_id.end_time,b_amenity_id.slot_time)])
    slot_time = fields.Integer("Slot Time")
    b_no_of_per = fields.Integer("Number of Persons")




