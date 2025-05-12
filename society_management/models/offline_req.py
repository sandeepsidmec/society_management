from odoo import models, fields,api


class OfflineReq(models.Model):
    _name = 'society.offline'
    _description = 'Society_Offline_Request'

    req_apart_num=fields.Many2one("society.apartment","Apartment Number")
    tot_cost=fields.Integer("Total Cost")
    m_y=fields.Char("Month & Year")
    # status=
