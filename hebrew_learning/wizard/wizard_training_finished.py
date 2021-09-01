import base64
import random
from odoo import models, fields, _
from odoo import modules

class WizardTrainingFinished(models.TransientModel):

    _name = 'wizard_training_finished'
    _description = 'Wizard for finished training'

    def get_default_img():
        few_success_image_names = (
            'image_success_1.png',
            'image_success_2.png',
            'image_success_3.png',
            'image_success_4.png',
            'image_success_5.png',
        )
        success_image = random.choice(few_success_image_names)
        with open(modules.get_module_resource('hebrew_learning', 'static/img', success_image),'rb') as f:
            return base64.b64encode(f.read())

    success_image = fields.Binary(
       string='Success image',
       default=get_default_img(),
    )
