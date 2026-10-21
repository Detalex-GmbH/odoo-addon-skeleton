# Copyright (c) 2026 Detalex GmbH, Dietmar Hamm <https://detalex.de>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo.http import request, route

from odoo.addons.portal.controllers.portal import CustomerPortal


class SkeletonCustomerPortal(CustomerPortal):

    def _prepare_portal_counter_values(self, counter):
        """Zähler für die Portal-Kachel (placeholder_count im portal.entry)."""
        if counter == 'skeleton_item_count':
            return 'skeleton.item', [], 'read'
        return super()._prepare_portal_counter_values(counter)

    @route('/my/skeleton', type='http', auth='user', website=True)
    def portal_my_skeleton_items(self, **kw):
        # Ohne sudo(): ir.access.csv filtert auf die eigene Firma des Portalbenutzers
        items = request.env['skeleton.item'].search([])
        values = self._prepare_portal_layout_values()
        values.update({'items': items, 'page_name': 'skeleton_item'})
        return request.render('addon_skeleton.portal_my_skeleton_items', values)
