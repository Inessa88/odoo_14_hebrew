from odoo import models, fields, api, _


class WizardWritingTraining(models.TransientModel):

    _name = 'wizard_writing_training'
    _description = 'Wizard for writing training'
    _inherit = ['common_part_for_all_trainings_mixin']

    first_word_typing = fields.Char(
        string='First word to type',
    )

    second_word_typing = fields.Char(
        string='Second word to type',
    )

    third_word_typing = fields.Char(
        string='Third word to type',
    )

    fourth_word_typing = fields.Char(
        string='Fourth word to type',
    )

    fifth_word_typing = fields.Char(
        string='Fifth word to type',
    )

    first_word_hard_to_learn = fields.Boolean(
        string='First word is hard to learn',
        related='first_word_to_train_id.hard_to_learn',
        readonly=False,
    )
    second_word_hard_to_learn = fields.Boolean(
        string='Second word is hard to learn',
        related='second_word_to_train_id.hard_to_learn',
        readonly=False,
    )
    third_word_hard_to_learn = fields.Boolean(
        string='Third word is hard to learn',
        related='third_word_to_train_id.hard_to_learn',
        readonly=False,
    )
    fourth_word_hard_to_learn = fields.Boolean(
        string='Fourth word is hard to learn',
        related='fourth_word_to_train_id.hard_to_learn',
        readonly=False,
    )
    fifth_word_hard_to_learn = fields.Boolean(
        string='Fifth word is hard to learn',
        related='fifth_word_to_train_id.hard_to_learn',
        readonly=False,
    )

    number_of_words_to_train = fields.Integer(
        string='Number of words to train',
    )

    def give_answer(self):
        current_context = self.env.context.copy()
        if self.env.context.get('given_fifth_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fifth_word_action')
            action['context'] = current_context
            if self._test_typing_is_right('fifth_'):
                self._update_last_exercise_date(self.fifth_word_to_train_id.id)
                # Notification for last question: interfere to click on close wizard on success wizard on small screens
                # Can be used Repeat all words option then!
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fifth_question_answered': True,
                })
                # Repeat all words training
                if 'repeat_all_words' in self.env.context:
                    return self.exercise_type_id.start_training()
                return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_fourth_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fourth_word_action')
            action['context'] = current_context
            if self._test_typing_is_right('fourth_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fifth_word_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fourth_question_answered': True,
                })
                self._update_last_exercise_date(self.fourth_word_to_train_id.id)
                # check if all words are learned
                if self.number_of_words_to_train == 4:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')
        elif self.env.context.get('given_third_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_third_word_action')
            action['context'] = current_context
            if self._test_typing_is_right('third_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fourth_word_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_third_question_answered': True,
                })
                self._update_last_exercise_date(self.third_word_to_train_id.id)
                # check if all words are learned
                if self.number_of_words_to_train == 3:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')
        elif self.env.context.get('given_second_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_second_word_action')
            action['context'] = current_context
            if self._test_typing_is_right('second_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_third_word_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_second_question_answered': True,
                })
                self._update_last_exercise_date(self.second_word_to_train_id.id)
                # check if all words are learned
                if self.number_of_words_to_train == 2:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')
        else: # there is self.env.context.get('given_first_answer')
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_first_word_action')
            action['context'] = current_context
            if self._test_typing_is_right('first_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_second_word_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_first_question_answered': True,
                })
                self._update_last_exercise_date(self.first_word_to_train_id.id)
                # check if all words are learned
                if self.number_of_words_to_train == 1:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')

        return action

    def _test_typing_is_right(self, field_prefix):
        """
        :param string field_prefix: 'first_' / 'second_' / ... / 'fifth_'
        :rtype: None или ValidationError
        """
        # It is m2o field
        right_answer = self[field_prefix + 'word_to_train_id'].hebrew_word
        right_answer_cleaned = right_answer.replace('\u202c', '').replace('\u202b', '') if right_answer else ''
        # It is Char field
        current_answer = self[field_prefix + 'word_typing']
        current_answer_cleaned = current_answer.replace('\u202c', '').replace('\u202b', '') if current_answer else ''
        return right_answer_cleaned == current_answer_cleaned
