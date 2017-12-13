# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp import api

class res_partner(models.Model):
    _inherit = 'res.partner'


    custom_delivery_days = fields.Integer('Dias de trayecto')