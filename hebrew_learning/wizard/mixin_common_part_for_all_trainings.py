
from odoo import models, fields, api, _ 



class CommonPartForAllTrainingsMixin(models.AbstractModel):
    """
    Mixin to add common functionality to all trainings
    """
    
    _name = 'common_part_for_all_trainings_mixin'
    _description = 'Mixin to add common functionality to all trainings'


    exercise_type_id = fields.Many2one(
        string='Exercise type id',
        comodel_name='exercise_types',
        required=True,
        ondelete='cascade',
    )

    number_of_words_left_to_train = fields.Integer(
        string='Number of words left to train',
        related='exercise_type_id.number_of_words_to_train',
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

    # FIRST WORD TO TRAIN BLOCK
    first_word_to_train_id = fields.Many2one(
        string='First word to train',
        comodel_name='words',
    )

    first_hebrew_word = fields.Char(
        string='Hebrew word first',
        related='first_word_to_train_id.hebrew_word',
    )

    first_hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud first',
        related='first_word_to_train_id.hebrew_word_nikud',
    )

    first_pronunciation_word = fields.Char(
        string='Pronunciation word in Latin first',
        related='first_word_to_train_id.pronunciation_word',
    )

    first_translation_word = fields.Char(
        string='Translation in Russian first',
        related='first_word_to_train_id.translation_word',
    )

    first_note = fields.Text(
        string='Note first',
        related='first_word_to_train_id.note',
    )

    first_picture = fields.Binary(
        string='Image first',
        related='first_word_to_train_id.picture',
    )

    first_picture_present = fields.Binary(
        string='Image first present tense',
        related='first_word_to_train_id.picture_present',
    )

    first_audio = fields.Char(
        string='Audio first',
        related='first_word_to_train_id.audio',
    )

    # SECOND WORD TO TRAIN BLOCK
    second_word_to_train_id = fields.Many2one(
        string='Second word to train',
        comodel_name='words',
    )

    second_hebrew_word = fields.Char(
        string='Hebrew word second',
        related='second_word_to_train_id.hebrew_word',
    )

    second_hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud second',
        related='second_word_to_train_id.hebrew_word_nikud',
    )

    second_pronunciation_word = fields.Char(
        string='Pronunciation word in Latin second',
        related='second_word_to_train_id.pronunciation_word',
    )

    second_translation_word = fields.Char(
        string='Translation in Russian second',
        related='second_word_to_train_id.translation_word',
    )

    second_note = fields.Text(
        string='Note second',
        related='second_word_to_train_id.note',
    )

    second_picture = fields.Binary(
        string='Image second',
        related='second_word_to_train_id.picture',
    )

    second_picture_present = fields.Binary(
        string='Image second present tense',
        related='second_word_to_train_id.picture_present',
    )

    # THIRD WORD TO TRAIN BLOCK
    third_word_to_train_id = fields.Many2one(
        string='Third word to train',
        comodel_name='words',
    )

    third_hebrew_word = fields.Char(
        string='Hebrew word third',
        related='third_word_to_train_id.hebrew_word',
    )

    third_hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud third',
        related='third_word_to_train_id.hebrew_word_nikud',
    )

    third_pronunciation_word = fields.Char(
        string='Pronunciation word in Latin third',
        related='third_word_to_train_id.pronunciation_word',
    )

    third_translation_word = fields.Char(
        string='Translation in Russian third',
        related='third_word_to_train_id.translation_word',
    )

    third_note = fields.Text(
        string='Note third',
        related='third_word_to_train_id.note',
    )

    third_picture = fields.Binary(
        string='Image third',
        related='third_word_to_train_id.picture',
    )

    third_picture_present = fields.Binary(
        string='Image third present tense',
        related='third_word_to_train_id.picture_present',
    )

    # FOURTH WORD TO TRAIN BLOCK
    fourth_word_to_train_id = fields.Many2one(
        string='Fourth word to train',
        comodel_name='words',
    )

    fourth_hebrew_word = fields.Char(
        string='Hebrew word fourth',
        related='fourth_word_to_train_id.hebrew_word',
    )

    fourth_hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud fourth',
        related='fourth_word_to_train_id.hebrew_word_nikud',
    )

    fourth_pronunciation_word = fields.Char(
        string='Pronunciation word in Latin fourth',
        related='fourth_word_to_train_id.pronunciation_word',
    )

    fourth_translation_word = fields.Char(
        string='Translation in Russian fourth',
        related='fourth_word_to_train_id.translation_word',
    )

    fourth_note = fields.Text(
        string='Note fourth',
        related='fourth_word_to_train_id.note',
    )

    fourth_picture = fields.Binary(
        string='Image fourth',
        related='fourth_word_to_train_id.picture',
    )

    fourth_picture_present = fields.Binary(
        string='Image fourth present tense',
        related='fourth_word_to_train_id.picture_present',
    )

    # FIFTH WORD TO TRAIN BLOCK
    fifth_word_to_train_id = fields.Many2one(
        string='Fifth word to train',
        comodel_name='words',
    )

    fifth_hebrew_word = fields.Char(
        string='Hebrew word fifth',
        related='fifth_word_to_train_id.hebrew_word',
    )

    fifth_hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud fifth',
        related='fifth_word_to_train_id.hebrew_word_nikud',
    )

    fifth_pronunciation_word = fields.Char(
        string='Pronunciation word in Latin fifth',
        related='fifth_word_to_train_id.pronunciation_word',
    )

    fifth_translation_word = fields.Char(
        string='Translation in Russian fifth',
        related='fifth_word_to_train_id.translation_word',
    )

    fifth_note = fields.Text(
        string='Note fifth',
        related='fifth_word_to_train_id.note',
    )

    fifth_picture = fields.Binary(
        string='Image fifth',
        related='fifth_word_to_train_id.picture',
    )

    fifth_picture_present = fields.Binary(
        string='Image fifth present tense',
        related='fifth_word_to_train_id.picture_present',
    )

    all_words_to_train_ids = fields.Many2many(
        string='All words to train',
        comodel_name='words',
    )


    def _update_last_exercise_date(self, word_id:int):
        uid = self.env.uid
        update_exercise_date_record = self.env['last_exercise_date'].search([
                ('user_id', '=', uid),
                ('exercise_type_id', '=', self.exercise_type_id.id),
                ('word_id', '=', word_id),
            ])
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
        """
        расширяем метод, чтобы убрать ненужные действия из кнопки "действие" на форме и списке заявок на хранение
        """
        res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                     submenu=submenu)
        model = res.get('model')
        if model and model in (
            'wizard_learning', 'wizard_sprint_training', 'wizard_translation_word_training',
            'wizard_word_translation_training', 'wizard_writing_training'
        ) and view_type == 'form':
            arch = res.get('arch')
            if arch:
                default_first_word_to_train_id = self.env.context.get('default_first_word_to_train_id')
                if default_first_word_to_train_id:
                    first_word_to_train = self.env['words'].browse(default_first_word_to_train_id)
                    if first_word_to_train:
                        if first_word_to_train.audio_present:
                            arch = arch.replace('first_audio_present', first_word_to_train.audio_present)
                        if first_word_to_train.audio:
                            arch = arch.replace('first_audio', first_word_to_train.audio)
                default_second_word_to_train_id = self.env.context.get('default_second_word_to_train_id')
                if default_second_word_to_train_id:
                    second_word_to_train = self.env['words'].browse(default_second_word_to_train_id)
                    if second_word_to_train:
                        if second_word_to_train.audio_present:
                            arch = arch.replace('second_audio_present', second_word_to_train.audio_present)
                        if second_word_to_train.audio:
                            arch = arch.replace('second_audio', second_word_to_train.audio)
                default_third_word_to_train_id = self.env.context.get('default_third_word_to_train_id')
                if default_third_word_to_train_id:
                    third_word_to_train = self.env['words'].browse(default_third_word_to_train_id)
                    if third_word_to_train:
                        if third_word_to_train.audio_present:
                            arch = arch.replace('third_audio_present', third_word_to_train.audio_present)
                        if third_word_to_train.audio:
                            arch = arch.replace('third_audio', third_word_to_train.audio)
                default_fourth_word_to_train_id = self.env.context.get('default_fourth_word_to_train_id')
                if default_fourth_word_to_train_id:
                    fourth_word_to_train = self.env['words'].browse(default_fourth_word_to_train_id)
                    if fourth_word_to_train:
                        if fourth_word_to_train.audio_present:
                            arch = arch.replace('fourth_audio_present', fourth_word_to_train.audio_present)
                        if fourth_word_to_train.audio:
                            arch = arch.replace('fourth_audio', fourth_word_to_train.audio)
                default_fifth_word_to_train_id = self.env.context.get('default_fifth_word_to_train_id')
                if default_fifth_word_to_train_id:
                    fifth_word_to_train = self.env['words'].browse(default_fifth_word_to_train_id)
                    if fifth_word_to_train:
                        if fifth_word_to_train.audio_present:
                            arch = arch.replace('fifth_audio_present', fifth_word_to_train.audio_present)
                        if fifth_word_to_train.audio:
                            arch = arch.replace('fifth_audio', fifth_word_to_train.audio)

                res['arch'] = arch


        return res

    def _return_success_action(self):
        action = self.env["ir.actions.actions"]._for_xml_id('hebrew_learning.wizard_training_finished_action')
        # Hide edit buttons
        action['flags'] = {'mode': 'readonly'}
        return action
        
