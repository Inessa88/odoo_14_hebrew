# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _


class ExerciseTypes(models.Model):
    _name = 'exercise_types'
    _description = 'Exercise types'

    name = fields.Char(
        string='Name',
        required=True,
    )
    
    exercise_image  = fields.Binary(
        string='Exercise mage',
    )

    words_to_train_ids = fields.Many2many(
        string='Words to train',
        comodel_name='words',
        compute='_compute_words_to_train',
    )

    number_of_words_to_train = fields.Integer(
        string='Words to train',
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
                    ('user_id', '=', uid)
                ])
                learned_word_ids_list = current_user_already_learned_words.ids
                word_to_learn_ids_list = list(set(word_ids_list)^set(learned_word_ids_list))
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

    def start_training(self):
        five_words_to_train = self.words_to_train_ids.ids[:5]
        first_word_to_train, second_word_to_train, third_word_to_train, fourth_word_to_train, fifth_word_to_train = \
            False, False, False, False, False
        if len(five_words_to_train) == 1:
            first_word_to_train = five_words_to_train[0]
        elif len(five_words_to_train) == 2:
            first_word_to_train, second_word_to_train = five_words_to_train[0], five_words_to_train[1]
        elif len(five_words_to_train) == 3:
            first_word_to_train, second_word_to_train, third_word_to_train = \
                five_words_to_train[0], five_words_to_train[1], five_words_to_train[2]
        elif len(five_words_to_train) == 4:
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
            'default_first_word_to_train': first_word_to_train,
            'default_second_word_to_train': second_word_to_train,
            'default_third_word_to_train': third_word_to_train,
            'default_fourth_word_to_train': fourth_word_to_train,
            'default_fifth_word_to_train': fifth_word_to_train,
        }
        return action    
"""
Нужно селекшн поле "правильный ответ" (хранит 1, 2... 5)
Передаём в это поле значение, например: "first"
На кнопках при вариантах ответов висит контекст и метод, что проверяет из контекста, 
чтобы контекст = правильному ответу. Если да, что на вопрос ответили - пишем в поле, что отвечено.
"""