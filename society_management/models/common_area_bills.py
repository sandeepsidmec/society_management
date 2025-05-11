from odoo import models, fields,api


class CommonArea(models.Model):
    _name = 'society.common_area'
    _description = 'Society_Common_Area'
    _rec_name = 'c_bill_type'

    c_bill_type = fields.Many2one("bill.type.settings", "Bill Type",domain=[('bill_type_category', "=", 'common area bills')])
    c_bill_date=fields.Date("Bill Date")
    c_bill_amt=fields.Float("Bill Amount")
    c_status=fields.Selection([('paid','Paid'),('unpaid','Unpaid')],"Status",default="unpaid")
    c_due_date = fields.Date("Bill Due Date")
    c_bill = fields.Binary("Upload bill")
    c_bill_payment = fields.Date("Bill Payment Date")