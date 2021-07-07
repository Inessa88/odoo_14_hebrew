from odoo import models, fields, _


class WizardLearning(models.TransientModel):

    _name = 'wizard_learning'
    _description = 'Wizard for learning'

 
    # agreement_ids = fields.Many2many(
    #     string='Agreements',
    #     comodel_name='prs_store.agreement',
    #     relation='prs_store_wizard__prs_store_agreement__rel',
    #     column1='wizard_id',
    #     column2='agreement_id',
    # )

    # def action_create_prolongation_invoice(self):
    #     """
    #     Создание счетов на продление услуг по хранению позиции при выбранных договорах
    #     :return: None
    #     """
    #     self.agreement_ids._create_prolongation_invoice()
