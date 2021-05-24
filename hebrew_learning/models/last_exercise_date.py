# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class LastExerciseDate(models.Model):
    _name = 'last_exercise_date'
    _description = 'Last exercise date'

    word_id = fields.Many2one(
        string='Word id',
        comodel_name='words',
        required=True,
        ondelete='cascade',
    )

    user_id = fields.Many2one(
        string='User id',
        comodel_name='res.users',
        required=True,
        ondelete='cascade',
    )

    exercise_type_id = fields.Many2one(
        string='Exercise type id',
        comodel_name='exercise_types',
        required=True,
        ondelete='cascade',
    )

    last_exercise_date = fields.Date(
        string='Last exercise date',
        required=True,
    )

    repetition_interval = fields.Selection(
        selection=[
            ('1', 'In a day'),
            ('2', 'In two days'),
            ('7', 'In a week'),
            ('14', 'In two weeks'),
            ('30', 'In a month'),
            ('90', 'In three month'),
            ('183', 'In half a year')
        ],
        string='Repetition interval', 
        required=True,
        default=1,
    )
    