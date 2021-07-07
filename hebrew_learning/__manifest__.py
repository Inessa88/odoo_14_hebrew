# -*- coding: utf-8 -*-
{
    'name': "Hebrew learning",  # Module title
    'summary': "Learn Hebrew words interactively",  # Module subtitle phrase
    'description': """App for learning Hebrew words on your own""",
    'author': "Inessa Petrova",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented because file is not added in this example)
    'data': [

        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/words.xml',
        'views/word_groups.xml',
        'views/exercise_types.xml',
        'views/last_exercise_date.xml',
        # 'views/outcome.xml',
        # 'views/currency_exchange.xml',
        # 'views/test_speed.xml',

        'views/hebrew_learning.xml',
                
        # 'data/res_user_data.xml',
        'data/exercise_types_data.xml',
        'data/word_groups_and_words_data.xml',

        'wizard/learning.xml',
        'wizard/word_translation_training.xml',
        'wizard/translation_word_training.xml',
        'wizard/writing_training.xml',
        'wizard/sprint_training.xml',
        'wizard/trainings.xml',
    ],
    'installable': True,
    'application': True,
}
