from odoo import models, fields,api


class UtilityBills(models.Model):
    _name = 'society.utility'
    _description = 'Society_Utility'
    # _rec_name = 'amenity_name'

    apart_num=fields.Many2one("society.apartment","Apartment Type")
    # bill_type
    # bill_date=