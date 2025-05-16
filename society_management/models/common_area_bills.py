from odoo import models, fields,api


class CommonArea(models.Model):
    _name = 'society.common_area'
    _description = 'Society_Common_Area'
    _rec_name = 'c_bill_type_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    c_apart_id=fields.Many2one("society.apartment","Apartment Number",tracking=True)
    c_bill_type_id = fields.Many2one("bill.type.settings", "Bill Type",domain=[('bill_type_category', "=", 'common_area')])
    c_bill_date=fields.Date("Bill Date")
    c_bill_amt=fields.Float("Bill Amount")
    c_status=fields.Selection([('paid','Paid'),('unpaid','Unpaid')],"Status",default="paid")
    c_due_date = fields.Date("Bill Due Date")
    c_bill = fields.Binary("Upload bill")
    c_proof_bill = fields.Binary("Upload Payment Proof")
    c_bill_payment = fields.Date("Bill Payment Date")

    def action_paid(self):
        for record in self:
            record.c_status = 'paid'

    def action_unpaid(self):
        for record in self:
            record.c_status = 'unpaid'