from odoo import models, fields, _


class WizardWordTranslationTraining(models.TransientModel):

    _name = 'wizard_word_translation_training'
    _description = 'Wizard for word->translation training'

 
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

    first_word_to_train = fields.Many2one(
        string='First word to train',
        comodel_name='words',
    )

    second_word_to_train = fields.Many2one(
        string='Second word to train',
        comodel_name='words',
    )

    third_word_to_train = fields.Many2one(
        string='Third word to train',
        comodel_name='words',
    )

    fourth_word_to_train = fields.Many2one(
        string='Fourth word to train',
        comodel_name='words',
    )

    fifth_word_to_train = fields.Many2one(
        string='Fifth word to train',
        comodel_name='words',
    )





    # def action_create_prolongation_invoice(self):
    #     """
    #     Создание счетов на продление услуг по хранению позиции при выбранных договорах
    #     :return: None
    #     """
    #     self.agreement_ids._create_prolongation_invoice()
