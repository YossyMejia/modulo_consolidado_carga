# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ConsolidatedCargo(models.TransientModel):
    _name = 'consolidated.cargo'
    _description = 'Stock Quantity History'
    _inherit = ['transport.routes']
    rutas = fields.Many2one("transport.routes", string="Ruta Seleccionada")
    fecha = fields.Datetime("Fecha", help="Choose a date to get the inventory at that date", default=fields.Datetime.now)


