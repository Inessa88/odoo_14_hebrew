# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _

import random

class ExerciseTypes(models.Model):
    _name = 'exercise_types'
    _description = 'Exercise types'

    name = fields.Char(
        string='Name',
        required=True,
    )
    
    exercise_image  = fields.Binary(
        string='Exercise image',
    )

    words_to_train_ids = fields.Many2many(
        string='Words to train',
        comodel_name='words',
        compute='_compute_words_to_train',
    )

    number_of_words_to_train = fields.Integer(
        string='Number of words to train',
        compute='_compute_words_to_train',
    )

    def _compute_words_to_train(self):
        # Current user id
        uid = self.env.uid
        for record in self:
            # Initial learning
            if record.id == self.env.ref('hebrew_learning.learning').id:
                current_user_all_words = self.env['words'].search([
                    ('word_user', '=', uid)
                ])
                word_ids_list = current_user_all_words.ids
                current_user_already_learned_words = self.env['last_exercise_date'].search([
                    ('word_id', 'in', word_ids_list),
                    ('user_id', '=', uid),
                    ('exercise_type_id', '=', record.id), # initial learning already has happened
                ])
                learned_word_ids_list = current_user_already_learned_words.mapped('word_id').ids
                # Only not learned words should be in this initial training
                word_to_learn_ids_list = list(set(word_ids_list) - set(learned_word_ids_list))
                record.words_to_train_ids = word_to_learn_ids_list
                record.number_of_words_to_train = len(word_to_learn_ids_list)
            # Other types of learning
            else:
                words_to_train = self.env['last_exercise_date'].search([
                    ('user_id', '=', uid),
                    ('exercise_type_id', '=', record.id),
                ]).filtered(
                    # Current date is equal or more than last training date + next training (days)
                    lambda lst_training_record: (lst_training_record.last_exercise_date + relativedelta(
                        days=int(lst_training_record.repetition_interval)
                    )) <= fields.Date.today()
                ).mapped('word_id')
                word_to_train_ids_list = words_to_train.ids
                record.words_to_train_ids = word_to_train_ids_list
                record.number_of_words_to_train = len(word_to_train_ids_list)

    def update_context_for_translation_exercises(self, five_words_to_train, action_context):
        number_of_words_to_train = len([n for n in five_words_to_train if n != False])
        first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
            False, False, False, False, False
        # No words to train case is covered in xml view part (<div t-if="record.number_of_words_to_train.raw_value != 0">)
        if number_of_words_to_train == 1:
            first_word_to_train = five_words_to_train[0]
        elif number_of_words_to_train == 2:
            first_word_to_train, second_word_to_train = five_words_to_train[0], five_words_to_train[1]
        elif number_of_words_to_train == 3:
            first_word_to_train, second_word_to_train, third_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2]
        elif number_of_words_to_train == 4:
            first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2], five_words_to_train[3]
        # There are all 5 words to train
        else:
            first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2], \
                    five_words_to_train[3], five_words_to_train[4]
        # first_right_answer_number always exists, next ones are optional
        second_right_answer_number = '0'
        third_right_answer_number = '0'
        fourth_right_answer_number = '0'
        fifth_right_answer_number = '0'

        # first_question_first_answer always exists, next ones are optional
        first_question_second_answer = ''
        first_question_third_answer = ''
        first_question_fourth_answer = ''
        first_question_fifth_answer = ''
        second_question_first_answer = ''
        second_question_second_answer = ''
        second_question_third_answer = ''
        second_question_fourth_answer = ''
        second_question_fifth_answer = ''
        third_question_first_answer = ''
        third_question_second_answer = ''
        third_question_third_answer = ''
        third_question_fourth_answer = ''
        third_question_fifth_answer = ''
        fourth_question_first_answer = ''
        fourth_question_second_answer = ''
        fourth_question_third_answer = ''
        fourth_question_fourth_answer = ''
        fourth_question_fifth_answer = ''
        fifth_question_first_answer = ''
        fifth_question_second_answer = ''
        fifth_question_third_answer = ''
        fifth_question_fourth_answer = ''
        fifth_question_fifth_answer = ''
        if number_of_words_to_train == 1:
            first_right_answer_number = '1'
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                # There is only one word to train - no need to shuffle list of words to train
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
        elif number_of_words_to_train == 2:
            # FIRST QUESTION
            random.shuffle(five_words_to_train) # five_words_to_train - list of maximum 5 ids of words
            first_right_answer_number = str(five_words_to_train.index(first_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
            # SECOND QUESTION
            random.shuffle(five_words_to_train)
            second_right_answer_number = str(five_words_to_train.index(second_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
        elif number_of_words_to_train == 3:
            # FIRST QUESTION
            random.shuffle(five_words_to_train)
            first_right_answer_number = str(five_words_to_train.index(first_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                first_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                first_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
            # SECOND QUESTION
            random.shuffle(five_words_to_train)
            second_right_answer_number = str(five_words_to_train.index(second_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                second_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                second_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
            # THIRD QUESTION
            random.shuffle(five_words_to_train)
            third_right_answer_number = str(five_words_to_train.index(third_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                third_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                third_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                third_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                third_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                third_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                third_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
        elif number_of_words_to_train == 4:
            # FIRST QUESTION
            random.shuffle(five_words_to_train)
            first_right_answer_number = str(five_words_to_train.index(first_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                first_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                first_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                first_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                first_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
            # SECOND QUESTION
            random.shuffle(five_words_to_train)
            second_right_answer_number = str(five_words_to_train.index(second_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                second_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                second_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                second_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                second_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
            # THIRD QUESTION
            random.shuffle(five_words_to_train)
            third_right_answer_number = str(five_words_to_train.index(third_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                third_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                third_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                third_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                third_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                third_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                third_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                third_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                third_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
            # FOURTH QUESTION
            random.shuffle(five_words_to_train)
            fourth_right_answer_number = str(five_words_to_train.index(fourth_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                fourth_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                fourth_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                fourth_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                fourth_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                fourth_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                fourth_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                fourth_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                fourth_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
        # There are all 5 words to train
        else:
            # FIRST QUESTION
            random.shuffle(five_words_to_train)
            first_right_answer_number = str(five_words_to_train.index(first_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                first_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                first_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
                first_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                first_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                first_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                first_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                first_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
                first_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).hebrew_word_nikud
            # SECOND QUESTION
            random.shuffle(five_words_to_train)
            second_right_answer_number = str(five_words_to_train.index(second_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                second_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                second_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
                second_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                second_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                second_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                second_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                second_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
                second_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).hebrew_word_nikud
            # THIRD QUESTION
            random.shuffle(five_words_to_train)
            third_right_answer_number = str(five_words_to_train.index(third_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                third_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                third_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                third_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                third_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
                third_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                third_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                third_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                third_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                third_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
                third_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).hebrew_word_nikud
            # FOURTH QUESTION
            random.shuffle(five_words_to_train)
            fourth_right_answer_number = str(five_words_to_train.index(fourth_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                fourth_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                fourth_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                fourth_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                fourth_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
                fourth_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                fourth_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                fourth_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                fourth_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                fourth_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
                fourth_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).hebrew_word_nikud
            # FIFTH QUESTION
            random.shuffle(five_words_to_train)
            fifth_right_answer_number = str(five_words_to_train.index(fifth_word_to_train) + 1)
            # Hebrew word --> translation training
            if action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.word_translation').id or self.id == self.env.ref('hebrew_learning.word_translation').id:
                fifth_question_first_answer = self.env['words'].browse(five_words_to_train[0]).translation_word
                fifth_question_second_answer = self.env['words'].browse(five_words_to_train[1]).translation_word
                fifth_question_third_answer = self.env['words'].browse(five_words_to_train[2]).translation_word
                fifth_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).translation_word
                fifth_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).translation_word
            # translation --> Hebrew word training
            elif action_context.get('default_exercise_type_id') == self.env.ref('hebrew_learning.translation_word').id or self.id == self.env.ref('hebrew_learning.translation_word').id:
                fifth_question_first_answer = self.env['words'].browse(five_words_to_train[0]).hebrew_word_nikud
                fifth_question_second_answer = self.env['words'].browse(five_words_to_train[1]).hebrew_word_nikud
                fifth_question_third_answer = self.env['words'].browse(five_words_to_train[2]).hebrew_word_nikud
                fifth_question_fourth_answer = self.env['words'].browse(five_words_to_train[3]).hebrew_word_nikud
                fifth_question_fifth_answer = self.env['words'].browse(five_words_to_train[4]).hebrew_word_nikud

        action_context.update({
            # Right answers block
            'default_first_right_answer_number': first_right_answer_number,
            'default_second_right_answer_number': second_right_answer_number,
            'default_third_right_answer_number': third_right_answer_number,
            'default_fourth_right_answer_number': fourth_right_answer_number,
            'default_fifth_right_answer_number': fifth_right_answer_number,
            # Answers block
            'default_first_question_first_answer': first_question_first_answer,
            'default_first_question_second_answer': first_question_second_answer,
            'default_first_question_third_answer': first_question_third_answer,
            'default_first_question_fourth_answer': first_question_fourth_answer,
            'default_first_question_fifth_answer': first_question_fifth_answer,
            'default_second_question_first_answer': second_question_first_answer,
            'default_second_question_second_answer': second_question_second_answer,
            'default_second_question_third_answer': second_question_third_answer,
            'default_second_question_fourth_answer': second_question_fourth_answer,
            'default_second_question_fifth_answer': second_question_fifth_answer,
            'default_third_question_first_answer': third_question_first_answer,
            'default_third_question_second_answer': third_question_second_answer,
            'default_third_question_third_answer': third_question_third_answer,
            'default_third_question_fourth_answer': third_question_fourth_answer,
            'default_third_question_fifth_answer': third_question_fifth_answer,
            'default_fourth_question_first_answer': fourth_question_first_answer,
            'default_fourth_question_second_answer': fourth_question_second_answer,
            'default_fourth_question_third_answer': fourth_question_third_answer,
            'default_fourth_question_fourth_answer': fourth_question_fourth_answer,
            'default_fourth_question_fifth_answer': fourth_question_fifth_answer,
            'default_fifth_question_first_answer': fifth_question_first_answer,
            'default_fifth_question_second_answer': fifth_question_second_answer,
            'default_fifth_question_third_answer': fifth_question_third_answer,
            'default_fifth_question_fourth_answer': fifth_question_fourth_answer,
            'default_fifth_question_fifth_answer': fifth_question_fifth_answer,
        })

    def update_context_for_sprint_exercise(self, five_words_to_train, action_context):
        number_of_words_to_train = len(five_words_to_train)
        first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
            False, False, False, False, False
        # No words to train case is covered in xml view part (<div t-if="record.number_of_words_to_train.raw_value != 0">)
        if number_of_words_to_train == 1:
            first_word_to_train = five_words_to_train[0]
        elif number_of_words_to_train == 2:
            first_word_to_train, second_word_to_train = five_words_to_train[0], five_words_to_train[1]
        elif number_of_words_to_train == 3:
            first_word_to_train, second_word_to_train, third_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2]
        elif number_of_words_to_train == 4:
            first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2], five_words_to_train[3]
        # There are all 5 words to train
        else:
            first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2], \
                    five_words_to_train[3], five_words_to_train[4]
        # first_right_answer_number always exists, next ones are optional
        second_right_answer_number = '0'
        third_right_answer_number = '0'
        fourth_right_answer_number = '0'
        fifth_right_answer_number = '0'

        # first_question_first_answer always exists, next ones are optional
        first_question_second_answer = ''
        second_question_first_answer = ''
        second_question_second_answer = ''
        third_question_first_answer = ''
        third_question_second_answer = ''
        fourth_question_first_answer = ''
        fourth_question_second_answer = ''
        fifth_question_first_answer = ''
        fifth_question_second_answer = ''

        if number_of_words_to_train == 1:
            first_right_answer_number = '1'
            # There is only one word to train - no need to shuffle list of words to train
            first_question_first_answer = self.words_to_train_ids[0].translation_word

        elif number_of_words_to_train == 2: # there is only 2 words in five_words_to_train
            # FIRST QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(first_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            first_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            first_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            first_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # SECOND QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(second_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            second_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            second_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            second_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word

        elif number_of_words_to_train == 3:
            # FIRST QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(first_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            first_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            first_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            first_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # SECOND QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(second_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            second_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            second_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            second_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # THIRD QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(third_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            third_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            third_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            third_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word

        elif number_of_words_to_train == 4:
            # FIRST QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(first_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            first_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            first_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            first_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # SECOND QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(second_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            second_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            second_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            second_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # THIRD QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(third_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            third_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            third_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            third_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # FOURTH QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(fourth_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            fourth_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            fourth_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            fourth_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
        # There are all 5 words to train
        else:
            # FIRST QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(first_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            first_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            first_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            first_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # SECOND QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(second_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            second_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            second_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            second_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # THIRD QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(third_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            third_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            third_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            third_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # FOURTH QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(fourth_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            fourth_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            fourth_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            fourth_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word
            # FIFTH QUESTION
            right_answer_index_in_five_words_to_train = five_words_to_train.index(fifth_word_to_train)
            right_answer = five_words_to_train[right_answer_index_in_five_words_to_train]
            wrong_answers = list(filter(lambda answer: answer != right_answer, five_words_to_train))
            # shuffle wrong_answers list
            random.shuffle(wrong_answers)
            two_answers_list = [
                right_answer,
                wrong_answers[0], # first one from wrong_answers list
            ]
            # shuffle list with one wrong and one right answer in it
            random.shuffle(two_answers_list)
            right_answer_index_in_two_answers_list = two_answers_list.index(right_answer)
            fifth_right_answer_number = str(right_answer_index_in_two_answers_list + 1)
            fifth_question_first_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[0]).translation_word
            fifth_question_second_answer = self.words_to_train_ids.filtered(lambda r: r.id == two_answers_list[1]).translation_word

        action_context.update({
            # Right answers block
            'default_first_right_answer_number': first_right_answer_number,
            'default_second_right_answer_number': second_right_answer_number,
            'default_third_right_answer_number': third_right_answer_number,
            'default_fourth_right_answer_number': fourth_right_answer_number,
            'default_fifth_right_answer_number': fifth_right_answer_number,
            # Answers block
            'default_first_question_first_answer': first_question_first_answer,
            'default_first_question_second_answer': first_question_second_answer,
            'default_second_question_first_answer': second_question_first_answer,
            'default_second_question_second_answer': second_question_second_answer,
            'default_third_question_first_answer': third_question_first_answer,
            'default_third_question_second_answer': third_question_second_answer,
            'default_fourth_question_first_answer': fourth_question_first_answer,
            'default_fourth_question_second_answer': fourth_question_second_answer,
            'default_fifth_question_first_answer': fifth_question_first_answer,
            'default_fifth_question_second_answer': fifth_question_second_answer,
        })

    def start_training(self):
        five_words_to_train = self.words_to_train_ids.ids[:5]
        first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
            False, False, False, False, False
        number_of_words_to_train = len(five_words_to_train)
        # No words to train case is covered in xml view part (<div t-if="record.number_of_words_to_train.raw_value != 0">)
        if number_of_words_to_train == 1:
            first_word_to_train = five_words_to_train[0]
        elif number_of_words_to_train == 2:
            first_word_to_train, second_word_to_train = five_words_to_train[0], five_words_to_train[1]
        elif number_of_words_to_train == 3:
            first_word_to_train, second_word_to_train, third_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2]
        elif number_of_words_to_train == 4:
            first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2], five_words_to_train[3]
        # There are all 5 words to train
        else:
            first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2], \
                    five_words_to_train[3], five_words_to_train[4]
        possible_trainings_dict = {
            # initial learning
            self.env.ref('hebrew_learning.learning').id: 'hebrew_learning.wizard_learning_action',
            # word translation training
            self.env.ref('hebrew_learning.word_translation').id: 'hebrew_learning.wizard_word_translation_training_action',
            # translation word training
            self.env.ref('hebrew_learning.translation_word').id: 'hebrew_learning.wizard_translation_word_training_action',
            # writing training
            self.env.ref('hebrew_learning.writing').id: 'hebrew_learning.wizard_writing_training_action',
            # sprint training
            self.env.ref('hebrew_learning.sprint').id: 'hebrew_learning.wizard_sprint_training_action',
        }
        training_action = possible_trainings_dict[self.id]
        action = self.env["ir.actions.actions"]._for_xml_id(training_action)
        action['context'] = {
            'default_all_words_to_train_ids': five_words_to_train,
            'default_exercise_type_id': self.id,
            'default_first_word_to_train_id': first_word_to_train,
            'default_second_word_to_train_id': second_word_to_train,
            'default_third_word_to_train_id': third_word_to_train,
            'default_fourth_word_to_train_id': fourth_word_to_train,
            'default_fifth_word_to_train_id': fifth_word_to_train,
            # Number of words to train
            'default_number_of_words_to_train': number_of_words_to_train,
        }

        # Additional context for translation trainings
        if self.id in (
            self.env.ref('hebrew_learning.word_translation').id,
            self.env.ref('hebrew_learning.translation_word').id
        ):
            self.update_context_for_translation_exercises(five_words_to_train, action['context'])

        # Additional context for sprint training
        if self.id == self.env.ref('hebrew_learning.sprint').id:
            self.update_context_for_sprint_exercise(five_words_to_train, action['context'])

        # Hide edit buttons except writing training
        if self.id != self.env.ref('hebrew_learning.writing').id:
            action['flags'] = {'mode': 'readonly'}

        return action    
