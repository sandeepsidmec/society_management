from odoo import models, fields,api


class Assets(models.Model):
    _name = 'society.assets'
    _description = 'Society_Asset'
    _rec_name = 'asset_name'

    asset_name=fields.Char("Name")
    # category=fields.Many2one("assets.category.settings","Category")
    condition=fields.Selection([('new','New'),('good','Good'),('needs repair','Needs Repair')],"Condition")
    tower=fields.Many2one("society.tower","Select Tower")
    floor = fields.Many2one("society.floor", "Select Floor")
    num=fields.Many2one("society.apartment","Apartment Number")
    loc=fields.Text("Location")
    date=fields.Date("Purchase Date")
    doc=fields.Binary("Upload Document")