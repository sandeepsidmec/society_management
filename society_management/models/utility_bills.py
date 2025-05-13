from odoo import models, fields,api


class UtilityBills(models.Model):
    _name = 'society.utility'
    _description = 'Society_Utility'
    _rec_name = 'u_bill_type'

    u_apart_num=fields.Many2one("society.apartment","Apartment Type")
    u_bill_type=fields.Many2one("bill.type.settings","Bill Type",domain=[('bill_type_category', '=', 'utility')])
    u_bill_date = fields.Date("Bill Date")
    u_bill_amt = fields.Float("Bill Amount")
    u_due_date=fields.Date("Bill Due Date")
    u_bill=fields.Binary("Upload bill")
    u_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')],"Status",default="paid")
    u_bill_payment=fields.Date("Bill Payment Date")

    def action_paid(self):
        for record in self:
            record.u_status = 'paid'

    def action_unpaid(self):
        for record in self:
            record.u_status = 'unpaid'

