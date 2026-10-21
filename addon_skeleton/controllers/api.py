# Copyright (c) 2026 Detalex GmbH, Dietmar Hamm <https://detalex.de>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo.exceptions import AccessError
from odoo.http import Controller, request, route


class SkeletonApi(Controller):
    """REST-artige JSON-Endpunkte.

    auth='bearer': Anmeldung über einen API-Schlüssel des Benutzers
    (Header "Authorization: Bearer <Schlüssel>"). Der Code läuft danach mit
    genau den Rechten dieses Benutzers – ir.access.csv gilt wie im Backend.
    """

    @route('/skeleton/api/items', type='json2', auth='bearer', bearer_scope='rpc',
           methods=['GET'], readonly=True)
    def api_items(self, **kw):
        # Kein sudo(): ein Portal-Schlüssel liefert nur Einträge der eigenen Firma
        return request.env['skeleton.item'].search_read(
            [], ['code', 'name', 'state', 'date', 'partner_id'],
        )

    @route('/skeleton/api/items/<int:item_id>/done', type='json2', auth='bearer',
           bearer_scope='rpc', methods=['POST'])
    def api_item_done(self, item_id, **kw):
        # Zusätzliche Prüfung im Code: nur die Gruppe Administrator darf abschließen
        if not request.env.user.has_group('addon_skeleton.group_skeleton_manager'):
            raise AccessError(request.env._('Only Skeleton administrators may close items.'))
        item = request.env['skeleton.item'].browse(item_id).exists()
        item.action_done()
        return {'id': item.id, 'code': item.code, 'state': item.state}
