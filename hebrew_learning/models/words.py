# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Words(models.Model):
    _name = 'words'
    _description = 'Words'


    hebrew_word = fields.Char(
        string='Hebrew word',
    )

    hebrew_word_nikud = fields.Char(
        string='Hebrew word with nikud',
        required=True,
    )

    pronunciation_word = fields.Char(
        string='Pronunciation word in Latin',
        required=True,
    )

    translation_word = fields.Char(
        string='Translation in Russian',
        required=True,
    )

    note = fields.Text(
        string='Note',
    )

    picture = fields.Binary(
        string='Image',
    )

    picture_present = fields.Binary(
        string='Image present tense',
    )

    audio = fields.Char(
        string='Audio',
    )

    audio_present = fields.Char(
        string='Audio present tense',
    )

    word_user = fields.Many2many(
        string='Users who added the word',
        comodel_name='res.users',
    )

    button_learn_this_word_visible = fields.Boolean(
        string='Button "Learn this word" is visible',
        compute='_compute_button_learn_this_word_visible',
    )

    picture_exists = fields.Boolean(
        string='There is picture for this word',
        compute='_compute_picture_exists',
        store=True,
        default=False,
    )

    hard_to_learn = fields.Boolean(
        string='This word is hard one!',
        default=False,
    )

    properly_learned = fields.Boolean(
        string='This word is properly learned!',
        default=False,
    )

    def name_get(self):
        # Возвращать название рекорда в форме: "hebrew_word"
        return [(record.id, record.hebrew_word) for record in self]

    def CleanNikkudFromHebrew(self, hebrew):
        nikkud  = (
            "֑", "֒", "֓", "֔", "֕", "֖", "֗", "֘", "֙", "֚", "֛", "֜", "֝", "֞", "֟", "֠", "֡", "֢", "֣", "֤", "֥", "֦",
            "֧", "֨", "֩", "֪", "֫", "֬", "֭", "֮", "֯", "ְ", "ֱ", "ֲ", "ֳ", "ִ", "ֵ", "ֶ", "ַ", "ָ", "ֹ", "ֺ", "ֻ", "ּ",
            "ֽ", "־", "ֿ", "׀", "ׁ", "ׂ", "׃", "ׄ", "ׅ", "׆", "ׇ", 
        )
        for character in nikkud:
            if character in hebrew:
                hebrew = hebrew.replace(character, "")
        return hebrew

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if values.get('hebrew_word_nikud'):
                values['hebrew_word'] = self.CleanNikkudFromHebrew(values.get('hebrew_word_nikud'))
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('hebrew_word_nikud'):
            vals['hebrew_word'] = self.CleanNikkudFromHebrew(vals.get('hebrew_word_nikud'))
        return super().write(vals)

    def learn_this_word(self):
        uid = self.env.uid
        for word in self:
            word.word_user = [(4, uid)]

    def _compute_button_learn_this_word_visible(self):
        # Current user id
        uid = self.env.uid
        for record in self:
            if uid in record.word_user.ids:
                record.button_learn_this_word_visible = False
            else:
                record.button_learn_this_word_visible = True

    @api.depends("picture")
    def _compute_picture_exists(self):
        for record in self:
            if record.picture:
                record.picture_exists = True
            else:
                record.picture_exists = False