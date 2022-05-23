# -*- coding: utf-8 -*-
{
    'name': "Hebrew learning",  # Module title
    'summary': "Learn Hebrew words interactively",  # Module subtitle phrase
    'description': """App for learning Hebrew words on your own""",
    'author': "Inessa Petrova",
    'category': 'Uncategorized',
    'version': '14.0.1',
    "depends": ["web", "bus", "base"],
    # This data files will be loaded at the installation (commented because file is not added in this example)
    'data': [

        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/words.xml',
        'views/word_groups.xml',
        'views/sentences.xml',
        'views/exercise_types.xml',
        'views/last_exercise_date.xml',
        'views/hebrew_learning.xml',
                
        'data/exercise_types_data.xml',
        'data/word_groups_and_words_data_1.xml',
        'data/word_groups_and_words_data_2.xml',
        'data/word_groups_and_words_data_3.xml',
        'data/word_groups_and_words_data_4.xml',
        'data/word_groups_and_words_data_5.xml',
        'data/sentences_data.xml',

        'wizard/learning.xml',
        'wizard/word_translation_training.xml',
        'wizard/translation_word_training.xml',
        'wizard/writing_training.xml',
        'wizard/sprint_training.xml',
        'wizard/sentence_writing.xml',
        'wizard/training_finished.xml',
        'wizard/trainings.xml',

        "views/web_notify.xml"
    ],
    'installable': True,
    'application': True,
}
