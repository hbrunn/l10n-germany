# Copyright 2023 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    """
    Preset account.account#datev_export_nonautomatic for known COAs
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    for company in env["res.company"].search([("chart_template_id", "!=", False)]):
        company.chart_template_id._datev_set_nonautomatic_flag(company)
