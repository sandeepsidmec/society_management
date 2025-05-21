from odoo import models,fields,api


class Services(models.Model):
    _name = 'society.services'
    _description = 'Society_Services'
    _rec_name = 'service_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    service_id = fields.Many2one("service.type.settings", "Select Services")
    service_lines = fields.One2many("society.line.services", "service", string="Services")

    @api.model
    def create(self, vals):
        # Create the society.services record
        record = super(Services, self).create(vals)

        # Loop through each service line (fully created)
        for line in record.service_lines:
            existing = self.env["society.add.services"].search([
                ('service_id', '=', line.service_id.id),
                ('apartment_id', '=', line.apartment_id.id)
            ], limit=1)
            if existing:
                continue

            # Create new add.services record
            self.env["society.add.services"].create({
                'service_id': line.service_id.id,
                'tower_id': line.tower_id.id,
                'floor_id': line.floor_id.id,
                'apartment_id': line.apartment_id.id,
                'contact': line.contact,
                'contact_no': line.contact_no,
                'company': line.company,
                'website': line.website,
                'frequency': line.frequency,
                'price': line.price,  # ✅ Works here because the line is fully created
                'desc': line.desc,
                'status': line.status,
                'photo': line.photo,
                'help': line.help,
                'services_id': record.id,
            })

        return record


    # @api.model
    # def create(self, vals):
    #     # Create the society.services record
    #     record = super(Services, self).create(vals)
    #
    #     # Loop through each service line and create corresponding add.services records
    #     for line in record.service_lines:
    #         # Optional: check if such a record already exists (to avoid duplicates)
    #         existing = self.env["society.add.services"].search([
    #             ('service_id', '=', line.service_id.id),
    #             ('apartment_id', '=', line.apartment_id.id)
    #         ], limit=1)
    #         if existing:
    #             continue  # skip duplicate
    #
    #         # Create new society.add.services record
    #         self.env["society.add.services"].create({
    #             'service_id': line.service_id.id,
    #             'tower_id': line.tower_id.id,
    #             'floor_id': line.floor_id.id,
    #             'apartment_id': line.apartment_id.id,
    #             'contact': line.contact,
    #             'contact_no': line.contact_no,
    #             'company': line.company,
    #             'website': line.website,
    #             'frequency': line.frequency,
    #             'price': line.price,
    #             'desc': line.desc,
    #             'status': line.status,
    #             'photo': line.photo,
    #             'help': line.help,
    #             'services_id': record.id,  # Link back to society.services
    #         })
    #
    #     return record


class ServicesLines(models.Model):
    _name = 'society.line.services'
    _description = 'Society_line_Services'
    _rec_name = 'contact'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    service=fields.Many2one("society.services","Select Services")
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