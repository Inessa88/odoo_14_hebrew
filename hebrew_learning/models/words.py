# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Words(models.Model):
    _name = 'words'
    _description = 'Words'


    hebrew_word = fields.Char(
        string='Hebrew word',
        required=True,
    )

    hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud',
        required=True,
    )

    pronunciation_word = fields.Char(
        string='Pronunciation word in latin',
        required=True,
    )

    translation_word = fields.Char(
        string='Translation in Russian',
        required=True,
    )

    picture = fields.Binary(
        string='Image',
    )

    word_user = fields.Many2many(
        string='Users who added the word',
        comodel_name='res.users',
    )
    