from odoo import models, fields,api

class Maintenance(models.Model):
    _name = 'society.maintenance'
    _description = 'Society_Maintenance'
    # _rec_name = 'amenity_name'

    m_year = fields.Date("Year")
    m_month = fields.Date("Month")
    payment_due = fields.Date("Payment Due Date")
    state = fields.Selection([('draft', 'Draft'), ('publish', 'Published')],"Status",default="draft")
    add_cost = fields.Char("Total Additional Cost")

    cost_title = fields.Char("Title")
    cost_amount = fields.Float("Amount (Per Apartment)")
    show_additional_cost = fields.Boolean("Show Additional Cost Fields")

    m_month = fields.Selection([
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ], string='Month')
    m_year = fields.Selection([
        (str(y), str(y)) for y in range(2020, 2026)
    ], string='Year')


    def toggle_add_cost_fields(self):
        self.show_additional_cost = not self.show_additional_cost



    def action_publish(self):
        for record in self:
            record.state = 'publish'

    def action_draft(self):
        for record in self:
            record.state = 'draft'


