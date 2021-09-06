
from odoo import models, fields, _ 



class ChooseOneOfFiveAnswersMixin(models.AbstractModel):
    """
    Mixin to add fields about 5 posible answers
    """
    
    _name = 'choose_one_of_five_answers_mixin'
    _description = 'Mixin to add fields about 5 posible answers'


    RIGHT_ANSWER_OPTIONS = [
            ('0', 'Not applicable! (There is no question.)'),
            ('1', 'First answer is right one!'),
            ('2', 'Second answer is right one!'),
            ('3', 'Third answer is right one!'),
            ('4', 'Fourth answer is right one!'),
            ('5', 'Fifth answer is right one!')
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

    first_question_third_answer = fields.Char(
        string='First question third answer',
    )

    first_question_fourth_answer = fields.Char(
        string='First question fourth answer',
    )

    first_question_fifth_answer = fields.Char(
        string='First question fifth answer',
    )

    # SECOND QUESTION
    second_question_first_answer = fields.Char(
        string='Second question first answer',
    )

    second_question_second_answer = fields.Char(
        string='Second question second answer',
    )

    second_question_third_answer = fields.Char(
        string='Second question third answer',
    )

    second_question_fourth_answer = fields.Char(
        string='Second question fourth answer',
    )

    second_question_fifth_answer = fields.Char(
        string='Second question fifth answer',
    )

    # THIRD QUESTION
    third_question_first_answer = fields.Char(
        string='Third question first answer',
    )

    third_question_second_answer = fields.Char(
        string='Third question second answer',
    )

    third_question_third_answer = fields.Char(
        string='Third question third answer',
    )

    third_question_fourth_answer = fields.Char(
        string='Third question fourth answer',
    )

    third_question_fifth_answer = fields.Char(
        string='Third question fifth answer',
    )   

    # FOURTH QUESTION
    fourth_question_first_answer = fields.Char(
        string='Fourth question first answer',
    )

    fourth_question_second_answer = fields.Char(
        string='Fourth question second answer',
    )

    fourth_question_third_answer = fields.Char(
        string='Fourth question third answer',
    )

    fourth_question_fourth_answer = fields.Char(
        string='Fourth question fourth answer',
    )

    fourth_question_fifth_answer = fields.Char(
        string='Fourth question fifth answer',
    )    

    # FIFTH QUESTION
    fifth_question_first_answer = fields.Char(
        string='Fifth question first answer',
    )

    fifth_question_second_answer = fields.Char(
        string='Fifth question second answer',
    )

    fifth_question_third_answer = fields.Char(
        string='Fifth question third answer',
    )

    fifth_question_fourth_answer = fields.Char(
        string='Fifth question fourth answer',
    )

    fifth_question_fifth_answer = fields.Char(
        string='Fifth question fifth answer',
    )    


    def _return_next_action(self):
        next_translation_word_action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_translation_word_training_action')
        next_writing_action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_action')
        # return action with next exercise
        if self._table == 'wizard_word_translation_training':
            action = next_translation_word_action
            # Hide edit buttons
            action['flags'] = {'mode': 'readonly'}
            exercise_type_id = self.env.ref('hebrew_learning.translation_word').id
        else: # self._table == 'wizard_translation_word_training':
            action = next_writing_action
            exercise_type_id = self.env.ref('hebrew_learning.writing').id
        action['context'] = self.env.context.copy()
        action['context'].update({
            'default_exercise_type_id': exercise_type_id,
            'default_first_question_answered': False,
            'default_second_question_answered': False,
            'default_third_question_answered': False,
            'default_fourth_question_answered': False,
            'given_fifth_answer_number': False,
            'given_fourth_answer_number': False,
            'given_third_answer_number': False,
            'given_second_answer_number': False,
            'given_first_answer_number': False,
        })
        if self._table == 'wizard_word_translation_training':
            five_words_to_train = [
                self.first_word_to_train_id.id, self.second_word_to_train_id.id,
                self.third_word_to_train_id.id, self.fourth_word_to_train_id.id,
                self.fifth_word_to_train_id.id
            ]
            current_exercise_type_id = self.exercise_type_id.id
            # switch type of exercise to initial learning
            self.exercise_type_id = self.env.ref('hebrew_learning.learning').id
            self.exercise_type_id.update_context_for_translation_exercises(
                five_words_to_train, action['context']
            )
            self.exercise_type_id = current_exercise_type_id

        return action

    def give_answer(self):
        # return_action_name can be: 'hebrew_learning.wizard_word_translation_training_action' or 'hebrew_learning.wizard_translation_word_training_action'
        action = self.env["ir.actions.actions"]._for_xml_id(
            self.env.context.get('return_action_name')
        )
        action['context'] = self.env.context.copy()
        # next action (in case of initial learning)

        if self.env.context.get('given_fifth_answer_number'):
            if self.env.context.get('given_fifth_answer_number') == self.fifth_right_answer_number:
                # Notification for last question: interfere to click on close wizard on success wizard on small screens
                # Can be used Repeat all words option then!
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fifth_question_answered': True,
                })
                self._update_last_exercise_date()
                if 'initial_learning' in self.env.context:
                    return self._return_next_action()
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
                if self.number_of_words_to_train == 4:
                    self._update_last_exercise_date()
                    if 'initial_learning' in self.env.context:
                        return self._return_next_action()
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_third_answer_number'):
            if self.env.context.get('given_third_answer_number') == self.third_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_third_question_answered': True,
                })
                if self.number_of_words_to_train == 3:
                    self._update_last_exercise_date()
                    if 'initial_learning' in self.env.context:
                        return self._return_next_action()
                    return self._return_success_action()

            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_second_answer_number'):
            if self.env.context.get('given_second_answer_number') == self.second_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_second_question_answered': True,
                })
                if self.number_of_words_to_train == 2:
                    self._update_last_exercise_date()
                    if 'initial_learning' in self.env.context:
                        return self._return_next_action()
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        else: # there is self.env.context.get('given_first_answer_number')
            if self.env.context.get('given_first_answer_number') == self.first_right_answer_number:
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_first_question_answered': True,
                })
                if self.number_of_words_to_train == 1:
                    self._update_last_exercise_date()
                    if 'initial_learning' in self.env.context:
                        return self._return_next_action()
                    return self._return_success_action()
            else: # wrong anser on this question
                self.env.user.notify_warning(message='Warning')

        # Hide edit buttons
        action['flags'] = {'mode': 'readonly'}

        return action
