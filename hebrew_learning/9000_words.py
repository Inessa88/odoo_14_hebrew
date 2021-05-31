"""
HOW IT WORKS:

INITIAL DATA:

    NUMBER_TO_START_COUNTING_GROUPS = 1
    NUMBER_TO_START_COUNTING_WORDS = 1

AND

    groups_and_words_to_parce = [
        # first group name
        (
            "first_group_name_ru",
            # first group's words
            [
                (
                    "translation_word_1",
                    "pronunciation_word_1",
                    "hebrew_word_nikud_1"
                ),
                (
                    "translation_word_2",
                    "pronunciation_word_2",
                    "hebrew_word_nikud_2"
                ),
            ]
        ),
        # second group name
        (
            "second_group_name_ru",
            # second group's' words
            [
                (
                    "translation_word_3",
                    "pronunciation_word_3",
                    "hebrew_word_nikud_3"
                ),
                (
                    "translation_word_4",
                    "pronunciation_word_4",
                    "hebrew_word_nikud_4"
                ),
            ]
        ),
    ]

RESULT:

        <record id="group_1" model="word_groups">
            <field name="word_group_name">first_group_name_ru</field>
        </record>

    
        <record id="word_1" model="words">
            <field name="translation_word">translation_word_1</field>
            <field name="pronunciation_word">pronunciation_word_1</field>
            <field name="hebrew_word_nikud">hebrew_word_nikud_1</field>
            <!-- <field name="picture" type="base64" file="hebrew_learning/static/img/word_1.png"/> -->
            <field name="group_ids" eval="[(4, ref('group_1'))]"/>
        </record>

        
        <record id="word_2" model="words">
            <field name="translation_word">translation_word_2</field>
            <field name="pronunciation_word">pronunciation_word_2</field>
            <field name="hebrew_word_nikud">hebrew_word_nikud_2</field>
            <!-- <field name="picture" type="base64" file="hebrew_learning/static/img/word_2.png"/> -->
            <field name="group_ids" eval="[(4, ref('group_1'))]"/>
        </record>

        
        <record id="group_2" model="word_groups">
            <field name="word_group_name">second_group_name_ru</field>
        </record>

    
        <record id="word_3" model="words">
            <field name="translation_word">translation_word_3</field>
            <field name="pronunciation_word">pronunciation_word_3</field>
            <field name="hebrew_word_nikud">hebrew_word_nikud_3</field>
            <!-- <field name="picture" type="base64" file="hebrew_learning/static/img/word_3.png"/> -->
            <field name="group_ids" eval="[(4, ref('group_2'))]"/>
        </record>

        
        <record id="word_4" model="words">
            <field name="translation_word">translation_word_4</field>
            <field name="pronunciation_word">pronunciation_word_4</field>
            <field name="hebrew_word_nikud">hebrew_word_nikud_4</field>
            <!-- <field name="picture" type="base64" file="hebrew_learning/static/img/word_4.png"/> -->
            <field name="group_ids" eval="[(4, ref('group_2'))]"/>
        </record>

"""

NUMBER_TO_START_COUNTING_GROUPS = 1
NUMBER_TO_START_COUNTING_WORDS = 1

def form_group_creation_record(group_name_ru):
    return (

    """
        <record id="group_{}" model="word_groups">
            <field name="word_group_name">{}</field>
        </record>

    """.format(NUMBER_TO_START_COUNTING_GROUPS, group_name_ru)
    )

def form_word_creation_record(words_list, NUMBER_TO_START_COUNTING_WORDS, group_name_eng):
    words_creation_records = ""
    for word_data in words_list:
        words_creation_records += """
        <record id="word_{}" model="words">
            <field name="translation_word">{}</field>
            <field name="pronunciation_word">{}</field>
            <field name="hebrew_word_nikud">{}</field>
            <!-- <field name="picture" type="base64" file="hebrew_learning/static/img/word_{}.png"/> -->
            <field name="group_ids" eval="[(4, ref('group_{}'))]"/>
        </record>

        """.format(
            # number in <record id="word_{}"...
            NUMBER_TO_START_COUNTING_WORDS,
            # translation
            word_data[0],
            # pronunciation
            word_data[1],
            # nikud
            word_data[2],
            # number in <field name="picture"... file="hebrew_learning/static/img/word_{}.png"
            NUMBER_TO_START_COUNTING_WORDS,
            # group name
            group_name_eng
        )
        NUMBER_TO_START_COUNTING_WORDS += 1
        

    return words_creation_records, NUMBER_TO_START_COUNTING_WORDS




groups_and_words_to_parce = [
    # (
    #     # group_name_ru
    #     "1. Местоимения",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "я",
    #             # pronunciation_word
    #             "ani",
    #             # hebrew_word_nikud
    #             "‫אֲנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ты (муж. род)",
    #             # pronunciation_word
    #             "ata",
    #             # hebrew_word_nikud
    #             "‬‫אַתָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "ты (жен. род)",
    #             # pronunciation_word
    #             "at",
    #             # hebrew_word_nikud
    #             "‫אַת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "он",
    #             # pronunciation_word
    #             "hu",
    #             # hebrew_word_nikud
    #             "‫הוּא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "она",
    #             # pronunciation_word
    #             "hi",
    #             # hebrew_word_nikud
    #             "‬‫הִיא‬"
    #         ),
    #         (
    #             # translation_word
    #             "мы",
    #             # pronunciation_word
    #             "a'naχnu",
    #             # hebrew_word_nikud
    #             "‫אֲנַחנו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вы (муж. род)",
    #             # pronunciation_word
    #             "atem",
    #             # hebrew_word_nikud
    #             "‫אַתֶם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вы (жен. род)",
    #             # pronunciation_word
    #             "aten",
    #             # hebrew_word_nikud
    #             "‬‫אַתֶן‬"
    #         ),
    #         (
    #             # translation_word
    #             "Вы (вежл. форма, ед., муж. род)",
    #             # pronunciation_word
    #             "ata",
    #             # hebrew_word_nikud
    #             "‬‫אַתָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Вы (вежл. форма, ед., жен. род)",
    #             # pronunciation_word
    #             "at",
    #             # hebrew_word_nikud
    #             "‬‫אַת‬"
    #         ),
    #         (
    #             # translation_word
    #             "Вы (вежл. форма, мн., муж. род)",
    #             # pronunciation_word
    #             "atem",
    #             # hebrew_word_nikud
    #             "‫אַתֶם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Вы (вежл. форма, мн., жен. род",
    #             # pronunciation_word
    #             "aten",
    #             # hebrew_word_nikud
    #             "‬‫אַתֶן‬"
    #         ),
    #         (
    #             # translation_word
    #             "они (муж. род)",
    #             # pronunciation_word
    #             "hem",
    #             # hebrew_word_nikud
    #             "‬‫הֵם‬"
    #         ),
    #         (
    #             # translation_word
    #             "они (жен. род)",
    #             # pronunciation_word
    #             "hen",
    #             # hebrew_word_nikud
    #             "‬‫הֵן‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "2. Приветствия. Прощания. Извинения. Благодарность",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Здравствуй!",
    #             # pronunciation_word
    #             "ʃalom!",
    #             # hebrew_word_nikud
    #             "‬!‫שָלוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "Здравствуйте!",
    #             # pronunciation_word
    #             "ʃalom!",
    #             # hebrew_word_nikud
    #             "!‫שָלוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Доброе утро!",
    #             # pronunciation_word
    #             "'boker tov!",
    #             # hebrew_word_nikud
    #             "בּוֹקֶר‬ ‫טוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "Добрый день!",
    #             # pronunciation_word
    #             "ʦaha'rayim tovim!",
    #             # hebrew_word_nikud
    #             "צָהֳרַיִים‬ ‫טוֹבִים‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Добрый вечер!",
    #             # pronunciation_word
    #             "'erev tov!",
    #             # hebrew_word_nikud
    #             "‬‬עֶרֶב‬ ‫טוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "здороваться, приветствовать",
    #             # pronunciation_word
    #             "lomar ʃalom",
    #             # hebrew_word_nikud
    #             "‬‫‬לוֹמַר‬ ‫שָלוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "Привет!",
    #             # pronunciation_word
    #             "hai!",
    #             # hebrew_word_nikud
    #             "!‫הַיי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "привет, приветствие",
    #             # pronunciation_word
    #             "ahlan",
    #             # hebrew_word_nikud
    #             "‬‫אַהלַן‬"
    #         ),
    #         (
    #             # translation_word
    #             "Как дела? (к муж.)",
    #             # pronunciation_word
    #             "ma ʃlomχa?",
    #             # hebrew_word_nikud
    #             "‬‬‬מַה‬ ‫שלוֹמך‬"
    #         ),
    #         (
    #             # translation_word
    #             "Как дела? (у тебя)",
    #             # pronunciation_word
    #             "ma niʃma?",
    #             # hebrew_word_nikud
    #             "‬‬מַה‬ ‫נִשמָע‬"
    #         ),
    #         (
    #             # translation_word
    #             "Что нового?",
    #             # pronunciation_word
    #             "ma χadaʃ?",
    #             # hebrew_word_nikud
    #             "‬‬מַה‬ ‫חָדָש‬"
    #         ),
    #         (
    #             # translation_word
    #             "До свидания! (на «Вы»)",
    #             # pronunciation_word
    #             "lehitraʾot!",
    #             # hebrew_word_nikud
    #             "‬‬‫לְהִתרָאוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "До свидания! Пока! (на «ты»)",
    #             # pronunciation_word
    #             "bai!",
    #             # hebrew_word_nikud
    #             "‬!‫בַּי‬"
    #         ),
    #         (
    #             # translation_word
    #             "До скорой встречи!",
    #             # pronunciation_word
    #             "lehitraʾot bekarov!",
    #             # hebrew_word_nikud
    #             "לְהִתרָאוֹת‬ ‫בְּקָרוֹב‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прощаться",
    #             # pronunciation_word
    #             "lomar lehitraʾot",
    #             # hebrew_word_nikud
    #             "‬‬לוֹמַר‬ ‫לְהִתרָאוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "Спасибо!",
    #             # pronunciation_word
    #             "toda!",
    #             # hebrew_word_nikud
    #             "‬!‫תוֹדָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Большое спасибо!",
    #             # pronunciation_word
    #             "toda raba!",
    #             # hebrew_word_nikud
    #             "‬‬תוֹדָה‬ ‫רַבָּה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Пожалуйста (ответ)",
    #             # pronunciation_word
    #             "bevakaʃa",
    #             # hebrew_word_nikud
    #             "‬‫בְּבַקָשָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Не стоит благодарности",
    #             # pronunciation_word
    #             "al lo davar",
    #             # hebrew_word_nikud
    #             "עַל‬ ‫לֹא‬ ‫דָבָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "Не за что",
    #             # pronunciation_word
    #             "ein beʿad ma",
    #             # hebrew_word_nikud
    #             "‬אֵין‬ ‫בְּעַד‬ ‫מָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Извини! Извините!",
    #             # pronunciation_word
    #             "sliχa!",
    #             # hebrew_word_nikud
    #             "!‫סלִיחָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "извинять",
    #             # pronunciation_word
    #             "lis'loaχ",
    #             # hebrew_word_nikud
    #             "‬‫לִסלוֹח‬"
    #         ),
    #         (
    #             # translation_word
    #             "извиняться",
    #             # pronunciation_word
    #             "lehitnaʦel",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתנַצֵל‬"
    #         ),
    #         (
    #             # translation_word
    #             "Мои извинения. (м.р.)",
    #             # pronunciation_word
    #             "ani mitnaʦel",
    #             # hebrew_word_nikud
    #             "‬אֲנִי‬ ‫מִתנַצֵל‬"
    #         ),
    #         (
    #             # translation_word
    #             "Мои извинения. (ж.р.)",
    #             # pronunciation_word
    #             "ani mitna'ʦelet",
    #             # hebrew_word_nikud
    #             "אֲנִי‬ ‫מִתנַצֵלֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Простите! (м.р.)",
    #             # pronunciation_word
    #             "ani miʦtaʿer",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "Простите!(ж.р.)",
    #             # pronunciation_word
    #             "ani miʦta'ʿeret",
    #             # hebrew_word_nikud
    #             "‬אֲנִי‬ ‫מִצטַעֵרֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "прощать (кого-л.)",
    #             # pronunciation_word
    #             "lis'loaχ",
    #             # hebrew_word_nikud
    #             "‫לִסלוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Ничего страшного (ответ)",
    #             # pronunciation_word
    #             "lo nora",
    #             # hebrew_word_nikud
    #             "לֹא‬ ‫נוֹרָא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пожалуйста (при просьбе)",
    #             # pronunciation_word
    #             "bevakaʃa",
    #             # hebrew_word_nikud
    #             "‫בְּבַקָשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Не забудьте! (м.р.)",
    #             # pronunciation_word
    #             "al tiʃkaχ!",
    #             # hebrew_word_nikud
    #             "אַל‬ ‫תִשכַּח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Конечно!",
    #             # pronunciation_word
    #             "'betaχ!",
    #             # hebrew_word_nikud
    #             "‫בֶּטַח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Конечно нет!",
    #             # pronunciation_word
    #             "'betaχ ʃelo!",
    #             # hebrew_word_nikud
    #             "בֶּטַח‬ ‫שֶלֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Согласен!",
    #             # pronunciation_word
    #             "okei!",
    #             # hebrew_word_nikud
    #             "‫אוֹקֵיי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Хватит!",
    #             # pronunciation_word
    #             "maspik!",
    #             # hebrew_word_nikud
    #             "‫מַספִּיק‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "3. Обращения",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Извините! (обращение)",
    #             # pronunciation_word
    #             "sliχa!",
    #             # hebrew_word_nikud
    #             "‬!‫סלִיחָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "господин",
    #             # pronunciation_word
    #             "adon",
    #             # hebrew_word_nikud
    #             "‫אָדוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "госпожа",
    #             # pronunciation_word
    #             "gvirti",
    #             # hebrew_word_nikud
    #             "‬‫גבִרתִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "девушка",
    #             # pronunciation_word
    #             "'gveret",
    #             # hebrew_word_nikud
    #             "‫גבֶרֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "молодой человек",
    #             # pronunciation_word
    #             "baχur ʦaʿir",
    #             # hebrew_word_nikud
    #             "בָּחוּר‬ ‫צָעִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мальчик",
    #             # pronunciation_word
    #             "'yeled",
    #             # hebrew_word_nikud
    #             "‫יֶלֶד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "девочка",
    #             # pronunciation_word
    #             "yalda",
    #             # hebrew_word_nikud
    #             "‫יַלדָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "4. Числа от 1 до 100",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "0 ноль",
    #             # pronunciation_word
    #             "'efes",
    #             # hebrew_word_nikud
    #             "‬‫אֶפֶס‬"
    #         ),
    #         (
    #             # translation_word
    #             "1 один",
    #             # pronunciation_word
    #             "eχad",
    #             # hebrew_word_nikud
    #             "‬‫אֶחָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "1 одна",
    #             # pronunciation_word
    #             "aχat",
    #             # hebrew_word_nikud
    #             "‬‫אַחַת‬"
    #         ),
    #         (
    #             # translation_word
    #             "2 два",
    #             # pronunciation_word
    #             "'ʃtayim",
    #             # hebrew_word_nikud
    #             "‬‫שתַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "3 три",
    #             # pronunciation_word
    #             "ʃaloʃ",
    #             # hebrew_word_nikud
    #             "‬‫שָלוֹש‬"
    #         ),
    #         (
    #             # translation_word
    #             "4 четыре",
    #             # pronunciation_word
    #             "arba",
    #             # hebrew_word_nikud
    #             "‬‫אַרבַּע‬"
    #         ),
    #         (
    #             # translation_word
    #             "5 пять",
    #             # pronunciation_word
    #             "χameʃ",
    #             # hebrew_word_nikud
    #             "‬‫חָמֵש‬"
    #         ),
    #         (
    #             # translation_word
    #             "6 шесть",
    #             # pronunciation_word
    #             "ʃeʃ",
    #             # hebrew_word_nikud
    #             "‬‫שֵש‬"
    #         ),
    #         (
    #             # translation_word
    #             "7 семь",
    #             # pronunciation_word
    #             "'ʃeva",
    #             # hebrew_word_nikud
    #             "‫שֶבַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "8 восемь",
    #             # pronunciation_word
    #             "'ʃmone",
    #             # hebrew_word_nikud
    #             "‬‫שמוֹנֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "9 девять",
    #             # pronunciation_word
    #             "'teʃa",
    #             # hebrew_word_nikud
    #             "‬‫תֵשַע‬"
    #         ),
    #         (
    #             # translation_word
    #             "10 десять",
    #             # pronunciation_word
    #             "'eser",
    #             # hebrew_word_nikud
    #             "‫עֶשֶׂר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "11 одиннадцать",
    #             # pronunciation_word
    #             "aχat esre",
    #             # hebrew_word_nikud
    #             "‬‫אַחַת־עֶשׂרֵה‬"
    #         ),
    #         (
    #             # translation_word
    #             "12 двенадцать",
    #             # pronunciation_word
    #             "ʃteim esre",
    #             # hebrew_word_nikud
    #             "‫שתֵים־עֶשֹרֵה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "13 тринадцать",
    #             # pronunciation_word
    #             "ʃloʃ esre",
    #             # hebrew_word_nikud
    #             "‫שלוֹש־עֶשֹרֵה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "14 четырнадцать",
    #             # pronunciation_word
    #             "arba esre",
    #             # hebrew_word_nikud
    #             "‬‫אַרְבַּע־עֶשֹרֵה‬"
    #         ),
    #         (
    #             # translation_word
    #             "15 пятнадцать",
    #             # pronunciation_word
    #             "χameʃ esre",
    #             # hebrew_word_nikud
    #             "‬‫חֲמֵש־עֶשֹרֵה‬"
    #         ),
    #         (
    #             # translation_word
    #             "16 шестнадцать",
    #             # pronunciation_word
    #             "ʃeʃ esre",
    #             # hebrew_word_nikud
    #             "‫שֵש־עֶשֹרֵה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "17 семнадцать",
    #             # pronunciation_word
    #             "ʃva esre",
    #             # hebrew_word_nikud
    #             "‬‫שבַע־עֶשֹרֵה‬"
    #         ),
    #         (
    #             # translation_word
    #             "18 восемнадцать",
    #             # pronunciation_word
    #             "ʃmone esre",
    #             # hebrew_word_nikud
    #             "‫שמוֹנֶה־עֶשֹרֵה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "19 девятнадцать",
    #             # pronunciation_word
    #             "tʃa esre",
    #             # hebrew_word_nikud
    #             "‬‫תשַע־עֶשֹרֵה‬"
    #         ),
    #         (
    #             # translation_word
    #             "20 двадцать",
    #             # pronunciation_word
    #             "esrim",
    #             # hebrew_word_nikud
    #             "‬‫עֶשׂרִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "21 двадцать один",
    #             # pronunciation_word
    #             "esrim veʾeχad",
    #             # hebrew_word_nikud
    #             "‬עֶשׂרִים‬ ‫וְאֶחָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "22 двадцать два",
    #             # pronunciation_word
    #             "esrim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "עֶשׂרִים‬ ‫וּשנַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "23 двадцать три",
    #             # pronunciation_word
    #             "esrim uʃloʃa",
    #             # hebrew_word_nikud
    #             "עֶשׂרִים‬ ‫וּשלוֹשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "30 тридцать",
    #             # pronunciation_word
    #             "ʃloʃim",
    #             # hebrew_word_nikud
    #             "‫שלוֹשִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "31 тридцать один",
    #             # pronunciation_word
    #             "ʃloʃim veʾeχad",
    #             # hebrew_word_nikud
    #             "‬שלוֹשִים‬ ‫וְאֶחָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "32 тридцать два",
    #             # pronunciation_word
    #             "ʃloʃim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "שלוֹשִים‬ ‫וּשנַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "33 тридцать три",
    #             # pronunciation_word
    #             "ʃloʃim uʃloʃa",
    #             # hebrew_word_nikud
    #             "שלוֹשִים‬ ‫וּשלוֹשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "40 сорок",
    #             # pronunciation_word
    #             "arbaʿim",
    #             # hebrew_word_nikud
    #             "‬‫אַרבָּעִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "41 сорок один",
    #             # pronunciation_word
    #             "arbaʿim veʾeχad",
    #             # hebrew_word_nikud
    #             "אַרבָּעִים‬ ‫וְאֶחָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "42 сорок два",
    #             # pronunciation_word
    #             "arbaʿim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "אַרבָּעִים‬ ‫וּשנַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "43 сорок три",
    #             # pronunciation_word
    #             "arbaʿim uʃloʃa",
    #             # hebrew_word_nikud
    #             "אַרבָּעִים‬ ‫וּשלוֹשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "50 пятьдесят",
    #             # pronunciation_word
    #             "χamiʃim",
    #             # hebrew_word_nikud
    #             "‫חֲמִישִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "51 пятьдесят один",
    #             # pronunciation_word
    #             "χamiʃim veʾeχad",
    #             # hebrew_word_nikud
    #             "חֲמִישִים‬ ‫וְאֶחָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "52 пятьдесят два",
    #             # pronunciation_word
    #             "χamiʃim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "‬חֲמִישִים‬ ‫וּשנַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "53 пятьдесят три",
    #             # pronunciation_word
    #             "χamiʃim uʃloʃa",
    #             # hebrew_word_nikud
    #             "‬חֲמִישִים‬ ‫וּשלוֹשָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "60 шестьдесят",
    #             # pronunciation_word
    #             "ʃiʃim",
    #             # hebrew_word_nikud
    #             "‫שִישִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "61 шестьдесят один",
    #             # pronunciation_word
    #             "ʃiʃim veʾeχad",
    #             # hebrew_word_nikud
    #             "שִישִים‬ ‫וְאֶחָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "62 шестьдесят два",
    #             # pronunciation_word
    #             "ʃiʃim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "‬שִישִים‬ ‫וּשנַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "63 шестьдесят три",
    #             # pronunciation_word
    #             "ʃiʃim uʃloʃa",
    #             # hebrew_word_nikud
    #             "‬שִישִים‬ ‫וּשלוֹשָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "70 семьдесят",
    #             # pronunciation_word
    #             "ʃivʿim",
    #             # hebrew_word_nikud
    #             "‬‫שִבעִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "71 семьдесят один",
    #             # pronunciation_word
    #             "ʃivʿim veʾeχad",
    #             # hebrew_word_nikud
    #             "שִבעִים‬ ‫וְאֶחָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "72 семьдесят два",
    #             # pronunciation_word
    #             "ʃivʿim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "שִבעִים‬ ‫וּשנַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "73 семьдесят три",
    #             # pronunciation_word
    #             "ʃivʿim uʃloʃa",
    #             # hebrew_word_nikud
    #             "שִבעִים‬ ‫וּשלוֹשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "80 восемьдесят",
    #             # pronunciation_word
    #             "ʃmonim",
    #             # hebrew_word_nikud
    #             "‬‫שמוֹנִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "81 восемьдесят один",
    #             # pronunciation_word
    #             "ʃmonim veʾeχad",
    #             # hebrew_word_nikud
    #             "‬שמוֹנִים‬ ‫וְאֶחָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "82 восемьдесят два",
    #             # pronunciation_word
    #             "ʃmonim u'ʃnayim",
    #             # hebrew_word_nikud
    #             "‬שמוֹנִים‬ ‫וּשנַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "83 восемьдесят три",
    #             # pronunciation_word
    #             "ʃmonim uʃloʃa",
    #             # hebrew_word_nikud
    #             "‬שמוֹנִים‬ ‫וּשלוֹשָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "90 девяносто",
    #             # pronunciation_word
    #             "tiʃʿim",
    #             # hebrew_word_nikud
    #             "‫תִשעִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "91 девяносто один",
    #             # pronunciation_word
    #             "tiʃʿim veʾeχad",
    #             # hebrew_word_nikud
    #             "‬תִשעִים‬ ‫וְאֶחָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "92 девяносто два",
    #             # pronunciation_word
    #             "tiʃʿim u'ʃayim",
    #             # hebrew_word_nikud
    #             "תִשעִים‬ ‫וּשנַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "93 девяносто три",
    #             # pronunciation_word
    #             "tiʃʿim uʃloʃa",
    #             # hebrew_word_nikud
    #             "‬תִשעִים‬ ‫וּשלוֹשָה‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "5. Числа от 100",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "100 сто",
    #             # pronunciation_word
    #             "'meʾa",
    #             # hebrew_word_nikud
    #             "‬‫מֵאָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "200 двести",
    #             # pronunciation_word
    #             "ma'tayim",
    #             # hebrew_word_nikud
    #             "‫מָאתַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "300 триста",
    #             # pronunciation_word
    #             "ʃloʃ meʾot",
    #             # hebrew_word_nikud
    #             "‬שלוֹש‬ ‫מֵאוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "400 четыреста",
    #             # pronunciation_word
    #             "arba meʾot",
    #             # hebrew_word_nikud
    #             "אַרבַּע‬ ‫מֵאוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "500 пятьсот",
    #             # pronunciation_word
    #             "χameʃ meʾot",
    #             # hebrew_word_nikud
    #             "חָמֵש‬ ‫מֵאוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "600 шестьсот",
    #             # pronunciation_word
    #             "ʃeʃ meʾot",
    #             # hebrew_word_nikud
    #             "‬שֵש‬ ‫מֵאוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "700 семьсот",
    #             # pronunciation_word
    #             "ʃva meʾot",
    #             # hebrew_word_nikud
    #             "‬שבַע‬ ‫מֵאוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "800 восемьсот",
    #             # pronunciation_word
    #             "ʃmone meʾot",
    #             # hebrew_word_nikud
    #             "‬שמוֹנֶה‬ ‫מֵאוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "900 девятьсот",
    #             # pronunciation_word
    #             "tʃa meʾot",
    #             # hebrew_word_nikud
    #             "תשַע‬ ‫מֵאוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "1000 тысяча",
    #             # pronunciation_word
    #             "'elef",
    #             # hebrew_word_nikud
    #             "‬‫אֶלֶף‬"
    #         ),
    #         (
    #             # translation_word
    #             "2000 две тысячи",
    #             # pronunciation_word
    #             "al'payim",
    #             # hebrew_word_nikud
    #             "‫אַלפַּיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "3000 три тысячи",
    #             # pronunciation_word
    #             "'ʃloʃet alafim",
    #             # hebrew_word_nikud
    #             "‬שלוֹשֶת‬ ‫אֲלָפִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "10000 десять тысяч",
    #             # pronunciation_word
    #             "a'seret alafim",
    #             # hebrew_word_nikud
    #             "עֲשֶׂרֶת‬ ‫אֲלָפִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "100000 сто тысяч",
    #             # pronunciation_word
    #             "'meʾa 'elef",
    #             # hebrew_word_nikud
    #             "‬מֵאָה‬ ‫אֶלֶף‬"
    #         ),
    #         (
    #             # translation_word
    #             "миллион",
    #             # pronunciation_word
    #             "milyon",
    #             # hebrew_word_nikud
    #             "‫מִיליוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "миллиард",
    #             # pronunciation_word
    #             "milyard",
    #             # hebrew_word_nikud
    #             "‬‫מִיליַארד‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "6. Числа. Порядковые числительные",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "первый",
    #             # pronunciation_word
    #             "riʃon",
    #             # hebrew_word_nikud
    #             "‫רִאשוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "второй",
    #             # pronunciation_word
    #             "ʃeni",
    #             # hebrew_word_nikud
    #             "‫שֵנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "третий",
    #             # pronunciation_word
    #             "ʃliʃi",
    #             # hebrew_word_nikud
    #             "‬‫שלִישִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "четвёртый",
    #             # pronunciation_word
    #             "reviʿi",
    #             # hebrew_word_nikud
    #             "‬‫רְבִיעִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "пятый",
    #             # pronunciation_word
    #             "χamiʃi",
    #             # hebrew_word_nikud
    #             "‫חֲמִישִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шестой",
    #             # pronunciation_word
    #             "ʃiʃi",
    #             # hebrew_word_nikud
    #             "‬‫שִישִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "седьмой",
    #             # pronunciation_word
    #             "ʃviʿi",
    #             # hebrew_word_nikud
    #             "‬‫שבִיעִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "восьмой",
    #             # pronunciation_word
    #             "ʃmini",
    #             # hebrew_word_nikud
    #             "‬‫שמִינִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "девятый",
    #             # pronunciation_word
    #             "tʃiʿi",
    #             # hebrew_word_nikud
    #             "‬‫תשִיעִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "десятый",
    #             # pronunciation_word
    #             "asiri",
    #             # hebrew_word_nikud
    #             "‫עֲשִׂירִי‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "7. Числа. Дроби",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "дробь",
    #             # pronunciation_word
    #             "'ʃever",
    #             # hebrew_word_nikud
    #             "‫שֶבֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "одна вторая",
    #             # pronunciation_word
    #             "χeʦi",
    #             # hebrew_word_nikud
    #             "‬‫חֵצִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "одна третья",
    #             # pronunciation_word
    #             "ʃliʃ",
    #             # hebrew_word_nikud
    #             "‬‫שלִיש‬"
    #         ),
    #         (
    #             # translation_word
    #             "одна четвёртая",
    #             # pronunciation_word
    #             "'reva",
    #             # hebrew_word_nikud
    #             "‫רֶבַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "одна восьмая",
    #             # pronunciation_word
    #             "ʃminit",
    #             # hebrew_word_nikud
    #             "‫שמִינִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "одна десятая",
    #             # pronunciation_word
    #             "asirit",
    #             # hebrew_word_nikud
    #             "‫עֲשִׂירִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "две третьих",
    #             # pronunciation_word
    #             "ʃnei ʃliʃim",
    #             # hebrew_word_nikud
    #             "‬שנֵי‬ ‫שלִישִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "три четвёртых",
    #             # pronunciation_word
    #             "'ʃloʃet rivʿei",
    #             # hebrew_word_nikud
    #             "שלוֹשֶת‬ ‫רִבעֵי‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "8. Числа. Математические действия",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "вычитание",
    #             # pronunciation_word
    #             "χisur",
    #             # hebrew_word_nikud
    #             "‬‫חִיסוּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "вычитать",
    #             # pronunciation_word
    #             "leχaser",
    #             # hebrew_word_nikud
    #             "‬‫לְחַסֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "деление",
    #             # pronunciation_word
    #             "χiluk",
    #             # hebrew_word_nikud
    #             "‫חִילוּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "делить",
    #             # pronunciation_word
    #             "leχalek",
    #             # hebrew_word_nikud
    #             "‬‫לְחַלֵק‬"
    #         ),
    #         (
    #             # translation_word
    #             "сложение",
    #             # pronunciation_word
    #             "χibur",
    #             # hebrew_word_nikud
    #             "‬‫חִיבּוּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "сложить (матем.)",
    #             # pronunciation_word
    #             "leχaber",
    #             # hebrew_word_nikud
    #             "‫לְחַבֵּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прибавлять",
    #             # pronunciation_word
    #             "leχaber",
    #             # hebrew_word_nikud
    #             "‫לְחַבֵּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "умножение",
    #             # pronunciation_word
    #             "kefel",
    #             # hebrew_word_nikud
    #             "‫כֶּפֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "умножать",
    #             # pronunciation_word
    #             "lehaχpil",
    #             # hebrew_word_nikud
    #             "‬‫לְהַכפִּיל‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "9. Числа. Разное",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "цифра",
    #             # pronunciation_word
    #             "sifra",
    #             # hebrew_word_nikud
    #             "‫סִפרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "число",
    #             # pronunciation_word
    #             "mispar",
    #             # hebrew_word_nikud
    #             "‫מִספָּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "числительное",
    #             # pronunciation_word
    #             "ʃem mispar",
    #             # hebrew_word_nikud
    #             "שֵם‬ ‫מִספָּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "минус",
    #             # pronunciation_word
    #             "'minus",
    #             # hebrew_word_nikud
    #             "‬‫מִינוּס‬"
    #         ),
    #         (
    #             # translation_word
    #             "плюс",
    #             # pronunciation_word
    #             "plus",
    #             # hebrew_word_nikud
    #             "‬‫פּלוּס‬"
    #         ),
    #         (
    #             # translation_word
    #             "формула",
    #             # pronunciation_word
    #             "nusχa",
    #             # hebrew_word_nikud
    #             "‫נוּסחָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вычисление",
    #             # pronunciation_word
    #             "χiʃuv",
    #             # hebrew_word_nikud
    #             "‬‫חִישוּב‬"
    #         ),
    #         (
    #             # translation_word
    #             "считать",
    #             # pronunciation_word
    #             "lispor",
    #             # hebrew_word_nikud
    #             "‫לִספּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подсчитывать",
    #             # pronunciation_word
    #             "leχaʃev",
    #             # hebrew_word_nikud
    #             "‬‫לְחַשֵב‬"
    #         ),
    #         (
    #             # translation_word
    #             "сравнивать",
    #             # pronunciation_word
    #             "lehaʃvot",
    #             # hebrew_word_nikud
    #             "‬‫לְהַשווֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "Сколько?",
    #             # pronunciation_word
    #             "kama?",
    #             # hebrew_word_nikud
    #             "‬?‫כַּמָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "сумма",
    #             # pronunciation_word
    #             "sχum",
    #             # hebrew_word_nikud
    #             "‬‫סכוּם‬"
    #         ),
    #         (
    #             # translation_word
    #             "результат",
    #             # pronunciation_word
    #             "toʦaʾa",
    #             # hebrew_word_nikud
    #             "‬‫תוֹצָאָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "остаток",
    #             # pronunciation_word
    #             "ʃeʾerit",
    #             # hebrew_word_nikud
    #             "‫שְאֵרִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "несколько",
    #             # pronunciation_word
    #             "'kama",
    #             # hebrew_word_nikud
    #             "‫כַּמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мало (неисч.)",
    #             # pronunciation_word
    #             "kʦat",
    #             # hebrew_word_nikud
    #             "‫קצָת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "немного",
    #             # pronunciation_word
    #             "meʿat",
    #             # hebrew_word_nikud
    #             "‫מְעַט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "остальное",
    #             # pronunciation_word
    #             "ʃeʾar",
    #             # hebrew_word_nikud
    #             "‫שְאָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полтора",
    #             # pronunciation_word
    #             "eχad va'χeʦi",
    #             # hebrew_word_nikud
    #             "‬אֶחָד‬ ‫וָחֵצִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "дюжина",
    #             # pronunciation_word
    #             "tresar",
    #             # hebrew_word_nikud
    #             "‫תרֵיסָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пополам (на 2 части)",
    #             # pronunciation_word
    #             "'χeʦi 'χeʦi",
    #             # hebrew_word_nikud
    #             "‬‫חֵצִי‬ ‫חֵצִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "поровну",
    #             # pronunciation_word
    #             "ʃave beʃave",
    #             # hebrew_word_nikud
    #             "‬שָווֶה‬ ‫בְּשָווֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "половина",
    #             # pronunciation_word
    #             "'χeʦi",
    #             # hebrew_word_nikud
    #             "‫חֵצִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "раз",
    #             # pronunciation_word
    #             "paʿam",
    #             # hebrew_word_nikud
    #             "‫פַּעַם‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "10. Самые важные глаголы - 1",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "бежать",
    #             # pronunciation_word
    #             "laruʦ",
    #             # hebrew_word_nikud
    #             "‫לָרוּץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бояться",
    #             # pronunciation_word
    #             "lefaχed",
    #             # hebrew_word_nikud
    #             "‫לְפַחֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "брать",
    #             # pronunciation_word
    #             "la'kaχat",
    #             # hebrew_word_nikud
    #             "‫לָקַחַת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "быть",
    #             # pronunciation_word
    #             "lihyot",
    #             # hebrew_word_nikud
    #             "‫לִהיוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "видеть",
    #             # pronunciation_word
    #             "lirʾot",
    #             # hebrew_word_nikud
    #             "‬‫לִראוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "владеть",
    #             # pronunciation_word
    #             "lihyot 'baʿal ʃel",
    #             # hebrew_word_nikud
    #             "‬לִהיוֹת‬ ‫בַּעַל‬ ‫שֶל‬"
    #         ),
    #         (
    #             # translation_word
    #             "возражать",
    #             # pronunciation_word
    #             "lehitnaged",
    #             # hebrew_word_nikud
    #             "‫לְהִתנַגֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "входить (в комнату и т.п.)",
    #             # pronunciation_word
    #             "lehikanes",
    #             # hebrew_word_nikud
    #             "‬‫לְהִיכָּנֵס‬"
    #         ),
    #         (
    #             # translation_word
    #             "выбирать",
    #             # pronunciation_word
    #             "livχor",
    #             # hebrew_word_nikud
    #             "‬‫לִבחוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "выходить (из дома)",
    #             # pronunciation_word
    #             "laʦet",
    #             # hebrew_word_nikud
    #             "‫לָצֵאת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "говорить (разговаривать)",
    #             # pronunciation_word
    #             "ledaber",
    #             # hebrew_word_nikud
    #             "‬‫לְדַבֵּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "готовить (обед)",
    #             # pronunciation_word
    #             "levaʃel",
    #             # hebrew_word_nikud
    #             "‫לְבַשֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "давать",
    #             # pronunciation_word
    #             "latet",
    #             # hebrew_word_nikud
    #             "‬‫לָתֵת‬"
    #         ),
    #         (
    #             # translation_word
    #             "делать",
    #             # pronunciation_word
    #             "laʿasot",
    #             # hebrew_word_nikud
    #             "‬‫לַעֲשׂוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "доверять",
    #             # pronunciation_word
    #             "liv'toaχ",
    #             # hebrew_word_nikud
    #             "‫לִבטוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "думать",
    #             # pronunciation_word
    #             "laχʃov",
    #             # hebrew_word_nikud
    #             "‫לַחשוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жаловаться",
    #             # pronunciation_word
    #             "lehitlonen",
    #             # hebrew_word_nikud
    #             "‫לְהִתלוֹנֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ждать",
    #             # pronunciation_word
    #             "lehamtin",
    #             # hebrew_word_nikud
    #             "‫לְהַמתִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "забывать",
    #             # pronunciation_word
    #             "liʃ'koaχ",
    #             # hebrew_word_nikud
    #             "‫לִשכּוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "завтракать",
    #             # pronunciation_word
    #             "leʾeχol aruχat 'boker",
    #             # hebrew_word_nikud
    #             "‬לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‫בּוֹקֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "заказывать",
    #             # pronunciation_word
    #             "lehazmin",
    #             # hebrew_word_nikud
    #             "‬‫לְהַזמִין‬"
    #         ),
    #         (
    #             # translation_word
    #             "заканчивать",
    #             # pronunciation_word
    #             "lesayem",
    #             # hebrew_word_nikud
    #             "‬‫לְסַייֵם‬"
    #         ),
    #         (
    #             # translation_word
    #             "замечать (увидеть)",
    #             # pronunciation_word
    #             "lasim lev",
    #             # hebrew_word_nikud
    #             "לָשִׂים‬ ‫לֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "записывать",
    #             # pronunciation_word
    #             "lirʃom",
    #             # hebrew_word_nikud
    #             "‫לִרשוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "защищать (страну)",
    #             # pronunciation_word
    #             "lehagen",
    #             # hebrew_word_nikud
    #             "‬‫לְהָגֵן‬"
    #         ),
    #         (
    #             # translation_word
    #             "звать (на помощь и т.п.)",
    #             # pronunciation_word
    #             "likro",
    #             # hebrew_word_nikud
    #             "‫לִקרוֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "знать (кого-л.)",
    #             # pronunciation_word
    #             "lehakir et",
    #             # hebrew_word_nikud
    #             "לְהַכִּיר‬ ‫אֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "знать (что-л.)",
    #             # pronunciation_word
    #             "la'daʿat",
    #             # hebrew_word_nikud
    #             "‬‫לָדַעַת‬"
    #         ),
    #         (
    #             # translation_word
    #             "играть",
    #             # pronunciation_word
    #             "lesaχek",
    #             # hebrew_word_nikud
    #             "‫לְשַׂחֵק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "идти",
    #             # pronunciation_word
    #             "la'leχet",
    #             # hebrew_word_nikud
    #             "‬‫לָלֶכֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "извинять",
    #             # pronunciation_word
    #             "lis'loaχ",
    #             # hebrew_word_nikud
    #             "‬‫לִסלוֹח‬"
    #         ),
    #         (
    #             # translation_word
    #             "извиняться",
    #             # pronunciation_word
    #             "lehitnaʦel",
    #             # hebrew_word_nikud
    #             "‫לְהִתנַצֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "изменить (поменять)",
    #             # pronunciation_word
    #             "leʃanot",
    #             # hebrew_word_nikud
    #             "‫לְשַנוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "изучать",
    #             # pronunciation_word
    #             "lilmod",
    #             # hebrew_word_nikud
    #             "‫לִלמוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "иметь",
    #             # pronunciation_word
    #             "lehaχzik",
    #             # hebrew_word_nikud
    #             "‬‫לְהַחזִיק‬"
    #         ),
    #         (
    #             # translation_word
    #             "интересоваться",
    #             # pronunciation_word
    #             "lehitʿanyen be…",
    #             # hebrew_word_nikud
    #             "‬לְהִתעַנייֵן‬ ‫ב‬"
    #         ),
    #         (
    #             # translation_word
    #             "информировать",
    #             # pronunciation_word
    #             "leho'dia",
    #             # hebrew_word_nikud
    #             "‫לְהוֹדִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "искать …",
    #             # pronunciation_word
    #             "leχapes",
    #             # hebrew_word_nikud
    #             "‫לְחַפֵּש‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #         (
    #             # translation_word
    #             "",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "‬"
    #         ),
    #     ]
    # ),
# INESSA PUTS HER GROUPS HERE (FROM GROUP 125):
    (
        # group_name_ru
        "",
        # words
        [
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "цифра",
                # pronunciation_word
                "sifra",
                # hebrew_word_nikud
                "‫סִפרָה‬‬"
            ),
            (
                # translation_word
                "",
                # pronunciation_word
                "",
                # hebrew_word_nikud
                "‬"
            ),
        ]
    ),
]



result = ""
for group_with_words in groups_and_words_to_parce:
    group_name_ru = group_with_words[0]
    words_list = group_with_words[1]

    result += form_group_creation_record(group_name_ru)

    words_result, NUMBER_TO_START_COUNTING_WORDS =  form_word_creation_record(
        words_list,
        NUMBER_TO_START_COUNTING_WORDS,
        NUMBER_TO_START_COUNTING_GROUPS
    )
    result += words_result
    NUMBER_TO_START_COUNTING_GROUPS += 1

print(result)


# CONTENT:
# Местоимения
# Приветствия. Прощания. Извинения. Благодарность
# Обращения
# Числа от 1 до 100
# Числа от 100
# Числа. Порядковые числительные
# Числа. Дроби
# Числа. Математические действия
# Числа. Разное
# Самые важные глаголы - 1
# Самые важные глаголы - 2
# Самые важные глаголы - 3
# Самые важные глаголы - 4
# Цвета
# Вопросы
# Основные предлоги
# Вводные и служебные слова. Наречия - 1
# Вводные и служебные слова. Наречия - 2
# Противоположности
# Дни недели
# Часы. Время суток
# Месяцы. Времена года
# Время. Разное
# Линии и формы
# Меры измерения
# Ёмкости
# Материалы
# Металлы
# Человек. Общие понятия
# Анатомия
# Голова
# Тело
# Верхняя одежда
# Одежда
# Одежда. Бельё
# Головной убор
# Обувь
# Ткани. Материалы
# Аксессуары
# Одежда. Разное
# Предметы личной гигиены. Косметика
# Украшения. Драгоценности
# Часы
# Продукты
# Напитки
# Овощи
# Фрукты. Орехи
# Сладости. Хлеб
# Блюда
# Приправы. Специи
# Приём пищи
# Сервировка стола
# Ресторан
# Анкета. Анкетные данные
# Семья. Родственники
# Друзья. Знакомые. Коллеги
# Женщина. Мужчина
# Возраст
# Ребёнок
# Супруги. Супружеская жизнь
# Чувства. Состояние человека
# Черты характера. Личность
# Сон. Состояние сна
# Юмор. Смех. Радость
# Общение. Диалог. Разговор - 1
# Общение. Диалог. Разговор - 2
# Общение. Диалог. Разговор - 3
# Согласие. Несогласие. Одобрение
# Успех. Удача. Поражение
# Обиды. Ссора. Негативные эмоции
# Болезни
# Симптомы болезней. Лечение - 1
# Симптомы болезней. Лечение - 2
# Симптомы болезней. Лечение - 3
# Врачи
# Лекарства. Принадлежности
# Курение. Табачные изделия
# Город. Жизнь в городе
# Городские учреждения
# Вывески. Указатели
# Городской транспорт
# Достопримечательности
# Покупки
# Деньги
# Почта
# Дом. Жилище
# Дом. Подъезд. Лифт
# Дом. Электричество
# Дом. Дверь. Замок
# Загородный дом. Дом в деревне
# Особняк. Вилла
# Замок. Дворец
# Квартира
# Квартира. Уборка
# Мебель. Интерьер
# Постельные принадлежности
# Кухня
# Ванная комната
# Бытовая техника
# Ремонт
# Водопровод
# Пожар
# Офис. Работа в офисе
# Работа. Бизнес-процессы - 1
# Работа. Бизнес-процессы - 2
# Производство
# Контракт
# Импорт-Экспорт
# Финансы
# Маркетинг
# Реклама
# Банк
# Телефон. Общение по телефону
# Телефон. Мобильный телефон
# Канцелярские принадлежности
# Документы. Названия документов
# Отрасли и виды бизнеса
# Выставка
# Средства массовой информации
# Сельское хозяйство
# Стройка. Строительные работы
# Наука. Исследования. Учёные
# Поиск работы. Увольнение
# Люди в среде бизнеса
# Профессии в сфере услуг
# Военные профессии. Звания
# Государственные и религиозные служащие
# Профессии в сельском хозяйстве
# Профессии в области искусства
# Профессии различные
# Занятия. Социальное положение
# Виды спорта. Спортсмены
# Виды спорта. Разное
# Спортивный зал
# Хоккей
# Футбол
# Горные лыжи
# Теннис. Гольф
# Шахматы
# Бокс
# Спорт. Разное
# Школа
# Высшее учебное заведение
# Названия наук и дисциплин
# Письмо. Части речи. Орфография
# Изучение иностранных языков
# Сказочные персонажи
# Знаки зодиака
# Театр
# Кино
# Изобразительное искусство
# Литература. Поэзия
# Цирк
# Музыка. Эстрада
# Турпоездка
# Гостиница
# Книга. Чтение
# Охота. Рыбалка
# Игры. Бильярд
# Игры. Карты
# Казино
# Отдых. Игры. Разное
# Фотография
# Пляж
# Компьютер
# Интернет. E-mail
# Электричество
# Инструменты
# Самолёт
# Поезд
# Корабль
# Аэропорт
# Велосипед. Мотоцикл
# Автомобиль. Виды
# Автомобиль. Кузов
# Автомобиль. Салон
# Автомобиль. Двигатель
# Автомобиль. Авария. Ремонт
# Автомобиль. Дорога
# Знаки дорожные
# Праздник. Событие
# Похороны
# Война. Люди
# Война. Военные действия - 1
# Война. Военные действия - 2
# Оружие
# Первобытные люди
# Средние века
# Правитель. Шеф. Руководитель
# Дорога. Путь
# Нарушения закона. Преступники - 1
# Нарушения закона. Преступники - 2
# Полиция. Закон - 1
# Полиция. Закон - 2
# Космос
# Планета Земля
# Части света
# Море. Океан
# Названия морей и океанов
# Горы
# Названия гор
# Река
# Названия рек
# Лес
# Природные ресурсы
# Погода
# Стихия
# Шумы. Звуки
# Зима
# Млекопитающие. Хищники
# Дикие животные
# Домашние животные
# Собака. Породы
# Звуки, издаваемые животными
# Детёныши животных и птиц
# Птицы
# Птицы. Пение. Звуки
# Рыбы. Морские животные
# Земноводные. Пресмыкающиеся
# Насекомые. Беспозвоночные
# Животные. Части тела
# Животные. Действия
# Животные. Среда обитания
# Уход за животными
# Животные. Разное
# Лошадь
# Деревья
# Кустарники
# Грибы
# Фрукты. Ягоды
# Цветы. Растения
# Зерновые
# Овощи. Зелень
# Западная Европа
# Центральная и Восточная Европа
# Страны СНГ
# Азия
# Северная Америка
# Центральная и Южная Америка
# Африка
# Австралия и Океания
# Города
# Политика. Правительство - 1
# Политика. Правительство - 2
# Страны. Разное
# Мировые религии. Конфессии
# Религии. Люди
# Вера. Христианство. Ислам
# Термины общего характера
# Определения А-Н
# Определения О-Я
# Глаголы А-Е
# Глаголы Ж-М
# Глаголы Н-О
# Глаголы П-Р
# Глаголы С-Ш