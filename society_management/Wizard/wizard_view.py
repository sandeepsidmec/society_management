from odoo import fields, models,api

class Clock_In_Out(models.TransientModel):
    _name = 'society.clock.wizard'
    _description = 'clock_in/out_report'
    _rec_name = 'provider_id'

    service_id= fields.Many2one("service.type.settings",String="Service Person")
    provider_id=fields.Many2one("society.add.services","Service Provider")
    clock_in=fields.Datetime("Clock In")
    clock_out=fields.Datetime("Clock Out")



    def create_clock_record(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            record = self.env['society.clock'].browse(active_id)
            if record.exists():
                record.write({
                    'service_id': self.service_id.id,
                    'provider_id': self.provider_id.id,
                    'clock_in': self.clock_in,
                    'clock_out': self.clock_out
                })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Clock Records',
            'res_model': 'society.clock',
            'view_mode': 'list',
            'target': 'current',
        }