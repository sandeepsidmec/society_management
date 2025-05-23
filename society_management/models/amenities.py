from odoo import models, fields,api
from datetime import datetime


class Amenities(models.Model):
    _name = 'society.amenities'
    _description = 'Society_Amenities'
    _rec_name = 'amenity_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    amenity_name=fields.Char("Amenity Name", tracking=True)
    amenity_status=fields.Selection([('available','Available'),('not_available','Not Available')],default="not_available",string="Amenity Status")
    booking_req = fields.Boolean("Booking Required")
    l_booking_req=fields.Char("Booking Required",compute="booking")
    start_time=fields.Datetime("Start Time")# only time field ???
    end_time = fields.Datetime("End Time")
    slot_time=fields.Integer("Slot Time(Mins)")
    l_slot_time=fields.Text("Slot Timing",compute="booking")
    mul_booking=fields.Boolean("Multiple Bookings Allowed")
    l_mul_booking = fields.Text("Multiple Bookings Allowed",compute="mul_bookings")
    no_of_per=fields.Integer("Number of Persons allowed per Booking")


    def booking(self):
        for i in self:
            if i.booking_req:
                i.l_booking_req=f"Yes"
                i.l_slot_time=f"Start time:{i.start_time.strftime("%d %B %Y, %I:%M %p")}\n End time:{i.end_time.strftime("%d %B %Y, %I:%M %p")}\n Slot time:{i.slot_time}"
            else:
                i.l_booking_req = f"No"
                i.l_slot_time = ""

    def mul_bookings(self):
        for i in self:
            if i.mul_booking:
                i.l_mul_booking = f"Multiple Bookings Allowed:Yes\nMaximum Persons:{i.no_of_per}"
            else:
                i.l_mul_booking = f"No"

    def action_available(self):
        for record in self:
            record.amenity_status = 'available'

    def action_not_available(self):
        for record in self:
            record.amenity_status = 'not_available'





