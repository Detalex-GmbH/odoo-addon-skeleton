# Copyright (c) 2026 Detalex GmbH, Dietmar Hamm <https://detalex.de>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import api, fields, models


class SkeletonItem(models.Model):
    """Beispielmodell: ein Eintrag mit Nummer, Kunde, Verantwortlichem und Status."""

    _name = 'skeleton.item'
    _description = 'Skeleton Item'
    _inherit = ['mail.thread']
    _order = 'sequence, id desc'

    code = fields.Char(string='Number', readonly=True, copy=False, default='/')
    name = fields.Char(string='Title', required=True, tracking=True)
    description = fields.Html(string='Description')
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    date = fields.Date(default=fields.Date.context_today)
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    user_id = fields.Many2one(
        'res.users', string='Responsible', default=lambda self: self.env.user, tracking=True,
    )
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done')],
        default='draft', required=True, tracking=True,
    )

    _code_uniq = models.Constraint('UNIQUE(code)', 'The number must be unique.')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('code', '/') == '/':
                vals['code'] = self.env['ir.sequence'].next_by_code('skeleton.item') or '/'
        return super().create(vals_list)

    def action_done(self):
        self.write({'state': 'done'})

    def action_draft(self):
        self.write({'state': 'draft'})
