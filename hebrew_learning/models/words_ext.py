# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class WordsExt(models.Model):
    _inherit = 'words'
    _description = 'Words model extension'


    group_ids = fields.Many2many(
        string='Groups',
        comodel_name='word_groups',
    )

    def repeat_this_word_today(self):
        self.ensure_one()
        uid = self.env.uid
        exercises_to_repeat_ids = (
            self.env.ref('hebrew_learning.word_translation').id,
            self.env.ref('hebrew_learning.translation_word').id,
            self.env.ref('hebrew_learning.writing').id,
            self.env.ref('hebrew_learning.sprint').id,
        )
        exercises_with_these_words = self.env['last_exercise_date'].search([
            ('word_id', '=', self.id),
            ('user_id', '=', uid),
            ('exercise_type_id', 'in', exercises_to_repeat_ids),
        ])
        for exercise in exercises_with_these_words:
            exercise.last_exercise_date = fields.Date.context_today(exercise) - relativedelta(
                days=int(exercise.repetition_interval)
            )
        if exercises_with_these_words:
            self.env.user.notify_success(message='Added to repeat today!')
        else:
            self.env.user.notify_warning(message='You need to learn word first!')

    