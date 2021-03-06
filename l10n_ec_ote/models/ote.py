# -*- coding: utf-8 -*-
from odoo import models, fields


class Canton(models.Model):
    _name = 'l10n_ec_ote.canton'

    state_id = fields.Many2one(
        'res.country.state', ondelete='restrict', string="Provincia", )
    name = fields.Char(string="Cantón")
    code = fields.Char(string="Código")


class Parish(models.Model):
    _name = 'l10n_ec_ote.parish'

    canton_id = fields.Many2one(
        'l10n_ec_ote.canton', ondelete='restrict', string="Cantón", )
    name = fields.Char(string="Parroquia")
    code = fields.Char(string="Código")
