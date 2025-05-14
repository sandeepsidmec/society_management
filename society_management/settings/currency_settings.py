from odoo import models, fields,api


class CurrencySettings(models.Model):
    _name = 'currency.settings'
    _rec_name = "currency_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    currency_id = fields.Char("Currency")
    currency_symbol = fields.Char("Currency Symbol")

    symbol_position = fields.Selection(
        [('left', 'Left'), ('right', 'Right')],
        string="Symbol Position", default='left'
    )
    thousand_separator = fields.Char("Thousand Separator", default=',')
    decimal_separator = fields.Char("Decimal Separator", default='.')
    decimal_places = fields.Integer("Number of Decimals", default=2)
    currency_format = fields.Char("Currency Format", compute="_compute_currency_format", store=True)

    @api.depends('currency_symbol', 'symbol_position', 'thousand_separator', 'decimal_separator', 'decimal_places')
    def _compute_currency_format(self):
        for record in self:
            # Example number
            example_number = 12345.6789
            rounded = f"{example_number:,.{record.decimal_places}f}"

            # Replace default separators
            formatted_number = rounded.replace(",", "TMP").replace(".", record.decimal_separator).replace("TMP",
                                                                                                          record.thousand_separator)

            if record.symbol_position == 'left':
                record.currency_format = f"{record.currency_symbol}{formatted_number}"
            else:
                record.currency_format = f"{formatted_number}{record.currency_symbol}"
