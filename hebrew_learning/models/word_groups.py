# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WordGroups(models.Model):
    _name = 'word_groups'
    _description = 'Word groups'

    word_group_name = fields.Char(
        string='Word group name',
        required=True,
    )
    
    word_in_group = fields.Many2many(
        string='Word in group',
        comodel_name='words',
    )

    group_user = fields.Many2many(
        string='Users who added the group',
        comodel_name='res.users',
    )
    