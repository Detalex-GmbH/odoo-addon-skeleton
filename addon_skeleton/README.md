# Addon Skeleton

Vorlage für ein eigenes Odoo-Addon (Odoo 20.0). Jeder Baustein eines Moduls ist einmal mit einem kleinen, lauffähigen Beispiel vertreten.

## Aufbau

```
addon_skeleton/
├── __init__.py              # importiert models und controllers
├── __manifest__.py          # Name, Version, Abhängigkeiten, geladene Dateien
├── models/
│   └── skeleton_item.py     # Modell skeleton.item
├── security/
│   ├── security.xml         # Bereich und Gruppen (User, Administrator)
│   └── ir.access.csv        # Zugriffsrechte, auch mit Domain (Portal)
├── views/
│   ├── skeleton_item_views.xml  # Liste, Formular, Suche, Aktion
│   ├── portal_templates.xml     # Portalseite /my/skeleton
│   └── menus.xml                # Hauptmenü mit App-Icon
├── data/
│   ├── ir_sequence_data.xml     # Nummernkreis SKI/<Jahr>/0001
│   └── portal_entry_data.xml    # Kachel im Kundenportal
├── controllers/
│   ├── portal.py            # Webseite: Route /my/skeleton und Kachel-Zähler
│   └── api.py               # JSON-API mit API-Schlüssel (Bearer)
└── static/
    ├── description/         # icon.png, cover.png, index.html
    └── src/                 # SCSS, Bilder (später JS und Owl-Templates)
```

## API ausprobieren

API-Schlüssel anlegen (Mein Profil › Kontosicherheit › Neuer API-Schlüssel), dann:

```bash
curl -H "Authorization: Bearer <Schlüssel>" -H "X-Odoo-Database: <datenbank>" https://<host>/skeleton/api/items
curl -X POST -H "Authorization: Bearer <Schlüssel>" -H "X-Odoo-Database: <datenbank>" https://<host>/skeleton/api/items/1/done
```

`X-Odoo-Database` ist nur nötig, wenn auf dem Server mehrere Datenbanken laufen. Die Antwort enthält nur Einträge, die der Benutzer laut `ir.access.csv` sehen darf. Abschließen per API dürfen nur Administratoren der App.

## Eigenes Modul daraus machen

1. Ordner kopieren und umbenennen, z. B. `mein_modul`.
2. `addon_skeleton` überall durch `mein_modul` ersetzen (Manifest, XML-IDs, Asset-Pfade, `web_icon`).
3. Modell `skeleton.item` umbenennen, Felder anpassen.
4. In `ir.access.csv` die Modellnamen anpassen.
5. Icon, Cover und `index.html` ersetzen.

## Installation

Ordner in den `addons_path` legen, Apps-Liste aktualisieren und „Addon Skeleton“ installieren. Abhängigkeit: `portal`.

## Lizenz

LGPL-3. Copyright (c) 2026 Detalex GmbH, Dietmar Hamm. Fragen an support@detalex.de.
