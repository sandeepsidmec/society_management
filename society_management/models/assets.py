from odoo import models, fields,api


class Assets(models.Model):
    _name = 'society.assets'
    _description = 'Society_Asset'
    _rec_name = 'asset_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    asset_name=fields.Char("Name",tracking=True)
    category_id=fields.Many2one("asset.category.settings","Category")
    condition=fields.Selection([('new','New'),('good','Good'),('needs repair','Needs Repair')],"Condition")
    tower_id=fields.Many2one("society.tower","Select Tower")
    floor_id = fields.Many2one("society.floor", "Select Floor")
    aprt_num_id=fields.Many2one("society.apartment","Apartment Number")
    loc=fields.Text("Location")
    date=fields.Date("Purchase Date")
    doc=fields.Binary("Upload Document")