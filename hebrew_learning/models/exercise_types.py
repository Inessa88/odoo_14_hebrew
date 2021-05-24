# -*- coding: utf-8 -*-

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
    