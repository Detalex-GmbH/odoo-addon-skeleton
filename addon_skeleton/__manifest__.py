# Copyright (c) 2026 Detalex GmbH, Dietmar Hamm <https://detalex.de>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    # Anzeige im App-Menü
    "name": "Addon Skeleton",
    "summary": "Vorlage für ein Odoo-Addon: Modell, Rechte, Ansichten, Portal und Daten",
    "description": "Lehrbeispiel mit allen Bausteinen eines Odoo-Addons.",
    "category": "Productivity",
    # <Odoo-Version>.<Major>.<Minor>.<Patch>
    "version": "20.0.1.1.0",
    "author": "Detalex GmbH, Dietmar Hamm",
    "maintainer": "Detalex GmbH",
    "website": "https://detalex.de",
    "support": "support@detalex.de",
    "license": "LGPL-3",
    # Module, die vorher installiert sein müssen
    "depends": [
        "portal",
    ],
    # Python-Pakete (Importname) und Programme, die auf dem Server
    # installiert sein müssen; fehlt eines, verweigert Odoo die Installation.
    # Beispiel: {"python": ["openpyxl"], "bin": ["wkhtmltopdf"]}
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    # Wird bei Installation und Update in dieser Reihenfolge geladen:
    # erst Gruppen und Rechte, dann Daten, dann Ansichten und Menüs
    "data": [
        "security/security.xml",
        "security/ir.access.csv",
        "data/ir_sequence_data.xml",
        "data/portal_entry_data.xml",
        "views/skeleton_item_views.xml",
        "views/portal_templates.xml",
        "views/menus.xml",
    ],
    # Dateien für den Browser, gebündelt in Asset-Bundles
    "assets": {
        "web.assets_backend": [
            "addon_skeleton/static/src/scss/addon_skeleton.scss",
        ],
    },
    # Bilder für den App Store (Cover zuerst)
    "images": [
        "static/description/cover.png",
    ],
    "installable": True,
    "application": True,
}
