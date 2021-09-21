from odoo import models, fields, api, _


class WizardSentenceTraining(models.TransientModel):

    _name = 'wizard_sentence_training'
    _description = 'Wizard for sentence training'


    exercise_type_id = fields.Many2one(
        string='Exercise type id',
        comodel_name='exercise_types',
        required=True,
        ondelete='cascade',
    )

    number_of_sentences_left_to_train = fields.Integer(
        string='Number of sentences left to train',
        related='exercise_type_id.number_of_sentences_to_train',
    )

    first_sentence_typing = fields.Char(
        string='First sentence to type',
    )

    second_sentence_typing = fields.Char(
        string='Second sentence to type',
    )

    third_sentence_typing = fields.Char(
        string='Third sentence to type',
    )

    fourth_sentence_typing = fields.Char(
        string='Fourth sentence to type',
    )

    fifth_sentence_typing = fields.Char(
        string='Fifth sentence to type',
    )

    first_sentence_help = fields.Boolean(
        string='First sentence help to type',
    )

    second_sentence_help = fields.Boolean(
        string='Second sentence help to type',
    )

    third_sentence_help = fields.Boolean(
        string='Third sentence help to type',
    )

    fourth_sentence_help = fields.Boolean(
        string='Fourth sentence help to type',
    )

    fifth_sentence_help = fields.Boolean(
        string='Fifth sentence help to type',
    )

    number_of_sentences_to_train = fields.Integer(
        string='Number of sentences to train',
    )

    # ANSWERED QUESTIONS BLOCK
    first_question_answered = fields.Boolean(
        string='First question answered',
    )

    second_question_answered = fields.Boolean(
        string='Second question answered',
    )

    third_question_answered = fields.Boolean(
        string='Third question answered',
    )

    fourth_question_answered = fields.Boolean(
        string='Fourth question answered',
    )

    fifth_question_answered = fields.Boolean(
        string='Fifth question answered',
    )

    # FIRST SENTENCE TO TRAIN BLOCK
    first_sentence_to_train_id = fields.Many2one(
        string='First sentence to train',
        comodel_name='sentences',
    )

    first_hebrew_sentence = fields.Char(
        string='Hebrew sentence first',
        related='first_sentence_to_train_id.hebrew_sentence',
    )

    first_translation_sentence = fields.Char(
        string='Translation in Russian first',
        related='first_sentence_to_train_id.translation_sentence',
    )

    first_picture = fields.Binary(
        string='Image first',
        related='first_sentence_to_train_id.picture',
    )

    first_audio = fields.Char(
        string='Audio first',
        related='first_sentence_to_train_id.audio',
    )

    # SECOND SENTENCE TO TRAIN BLOCK
    second_sentence_to_train_id = fields.Many2one(
        string='Second sentence to train',
        comodel_name='sentences',
    )

    second_hebrew_sentence = fields.Char(
        string='Hebrew sentence second',
        related='second_sentence_to_train_id.hebrew_sentence',
    )

    second_translation_sentence = fields.Char(
        string='Translation in Russian second',
        related='second_sentence_to_train_id.translation_sentence',
    )

    second_picture = fields.Binary(
        string='Image second',
        related='second_sentence_to_train_id.picture',
    )

    # THIRD SENTENCE TO TRAIN BLOCK
    third_sentence_to_train_id = fields.Many2one(
        string='Third sentence to train',
        comodel_name='sentences',
    )

    third_hebrew_sentence = fields.Char(
        string='Hebrew sentence third',
        related='third_sentence_to_train_id.hebrew_sentence',
    )

    third_translation_sentence = fields.Char(
        string='Translation in Russian third',
        related='third_sentence_to_train_id.translation_sentence',
    )

    third_picture = fields.Binary(
        string='Image third',
        related='third_sentence_to_train_id.picture',
    )

    # FOURTH SENTENCE TO TRAIN BLOCK
    fourth_sentence_to_train_id = fields.Many2one(
        string='Fourth sentence to train',
        comodel_name='sentences',
    )

    fourth_hebrew_sentence = fields.Char(
        string='Hebrew sentence fourth',
        related='fourth_sentence_to_train_id.hebrew_sentence',
    )

    fourth_translation_sentence = fields.Char(
        string='Translation in Russian fourth',
        related='fourth_sentence_to_train_id.translation_sentence',
    )

    fourth_picture = fields.Binary(
        string='Image fourth',
        related='fourth_sentence_to_train_id.picture',
    )

    # FIFTH SENTENCE TO TRAIN BLOCK
    fifth_sentence_to_train_id = fields.Many2one(
        string='Fifth sentence to train',
        comodel_name='sentences',
    )

    fifth_hebrew_sentence = fields.Char(
        string='Hebrew sentence fifth',
        related='fifth_sentence_to_train_id.hebrew_sentence',
    )

    fifth_translation_sentence = fields.Char(
        string='Translation in Russian fifth',
        related='fifth_sentence_to_train_id.translation_sentence',
    )

    fifth_picture = fields.Binary(
        string='Image fifth',
        related='fifth_sentence_to_train_id.picture',
    )

    all_sentences_to_train_ids = fields.Many2many(
        string='All sentences to train',
        comodel_name='sentences',
    )


    def _update_last_exercise_date(self, sentence_id:int):
        uid = self.env.uid
        update_exercise_date_record = self.env['last_exercise_date'].search([
                ('user_id', '=', uid),
                ('exercise_type_id', '=', self.exercise_type_id.id),
                ('sentence_id', '=', sentence_id),
            ])

        # Initial training of this sentence
        if not update_exercise_date_record:
            self.env['last_exercise_date'].create({
                'user_id': uid,
                'exercise_type_id': self.exercise_type_id.id,
                'sentence_id': sentence_id,
                'number_of_times_exercise_is_done': 1,
            })
        else:
            current_number_of_repetitions = update_exercise_date_record.number_of_times_exercise_is_done + 1
            data = {
                'last_exercise_date': fields.Date.context_today(update_exercise_date_record),
                'number_of_times_exercise_is_done': current_number_of_repetitions,
            }
            # ('1', 'In a day'), X 5 TIMES => SUM TIMES: 5
            # ('3', 'In three days'), => SUM TIMES: 6
            # ('7', 'In a week'), => SUM TIMES: 7
            # ('14', 'In two weeks'), => SUM TIMES: 8
            # ('30', 'In a month'), X 3 TIMES => SUM TIMES: 11
            # ('90', 'In three months'), => SUM TIMES: 12
            # ('183', 'In half a year'), => SUM TIMES: 13-14-...
            # ('1000000', 'Never (initial learning)'),
            # Right now we learned 3rd time 3 days in a row, so move to next interval
            if update_exercise_date_record.repetition_interval == '1' and current_number_of_repetitions == 5:
                data['repetition_interval'] = '3'
            elif update_exercise_date_record.repetition_interval == '3' and current_number_of_repetitions == 6:
                data['repetition_interval'] = '7'
            elif update_exercise_date_record.repetition_interval == '7' and current_number_of_repetitions == 7:
                data['repetition_interval'] = '14'
            elif update_exercise_date_record.repetition_interval == '14' and current_number_of_repetitions == 8:
                data['repetition_interval'] = '30'
            elif update_exercise_date_record.repetition_interval == '30' and current_number_of_repetitions == 11:
                data['repetition_interval'] = '90'
            elif update_exercise_date_record.repetition_interval == '90' and current_number_of_repetitions == 12:
                data['repetition_interval'] = '183'
            update_exercise_date_record.write(data)

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                     submenu=submenu)
        model = res.get('model')
        if model and model == 'wizard_sentence_training' and view_type == 'form':
            arch = res.get('arch')
            if arch:
                default_first_sentence_to_train_id = self.env.context.get('default_first_sentence_to_train_id')
                if default_first_sentence_to_train_id:
                    first_sentence_to_train = self.env['sentences'].browse(default_first_sentence_to_train_id)
                    if first_sentence_to_train:
                        if first_sentence_to_train.audio:
                            arch = arch.replace('first_audio', first_sentence_to_train.audio)
                default_second_sentence_to_train_id = self.env.context.get('default_second_sentence_to_train_id')
                if default_second_sentence_to_train_id:
                    second_sentence_to_train = self.env['sentences'].browse(default_second_sentence_to_train_id)
                    if second_sentence_to_train:
                        if second_sentence_to_train.audio:
                            arch = arch.replace('second_audio', second_sentence_to_train.audio)
                default_third_sentence_to_train_id = self.env.context.get('default_third_sentence_to_train_id')
                if default_third_sentence_to_train_id:
                    third_sentence_to_train = self.env['sentences'].browse(default_third_sentence_to_train_id)
                    if third_sentence_to_train:
                        if third_sentence_to_train.audio:
                            arch = arch.replace('third_audio', third_sentence_to_train.audio)
                default_fourth_sentence_to_train_id = self.env.context.get('default_fourth_sentence_to_train_id')
                if default_fourth_sentence_to_train_id:
                    fourth_sentence_to_train = self.env['sentences'].browse(default_fourth_sentence_to_train_id)
                    if fourth_sentence_to_train:
                        if fourth_sentence_to_train.audio:
                            arch = arch.replace('fourth_audio', fourth_sentence_to_train.audio)
                default_fifth_sentence_to_train_id = self.env.context.get('default_fifth_sentence_to_train_id')
                if default_fifth_sentence_to_train_id:
                    fifth_sentence_to_train = self.env['sentences'].browse(default_fifth_sentence_to_train_id)
                    if fifth_sentence_to_train:
                        if fifth_sentence_to_train.audio:
                            arch = arch.replace('fifth_audio', fifth_sentence_to_train.audio)

                res['arch'] = arch


        return res

    def _return_success_action(self):
        action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_training_finished_action')
        # Hide edit buttons
        action['flags'] = {'mode': 'readonly'}
        return action

    def give_answer(self):
        current_context = self.env.context.copy()
        if self.env.context.get('given_fifth_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fifth_sentence_action')
            action['context'] = current_context
            if self._test_typing_is_right('fifth_'):
                self._update_last_exercise_date(self.fifth_sentence_to_train_id.id)
                # Notification for last question: interfere to click on close wizard on success wizard on small screens
                # Can be used Repeat all sentences option then!
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fifth_question_answered': True,
                })
                # Repeat all sentences training
                if 'repeat_all_sentences' in self.env.context:
                    return self.exercise_type_id.start_training()
                return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')

        elif self.env.context.get('given_fourth_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fourth_sentence_action')
            action['context'] = current_context
            if self._test_typing_is_right('fourth_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fifth_sentence_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_fourth_question_answered': True,
                })
                self._update_last_exercise_date(self.fourth_sentence_to_train_id.id)
                # check if all sentences are learned
                if self.number_of_sentences_to_train == 4:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')
        elif self.env.context.get('given_third_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_third_sentence_action')
            action['context'] = current_context
            if self._test_typing_is_right('third_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_fourth_sentence_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_third_question_answered': True,
                })
                self._update_last_exercise_date(self.third_sentence_to_train_id.id)
                # check if all sentences are learned
                if self.number_of_sentences_to_train == 3:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')
        elif self.env.context.get('given_second_answer'):
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_second_sentence_action')
            action['context'] = current_context
            if self._test_typing_is_right('second_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_third_sentence_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_second_question_answered': True,
                })
                self._update_last_exercise_date(self.second_sentence_to_train_id.id)
                # check if all sentences are learned
                if self.number_of_sentences_to_train == 2:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')
        else: # there is self.env.context.get('given_first_answer')
            action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_first_sentence_action')
            action['context'] = current_context
            if self._test_typing_is_right('first_'):
                action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_writing_training_second_sentence_action')
                action['context'] = current_context
                self.env.user.notify_success(message='Success')
                action['context'].update({
                    'default_first_question_answered': True,
                })
                self._update_last_exercise_date(self.first_sentence_to_train_id.id)
                # check if all sentences are learned
                if self.number_of_sentences_to_train == 1:
                    return self._return_success_action()
            else:
                self.env.user.notify_warning(message='Warning')

        return action

    def _test_typing_is_right(self, field_prefix):
        """
        :param string field_prefix: 'first_' / 'second_' / ... / 'fifth_'
        :rtype: Boolean
        """
        # It is m2o field
        right_answer = self[field_prefix + 'sentence_to_train_id'].hebrew_sentence
        right_answer_cleaned = right_answer.replace('\u202c', '').replace('\u202b', '') if right_answer else ''
        # It is Char field
        current_answer = self[field_prefix + 'sentence_typing']
        current_answer_cleaned = current_answer.replace('\u202c', '').replace('\u202b', '') if current_answer else ''
        return right_answer_cleaned == current_answer_cleaned
