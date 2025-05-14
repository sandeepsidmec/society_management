from odoo import models, fields
from datetime import datetime
from odoo.exceptions import UserError

class OfflineReq(models.Model):
    _name = 'society.offline'
    _description = 'Society_Offline_Request'
    _rec_name = "r_tenant_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    req_apart_id=fields.Many2one("society.apartment","Apartment Number")
    r_tenant_id=fields.Many2one("society.tenant","Tenant Name")
    tot_cost=fields.Integer("Total Cost")
    r_month = fields.Selection([
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
    ], string='Rent For Month')
    r_year = fields.Selection([
        (str(y), str(y)) for y in range(2020, 2026)
    ], string='Rent For Year')
    m_y = fields.Char(string="Month & Year", compute="_compute_rent_")

    status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], string="Status", default='unpaid')



    def _compute_rent_(self):
        for i in self:
            if i.r_month and i.r_year:
                i.m_y = f"{i.r_month} {i.r_year}"
            else:
                i.m_y =f"invalid"

    # def _get_month_year_options(self):
    #     from datetime import datetime
    #     now = datetime.now()
    #     return [('%02d-%d' % (m, y), '%s %d' % (datetime(1900, m, 1).strftime('%B'), y))
    #             for y in range(now.year - 2, now.year + 3)
    #             for m in range(1, 13)]

    # m_y = fields.Selection(_get_month_year_options, string="Month & Year", required=True)


    def confirm_appointment(self):
        for rec in self:

            # Check if rent already paid
            existing_rent = self.env["society.rent"].search([
                ('r_apart_id', '=', rec.req_apart_id.id),
                ('r_month', '=', rec.r_month),
                ('r_year', '=', rec.r_year),
                ('r_status', '=', 'paid')
            ], limit=1)

            if existing_rent:
                raise UserError("Rent already paid for this apartment and month.")

            # If not paid, create a new rent record
            vals = {
                'r_apart_id': rec.req_apart_id.id,
                'r_month': rec.r_month,
                'r_year': rec.r_year,
                'rent_amt': rec.tot_cost,
                'r_tenant_id': rec.r_tenant_id.id,
                'r_date': fields.Date.today(),
                'r_status': 'paid',  # explicitly marking it as paid
            }
            self.env["society.rent"].create(vals)

            rec.status = 'paid'  # update status on the wizard or source model

    def action_paid(self):
        for record in self:
            record.status = 'paid'

    def action_unpaid(self):
        for record in self:
            record.status = 'unpaid'

