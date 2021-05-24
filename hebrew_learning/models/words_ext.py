# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WordsExt(models.Model):
    _inherit = 'words'
    _description = 'Words model extension'


    group_ids = fields.Many2many(
        string='Groups',
        comodel_name='word_groups',
    )
    