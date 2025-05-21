from odoo import models, fields, api


class AddServices(models.Model):
    _name = 'society.add.services'
    _description = 'Society_add_Services'
    _rec_name = 'contact'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    service_id=fields.Many2one("service.type.settings","Select Services")
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

    services_id = fields.Many2one('society.services', string="Linked Service")

    @api.model
    def create(self, vals):
        # Create the actual add.services record first
        record = super(AddServices, self).create(vals)

        # Check if a society.services record with the same service_id already exists
        services_record = self.env['society.services'].search([
            ('service_id', '=', record.service_id.id)
        ], limit=1)

        if not services_record:
            # Create new services record if not found
            services_record = self.env['society.services'].create({
                'service_id': record.service_id.id,
            })

        # Create service line under the found or new services record
        self.env['society.line.services'].create({
            'service': services_record.id,  # Link to society.services
            'service_id': record.service_id.id,
            'tower_id': record.tower_id.id,
            'floor_id': record.floor_id.id,
            'apartment_id': record.apartment_id.id,
            'contact': record.contact,
            'contact_no': record.contact_no,
            'company': record.company,
            'website': record.website,
            'frequency': record.frequency,
            'price': record.price,
            'desc': record.desc,
            'status': record.status,
            'photo': record.photo,
            'help': record.help,
        })

        return record


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