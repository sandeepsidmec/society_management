from odoo import models, fields,api
from datetime import datetime

class Rent(models.Model):
    _name = 'society.rent'
    _description = 'Society_Rent'
    _rec_name = "r_apart_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']



    r_apart_id=fields.Many2one("society.apartment","Apartment Number")
    r_tenant_id=fields.Many2one("society.tenant","Tenant Name")
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
    rent_for = fields.Char(string="Rent For", compute="_compute_rent_for")
    rent_amt = fields.Float("Rent Amount")
    r_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], "Status",default="unpaid")
    formatted_rent_amt = fields.Char(string="Rent Amount", compute="_compute_formatted_rent_amt", store=False)
    r_date = fields.Date("Payment Date",default=fields.Date.context_today)

    # @api.onchange('r_apart_id')
    # def rent_apart(self):
    #    for i in self:
    #        if i.r_apart_id:
    #             i.r_apart_id.apart_status = "occupied"



    def _compute_rent_for(self):
        for i in self:
            if i.r_month and i.r_year:
                i.rent_for = f"{i.r_month} {i.r_year}"
            else:
                i.rent_for =f"invalid"


    @api.onchange("r_apart_id")
    def onchange_r_apart_id(self):
        for i in self:
            i.r_tenant_id = i.r_tenant_id
            i.r_month=datetime.now().strftime('%B')
            i.r_year=str(datetime.now().year)

    @api.depends('rent_amt', 'r_apart_id', 'r_month', 'r_year')
    def _compute_formatted_rent_amt(self):
        settings = self.env['currency.settings'].search([], limit=1)
        for rec in self:
            total_amt = rec.rent_amt or 0.0

            # Parse month and year
            try:
                month_num = datetime.strptime(rec.r_month, "%B").month
                year_num = int(rec.r_year)
            except:
                rec.formatted_rent_amt = "Invalid Date"
                continue

            # --- Sum Utility Bills for Apartment ---
            utility_bills = self.env['society.utility'].search([
                ('u_apart_id', '=', rec.r_apart_id.id),
                ('u_bill_date', '!=', False)
            ])
            for bill in utility_bills:
                if bill.u_bill_date.month == month_num and bill.u_bill_date.year == year_num:
                    total_amt += bill.u_bill_amt or 0.0

            # --- Sum Common Area Bills for same month/year ---
            common_bills = self.env['society.common_area'].search([
                ('c_apart_id', '=', rec.r_apart_id.id),
                ('c_bill_date', '!=', False)
            ])
            for bill in common_bills:
                if bill.c_bill_date.month == month_num and bill.c_bill_date.year == year_num:
                    total_amt += bill.c_bill_amt or 0.0

            # --- Add Maintenance Cost for Month/Year ---
            maintenances = self.env['society.maintenance'].search([
                ('m_month', '=', rec.r_month),
                ('m_year', '=', rec.r_year),
                ('state', '=', 'publish'),
            ])

            for maintenance in maintenances:
                total_amt += maintenance.cost_amount or 0.0

            # --- Format ---
            if not settings:
                rec.formatted_rent_amt = str(total_amt)
                continue

            formatted = f"{total_amt:,.{settings.decimal_places}f}"
            formatted = formatted.replace(",", "TMP").replace(".", settings.decimal_separator).replace("TMP",
                                                                                                       settings.thousand_separator)
            if settings.symbol_position == 'left':
                rec.formatted_rent_amt = f"{settings.currency_symbol}{formatted}"
            else:
                rec.formatted_rent_amt = f"{formatted}{settings.currency_symbol}"



    def action_paid(self):
        for record in self:
            record.r_status = 'paid'
            # record.r_apart_id.apart_status = "occupied"

            # Parse month and year from rent
            try:
                month_num = datetime.strptime(record.r_month, "%B").month
                year_num = int(record.r_year)
            except Exception:
                continue  # Skip if invalid month/year

            # Mark utility bills as paid for the apartment in the same month/year
            utility_bills = self.env['society.utility'].search([
                ('u_apart_id', '=', record.r_apart_id.id),
                ('u_bill_date', '!=', False)
            ])
            for ub in utility_bills:
                if ub.u_bill_date.month == month_num and ub.u_bill_date.year == year_num:
                    ub.u_status = 'paid'

            # Mark common area bills as paid for the same month/year (applies to all apartments)
            common_bills = self.env['society.common_area'].search([
                ('c_apart_id', '=', record.r_apart_id.id),
                ('c_bill_date', '!=', False)
            ])
            for cb in common_bills:
                if cb.c_bill_date.month == month_num and cb.c_bill_date.year == year_num:
                    cb.c_status = 'paid'

            record.r_apart_id.apart_status = 'occupied'


    def action_unpaid(self):
        for record in self:
            record.r_status = 'unpaid'

            try:
                month_num = datetime.strptime(record.r_month, "%B").month
                year_num = int(record.r_year)
            except Exception:
                continue  # Skip if invalid month/year

            # Mark utility bills as paid for the apartment in the same month/year
            utility_bills = self.env['society.utility'].search([
                ('u_apart_id', '=', record.r_apart_id.id),
                ('u_bill_date', '!=', False)
            ])
            for ub in utility_bills:
                if ub.u_bill_date.month == month_num and ub.u_bill_date.year == year_num:
                    ub.u_status = 'unpaid'

            # Mark common area bills as paid for the same month/year (applies to all apartments)
            common_bills = self.env['society.common_area'].search([
                ('c_apart_id', '=', record.r_apart_id.id),
                ('c_bill_date', '!=', False)
            ])
            for cb in common_bills:
                if cb.c_bill_date.month == month_num and cb.c_bill_date.year == year_num:
                    cb.c_status = 'unpaid'

            record.r_apart_id.apart_status = 'occupied'




