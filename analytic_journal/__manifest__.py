# Copyright 2015 Odoo SA
# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Analytic Journal",
    "version": "12.0.1.0.0",
    "summary": "Analytic Journals as in previous Odoo versions",
    "author": "Odoo SA",
    "license": "LGPL-3",
    "category": "Analytic",
    "depends": ["account", "analytic"],
    "data": ["views/analytic_view.xml", "security/ir.model.access.csv"],
    "installable": True,
    "post_init_hook": "post_init_hook",
}
