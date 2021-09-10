import base64
from odoo import models, fields, _
from odoo import modules

class WizardTrainingFinished(models.TransientModel):

    _name = 'wizard_training_finished'
    _description = 'Wizard for finished training'

    def get_default_img():
        with open(modules.get_module_resource('hebrew_learning', 'static/img', 'image_success_2.png'),'rb') as f:
            return base64.b64encode(f.read())

    success_image = fields.Binary(
       string='Success image',
       default=get_default_img(),
    )

    def reload_page(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
