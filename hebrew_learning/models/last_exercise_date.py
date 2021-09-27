# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class LastExerciseDate(models.Model):
    _name = 'last_exercise_date'
    _description = 'Last exercise date'
    _order = 'last_exercise_date'

    word_id = fields.Many2one(
        string='Word id',
        comodel_name='words',
        ondelete='cascade',
    )

    sentence_id = fields.Many2one(
        string='Sentence id',
        comodel_name='sentences',
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
        default=fields.Date.today(),
    )

    number_of_times_exercise_is_done = fields.Integer(
        string='Number of repetitions of this exercise, word by this user',
        default=0,
    )

    repetition_interval = fields.Selection(
        selection=[
            ('1', 'In a day'),
            ('3', 'In three days'),
            ('7', 'In a week'),
            ('14', 'In two weeks'),
            ('30', 'In a month'),
            ('90', 'In three months'),
            ('183', 'In half a year'),
            ('1000000', 'Never (initial learning)'),
        ],
        string='Repetition interval', 
        required=True,
        default='1',
    )
