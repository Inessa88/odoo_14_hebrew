from dateutil.relativedelta import relativedelta

from odoo import models, fields, _


class WizardLearning(models.TransientModel):

    _name = 'wizard_learning'
    _description = 'Wizard for learning'
    _inherit = ['common_part_for_all_trainings_mixin']

 
    number_of_words_to_train = fields.Integer(
        string='Number of words to train',
    )


    def _return_next_action(self):
        next_exercise_action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_word_translation_training_action')
        word_translation_exercise_type_id = self.env.ref('hebrew_learning.word_translation').id
        # copy current context dictionary
        next_exercise_action['context'] = self.env.context.copy()
        five_words_to_train = next_exercise_action['context'].get('default_all_words_to_train_ids')
        # this context is required to know: we are at initial learning process + cleaning _question_answered part
        # + _exercise_type_id will be of next exercise

        next_exercise_action['context'].update({
            'initial_learning': True,
            'default_exercise_type_id': word_translation_exercise_type_id,
            'default_first_question_answered': False,
            'default_second_question_answered': False,
            'default_third_question_answered': False,
            'default_fourth_question_answered': False,
            'default_fifth_question_answered': False,
            'given_first_answer': False,
            'given_second_answer': False,
            'given_third_answer': False,
            'given_fourth_answer': False,
            'given_fifth_answer': False,
        })
        self.exercise_type_id.update_context_for_translation_exercises(
            five_words_to_train, next_exercise_action['context']
        )
        # Hide edit buttons
        next_exercise_action['flags'] = {'mode': 'readonly'}
        return next_exercise_action

    def _create_last_exercise_date_for_all_trainings(self):
        today_date = fields.Date.context_today(self)
        yesterday_date = today_date + relativedelta(days=-1)
        uid = self.env.uid
        # exercise_type_id for initial learing
        initial_learning = self.env.ref('hebrew_learning.learning').id
        exercise_type_ids = (
            self.env.ref('hebrew_learning.word_translation').id,
            self.env.ref('hebrew_learning.translation_word').id,
            self.env.ref('hebrew_learning.writing').id,
            self.env.ref('hebrew_learning.sprint').id,
        )
        for word_id in self.all_words_to_train_ids.ids:
            # initial learining is never repeated
            self.env['last_exercise_date'].create({
                'word_id': word_id,
                'user_id': uid,
                'exercise_type_id': initial_learning,
                'last_exercise_date': today_date,
                'number_of_times_exercise_is_done': 1,
                'repetition_interval': '1000000', # 'Never'
            })
            # for other types of exercises we create it with yesterday date
            # (in case initial learing is stopped at some point) - to train it today
            for exercise_type_id in exercise_type_ids:
                self.env['last_exercise_date'].create({
                    'word_id': word_id,
                    'user_id': uid,
                    'exercise_type_id': exercise_type_id,
                    'last_exercise_date': yesterday_date,
                    'repetition_interval': '1', # 'In a day'
                })

    def give_answer(self):
        action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_learning_action')
        action['context'] = self.env.context.copy()
        if self.env.context.get('given_fifth_answer'):
            # Notification for last question: interfere to click on close wizard on success wizard on small screens
            # Can be used Repeat all words option then!
            self.env.user.notify_success(message='Success')
            self._create_last_exercise_date_for_all_trainings()
            return self._return_next_action()

        elif self.env.context.get('given_fourth_answer'):
            self.env.user.notify_success(message='Success')
            # check if all words are learned
            if self.number_of_words_to_train == 4:
                self._create_last_exercise_date_for_all_trainings()
                return self._return_next_action()
            else:
                action['context'].update({
                    'default_fourth_question_answered': True,
                })
        elif self.env.context.get('given_third_answer'):
            self.env.user.notify_success(message='Success')
            # check if all words are learned
            if self.number_of_words_to_train == 3:
                self._create_last_exercise_date_for_all_trainings()
                return self._return_next_action()
            else:
                action['context'].update({
                    'default_third_question_answered': True,
                })
        elif self.env.context.get('given_second_answer'):
            self.env.user.notify_success(message='Success')
            # check if all words are learned
            if self.number_of_words_to_train == 2:
                self._create_last_exercise_date_for_all_trainings()
                return self._return_next_action()
            else:
                action['context'].update({
                    'default_second_question_answered': True,
                })
        else: # there is 'given_first_answer' in self.env.context
            self.env.user.notify_success(message='Success')
            # check if all words are learned
            if self.number_of_words_to_train == 1:
                self._create_last_exercise_date_for_all_trainings()
                return self._return_next_action()
            else:
                action['context'].update({
                    'default_first_question_answered': True,
                })
        # Hide edit buttons
        action['flags'] = {'mode': 'readonly'}

        return action
