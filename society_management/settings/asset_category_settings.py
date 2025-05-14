from odoo import models, fields


class AssetCategorySettings(models.Model):
    _name = 'asset.category.settings'
    _rec_name = "asset_category"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    asset_category = fields.Char("Asset Category")