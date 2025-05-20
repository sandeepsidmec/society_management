from odoo import models, fields, api

class AddServices(models.Model):
    _name = 'society.add_services'
    _description = 'Society_Add_Services'
    _rec_name = 'service'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    service=fields.Char("Services")

class Services(models.Model):
        _name = 'society.services'
        _description = 'Society_Services'
        _rec_name = 'service_id'
        _inherit = ['mail.thread', 'mail.activity.mixin']

        service_id = fields.Many2one("society.add_services", "Select Services")
        service_lines=fields.One2many("society.maid_services",inverse_name="service_id",string="Services")



class MaidServices(models.Model):
    _name = 'society.maid_services'
    _description = 'Society_Maid_Services'
    _rec_name = 'service_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    service_id=fields.Many2one("society.add_services","Select Services")
    tower_id=fields.Many2one("society.tower","Select Tower")
    floor_id=fields.Many2one("society.floor","Select Floor")
    apartment_id=fields.Many2one("society.apartment","Select Apartment")
    contact=fields.Char("Contact Person Name")
    contact_no= fields.Char("Contact Number")
    company=fields.Char("Company Name")
    website= fields.Char("Website Link")
    frequency = fields.Selection([
            ('visit', 'Per Visit'),
            ('hour', 'Per Hour'),
            ('day', 'Per Day'),
            ('week', 'Per Week'),
            ('month', 'Per Month'),
            ('year', 'Per Year'),
        ],string="Payment Frequency",default='visit')
    price=fields.Float("Price")
    desc=fields.Text("Description")
    status=fields.Selection([('available','Available'),('not_available','Not Available')])
    photo=fields.Binary("Upload Photo")
    help= fields.Boolean(string="Daily Help Availability")
    l_help=fields.Char("Daily Help Availability",compute="help_avail")
    l_price=fields.Text("Price",compute="lprice")

    def help_avail(self):
        for i in self:
            if i.help:
                i.l_help = "Yes"
            else:
                i.l_help = "No"

    def lprice(self):
        for i in self:
            if i.price and i.frequency:
                i.l_price = f"${i.price}\n{i.frequency}"
            else:
                i.l_price = "No"




