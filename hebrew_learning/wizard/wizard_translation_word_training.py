from odoo import models, fields, _


class WizardTranslationWordTraining(models.TransientModel):

    _name = 'wizard_translation_word_training'
    _description = 'Wizard for translation->word training'
    _inherit = ['choose_one_of_five_answers_mixin', 'common_part_for_all_trainings_mixin']


    number_of_words_to_train = fields.Integer(
        string='Number of words to train',
    )
 