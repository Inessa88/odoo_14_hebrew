from odoo import models, fields, _


class WizardSprintTraining(models.TransientModel):

    _name = 'wizard_sprint_training'
    _description = 'Wizard for sprint training'
    _inherit = ['common_part_for_all_trainings_mixin']

 
    RIGHT_ANSWER_OPTIONS = [
            ('0', 'Not applicable! (There is no question.)'),
            ('1', 'First answer is right one!'),
            ('2', 'Second answer is right one!'),
        ]

    # RIGHT ANSWERS BLOCK
    first_right_answer_number = fields.Selection(
        selection=RIGHT_ANSWER_OPTIONS,
        string='First right answer number', 
        required=True,
        default='0'
    )

    second_right_answer_number = fields.Selection(
        selection=RIGHT_ANSWER_OPTIONS,
        string='Second right answer number', 
        required=True,
        default='0'
    )

    third_right_answer_number = fields.Selection(
        selection=RIGHT_ANSWER_OPTIONS,
        string='Third right answer number', 
        required=True,
        default='0'
    )

    fourth_right_answer_number = fields.Selection(
        selection=RIGHT_ANSWER_OPTIONS,
        string='Fourth right answer number', 
        required=True,
        default='0'
    )

    fifth_right_answer_number = fields.Selection(
        selection=RIGHT_ANSWER_OPTIONS,
        string='Fifth right answer number', 
        required=True,
        default='0'
    )

    # POSSIBLE ANSWERS BLOCK
    # FIRST QUESTION
    first_question_first_answer = fields.Char(
        string='First question first answer',
    )

    first_question_second_answer = fields.Char(
        string='First question second answer',
    )


    # SECOND QUESTION
    second_question_first_answer = fields.Char(
        string='Second question first answer',
    )

    second_question_second_answer = fields.Char(
        string='Second question second answer',
    )


    # THIRD QUESTION
    third_question_first_answer = fields.Char(
        string='Third question first answer',
    )

    third_question_second_answer = fields.Char(
        string='Third question second answer',
    )


    # FOURTH QUESTION
    fourth_question_first_answer = fields.Char(
        string='Fourth question first answer',
    )

    fourth_question_second_answer = fields.Char(
        string='Fourth question second answer',
    )


    # FIFTH QUESTION
    fifth_question_first_answer = fields.Char(
        string='Fifth question first answer',
    )

    fifth_question_second_answer = fields.Char(
        string='Fifth question second answer',
    )

    number_of_words_to_train = fields.Integer(
        string='Number of words to train',
    )

    def give_answer(self):
        action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_sprint_training_action')
        action['context'] = self.env.context.copy()
        if self.env.context.get('given_fifth_answer_number'):
            if self.env.context.get('given_fifth_answer_number') == self.fifth_right_answer_number:
                # Notification for last question: interfere to click on close wizard on success wizard on small screens
                # Can be used Repeat all words option then!
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fifth_question_answered': True,
                })
                self._update_last_exercise_date(self.fifth_word_to_train_id.id)
                # Repeat all words training
                if 'repeat_all_words' in self.env.context:
                    return self.exercise_type_id.start_training()
                return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_fourth_answer_number'):
            if self.env.context.get('given_fourth_answer_number') == self.fourth_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fourth_question_answered': True,
                })
                self._update_last_exercise_date(self.fourth_word_to_train_id.id)
                if self.number_of_words_to_train == 4:
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_third_answer_number'):
            if self.env.context.get('given_third_answer_number') == self.third_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_third_question_answered': True,
                })
                self._update_last_exercise_date(self.third_word_to_train_id.id)
                if self.number_of_words_to_train == 3:
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_second_answer_number'):
            if self.env.context.get('given_second_answer_number') == self.second_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_second_question_answered': True,
                })
                self._update_last_exercise_date(self.second_word_to_train_id.id)
                if self.number_of_words_to_train == 2:
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        else: # there is 'given_first_answer_number' in self.env.context
            if self.env.context.get('given_first_answer_number') == self.first_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_first_question_answered': True,
                })
                self._update_last_exercise_date(self.first_word_to_train_id.id)
                if self.number_of_words_to_train == 1:
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        # Hide edit buttons
        action['flags'] = {'mode': 'readonly'}

        return action
