# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class DmBookings(models.Model):
    _name='dm.bookings'
    _description='This is Booking model.'

    name = fields.Char(string="Event Name", required=True, translate=True)
    description= fields.Html(string="Description")
    price=fields.Float(string="Price")
    active = fields.Boolean(default=True)
    category_id = fields.Many2one(string="Category", comodel_name="dm.events.category")
    tag_ids = fields.Many2many(string="Tags", comodel_name="dm.events.tags")
    company_id = fields.Many2one(string="Company", comodel_name='res.company')