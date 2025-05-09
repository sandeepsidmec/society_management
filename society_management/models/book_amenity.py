from odoo import models, fields,api

class BookAmenities(models.Model):
    _name = 'society.book_amenities'
    _description = 'Society_Book_Amenities'
    _rec_name = 'b_amenity_name'

    # bid=fields.Char("")
    b_amenity_name=fields.Many2one("society.amenities","Amenity Name")
    # booked_by=
    booking_date=fields.Date("Booking Date")
    # b_time
    slot_time = fields.Integer("Slot Time")
    b_no_of_per=fields.Integer("Number of Persons")