
from odoo import models, fields,api
from datetime import datetime

class Rent(models.Model):
    _name = 'society.rent'
    _description = 'Society_Rent'
    _rec_name = "r_apart_num"


    r_apart_num=fields.Many2one("society.apartment","Apartment Number")
    r_tenant_name=fields.Many2one("society.tenant","Tenant Name")
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
    r_date = fields.Date("Payment Date")

    def _compute_rent_for(self):
        for i in self:
            if i.r_month and i.r_year:
                i.rent_for = f"{i.r_month} {i.r_year}"
            else:
                i.rent_for =f"invalid"


    @api.onchange("r_apart_num")
    def onchange_r_apart_num(self):
        for i in self:
            i.r_tenant_name = i.r_tenant_name
            i.r_month=datetime.now().strftime('%B')
            i.r_year=str(datetime.now().year)


    def _compute_formatted_rent_amt(self):
        settings = self.env['currency.settings'].search([], limit=1)
        for rec in self:
            if not settings:
                rec.formatted_rent_amt = str(rec.rent_amt)
                continue
            formatted = f"{rec.rent_amt:,.{settings.decimal_places}f}"
            formatted = formatted.replace(",", "TMP").replace(".", settings.decimal_separator).replace("TMP", settings.thousand_separator)
            if settings.symbol_position == 'left':
                rec.formatted_rent_amt = f"{settings.currency_symbol}{formatted}"
            else:
                rec.formatted_rent_amt = f"{formatted}{settings.currency_symbol}"