# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class DmEventsTags(models.Model):
    _name='dm.events.tags'
    _description='This is Tags model.'
    
    name = fields.Char(string="Tag name", required=True, translate=True)
    
class DmEventsCategory(models.Model):
    _name='dm.events.category'
    _description='This is Category model.'
    
    name = fields.Char(string="Category name", required=True, translate=True)

class DmEvents(models.Model):
    _name='dm.events'
    _description='This is Events model.'

    name = fields.Char(string="Event Name", required=True, translate=True)
    description= fields.Html(string="Description")
    price=fields.Float(string="Price")
    active = fields.Boolean(default=True)
    category_id = fields.Many2one(string="Category", comodel_name="dm.events.category")
    tag_ids = fields.Many2many(string="Tags", comodel_name="dm.events.tags")
    company_id = fields.Many2one(string="Company", comodel_name='res.company')