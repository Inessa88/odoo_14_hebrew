# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Sentences(models.Model):
    _name = 'sentences'
    _description = 'Sentences'


    hebrew_sentence = fields.Char(
        string='Hebrew sentence',
        required=True,
    )

    translation_sentence = fields.Char(
        string='Translation in Russian',
        required=True,
    )

    picture = fields.Binary(
        string='Image',
        required=True,
    )

    audio = fields.Char(
        string='Audio',
    )

    sentence_user = fields.Many2many(
        string='Users who added the sentence',
        comodel_name='res.users',
    )

    button_learn_this_sentence_visible = fields.Boolean(
        string='Button "Learn this sentence" is visible',
        compute='_compute_button_learn_this_sentence_visible',
    )

    def name_get(self):
        # Возвращать название рекорда в форме: "translation_sentence"
        return [(record.id, record.translation_sentence) for record in self]

    def learn_this_sentence(self):
        uid = self.env.uid
        for sentence in self:
            sentence.sentence_user = [(4, uid)]

    def _compute_button_learn_this_sentence_visible(self):
        # Current user id
        uid = self.env.uid
        for record in self:
            if uid in record.sentence_user.ids:
                record.button_learn_this_sentence_visible = False
            else:
                record.button_learn_this_sentence_visible = True

    def repeat_this_sentence_today(self):
        self.ensure_one()
        uid = self.env.uid
        sentences_training = self.env.ref('hebrew_learning.sentences').id,
        exercises_with_these_sentences = self.env['last_exercise_date'].search([
            ('sentence_id', '=', self.id),
            ('user_id', '=', uid),
            ('exercise_type_id', '=', sentences_training),
        ])
        for exercise in exercises_with_these_sentences:
            exercise.last_exercise_date = fields.Date.context_today(exercise) - relativedelta(
                days=int(exercise.repetition_interval)
            )
        if exercises_with_these_sentences:
            self.env.user.notify_success(message='Added to repeat today!')
        else:
            self.env.user.notify_warning(message='You need to learn sentence first!')
    