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
    # (
    #     # group_name_ru
    #     "125. Профессии в сфере услуг",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "повар",
    #             # pronunciation_word
    #             "tabaχ",
    #             # hebrew_word_nikud
    #             "‬‫טַבָּח‬"
    #         ),
    #         (
    #             # translation_word
    #             "шеф-повар",
    #             # pronunciation_word
    #             "ʃef",
    #             # hebrew_word_nikud
    #             "‬‫שֶף‬"
    #         ),
    #         (
    #             # translation_word
    #             "пекарь",
    #             # pronunciation_word
    #             "ofe",
    #             # hebrew_word_nikud
    #             "‬‫אוֹפֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "бармен",
    #             # pronunciation_word
    #             "'barmen",
    #             # hebrew_word_nikud
    #             "‫בַּרמֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "официант",
    #             # pronunciation_word
    #             "melʦar",
    #             # hebrew_word_nikud
    #             "‬‫מֶלצָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "официантка",
    #             # pronunciation_word
    #             "melʦarit",
    #             # hebrew_word_nikud
    #             "‫מֶלצָרִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "адвокат, юрист",
    #             # pronunciation_word
    #             "oreχ din",
    #             # hebrew_word_nikud
    #             "עוֹרֵך‬‬ ‫דִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нотариус",
    #             # pronunciation_word
    #             "notaryon",
    #             # hebrew_word_nikud
    #             "‫נוֹטַריוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "электрик",
    #             # pronunciation_word
    #             "χaʃmalai",
    #             # hebrew_word_nikud
    #             "‬‫חַשמַלאַי‬"
    #         ),
    #         (
    #             # translation_word
    #             "сантехник",
    #             # pronunciation_word
    #             "ʃravrav",
    #             # hebrew_word_nikud
    #             "‫שרַברָב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плотник",
    #             # pronunciation_word
    #             "nagar",
    #             # hebrew_word_nikud
    #             "‫נַגָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "массажист",
    #             # pronunciation_word
    #             "maʿase",
    #             # hebrew_word_nikud
    #             "‬‫מְעַסֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "массажистка",
    #             # pronunciation_word
    #             "masa'ʒistit",
    #             # hebrew_word_nikud
    #             "‫מַסָזִ׳יסטִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "врач",
    #             # pronunciation_word
    #             "rofe",
    #             # hebrew_word_nikud
    #             "‬‫רוֹפֵא‬"
    #         ),
    #         (
    #             # translation_word
    #             "таксист",
    #             # pronunciation_word
    #             "nahag monit",
    #             # hebrew_word_nikud
    #             "נַהַג‬‬‬ ‫מוֹנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шофёр",
    #             # pronunciation_word
    #             "nahag",
    #             # hebrew_word_nikud
    #             "‬‫נַהָג‬"
    #         ),
    #         (
    #             # translation_word
    #             "курьер",
    #             # pronunciation_word
    #             "ʃa'liaχ",
    #             # hebrew_word_nikud
    #             "‫שָלִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "горничная",
    #             # pronunciation_word
    #             "χadranit",
    #             # hebrew_word_nikud
    #             "‫חַדרָנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "охранник",
    #             # pronunciation_word
    #             "ʃomer",
    #             # hebrew_word_nikud
    #             "‫שוֹמֵר‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стюардесса",
    #             # pronunciation_word
    #             "da'yelet",
    #             # hebrew_word_nikud
    #             "‫דַייֶלֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учитель",
    #             # pronunciation_word
    #             "more",
    #             # hebrew_word_nikud
    #             "‫מוֹרֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "библиотекарь",
    #             # pronunciation_word
    #             "safran",
    #             # hebrew_word_nikud
    #             "‫סַפרָן‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переводчик",
    #             # pronunciation_word
    #             "metargem",
    #             # hebrew_word_nikud
    #             "‫מְתַרגֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переводчик",
    #             # pronunciation_word
    #             "meturgeman",
    #             # hebrew_word_nikud
    #             "‫מְתוּרגְמָן‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гид (экскурсовод)",
    #             # pronunciation_word
    #             "madriχ tiyulim",
    #             # hebrew_word_nikud
    #             "מַדרִיך‬ ‫טִיוּלִים‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "парикмахер",
    #             # pronunciation_word
    #             "sapar",
    #             # hebrew_word_nikud
    #             "‫סַפָּר‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "почтальон",
    #             # pronunciation_word
    #             "davar",
    #             # hebrew_word_nikud
    #             "‫דַווָר‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "продавец",
    #             # pronunciation_word
    #             "moχer",
    #             # hebrew_word_nikud
    #             "‫מוֹכֵר‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "садовник",
    #             # pronunciation_word
    #             "ganan",
    #             # hebrew_word_nikud
    #             "‫גַנָן‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слуга",
    #             # pronunciation_word
    #             "meʃaret",
    #             # hebrew_word_nikud
    #             "‫מְשָרֵת‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "служанка",
    #             # pronunciation_word
    #             "meʃa'retet",
    #             # hebrew_word_nikud
    #             "‬‬‫מְשָרֵתֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "уборщица",
    #             # pronunciation_word
    #             "menaka",
    #             # hebrew_word_nikud
    #             "‫מְנַקֶה‬‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "126. Военные профессии. Звания",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "рядовой",
    #             # pronunciation_word
    #             "turai",
    #             # hebrew_word_nikud
    #             "‫טוּרַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сержант",
    #             # pronunciation_word
    #             "samal",
    #             # hebrew_word_nikud
    #             "‫סַמָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лейтенант",
    #             # pronunciation_word
    #             "'segen",
    #             # hebrew_word_nikud
    #             "‫סֶגֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "капитан",
    #             # pronunciation_word
    #             "'seren",
    #             # hebrew_word_nikud
    #             "‫סֶרֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "майор",
    #             # pronunciation_word
    #             "rav 'seren",
    #             # hebrew_word_nikud
    #             "‫רַב־סֶרֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полковник",
    #             # pronunciation_word
    #             "aluf miʃne",
    #             # hebrew_word_nikud
    #             "אַלוּף‬ ‫מִשנֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "генерал",
    #             # pronunciation_word
    #             "aluf",
    #             # hebrew_word_nikud
    #             "‫אַלוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "маршал",
    #             # pronunciation_word
    #             "'marʃal",
    #             # hebrew_word_nikud
    #             "‫מַרשָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "адмирал",
    #             # pronunciation_word
    #             "admiral",
    #             # hebrew_word_nikud
    #             "‫אַדמִירָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "военный",
    #             # pronunciation_word
    #             "iʃ ʦava",
    #             # hebrew_word_nikud
    #             "‫צָבָא‬ ‫אִיש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "солдат",
    #             # pronunciation_word
    #             "χayal",
    #             # hebrew_word_nikud
    #             "‫חַייָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "офицер",
    #             # pronunciation_word
    #             "kaʦin",
    #             # hebrew_word_nikud
    #             "‬‫קָצִין‬"
    #         ),
    #         (
    #             # translation_word
    #             "командир",
    #             # pronunciation_word
    #             "mefaked",
    #             # hebrew_word_nikud
    #             "‫מְפַקֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пограничник",
    #             # pronunciation_word
    #             "ʃomer gvul",
    #             # hebrew_word_nikud
    #             "שוֹמֵר‬ ‫גבוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "радист",
    #             # pronunciation_word
    #             "alχutai",
    #             # hebrew_word_nikud
    #             "‬‫אַלחוּטַאי‬"
    #         ),
    #         (
    #             # translation_word
    #             "разведчик",
    #             # pronunciation_word
    #             "iʃ modiʿin kravi",
    #             # hebrew_word_nikud
    #             "אִיש‬ ‫מוֹדִיעִין‬ ‫קרָבִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сапёр",
    #             # pronunciation_word
    #             "χablan",
    #             # hebrew_word_nikud
    #             "‫חַבּלָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стрелок",
    #             # pronunciation_word
    #             "ʦalaf",
    #             # hebrew_word_nikud
    #             "‫צַלָף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "штурман",
    #             # pronunciation_word
    #             "navat",
    #             # hebrew_word_nikud
    #             "‫נַווָט‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "127. Государственные и религиозные служащие",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "президент",
    #             # pronunciation_word
    #             "nasi",
    #             # hebrew_word_nikud
    #             "‫נָשִׂיא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "министр",
    #             # pronunciation_word
    #             "sar",
    #             # hebrew_word_nikud
    #             "‫שַׂר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "премьер-министр",
    #             # pronunciation_word
    #             "roʃ memʃala",
    #             # hebrew_word_nikud
    #             "רֹאש‬ ‫מֶמשָלָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дипломат",
    #             # pronunciation_word
    #             "diplomat",
    #             # hebrew_word_nikud
    #             "‫דִיפּלוֹמָט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "консул",
    #             # pronunciation_word
    #             "'konsul",
    #             # hebrew_word_nikud
    #             "‫קוֹנסוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чиновник",
    #             # pronunciation_word
    #             "pakid",
    #             # hebrew_word_nikud
    #             "‫פָּקִיד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мэр",
    #             # pronunciation_word
    #             "roʃ haʿir",
    #             # hebrew_word_nikud
    #             "רֹאש‬ ‫הָעִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "судья",
    #             # pronunciation_word
    #             "ʃofet",
    #             # hebrew_word_nikud
    #             "‫שוֹפֵט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прокурор",
    #             # pronunciation_word
    #             "to'veʿa",
    #             # hebrew_word_nikud
    #             "‫תוֹבֵע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "монах",
    #             # pronunciation_word
    #             "nazir",
    #             # hebrew_word_nikud
    #             "‫נָזִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "раввин",
    #             # pronunciation_word
    #             "rav",
    #             # hebrew_word_nikud
    #             "‫רַב‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "128. Профессии в сельском хозяйстве",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "пчеловод",
    #             # pronunciation_word
    #             "kavran",
    #             # hebrew_word_nikud
    #             "‬‫כַּוורָן‬"
    #         ),
    #         (
    #             # translation_word
    #             "ветеринар",
    #             # pronunciation_word
    #             "veterinar",
    #             # hebrew_word_nikud
    #             "‫וֶטֶרִינָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "фермер",
    #             # pronunciation_word
    #             "χavai",
    #             # hebrew_word_nikud
    #             "‫חַווַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "винодел",
    #             # pronunciation_word
    #             "yeinan",
    #             # hebrew_word_nikud
    #             "‫יֵינָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зоолог",
    #             # pronunciation_word
    #             "zoʾolog",
    #             # hebrew_word_nikud
    #             "‬‫זוֹאוֹלוֹג‬"
    #         ),
    #         (
    #             # translation_word
    #             "ковбой",
    #             # pronunciation_word
    #             "'kaʾuboi",
    #             # hebrew_word_nikud
    #             "‫קָאוּבּוֹי‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "129. Профессии в области искусства",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "актёр, артист",
    #             # pronunciation_word
    #             "saχkan",
    #             # hebrew_word_nikud
    #             "‫שַׂחקָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "актриса, артистка",
    #             # pronunciation_word
    #             "saχkanit",
    #             # hebrew_word_nikud
    #             "‫שַׂחקָנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "певец",
    #             # pronunciation_word
    #             "zamar",
    #             # hebrew_word_nikud
    #             "‫זַמָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "певица",
    #             # pronunciation_word
    #             "za'meret",
    #             # hebrew_word_nikud
    #             "‫זַמֶרֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "танцор",
    #             # pronunciation_word
    #             "rakdan",
    #             # hebrew_word_nikud
    #             "‫רַקדָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "танцовщица",
    #             # pronunciation_word
    #             "rakdanit",
    #             # hebrew_word_nikud
    #             "‬‫רַקדָנִית‬"
    #         ),
    #         (
    #             # translation_word
    #             "музыкант",
    #             # pronunciation_word
    #             "muzikai",
    #             # hebrew_word_nikud
    #             "‬‫מוּזִיקַאי‬"
    #         ),
    #         (
    #             # translation_word
    #             "пианист",
    #             # pronunciation_word
    #             "psantran",
    #             # hebrew_word_nikud
    #             "‫פּסַנתרָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гитарист",
    #             # pronunciation_word
    #             "nagan gi'tara",
    #             # hebrew_word_nikud
    #             "נ‫ַגַן‬ ‫גִיטָרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "композитор",
    #             # pronunciation_word
    #             "malχin",
    #             # hebrew_word_nikud
    #             "‫מַלחִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "режиссёр",
    #             # pronunciation_word
    #             "bamai",
    #             # hebrew_word_nikud
    #             "‬‫בַּמַאי‬"
    #         ),
    #         (
    #             # translation_word
    #             "критик",
    #             # pronunciation_word
    #             "mevaker",
    #             # hebrew_word_nikud
    #             "‫מְבַקֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "писатель",
    #             # pronunciation_word
    #             "sofer",
    #             # hebrew_word_nikud
    #             "‫סוֹפֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поэт",
    #             # pronunciation_word
    #             "meʃorer",
    #             # hebrew_word_nikud
    #             "‫מְשוֹרֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скульптор",
    #             # pronunciation_word
    #             "pasal",
    #             # hebrew_word_nikud
    #             "‫פַּסָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "художник",
    #             # pronunciation_word
    #             "ʦayar",
    #             # hebrew_word_nikud
    #             "‫צַייָר‬‬"
    #         ),
    #     ]
    # ),   
    # (
    #     # group_name_ru
    #     "130. Профессии различные",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "врач",
    #             # pronunciation_word
    #             "rofe",
    #             # hebrew_word_nikud
    #             "‫רוֹפֵא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "медсестра",
    #             # pronunciation_word
    #             "aχot",
    #             # hebrew_word_nikud
    #             "‫אָחוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "психиатр",
    #             # pronunciation_word
    #             "psiχi'ʾater",
    #             # hebrew_word_nikud
    #             "‫פּסִיכִיאָטֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стоматолог",
    #             # pronunciation_word
    #             "rofe ʃi'nayim",
    #             # hebrew_word_nikud
    #             "‬רוֹפֵא‬ ‫שִינַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "хирург",
    #             # pronunciation_word
    #             "kirurg",
    #             # hebrew_word_nikud
    #             "‫כִּירוּרג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "астронавт",
    #             # pronunciation_word
    #             "astro'naʾut",
    #             # hebrew_word_nikud
    #             "‫אַסטרוֹנָאוּט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "астроном",
    #             # pronunciation_word
    #             "astronom",
    #             # hebrew_word_nikud
    #             "‫אַסטרוֹנוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лётчик, пилот",
    #             # pronunciation_word
    #             "tayas",
    #             # hebrew_word_nikud
    #             "‫טַייָס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "водитель",
    #             # pronunciation_word
    #             "nahag",
    #             # hebrew_word_nikud
    #             "‬‫נַהָג‬"
    #         ),
    #         (
    #             # translation_word
    #             "машинист",
    #             # pronunciation_word
    #             "nahag ra'kevet",
    #             # hebrew_word_nikud
    #             "נַהַג‬ ‫רַכֶּבֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "механик",
    #             # pronunciation_word
    #             "meχonai",
    #             # hebrew_word_nikud
    #             "‫מְכוֹנַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шахтёр",
    #             # pronunciation_word
    #             "kore",
    #             # hebrew_word_nikud
    #             "‫כּוֹרֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рабочий",
    #             # pronunciation_word
    #             "poʿel",
    #             # hebrew_word_nikud
    #             "‫פּוֹעֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слесарь",
    #             # pronunciation_word
    #             "misgad",
    #             # hebrew_word_nikud
    #             "‫מִסגָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "столяр",
    #             # pronunciation_word
    #             "nagar",
    #             # hebrew_word_nikud
    #             "‫נַגָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "строитель",
    #             # pronunciation_word
    #             "banai",
    #             # hebrew_word_nikud
    #             "‫בַּנַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "профессор",
    #             # pronunciation_word
    #             "pro'fesor",
    #             # hebrew_word_nikud
    #             "‫פּרוֹפֶסוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "архитектор",
    #             # pronunciation_word
    #             "adriχal",
    #             # hebrew_word_nikud
    #             "‫אַדרִיכָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учёный",
    #             # pronunciation_word
    #             "madʿan",
    #             # hebrew_word_nikud
    #             "‬‫מַדעָן‬"
    #         ),
    #         (
    #             # translation_word
    #             "археолог",
    #             # pronunciation_word
    #             "arχeʾolog",
    #             # hebrew_word_nikud
    #             "‫אַרכֵיאוֹלוֹג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "геолог",
    #             # pronunciation_word
    #             "geʾolog",
    #             # hebrew_word_nikud
    #             "‫גֵיאוֹלוֹג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "няня",
    #             # pronunciation_word
    #             "ʃmartaf",
    #             # hebrew_word_nikud
    #             "‫שמַרטַף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дизайнер",
    #             # pronunciation_word
    #             "meʿaʦev",
    #             # hebrew_word_nikud
    #             "‫מְעַצֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "компьютерщик",
    #             # pronunciation_word
    #             "mumχe maχʃevim",
    #             # hebrew_word_nikud
    #             "מוּמחֶה‬ ‫מַחשֵבִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "программист",
    #             # pronunciation_word
    #             "metaχnet",
    #             # hebrew_word_nikud
    #             "‫מְתַכנֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "инженер",
    #             # pronunciation_word
    #             "mehandes",
    #             # hebrew_word_nikud
    #             "‫מְהַנדֵס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "моряк",
    #             # pronunciation_word
    #             "yamai",
    #             # hebrew_word_nikud
    #             "‫יַמַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спасатель",
    #             # pronunciation_word
    #             "maʦil",
    #             # hebrew_word_nikud
    #             "‫מַצִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пожарный",
    #             # pronunciation_word
    #             "kabai",
    #             # hebrew_word_nikud
    #             "‫כַּבַּאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полицейский",
    #             # pronunciation_word
    #             "ʃoter",
    #             # hebrew_word_nikud
    #             "‫שוֹטֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сторож",
    #             # pronunciation_word
    #             "ʃomer",
    #             # hebrew_word_nikud
    #             "‫שוֹמֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "телохранитель",
    #             # pronunciation_word
    #             "ʃomer roʃ",
    #             # hebrew_word_nikud
    #             "שוֹמֵר‬ ‫רֹאש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спортсмен",
    #             # pronunciation_word
    #             "sportai",
    #             # hebrew_word_nikud
    #             "‫ספּוֹרטַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тренер",
    #             # pronunciation_word
    #             "meʾamen",
    #             # hebrew_word_nikud
    #             "‫מְאַמֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сапожник",
    #             # pronunciation_word
    #             "sandlar",
    #             # hebrew_word_nikud
    #             "‫סַנדלָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "модель",
    #             # pronunciation_word
    #             "dugmanit",
    #             # hebrew_word_nikud
    #             "‫דוּגמָנִית‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "131. Занятия. Социальное положение",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "школьник",
    #             # pronunciation_word
    #             "talmid",
    #             # hebrew_word_nikud
    #             "‫תַלמִיד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "студент",
    #             # pronunciation_word
    #             "student",
    #             # hebrew_word_nikud
    #             "‫סטוּדֶנט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "философ",
    #             # pronunciation_word
    #             "filosof",
    #             # hebrew_word_nikud
    #             "‫פִילוֹסוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "экономист",
    #             # pronunciation_word
    #             "kalkelan",
    #             # hebrew_word_nikud
    #             "‫כַּלכְּלָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "изобретатель",
    #             # pronunciation_word
    #             "mamʦi",
    #             # hebrew_word_nikud
    #             "‫מַמצִיא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "безработный",
    #             # pronunciation_word
    #             "muvtal",
    #             # hebrew_word_nikud
    #             "‫מוּבטָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пенсионер",
    #             # pronunciation_word
    #             "pensyoner",
    #             # hebrew_word_nikud
    #             "‫פֶּנסיוֹנֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шпион",
    #             # pronunciation_word
    #             "meragel",
    #             # hebrew_word_nikud
    #             "‫מְרַגֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "заключённый",
    #             # pronunciation_word
    #             "asir",
    #             # hebrew_word_nikud
    #             "‫אָסִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бюрократ",
    #             # pronunciation_word
    #             "birokrat",
    #             # hebrew_word_nikud
    #             "‫בִּירוֹקרָט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "путешественник",
    #             # pronunciation_word
    #             "metayel",
    #             # hebrew_word_nikud
    #             "‬‫מְטַייֵל‬"
    #         ),
    #         (
    #             # translation_word
    #             "гомосексуалист",
    #             # pronunciation_word
    #             "'lesbit, 'homo",
    #             # hebrew_word_nikud
    #             " ‫לֶסבִּית‬,‫הוֹמו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "наркоман",
    #             # pronunciation_word
    #             "narkoman",
    #             # hebrew_word_nikud
    #             "‫נַרקוֹמָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "проститутка",
    #             # pronunciation_word
    #             "zona",
    #             # hebrew_word_nikud
    #             "‫זוֹנָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "132. Виды спорта. Спортсмены",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "спортсмен",
    #             # pronunciation_word
    #             "sportai",
    #             # hebrew_word_nikud
    #             "‫ספּוֹרטַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вид спорта",
    #             # pronunciation_word
    #             "anaf sport",
    #             # hebrew_word_nikud
    #             "עָנַף‬ ‫ספּוֹרט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "баскетбол",
    #             # pronunciation_word
    #             "kadursal",
    #             # hebrew_word_nikud
    #             "‬‫כַּדוּרסַל‬"
    #         ),
    #         (
    #             # translation_word
    #             "футбол",
    #             # pronunciation_word
    #             "kadu'regel",
    #             # hebrew_word_nikud
    #             "‫כַּדוּרֶגֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "волейбол",
    #             # pronunciation_word
    #             "kadurʿaf",
    #             # hebrew_word_nikud
    #             "‫כַּדוּרעָף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "теннис",
    #             # pronunciation_word
    #             "'tenis",
    #             # hebrew_word_nikud
    #             "‫טֶניִס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плавание",
    #             # pronunciation_word
    #             "sχiya",
    #             # hebrew_word_nikud
    #             "‫שׂחִייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бег",
    #             # pronunciation_word
    #             "riʦa",
    #             # hebrew_word_nikud
    #             "‫רִיצָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "велоспорт",
    #             # pronunciation_word
    #             "reχiva al ofa'nayim",
    #             # hebrew_word_nikud
    #             "רְכִיבָה‬ ‫עַל‬ ‫אוֹפַנַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "велосипедист",
    #             # pronunciation_word
    #             "roχev ofa'nayim",
    #             # hebrew_word_nikud
    #             "רוֹכֵב‬ ‫אוֹפַנַיִים‬‬"
    #         ),
            
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "133. Виды спорта. Разное",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "бадминтон",
    #             # pronunciation_word
    #             "noʦit",
    #             # hebrew_word_nikud
    #             "‫נוֹצִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бильярд",
    #             # pronunciation_word
    #             "bilyard",
    #             # hebrew_word_nikud
    #             "‫בִּיליַארד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дайвинг",
    #             # pronunciation_word
    #             "ʦlila",
    #             # hebrew_word_nikud
    #             "‫צלִילָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "134. Спортивный зал",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "штанга",
    #             # pronunciation_word
    #             "miʃ'kolet",
    #             # hebrew_word_nikud
    #             "‫מִשקוֹלֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гантели",
    #             # pronunciation_word
    #             "miʃkolot",
    #             # hebrew_word_nikud
    #             "‫מִשקוֹלוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тренажёр",
    #             # pronunciation_word
    #             "maχʃir 'koʃer",
    #             # hebrew_word_nikud
    #             "מַכשִיר‬ ‫כּוֹשֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "велотренажёр",
    #             # pronunciation_word
    #             "ofanei 'koʃer",
    #             # hebrew_word_nikud
    #             "אוֹפַנֵי‬ ‫כּוֹשֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "беговая дорожка",
    #             # pronunciation_word
    #             "haliχon",
    #             # hebrew_word_nikud
    #             "‫הֲלִיכוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скакалка",
    #             # pronunciation_word
    #             "dalgit",
    #             # hebrew_word_nikud
    #             "‫דַלגִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "аэробика",
    #             # pronunciation_word
    #             "ei'robika",
    #             # hebrew_word_nikud
    #             "‬‫אֵירוֹבִּיקָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "йога",
    #             # pronunciation_word
    #             "yoga",
    #             # hebrew_word_nikud
    #             "‫יוֹגָה‬‬"
    #         ),
    #     ]
    # ),    
    # (
    #     # group_name_ru
    #     "135. Спорт. Разное",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Олимпийские игры",
    #             # pronunciation_word
    #             "hamisχakim haʾo'limpiyim",
    #             # hebrew_word_nikud
    #             "‬הַמִשׂחָקִים‬ ‫הָאוֹלִימפִּייִם‬"
    #         ),
    #         (
    #             # translation_word
    #             "победитель",
    #             # pronunciation_word
    #             "mena'ʦeaχ",
    #             # hebrew_word_nikud
    #             "‫מְנַצֵח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "побеждать",
    #             # pronunciation_word
    #             "lena'ʦeaχ",
    #             # hebrew_word_nikud
    #             "‫לְנַצֵח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лидер",
    #             # pronunciation_word
    #             "manhig",
    #             # hebrew_word_nikud
    #             "‫מַנהִיג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чемпион",
    #             # pronunciation_word
    #             "aluf",
    #             # hebrew_word_nikud
    #             "‫אַלוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чемпионат",
    #             # pronunciation_word
    #             "alifut",
    #             # hebrew_word_nikud
    #             "‫אַלִיפוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стадион",
    #             # pronunciation_word
    #             "iʦtadyon",
    #             # hebrew_word_nikud
    #             "‫אִצטַדיוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "противник",
    #             # pronunciation_word
    #             "yariv",
    #             # hebrew_word_nikud
    #             "‫יָרִיב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "проиграть",
    #             # pronunciation_word
    #             "lehafsid",
    #             # hebrew_word_nikud
    #             "‫לְהַפסִיד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "результат",
    #             # pronunciation_word
    #             "toʦaʾa",
    #             # hebrew_word_nikud
    #             "‫תוֹצָאָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "перерыв",
    #             # pronunciation_word
    #             "hafsaka",
    #             # hebrew_word_nikud
    #             "‫הַפסָקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "упражнение",
    #             # pronunciation_word
    #             "imun",
    #             # hebrew_word_nikud
    #             "‫אִימוּן‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "136. Школа",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "школа",
    #             # pronunciation_word
    #             "beit 'sefer",
    #             # hebrew_word_nikud
    #             "‬בֵּית‬ ‫סֵפֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "ученик",
    #             # pronunciation_word
    #             "talmid",
    #             # hebrew_word_nikud
    #             "‫תַלמִיד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ученица",
    #             # pronunciation_word
    #             "talmida",
    #             # hebrew_word_nikud
    #             "‫תַלמִידָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учить(об учителе)",
    #             # pronunciation_word
    #             "lelamed",
    #             # hebrew_word_nikud
    #             "‫לְלַמֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учить наизусть",
    #             # pronunciation_word
    #             "lilmod beʿal pe",
    #             # hebrew_word_nikud
    #             "‫פֶּה‬ ‫בְּעַל‬ ‫לִלמוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учить (что-л.)",
    #             # pronunciation_word
    #             "lilmod",
    #             # hebrew_word_nikud
    #             "‫לִלמוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "идти в школу",
    #             # pronunciation_word
    #             "la'leχet le'beit 'sefer",
    #             # hebrew_word_nikud
    #             "לָלֶכֶת‬ ‫לְבֵּית‬ ‫סֶפֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предмет (дисциплина)",
    #             # pronunciation_word
    #             "mik'ʦoʿa",
    #             # hebrew_word_nikud
    #             "‫מִקצוֹע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "класс",
    #             # pronunciation_word
    #             "kita",
    #             # hebrew_word_nikud
    #             "‫כִּיתָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "урок",
    #             # pronunciation_word
    #             "ʃiʿur",
    #             # hebrew_word_nikud
    #             "‫שִיעוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "парта",
    #             # pronunciation_word
    #             "ʃulχan limudim",
    #             # hebrew_word_nikud
    #             "שוּלחַן‬ ‫לִימוּדִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "доска (школьная)",
    #             # pronunciation_word
    #             "'luaχ",
    #             # hebrew_word_nikud
    #             "‫לוּח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отметка",
    #             # pronunciation_word
    #             "ʦiyun",
    #             # hebrew_word_nikud
    #             "‫צִיוּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ошибка",
    #             # pronunciation_word
    #             "taʿut",
    #             # hebrew_word_nikud
    #             "‫טָעוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "делать ошибки",
    #             # pronunciation_word
    #             "laʿasot taʿuyot",
    #             # hebrew_word_nikud
    #             "‬‫טָעוּיוֹת‬ ‫לַעֲשׂוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "исправлять (ошибку)",
    #             # pronunciation_word
    #             "letaken",
    #             # hebrew_word_nikud
    #             "‫לְתַקֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "домашнее задание",
    #             # pronunciation_word
    #             "ʃiʿurei 'bayit",
    #             # hebrew_word_nikud
    #             "שִיעוּרֵי‬ ‫בַּיִת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "упражнение",
    #             # pronunciation_word
    #             "targil",
    #             # hebrew_word_nikud
    #             "‫תַרגִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "присутствовать",
    #             # pronunciation_word
    #             "lihyot no'χeaχ",
    #             # hebrew_word_nikud
    #             "לִהיוֹת‬ ‫נוֹכֵח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отсутствовать",
    #             # pronunciation_word
    #             "leheʿader",
    #             # hebrew_word_nikud
    #             "‫לְהֵיעָדֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "карандаш",
    #             # pronunciation_word
    #             "iparon",
    #             # hebrew_word_nikud
    #             "‫עִיפָּרוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ручка",
    #             # pronunciation_word
    #             "et",
    #             # hebrew_word_nikud
    #             "‬‫עֵט‬"
    #         ),
    #         (
    #             # translation_word
    #             "тетрадь",
    #             # pronunciation_word
    #             "maχ'beret",
    #             # hebrew_word_nikud
    #             "‫מַחבֶּרֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учебник",
    #             # pronunciation_word
    #             "'sefer limud",
    #             # hebrew_word_nikud
    #             "סֵפֶר‬ ‫לִימוּד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "каникулы",
    #             # pronunciation_word
    #             "χufʃa",
    #             # hebrew_word_nikud
    #             "‫חוּפשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "экзамен",
    #             # pronunciation_word
    #             "bχina",
    #             # hebrew_word_nikud
    #             "‫בּחִינָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сдавать экзамены",
    #             # pronunciation_word
    #             "lehibaχen",
    #             # hebrew_word_nikud
    #             "‫לְהִיבָּחֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "контрольная работа",
    #             # pronunciation_word
    #             "mivχan",
    #             # hebrew_word_nikud
    #             "‫מִבחָן‬‬"
    #         ),
    #     ]
    # ),  
    # (
    #     # group_name_ru
    #     "137. Высшее учебное заведение",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "академия",
    #             # pronunciation_word
    #             "aka'demya",
    #             # hebrew_word_nikud
    #             "‫אֲקָדֶמיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "университет",
    #             # pronunciation_word
    #             "uni'versita",
    #             # hebrew_word_nikud
    #             "‫אוּנִיבֶרסִיטָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "факультет",
    #             # pronunciation_word
    #             "fa'kulta",
    #             # hebrew_word_nikud
    #             "‫פָקוּלטָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "преподаватель",
    #             # pronunciation_word
    #             "marʦe",
    #             # hebrew_word_nikud
    #             "‫מַרצֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "студент",
    #             # pronunciation_word
    #             "student",
    #             # hebrew_word_nikud
    #             "‫סטוּדֶנט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "студентка",
    #             # pronunciation_word
    #             "stu'dentit",
    #             # hebrew_word_nikud
    #             "‬‫סטוּדֶנטִית‬"
    #         ),
    #         (
    #             # translation_word
    #             "аудитория (помещение)",
    #             # pronunciation_word
    #             "ulam harʦaʾot",
    #             # hebrew_word_nikud
    #             "אוּלַם‬ ‫הַרצָאוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "диплом",
    #             # pronunciation_word
    #             "di'ploma",
    #             # hebrew_word_nikud
    #             "‫דִיפּלוֹמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "диссертация",
    #             # pronunciation_word
    #             "diser'taʦya",
    #             # hebrew_word_nikud
    #             "‫דִיסֶרטַציָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лекция",
    #             # pronunciation_word
    #             "harʦaʾa",
    #             # hebrew_word_nikud
    #             "‫הַרצָאָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "однокурсник",
    #             # pronunciation_word
    #             "χaver lelimudim",
    #             # hebrew_word_nikud
    #             "חָבֵר‬ ‫לְלִימוּדִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стипендия",
    #             # pronunciation_word
    #             "milga",
    #             # hebrew_word_nikud
    #             "‫מִלגָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учёная степень",
    #             # pronunciation_word
    #             "'toʾar aka'demi",
    #             # hebrew_word_nikud
    #             "‫אָקָדֶמִי‬ ‫תוֹאַר‬‬"
    #         ),
    #     ]
    # ),     
    # (
    #     # group_name_ru
    #     "138. Названия наук и дисциплин",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "математика",
    #             # pronunciation_word
    #             "mate'matika",
    #             # hebrew_word_nikud
    #             "‫מָתֶמָטִיקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "астрономия",
    #             # pronunciation_word
    #             "astro'nomya",
    #             # hebrew_word_nikud
    #             "‫אַסטרוֹנוֹמיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "биология",
    #             # pronunciation_word
    #             "bio'logya",
    #             # hebrew_word_nikud
    #             "‫בִּיוֹלוֹגיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "география",
    #             # pronunciation_word
    #             "geʾo'grafya",
    #             # hebrew_word_nikud
    #             "‫גֵיאוֹגרַפיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "история",
    #             # pronunciation_word
    #             "his'torya",
    #             # hebrew_word_nikud
    #             "‫הִיסטוֹריָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "медицина",
    #             # pronunciation_word
    #             "refuʾa",
    #             # hebrew_word_nikud
    #             "‫רְפוּאָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "педагогика",
    #             # pronunciation_word
    #             "χinuχ",
    #             # hebrew_word_nikud
    #             "‫חִינוּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "право",
    #             # pronunciation_word
    #             "miʃpatim",
    #             # hebrew_word_nikud
    #             "‫מִשפָּטִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "физика",
    #             # pronunciation_word
    #             "'fizika",
    #             # hebrew_word_nikud
    #             "‫פִיזִיקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "химия",
    #             # pronunciation_word
    #             "'χimya",
    #             # hebrew_word_nikud
    #             "‫כִימיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "философия",
    #             # pronunciation_word
    #             "filo'sofya",
    #             # hebrew_word_nikud
    #             "‫פִילוֹסוֹפיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "психология",
    #             # pronunciation_word
    #             "psiχo'logya",
    #             # hebrew_word_nikud
    #             "‫פּסִיכוֹלוֹגיָה‬‬"
    #         ),
    #     ]
    # ),  
    # (
    #     # group_name_ru
    #     "139. Письмо. Части речи. Орфография",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "грамматика",
    #             # pronunciation_word
    #             "dikduk",
    #             # hebrew_word_nikud
    #             "‫דִקדוּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лексика",
    #             # pronunciation_word
    #             "oʦar milim",
    #             # hebrew_word_nikud
    #             "אוֹצַר‬ ‫מִילִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "существительное",
    #             # pronunciation_word
    #             "ʃem 'eʦem",
    #             # hebrew_word_nikud
    #             "שֵם‬ ‫עֶצֶם‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прилагательное",
    #             # pronunciation_word
    #             "ʃem 'toʾar",
    #             # hebrew_word_nikud
    #             "שֵם‬ ‫תוֹאַר‬‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "глагол",
    #             # pronunciation_word
    #             "poʿel",
    #             # hebrew_word_nikud
    #             "‫פּוֹעַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "наречие",
    #             # pronunciation_word
    #             "'toʾar 'poʿal",
    #             # hebrew_word_nikud
    #             "‬תוֹאַר‬ ‫פּוֹעַל‬"
    #         ),
    #         (
    #             # translation_word
    #             "местоимение",
    #             # pronunciation_word
    #             "ʃem guf",
    #             # hebrew_word_nikud
    #             "שֵם‬ ‫גוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предлог",
    #             # pronunciation_word
    #             "milat 'yaχas",
    #             # hebrew_word_nikud
    #             "מִילַת‬ ‫יַחַס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ударение",
    #             # pronunciation_word
    #             "'taʿam",
    #             # hebrew_word_nikud
    #             "‫טַעַם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "точка",
    #             # pronunciation_word
    #             "nekuda",
    #             # hebrew_word_nikud
    #             "‬‫נְקוּדָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "запятая",
    #             # pronunciation_word
    #             "psik",
    #             # hebrew_word_nikud
    #             "‫פּסִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вопросительный знак",
    #             # pronunciation_word
    #             "siman ʃeʾela",
    #             # hebrew_word_nikud
    #             "‬סִימַן‬ ‫שְאֵלָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "буква",
    #             # pronunciation_word
    #             "ot",
    #             # hebrew_word_nikud
    #             "‬‫אוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "гласный звук",
    #             # pronunciation_word
    #             "tnuʿa",
    #             # hebrew_word_nikud
    #             "‫תנוּעָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "согласный звук",
    #             # pronunciation_word
    #             "iʦur",
    #             # hebrew_word_nikud
    #             "‬‫עִיצוּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "предложение",
    #             # pronunciation_word
    #             "miʃpat",
    #             # hebrew_word_nikud
    #             "‫מִשפָּט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "строка",
    #             # pronunciation_word
    #             "ʃura",
    #             # hebrew_word_nikud
    #             "‫שוּרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слово",
    #             # pronunciation_word
    #             "mila",
    #             # hebrew_word_nikud
    #             "‬‫מִילָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "словосочетание",
    #             # pronunciation_word
    #             "ʦiruf milim",
    #             # hebrew_word_nikud
    #             "צִירוּף‬ ‫מִילִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "правило",
    #             # pronunciation_word
    #             "klal",
    #             # hebrew_word_nikud
    #             "‫כּלָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спряжение, склонение",
    #             # pronunciation_word
    #             "hataya",
    #             # hebrew_word_nikud
    #             "‫הַטָייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вопрос",
    #             # pronunciation_word
    #             "ʃeʾela",
    #             # hebrew_word_nikud
    #             "‫שְאֵלָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подчеркнуть",
    #             # pronunciation_word
    #             "lehadgiʃ",
    #             # hebrew_word_nikud
    #             "‫לְהַדגִיש‬‬"
    #         ),
    #     ]
    # ),   
    # (
    #     # group_name_ru
    #     "140. Изучение иностранных языков",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "язык (напр. русский)",
    #             # pronunciation_word
    #             "safa",
    #             # hebrew_word_nikud
    #             "‫שָׂפָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "иностранный",
    #             # pronunciation_word
    #             "zar",
    #             # hebrew_word_nikud
    #             "‬‫זָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "иностранный язык",
    #             # pronunciation_word
    #             "safa zara",
    #             # hebrew_word_nikud
    #             "שָׂפָה‬ ‫זָרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "читать",
    #             # pronunciation_word
    #             "likro",
    #             # hebrew_word_nikud
    #             "‫לִקרוֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "говорить",
    #             # pronunciation_word
    #             "ledaber",
    #             # hebrew_word_nikud
    #             "‫לְדַבֵּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "понимать",
    #             # pronunciation_word
    #             "lehavin",
    #             # hebrew_word_nikud
    #             "‫לְהָבִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "писать",
    #             # pronunciation_word
    #             "liχtov",
    #             # hebrew_word_nikud
    #             "‫לִכתוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "быстро",
    #             # pronunciation_word
    #             "maher",
    #             # hebrew_word_nikud
    #             "‫מַהֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "медленно",
    #             # pronunciation_word
    #             "leʾat",
    #             # hebrew_word_nikud
    #             "‫לְאַט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "свободно",
    #             # pronunciation_word
    #             "χofʃi",
    #             # hebrew_word_nikud
    #             "‫חוֹפשִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "словарь",
    #             # pronunciation_word
    #             "milon",
    #             # hebrew_word_nikud
    #             "‫מִילוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "самоучитель",
    #             # pronunciation_word
    #             "'sefer lelimud aʦmi",
    #             # hebrew_word_nikud
    #             "סֵפֶר‬ ‫לְלִימוּד‬ ‫עַצמִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "разговорник",
    #             # pronunciation_word
    #             "siχon",
    #             # hebrew_word_nikud
    #             "‫שִׂיחוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "говорить по буквам",
    #             # pronunciation_word
    #             "leʾayet",
    #             # hebrew_word_nikud
    #             "‫לְאַייֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "произношение",
    #             # pronunciation_word
    #             "hagiya",
    #             # hebrew_word_nikud
    #             "‬‫הֲגִייָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "акцент",
    #             # pronunciation_word
    #             "mivta",
    #             # hebrew_word_nikud
    #             "‬‫מִבטָא‬"
    #         ),
    #         (
    #             # translation_word
    #             "курсы",
    #             # pronunciation_word
    #             "kurs",
    #             # hebrew_word_nikud
    #             "‫קוּרס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "перевод",
    #             # pronunciation_word
    #             "tirgum",
    #             # hebrew_word_nikud
    #             "‫תִרגוּם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переводчик",
    #             # pronunciation_word
    #             "metargem",
    #             # hebrew_word_nikud
    #             "‫מְתַרגֵם‬"
    #         ),
    #         (
    #             # translation_word
    #             "память",
    #             # pronunciation_word
    #             "zikaron",
    #             # hebrew_word_nikud
    #             "‫זִיכָּרוֹן‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "141. Театр",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "театр",
    #             # pronunciation_word
    #             "teʾatron",
    #             # hebrew_word_nikud
    #             "‬‫תֵיאַטרוֹן‬"
    #         ),
    #         (
    #             # translation_word
    #             "опера",
    #             # pronunciation_word
    #             "'opera",
    #             # hebrew_word_nikud
    #             "‫אוֹפֶּרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "балет",
    #             # pronunciation_word
    #             "balet",
    #             # hebrew_word_nikud
    #             "‫בָּלֶט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "репетиция",
    #             # pronunciation_word
    #             "χazara",
    #             # hebrew_word_nikud
    #             "‫חֲזָרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "репетировать",
    #             # pronunciation_word
    #             "laʿaroχ χazara",
    #             # hebrew_word_nikud
    #             "לַעֲרוֹך‬ ‫חֲזָרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спектакль",
    #             # pronunciation_word
    #             "haʦaga",
    #             # hebrew_word_nikud
    #             "‫הַצָגָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "билет",
    #             # pronunciation_word
    #             "kartis",
    #             # hebrew_word_nikud
    #             "‬‫כַּרטִיס‬"
    #         ),
    #         (
    #             # translation_word
    #             "билетная касса",
    #             # pronunciation_word
    #             "kupa",
    #             # hebrew_word_nikud
    #             "‫קוּפָּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зритель",
    #             # pronunciation_word
    #             "ʦofe",
    #             # hebrew_word_nikud
    #             "‬‫צוֹפֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "хлопать (артистам)",
    #             # pronunciation_word
    #             "imχo ka'payim",
    #             # hebrew_word_nikud
    #             "לִמחוֹא‬ ‫כַּפַּיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сцена",
    #             # pronunciation_word
    #             "bama",
    #             # hebrew_word_nikud
    #             "‫בָּמָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "142. Кино",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "актёр",
    #             # pronunciation_word
    #             "saχkan",
    #             # hebrew_word_nikud
    #             "‫שַׂחקָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "актриса",
    #             # pronunciation_word
    #             "saχkanit",
    #             # hebrew_word_nikud
    #             "‫שַׂחקָנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кино (вид искусства)",
    #             # pronunciation_word
    #             "kol'noʿa",
    #             # hebrew_word_nikud
    #             "‫קוֹלנוֹע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кино, фильм",
    #             # pronunciation_word
    #             "'seret",
    #             # hebrew_word_nikud
    #             "‫סֶרֶט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "серия (часть фильма)",
    #             # pronunciation_word
    #             "epi'zoda",
    #             # hebrew_word_nikud
    #             "‫אֶפִּיזוֹדָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "детектив",
    #             # pronunciation_word
    #             "'seret balaʃi",
    #             # hebrew_word_nikud
    #             "סֶרֶט‬ ‫בַּלָשִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "боевик",
    #             # pronunciation_word
    #             "maʿarvon",
    #             # hebrew_word_nikud
    #             "‬‫מַעַרבוֹן‬"
    #         ),
    #         (
    #             # translation_word
    #             "фантастический фильм",
    #             # pronunciation_word
    #             "'seret mada bidyoni",
    #             # hebrew_word_nikud
    #             "סֶרֶט‬ ‫מַדָע‬ ‫בִּדיוֹנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "фильм ужасов",
    #             # pronunciation_word
    #             "'seret eima",
    #             # hebrew_word_nikud
    #             "‬‫אֵימָה‬ ‫סֶרֶט‬"
    #         ),
    #         (
    #             # translation_word
    #             "кинокомедия",
    #             # pronunciation_word
    #             "ko'medya",
    #             # hebrew_word_nikud
    #             "‬‫קוֹמֶדיָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "мелодрама",
    #             # pronunciation_word
    #             "melo'drama",
    #             # hebrew_word_nikud
    #             "‫מֶלוֹדרָמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "драма",
    #             # pronunciation_word
    #             "'drama",
    #             # hebrew_word_nikud
    #             "‫דרָמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мультфильм",
    #             # pronunciation_word
    #             "'seret ani'maʦya",
    #             # hebrew_word_nikud
    #             "סֶרֶט‬ ‫אֲנִימַציָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "играть (роль)",
    #             # pronunciation_word
    #             "lesaχek",
    #             # hebrew_word_nikud
    #             "‫לְשַׂחֵק‬‬"
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
    #             "популярный",
    #             # pronunciation_word
    #             "popu'lari",
    #             # hebrew_word_nikud
    #             "‫פּוֹפּוּלָרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "снимать фильм",
    #             # pronunciation_word
    #             "leʦalem 'seret",
    #             # hebrew_word_nikud
    #             "לְצַלֵם‬ ‫סֶרֶט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кинотеатр",
    #             # pronunciation_word
    #             "beit kol'noʿa",
    #             # hebrew_word_nikud
    #             "בֵּית‬ ‫קוֹלנוֹע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "субтитры",
    #             # pronunciation_word
    #             "ktuviyot",
    #             # hebrew_word_nikud
    #             "‫כּתוּבִיוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "перевод (с другого языка)",
    #             # pronunciation_word
    #             "tirgum",
    #             # hebrew_word_nikud
    #             "‫תִרגוּם‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "143. Изобразительное искусство",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "искусство",
    #             # pronunciation_word
    #             "amanut",
    #             # hebrew_word_nikud
    #             "‫אָמָנוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "выставка картин",
    #             # pronunciation_word
    #             "taʿaruχat amanut",
    #             # hebrew_word_nikud
    #             "תַעֲרוּכַת‬ ‫אָמָנוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "живопись",
    #             # pronunciation_word
    #             "ʦiyur",
    #             # hebrew_word_nikud
    #             "‫צִיוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "картина",
    #             # pronunciation_word
    #             "tmuna",
    #             # hebrew_word_nikud
    #             "‫תמוּנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скульптура, статуя",
    #             # pronunciation_word
    #             "pesel",
    #             # hebrew_word_nikud
    #             "‫פֶּסֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "краска",
    #             # pronunciation_word
    #             "'ʦeva",
    #             # hebrew_word_nikud
    #             "‫צֶבַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рисовать",
    #             # pronunciation_word
    #             "leʦayer",
    #             # hebrew_word_nikud
    #             "‬‫לְצַייֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "художник",
    #             # pronunciation_word
    #             "ʦayar",
    #             # hebrew_word_nikud
    #             "‫צַייָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "реставрировать",
    #             # pronunciation_word
    #             "leʃaχzer",
    #             # hebrew_word_nikud
    #             "‬‫לְשַחזֵר‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "144. Литература. Поэзия",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "литература",
    #             # pronunciation_word
    #             "sifrut",
    #             # hebrew_word_nikud
    #             "‫סִפרוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "автор",
    #             # pronunciation_word
    #             "sofer",
    #             # hebrew_word_nikud
    #             "‬‫סוֹפֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "оглавление",
    #             # pronunciation_word
    #             "'toχen inyanim",
    #             # hebrew_word_nikud
    #             "‬תוֹכֶן‬ ‫עִנייָנִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "страница",
    #             # pronunciation_word
    #             "amud",
    #             # hebrew_word_nikud
    #             "‬‫עַמוּד‬"
    #         ),
    #         (
    #             # translation_word
    #             "главный герой",
    #             # pronunciation_word
    #             "hagibor haraʃi",
    #             # hebrew_word_nikud
    #             "‬הַגִיבּוֹר‬ ‫הָרָאשִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "рассказ",
    #             # pronunciation_word
    #             "sipur kaʦar",
    #             # hebrew_word_nikud
    #             "‬‫קָצַר‬ ‫סִיפּוּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "повесть",
    #             # pronunciation_word
    #             "sipur",
    #             # hebrew_word_nikud
    #             "‫סִיפּוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "роман",
    #             # pronunciation_word
    #             "roman",
    #             # hebrew_word_nikud
    #             "‫רוֹמָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "детектив",
    #             # pronunciation_word
    #             "roman balaʃi",
    #             # hebrew_word_nikud
    #             "רוֹמָן‬ ‫בַּלָשִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стихотворение",
    #             # pronunciation_word
    #             "ʃir",
    #             # hebrew_word_nikud
    #             "‫שִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поэзия",
    #             # pronunciation_word
    #             "ʃira",
    #             # hebrew_word_nikud
    #             "‫שִירָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поэт",
    #             # pronunciation_word
    #             "meʃorer",
    #             # hebrew_word_nikud
    #             "‫מְשוֹרֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учебная литература",
    #             # pronunciation_word
    #             "sifrut limudit",
    #             # hebrew_word_nikud
    #             "סִפרוּת‬ ‫לִימוּדִית‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "145. Музыка. Эстрада",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "музыка",
    #             # pronunciation_word
    #             "'muzika",
    #             # hebrew_word_nikud
    #             "‫מוּזִיקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "музыкант",
    #             # pronunciation_word
    #             "muzikai",
    #             # hebrew_word_nikud
    #             "‫מוּזִיקַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "играть на ...",
    #             # pronunciation_word
    #             "enagen be...",
    #             # hebrew_word_nikud
    #             "...לְנַגֵן ‫ב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гитара",
    #             # pronunciation_word
    #             "gi'tara",
    #             # hebrew_word_nikud
    #             "‫גִיטָרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скрипка",
    #             # pronunciation_word
    #             "kinor",
    #             # hebrew_word_nikud
    #             "‬‫כִּינוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "пианино",
    #             # pronunciation_word
    #             "psanter",
    #             # hebrew_word_nikud
    #             "‫פּסַנתֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "барабан",
    #             # pronunciation_word
    #             "tof",
    #             # hebrew_word_nikud
    #             "‫תוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поп-музыка",
    #             # pronunciation_word
    #             "'muzikat pop",
    #             # hebrew_word_nikud
    #             "מוּזִיקַת‬ ‫פּוֹפ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рок-музыка",
    #             # pronunciation_word
    #             "'muzikat rok",
    #             # hebrew_word_nikud
    #             "מוּזִיקַת‬ ‫רוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "концерт",
    #             # pronunciation_word
    #             "konʦert",
    #             # hebrew_word_nikud
    #             "‫קוֹנצֶרט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "симфония",
    #             # pronunciation_word
    #             "si'fonya",
    #             # hebrew_word_nikud
    #             "‫סִימפוֹניָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "песня",
    #             # pronunciation_word
    #             "ʃir",
    #             # hebrew_word_nikud
    #             "‫שִיר‬‬"
    #         ),
    #     ]
    # ),    
    # (
    #     # group_name_ru
    #     "146. Турпоездка",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "туризм",
    #             # pronunciation_word
    #             "tayarut",
    #             # hebrew_word_nikud
    #             "‬‫תַייָרוּת‬"
    #         ),
    #         (
    #             # translation_word
    #             "турист",
    #             # pronunciation_word
    #             "tayar",
    #             # hebrew_word_nikud
    #             "‬‫תַייָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "путешествие",
    #             # pronunciation_word
    #             "tiyul",
    #             # hebrew_word_nikud
    #             "‫טִיוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поездка",
    #             # pronunciation_word
    #             "nesiʿa",
    #             # hebrew_word_nikud
    #             "‬‫נְסִיעָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "отпуск",
    #             # pronunciation_word
    #             "χufʃa",
    #             # hebrew_word_nikud
    #             "‫חוּפשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отдых",
    #             # pronunciation_word
    #             "menuχa",
    #             # hebrew_word_nikud
    #             "‫מְנוּחָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поезд",
    #             # pronunciation_word
    #             "ra'kevet",
    #             # hebrew_word_nikud
    #             "‫רַכֶּבֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "самолёт",
    #             # pronunciation_word
    #             "matos",
    #             # hebrew_word_nikud
    #             "‫מָטוֹס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "багаж",
    #             # pronunciation_word
    #             "mitʿan",
    #             # hebrew_word_nikud
    #             "‫מִטעָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "паспорт",
    #             # pronunciation_word
    #             "darkon",
    #             # hebrew_word_nikud
    #             "‫דַרכּוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "виза",
    #             # pronunciation_word
    #             "viza",
    #             # hebrew_word_nikud
    #             "‫וִיזָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "авиабилет",
    #             # pronunciation_word
    #             "kartis tisa",
    #             # hebrew_word_nikud
    #             "‫טִיסָה‬ ‫כַּרטִיס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "карта (географ.)",
    #             # pronunciation_word
    #             "mapa",
    #             # hebrew_word_nikud
    #             "‫מַפָּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "экскурсия",
    #             # pronunciation_word
    #             "tiyul",
    #             # hebrew_word_nikud
    #             "‫טִיוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "экскурсовод",
    #             # pronunciation_word
    #             "madriχ tiyulim",
    #             # hebrew_word_nikud
    #             "מַדרִיך‬ ‫טִיוּלִים‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "147. Гостиница",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "гостиница",
    #             # pronunciation_word
    #             "beit malon",
    #             # hebrew_word_nikud
    #             "בֵּית‬ ‫מָלוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отель",
    #             # pronunciation_word
    #             "malon",
    #             # hebrew_word_nikud
    #             "‫מָלוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "остановиться (в отеле)",
    #             # pronunciation_word
    #             "lehitʾaχsen",
    #             # hebrew_word_nikud
    #             "‫לְהִתאַכסֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "номер (в гостинице)",
    #             # pronunciation_word
    #             "'χeder",
    #             # hebrew_word_nikud
    #             "‫חֶדֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "одноместный номер",
    #             # pronunciation_word
    #             "'χeder yaχid",
    #             # hebrew_word_nikud
    #             "חֶדֶר‬ ‫יָחִיד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "двухместный номер",
    #             # pronunciation_word
    #             "'χeder zugi",
    #             # hebrew_word_nikud
    #             "חֶדֶר‬ ‫זוּגִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бронировать номер",
    #             # pronunciation_word
    #             "lehazmin 'χeder",
    #             # hebrew_word_nikud
    #             "‬לְהַזמִין‬ ‫חֶדֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "с ванной",
    #             # pronunciation_word
    #             "im am'batya",
    #             # hebrew_word_nikud
    #             "עִם‬ ‫אַמבַּטיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "с душем",
    #             # pronunciation_word
    #             "im mik'laχat",
    #             # hebrew_word_nikud
    #             "‬עִם‬ ‫מִקלַחַת‬"
    #         ),
    #         (
    #             # translation_word
    #             "кондиционер",
    #             # pronunciation_word
    #             "mazgan",
    #             # hebrew_word_nikud
    #             "‫מַזגָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полотенце",
    #             # pronunciation_word
    #             "ma'gevet",
    #             # hebrew_word_nikud
    #             "‫מַגֶבֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ключ",
    #             # pronunciation_word
    #             "maf'teaχ",
    #             # hebrew_word_nikud
    #             "‬‫מַפתֵח‬"
    #         ),
    #         (
    #             # translation_word
    #             "администратор",
    #             # pronunciation_word
    #             "amarkal",
    #             # hebrew_word_nikud
    #             "‫אֲמַרכָּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "горничная",
    #             # pronunciation_word
    #             "χadranit",
    #             # hebrew_word_nikud
    #             "‫חַדרָנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "носильщик",
    #             # pronunciation_word
    #             "sabal",
    #             # hebrew_word_nikud
    #             "‫סַבָּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ресторан",
    #             # pronunciation_word
    #             "misʿada",
    #             # hebrew_word_nikud
    #             "‬‫מִסעָדָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "бар",
    #             # pronunciation_word
    #             "bar",
    #             # hebrew_word_nikud
    #             "‬‫בָּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "завтрак",
    #             # pronunciation_word
    #             "aruχat 'boker",
    #             # hebrew_word_nikud
    #             "‬אֲרוּחַת‬ ‫בּוֹקֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "ужин",
    #             # pronunciation_word
    #             "aruχat 'erev",
    #             # hebrew_word_nikud
    #             "אֲרוּחַת‬ ‫עֶרֶב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шведский стол",
    #             # pronunciation_word
    #             "miznon",
    #             # hebrew_word_nikud
    #             "‫מִזנוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вестибюль",
    #             # pronunciation_word
    #             "'lobi",
    #             # hebrew_word_nikud
    #             "‫לוֹבִּי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лифт",
    #             # pronunciation_word
    #             "maʿalit",
    #             # hebrew_word_nikud
    #             "‫מַעֲלִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "НЕ БЕСПОКОИТЬ",
    #             # pronunciation_word
    #             "lo lehaf'riʿa",
    #             # hebrew_word_nikud
    #             "לֹא‬ ‫לְהַפרִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "НЕ КУРИТЬ!",
    #             # pronunciation_word
    #             "asur leʿaʃen!",
    #             # hebrew_word_nikud
    #             "!אָסוּר‬ ‫לְעַשֵן‬‬"
    #         ),
    #     ]
    # ),   
    # (
    #     # group_name_ru
    #     "148. Книга. Чтение",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "книга",
    #             # pronunciation_word
    #             "'sefer",
    #             # hebrew_word_nikud
    #             "‬‫סֶפֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "автор",
    #             # pronunciation_word
    #             "sofer",
    #             # hebrew_word_nikud
    #             "‫סוֹפֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "написать (книгу)",
    #             # pronunciation_word
    #             "liχtov",
    #             # hebrew_word_nikud
    #             "‫לִכתוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "читатель",
    #             # pronunciation_word
    #             "kore",
    #             # hebrew_word_nikud
    #             "‬‫קוֹרֵא‬"
    #         ),
    #         (
    #             # translation_word
    #             "читать",
    #             # pronunciation_word
    #             "likro",
    #             # hebrew_word_nikud
    #             "‫לִקרוֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чтение",
    #             # pronunciation_word
    #             "kriʾa",
    #             # hebrew_word_nikud
    #             "‫קרִיאָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "издатель",
    #             # pronunciation_word
    #             "moʦi leʾor",
    #             # hebrew_word_nikud
    #             "מוֹצִיא‬ ‫לְאוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "издательство",
    #             # pronunciation_word
    #             "hoʦaʾa laʾor",
    #             # hebrew_word_nikud
    #             "‬הוֹצָאָה‬ ‫לָאוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "книжный магазин",
    #             # pronunciation_word
    #             "χanut sfarim",
    #             # hebrew_word_nikud
    #             "חֲנוּת‬ ‫ספָרִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "библиотека",
    #             # pronunciation_word
    #             "sifriya",
    #             # hebrew_word_nikud
    #             "‫סִפרִייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сюжет",
    #             # pronunciation_word
    #             "alila",
    #             # hebrew_word_nikud
    #             "‫עֲלִילָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "содержание (список)",
    #             # pronunciation_word
    #             "'toχen",
    #             # hebrew_word_nikud
    #             "‫תוֹכֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "страница",
    #             # pronunciation_word
    #             "amud",
    #             # hebrew_word_nikud
    #             "‬‫עַמוּד‬"
    #         ),
    #         (
    #             # translation_word
    #             "текст",
    #             # pronunciation_word
    #             "tekst",
    #             # hebrew_word_nikud
    #             "‫טֶקסט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шрифт",
    #             # pronunciation_word
    #             "gufan",
    #             # hebrew_word_nikud
    #             "‫גוּפָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бестселлер",
    #             # pronunciation_word
    #             "rav 'meχer",
    #             # hebrew_word_nikud
    #             "‫רַב־מֶכֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "словарь",
    #             # pronunciation_word
    #             "milon",
    #             # hebrew_word_nikud
    #             "‫מִילוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "учебник",
    #             # pronunciation_word
    #             "'sefer limud",
    #             # hebrew_word_nikud
    #             "סֵפֶר‬ ‫לִימוּד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "энциклопедия",
    #             # pronunciation_word
    #             "enʦiklo'pedya",
    #             # hebrew_word_nikud
    #             "‫אֶנצִיקלוֹפֶּדיָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "149. Активные виды отдыха.",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "охота",
    #             # pronunciation_word
    #             "'ʦayid",
    #             # hebrew_word_nikud
    #             "‫צַיִד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рыбалка",
    #             # pronunciation_word
    #             "'dayig",
    #             # hebrew_word_nikud
    #             "‬‫דַיִג‬"
    #         ),
    #         (
    #             # translation_word
    #             "бильярд",
    #             # pronunciation_word
    #             "bilyard",
    #             # hebrew_word_nikud
    #             "‬‫בִּיליַארד‬"
    #         ),
    #         (
    #             # translation_word
    #             "карты",
    #             # pronunciation_word
    #             "klafim",
    #             # hebrew_word_nikud
    #             "‫קלָפִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "казино",
    #             # pronunciation_word
    #             "ka'zino",
    #             # hebrew_word_nikud
    #             "‫קָזִינו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гулять (прогуливаться)",
    #             # pronunciation_word
    #             "letayel ba'regel",
    #             # hebrew_word_nikud
    #             "‬לְטַייֵל‬ ‫בָּרֶגֶל‬"
    #         ),
    #         (
    #             # translation_word
    #             "пикник",
    #             # pronunciation_word
    #             "'piknik",
    #             # hebrew_word_nikud
    #             "‫פִּיקנִיק‬‬"
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
    #             "игра",
    #             # pronunciation_word
    #             "misχak",
    #             # hebrew_word_nikud
    #             "‫מִשׂחָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дискотека",
    #             # pronunciation_word
    #             "diskotek",
    #             # hebrew_word_nikud
    #             "‫דִיסקוֹטֶק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сауна",
    #             # pronunciation_word
    #             "'saʾuna",
    #             # hebrew_word_nikud
    #             "‫סָאוּנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поход",
    #             # pronunciation_word
    #             "tiyul maχanaʾut",
    #             # hebrew_word_nikud
    #             "טִיוּל‬ ‫מַחֲנָאוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лагерь",
    #             # pronunciation_word
    #             "maχane",
    #             # hebrew_word_nikud
    #             "‫מַחֲנֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "смотреть (телевизор)",
    #             # pronunciation_word
    #             "lirʾot",
    #             # hebrew_word_nikud
    #             "‫לִראוֹת‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "150. Пляж",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "пляж",
    #             # pronunciation_word
    #             "χof yam",
    #             # hebrew_word_nikud
    #             "חוֹף‬ ‫יָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "песок",
    #             # pronunciation_word
    #             "χol",
    #             # hebrew_word_nikud
    #             "‬‫חוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "пустынный (пляж)",
    #             # pronunciation_word
    #             "ʃomem",
    #             # hebrew_word_nikud
    #             "‫שוֹמֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "загар",
    #             # pronunciation_word
    #             "ʃizuf",
    #             # hebrew_word_nikud
    #             "‫שִיזוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "загорать",
    #             # pronunciation_word
    #             "lehiʃtazef",
    #             # hebrew_word_nikud
    #             "‫לְהִשתַזֵף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "крем для загара",
    #             # pronunciation_word
    #             "krem hagana",
    #             # hebrew_word_nikud
    #             "‬קרֶם‬ ‫הֲגָנָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "бикини",
    #             # pronunciation_word
    #             "bi'kini",
    #             # hebrew_word_nikud
    #             "‫בִּיקִינִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "купальник, плавки",
    #             # pronunciation_word
    #             "beged yam",
    #             # hebrew_word_nikud
    #             "בֶּגֶד‬ ‫יָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бассейн",
    #             # pronunciation_word
    #             "breχa",
    #             # hebrew_word_nikud
    #             "‫בּרֵיכָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плавать",
    #             # pronunciation_word
    #             "lisχot",
    #             # hebrew_word_nikud
    #             "‫לִשׂחוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переодеваться",
    #             # pronunciation_word
    #             "lehaχlif bgadim",
    #             # hebrew_word_nikud
    #             "לְהַחלִיף‬ ‫בּגָדִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лодка",
    #             # pronunciation_word
    #             "sira",
    #             # hebrew_word_nikud
    #             "‫סִירָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нырять",
    #             # pronunciation_word
    #             "liʦlol",
    #             # hebrew_word_nikud
    #             "‬‫לִצלוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "купаться",
    #             # pronunciation_word
    #             "lehitraχeʦ",
    #             # hebrew_word_nikud
    #             "‫לְהִתרַחֵץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "волна",
    #             # pronunciation_word
    #             "gal",
    #             # hebrew_word_nikud
    #             "‫גַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спасать",
    #             # pronunciation_word
    #             "lehaʦil",
    #             # hebrew_word_nikud
    #             "‫לְהַצִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спасатель",
    #             # pronunciation_word
    #             "maʦil",
    #             # hebrew_word_nikud
    #             "‫מַצִיל‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "151. Компьютер",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "компьютер",
    #             # pronunciation_word
    #             "maχʃev",
    #             # hebrew_word_nikud
    #             "‫מַחשֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ноутбук",
    #             # pronunciation_word
    #             "maχʃev nayad",
    #             # hebrew_word_nikud
    #             "מַחשֵב‬ ‫נַייָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "включить",
    #             # pronunciation_word
    #             "lehadlik",
    #             # hebrew_word_nikud
    #             "‬‫לְהַדלִיק‬"
    #         ),
    #         (
    #             # translation_word
    #             "выключить",
    #             # pronunciation_word
    #             "leχabot",
    #             # hebrew_word_nikud
    #             "‫לְכַבּוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "клавиатура",
    #             # pronunciation_word
    #             "mik'ledet",
    #             # hebrew_word_nikud
    #             "‫מִקלֶדֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мышь",
    #             # pronunciation_word
    #             "aχbar",
    #             # hebrew_word_nikud
    #             "‫עַכבָּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "курсор",
    #             # pronunciation_word
    #             "saman",
    #             # hebrew_word_nikud
    #             "‫סַמָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кнопка",
    #             # pronunciation_word
    #             "kaftor",
    #             # hebrew_word_nikud
    #             "‫כַּפתוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "монитор",
    #             # pronunciation_word
    #             "masaχ",
    #             # hebrew_word_nikud
    #             "‫מָסָך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "экран",
    #             # pronunciation_word
    #             "ʦag",
    #             # hebrew_word_nikud
    #             "‫צָג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жёсткий диск",
    #             # pronunciation_word
    #             "disk ka'ʃiaχ",
    #             # hebrew_word_nikud
    #             "דִיסק‬ ַ‫קָשִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "оперативная память",
    #             # pronunciation_word
    #             "zikaron giʃa akraʾit",
    #             # hebrew_word_nikud
    #             "זִיכָּרוֹן‬ ‫גיִשָה‬ ‫אַקרַאִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "файл",
    #             # pronunciation_word
    #             "'koveʦ",
    #             # hebrew_word_nikud
    #             "‫קוֹבֶץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "папка (комп.)",
    #             # pronunciation_word
    #             "tikiya",
    #             # hebrew_word_nikud
    #             "‬‫תִיקִייָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "открыть",
    #             # pronunciation_word
    #             "lif'toaχ",
    #             # hebrew_word_nikud
    #             "‫לִפתוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "закрыть",
    #             # pronunciation_word
    #             "lisgor",
    #             # hebrew_word_nikud
    #             "‫לִסגוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сохранить",
    #             # pronunciation_word
    #             "liʃmor",
    #             # hebrew_word_nikud
    #             "‫לִשמוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "удалить",
    #             # pronunciation_word
    #             "limχok",
    #             # hebrew_word_nikud
    #             "‫לִמחוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скопировать",
    #             # pronunciation_word
    #             "lehaʿatik",
    #             # hebrew_word_nikud
    #             "‫לְהַעֲתִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "программа, программное обеспечение",
    #             # pronunciation_word
    #             "toχna",
    #             # hebrew_word_nikud
    #             "‫תוֹכנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "программист",
    #             # pronunciation_word
    #             "metaχnet",
    #             # hebrew_word_nikud
    #             "‫מְתַכנֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "программировать",
    #             # pronunciation_word
    #             "letaχnet",
    #             # hebrew_word_nikud
    #             "‫לְתַכנֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "хакер",
    #             # pronunciation_word
    #             "'haker",
    #             # hebrew_word_nikud
    #             "‫הָאקֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пароль",
    #             # pronunciation_word
    #             "sisma",
    #             # hebrew_word_nikud
    #             "‫סִיסמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вирус",
    #             # pronunciation_word
    #             "'virus",
    #             # hebrew_word_nikud
    #             "‫וִירוּס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "байт",
    #             # pronunciation_word
    #             "bait",
    #             # hebrew_word_nikud
    #             "‫בַּייט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "данные",
    #             # pronunciation_word
    #             "netunim",
    #             # hebrew_word_nikud
    #             "‬‫נְתוּנִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "база данных",
    #             # pronunciation_word
    #             "bsis netunim",
    #             # hebrew_word_nikud
    #             "בּסִיס‬ ‫נְתוּנִים‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кабель",
    #             # pronunciation_word
    #             "'kevel",
    #             # hebrew_word_nikud
    #             "‬‫כֶּבֶל‬"
    #         ),
    #         (
    #             # translation_word
    #             "отсоединить",
    #             # pronunciation_word
    #             "lenatek",
    #             # hebrew_word_nikud
    #             "‬‫לְנַתֵק‬"
    #         ),(
    #             # translation_word
    #             "подсоединить",
    #             # pronunciation_word
    #             "leχaber",
    #             # hebrew_word_nikud
    #             "‫לְחַבֵּר‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "152. Интернет. E-mail",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "интернет",
    #             # pronunciation_word
    #             "'internet",
    #             # hebrew_word_nikud
    #             "‫אִינטֶרנֶט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "браузер",
    #             # pronunciation_word
    #             "dafdefan",
    #             # hebrew_word_nikud
    #             "‫דַפדְפָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "провайдер",
    #             # pronunciation_word
    #             "sapak",
    #             # hebrew_word_nikud
    #             "‫סַפָּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "веб-сайт",
    #             # pronunciation_word
    #             "atar",
    #             # hebrew_word_nikud
    #             "‬‫אֲתַר‬"
    #         ),
    #         (
    #             # translation_word
    #             "адрес",
    #             # pronunciation_word
    #             "'ktovet",
    #             # hebrew_word_nikud
    #             "‫כּתוֹבֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сообщение",
    #             # pronunciation_word
    #             "hodaʿa",
    #             # hebrew_word_nikud
    #             "‫הוֹדָעָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переписка",
    #             # pronunciation_word
    #             "hitkatvut",
    #             # hebrew_word_nikud
    #             "‫הִתכַּתבוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "связь",
    #             # pronunciation_word
    #             "χibur",
    #             # hebrew_word_nikud
    #             "‫חִיבּוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скорость",
    #             # pronunciation_word
    #             "mehirut",
    #             # hebrew_word_nikud
    #             "‫מְהִירוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "модем",
    #             # pronunciation_word
    #             "'modem",
    #             # hebrew_word_nikud
    #             "‫מוֹדֶם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "доступ",
    #             # pronunciation_word
    #             "giʃa",
    #             # hebrew_word_nikud
    #             "‫גִישָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "порт (комп.)",
    #             # pronunciation_word
    #             "port",
    #             # hebrew_word_nikud
    #             "‬‫פּוֹרט‬"
    #         ),
    #         (
    #             # translation_word
    #             "подключение",
    #             # pronunciation_word
    #             "χibur",
    #             # hebrew_word_nikud
    #             "‫חִיבּוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подключиться",
    #             # pronunciation_word
    #             "lehitχaber",
    #             # hebrew_word_nikud
    #             "‫לְהִתחַבֵּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "искать",
    #             # pronunciation_word
    #             "leχapes",
    #             # hebrew_word_nikud
    #             "‬‫לְחַפֵּש‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "153. Электричество",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "электричество",
    #             # pronunciation_word
    #             "χaʃmal",
    #             # hebrew_word_nikud
    #             "‫חַשמַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "электрический",
    #             # pronunciation_word
    #             "χaʃmali",
    #             # hebrew_word_nikud
    #             "‫חַשמַלִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "энергия",
    #             # pronunciation_word
    #             "e'nergya",
    #             # hebrew_word_nikud
    #             "‫אֶנֶרגיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "электроэнергия",
    #             # pronunciation_word
    #             "e'nergya χaʃmalit",
    #             # hebrew_word_nikud
    #             "‬אֶנֶרגיָה‬ ‫חַשמַלִית‬"
    #         ),
    #         (
    #             # translation_word
    #             "лампочка",
    #             # pronunciation_word
    #             "nura",
    #             # hebrew_word_nikud
    #             "‫נוּרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "свет (электричество)",
    #             # pronunciation_word
    #             "or",
    #             # hebrew_word_nikud
    #             "‫אוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "выключатель",
    #             # pronunciation_word
    #             "'meteg",
    #             # hebrew_word_nikud
    #             "‫מֶתֶג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "розетка",
    #             # pronunciation_word
    #             "'ʃeka",
    #             # hebrew_word_nikud
    #             "‫שֶקַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вилка",
    #             # pronunciation_word
    #             "'teka",
    #             # hebrew_word_nikud
    #             "‬‫תֶקַע‬"
    #         ),
    #         (
    #             # translation_word
    #             "удлинитель",
    #             # pronunciation_word
    #             "'kabel maʾariχ",
    #             # hebrew_word_nikud
    #             "כַּבֶּל‬ ‫מַאֲרִיך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предохранитель",
    #             # pronunciation_word
    #             "natiχ",
    #             # hebrew_word_nikud
    #             "‫נָתִיך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "электрик",
    #             # pronunciation_word
    #             "χaʃmalai",
    #             # hebrew_word_nikud
    #             "‫חַשמַלאַי‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "154. Самолёт",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "самолёт",
    #             # pronunciation_word
    #             "matos",
    #             # hebrew_word_nikud
    #             "‫מָטוֹס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "авиабилет",
    #             # pronunciation_word
    #             "kartis tisa",
    #             # hebrew_word_nikud
    #             "כַּרטִיס‬ ‫טִיסָה‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "авиакомпания",
    #             # pronunciation_word
    #             "χevrat teʿufa",
    #             # hebrew_word_nikud
    #             "חֶברַת‬ ‫תְעוּפָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "аэропорт",
    #             # pronunciation_word
    #             "nemal teʿufa",
    #             # hebrew_word_nikud
    #             "נְמַל‬ ‫תְעוּפָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пилот",
    #             # pronunciation_word
    #             "tayas",
    #             # hebrew_word_nikud
    #             "‫טַייָס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стюардесса",
    #             # pronunciation_word
    #             "da'yelet",
    #             # hebrew_word_nikud
    #             "‫דַייֶלֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "парашют",
    #             # pronunciation_word
    #             "miʦnaχ",
    #             # hebrew_word_nikud
    #             "‫מִצנָח‬‬"
    #         ),
    #     ]
    # ), 
    (
        # group_name_ru
        "155. Поезд",
        # words
        [
            (
                # translation_word
                "поезд",
                # pronunciation_word
                "ra'kevet",
                # hebrew_word_nikud
                "‫רַכֶּבֶת‬‬"
            ),
            (
                # translation_word
                "электричка",
                # pronunciation_word
                "ra'kevet parvarim",
                # hebrew_word_nikud
                "רַכֶּבֶת‬ ‫פַּרבָרִים‬‬"
            ),
            (
                # translation_word
                "вагон",
                # pronunciation_word
                "karon",
                # hebrew_word_nikud
                "‫קָרוֹן‬‬"
            ),
            (
                # translation_word
                "железная дорога",
                # pronunciation_word
                "mesilat barzel",
                # hebrew_word_nikud
                "מְסִילַת‬ ‫בַּרזֶל‬‬"
            ),
            (
                # translation_word
                "станция",
                # pronunciation_word
                "taχana",
                # hebrew_word_nikud
                "‫תַחֲנָה‬‬"
            ),
            (
                # translation_word
                "пассажир",
                # pronunciation_word
                "no'seʿa",
                # hebrew_word_nikud
                "‫נוֹסֵע‬‬"
            ),
            (
                # translation_word
                "машинист",
                # pronunciation_word
                "nahag ra'kevet",
                # hebrew_word_nikud
                "נַהַג‬ ‫רַכֶּבֶת‬‬"
            ),
            (
                # translation_word
                "контролёр",
                # pronunciation_word
                "bodek",
                # hebrew_word_nikud
                "‫בּוֹדֵק‬‬"
            ),
            (
                # translation_word
                "купе",
                # pronunciation_word
                "ta",
                # hebrew_word_nikud
                "‫תָא‬‬"
            ),
            (
                # translation_word
                "расписание",
                # pronunciation_word
                "'luaχ zmanim",
                # hebrew_word_nikud
                "לוּח‬ ‫זמַנִים‬‬"
            ),
            (
                # translation_word
                "приехать поездом",
                # pronunciation_word
                "leha'giʿa bera'kevet",
                # hebrew_word_nikud
                "לְהַגִיע‬ ‫בְּרַכֶּבֶת‬‬"
            ),
        ]
    ), 
    # (
    #     # group_name_ru
    #     "156. Аэропорт",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "аэропорт",
    #             # pronunciation_word
    #             "nemal teʿufa",
    #             # hebrew_word_nikud
    #             "נְמַל‬‬ ‫תְעוּפָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "самолёт",
    #             # pronunciation_word
    #             "matos",
    #             # hebrew_word_nikud
    #             "‫מָטוֹס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "авиакомпания",
    #             # pronunciation_word
    #             "χevrat teʿufa",
    #             # hebrew_word_nikud
    #             "חֶברַת‬‬ ‫תְעוּפָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вылет",
    #             # pronunciation_word
    #             "hamraʾa",
    #             # hebrew_word_nikud
    #             "‫הַמרָאָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прилёт",
    #             # pronunciation_word
    #             "neχita",
    #             # hebrew_word_nikud
    #             "‫נְחִיתָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прилететь",
    #             # pronunciation_word
    #             "leha'giʿa betisa",
    #             # hebrew_word_nikud
    #             "לְהַגִיע‬‬ ‫בְּטִיסָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "задерживаться (о рейсе)",
    #             # pronunciation_word
    #             "lehitʿakev",
    #             # hebrew_word_nikud
    #             "‫לְהִתעַכֵּב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "информационное табло",
    #             # pronunciation_word
    #             "'luaχ meida",
    #             # hebrew_word_nikud
    #             "לוּח‬‬ ‫מֵידָע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "информация",
    #             # pronunciation_word
    #             "meida",
    #             # hebrew_word_nikud
    #             "‫מֵידָע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "объявлять",
    #             # pronunciation_word
    #             "leho'dia",
    #             # hebrew_word_nikud
    #             "‫לְהוֹדִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рейс",
    #             # pronunciation_word
    #             "tisa",
    #             # hebrew_word_nikud
    #             "‫טִיסָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "таможня",
    #             # pronunciation_word
    #             "'meχes",
    #             # hebrew_word_nikud
    #             "‫מֶכֶס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "таможенная декларация",
    #             # pronunciation_word
    #             "haʦharat meχes",
    #             # hebrew_word_nikud
    #             "הַצהָרַת‬‬ ‫מֶכֶס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "багаж",
    #             # pronunciation_word
    #             "kvuda",
    #             # hebrew_word_nikud
    #             "‫כּבוּדָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ручная кладь",
    #             # pronunciation_word
    #             "kvudat yad",
    #             # hebrew_word_nikud
    #             "כּבוּדַת‬‬ ‫יָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "посадка",
    #             # pronunciation_word
    #             "neχita",
    #             # hebrew_word_nikud
    #             "‫נְחִיתָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "трап (к самолету)",
    #             # pronunciation_word
    #             "'keveʃ",
    #             # hebrew_word_nikud
    #             "‫כֶּבֶש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "регистрация",
    #             # pronunciation_word
    #             "ʧek in",
    #             # hebrew_word_nikud
    #             "צֶ׳ק‬‬ ‫אִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "посадочный талон",
    #             # pronunciation_word
    #             "kartis aliya lematos",
    #             # hebrew_word_nikud
    #             "‬כַּרטִיס‬‬ ‫עֲלִיָה‬ ‫לְמָטוֹס‬"
    #         ),
    #         (
    #             # translation_word
    #             "зал ожидания",
    #             # pronunciation_word
    #             "traklin tisa",
    #             # hebrew_word_nikud
    #             "טרַקלִין‬‬ ‫טיִסָה‬‬"
    #         ),
    #     ]
    # ),     
    # (
    #     # group_name_ru
    #     "157. Праздник. Событие",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "праздник (торжество)",
    #             # pronunciation_word
    #             "χagiga",
    #             # hebrew_word_nikud
    #             "‫חֲגִיגָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "национальный праздник",
    #             # pronunciation_word
    #             "χag leʾumi",
    #             # hebrew_word_nikud
    #             "חַג‬‬ ‫לְאוּמִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "праздничный день",
    #             # pronunciation_word
    #             "yom χag",
    #             # hebrew_word_nikud
    #             "‫יוֹם‬‬ ‫חַג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "праздновать",
    #             # pronunciation_word
    #             "laχgog",
    #             # hebrew_word_nikud
    #             "‫לַחגוֹג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "событие",
    #             # pronunciation_word
    #             "hitraχaʃut",
    #             # hebrew_word_nikud
    #             "‫הִתרַחֲשוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мероприятие (событие)",
    #             # pronunciation_word
    #             "ei'ruʿa",
    #             # hebrew_word_nikud
    #             "‫אֵירוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "годовщина",
    #             # pronunciation_word
    #             "yom haʃana",
    #             # hebrew_word_nikud
    #             "יוֹם‬‬ ‫הַשָנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "юбилей",
    #             # pronunciation_word
    #             "χag hayovel",
    #             # hebrew_word_nikud
    #             "חַג‬‬ ‫הַיוֹבֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Новый год",
    #             # pronunciation_word
    #             "ʃana χadaʃa",
    #             # hebrew_word_nikud
    #             "שָנָה‬‬ ‫חָדָשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "С Новым Годом!",
    #             # pronunciation_word
    #             "ʃana tova!",
    #             # hebrew_word_nikud
    #             "!שָנָה‬‬ ‫טוֹבָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Рождество",
    #             # pronunciation_word
    #             "χag hamolad",
    #             # hebrew_word_nikud
    #             "חַג‬‬ ‫הַמוֹלָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "салют (фейерверк)",
    #             # pronunciation_word
    #             "zikukim",
    #             # hebrew_word_nikud
    #             "‫זִיקוּקִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "свадьба",
    #             # pronunciation_word
    #             "χatuna",
    #             # hebrew_word_nikud
    #             "‫חֲתוּנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жених",
    #             # pronunciation_word
    #             "χatan",
    #             # hebrew_word_nikud
    #             "‫חָתָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "невеста",
    #             # pronunciation_word
    #             "kala",
    #             # hebrew_word_nikud
    #             "‫הַזמָנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "приглашать",
    #             # pronunciation_word
    #             "lehazmin",
    #             # hebrew_word_nikud
    #             "‬‫לְהַזמִין‬"
    #         ),
    #         (
    #             # translation_word
    #             "приглашение (документ)",
    #             # pronunciation_word
    #             "hazmana",
    #             # hebrew_word_nikud
    #             "‫הַזמָנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гость",
    #             # pronunciation_word
    #             "o'reaχ",
    #             # hebrew_word_nikud
    #             "‫אוֹרֵח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "идти в гости",
    #             # pronunciation_word
    #             "levaker",
    #             # hebrew_word_nikud
    #             "‬‫לְבַקֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "встречать гостей",
    #             # pronunciation_word
    #             "lekabel orχim",
    #             # hebrew_word_nikud
    #             "לְקַבֵּל‬‬ ‫אוֹרחִים‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "подарок",
    #             # pronunciation_word
    #             "matana",
    #             # hebrew_word_nikud
    #             "‫מַתָנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дарить (подарок)",
    #             # pronunciation_word
    #             "latet matana",
    #             # hebrew_word_nikud
    #             "לָתֵת‬‬ ‫מַתָנָה‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "получать подарки",
    #             # pronunciation_word
    #             "lekabel matanot",
    #             # hebrew_word_nikud
    #             "לְקַבֵּל‬‬ ‫מַתָנוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "букет",
    #             # pronunciation_word
    #             "zer",
    #             # hebrew_word_nikud
    #             "‫זֵר‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "поздравление",
    #             # pronunciation_word
    #             "braχa",
    #             # hebrew_word_nikud
    #             "‫בּרָכָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поздравлять",
    #             # pronunciation_word
    #             "levareχ",
    #             # hebrew_word_nikud
    #             "‫לְבָרֵך‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "тост",
    #             # pronunciation_word
    #             "leharim kosit",
    #             # hebrew_word_nikud
    #             "לְהָרִים‬‬ ‫כוֹסִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "угощать",
    #             # pronunciation_word
    #             "leχabed",
    #             # hebrew_word_nikud
    #             "‫לְכַבֵּד‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "шампанское",
    #             # pronunciation_word
    #             "ʃam'panya",
    #             # hebrew_word_nikud
    #             "‫שַמפַּניָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "веселье",
    #             # pronunciation_word
    #             "aliʦut",
    #             # hebrew_word_nikud
    #             "‬‫עֲלִיצוּת‬"
    #         ),
    #          (
    #             # translation_word
    #             "радость",
    #             # pronunciation_word
    #             "simχa",
    #             # hebrew_word_nikud
    #             "‫שִׂמחָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "танец",
    #             # pronunciation_word
    #             "rikud",
    #             # hebrew_word_nikud
    #             "‫רִיקוּד‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "танцевать",
    #             # pronunciation_word
    #             "lirkod",
    #             # hebrew_word_nikud
    #             "‫לִרקוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "похороны",
    #             # pronunciation_word
    #             "levaya",
    #             # hebrew_word_nikud
    #             "‫לְווָיָה‬‬"
    #         ),
    #     ]
    # ),  
    # (
    #     # group_name_ru
    #     "158. Правитель. Шеф. Руководитель",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "король",
    #             # pronunciation_word
    #             "'meleχ",
    #             # hebrew_word_nikud
    #             "‫מֶלֶך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "королева",
    #             # pronunciation_word
    #             "malka",
    #             # hebrew_word_nikud
    #             "‫מַלכָּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "президент",
    #             # pronunciation_word
    #             "nasi",
    #             # hebrew_word_nikud
    #             "‫נָשִׂיא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сенатор",
    #             # pronunciation_word
    #             "se'nator",
    #             # hebrew_word_nikud
    #             "‫סֶנָאטוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "монарх",
    #             # pronunciation_word
    #             "'meleχ",
    #             # hebrew_word_nikud
    #             "‫מֶלֶך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "правитель",
    #             # pronunciation_word
    #             "ʃalit",
    #             # hebrew_word_nikud
    #             "‫שַלִיט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "диктатор",
    #             # pronunciation_word
    #             "rodan",
    #             # hebrew_word_nikud
    #             "‫רוֹדָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тиран",
    #             # pronunciation_word
    #             "aruʦ",
    #             # hebrew_word_nikud
    #             "‫עָרוּץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "директор",
    #             # pronunciation_word
    #             "menahel",
    #             # hebrew_word_nikud
    #             "‫מְנַהֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "босс",
    #             # pronunciation_word
    #             "bos",
    #             # hebrew_word_nikud
    #             "‫בּוֹס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "хозяин (владелец)",
    #             # pronunciation_word
    #             "'baʿal",
    #             # hebrew_word_nikud
    #             "‫בַּעַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "глава (~ делегации)",
    #             # pronunciation_word
    #             "roʃ",
    #             # hebrew_word_nikud
    #             "‫רֹאש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "начальство",
    #             # pronunciation_word
    #             "memunim",
    #             # hebrew_word_nikud
    #             "‫מְמוּנִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "губернатор",
    #             # pronunciation_word
    #             "moʃel",
    #             # hebrew_word_nikud
    #             "‫מוֹשֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "консул",
    #             # pronunciation_word
    #             "'konsul",
    #             # hebrew_word_nikud
    #             "‫קוֹנסוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дипломат",
    #             # pronunciation_word
    #             "diplomat",
    #             # hebrew_word_nikud
    #             "‫דִיפּלוֹמָט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мэр",
    #             # pronunciation_word
    #             "roʃ haʿir",
    #             # hebrew_word_nikud
    #             "רֹאש‬‬ ‫הָעִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "шериф",
    #             # pronunciation_word
    #             "ʃerif",
    #             # hebrew_word_nikud
    #             "‫שֶרִיף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "император",
    #             # pronunciation_word
    #             "keisar",
    #             # hebrew_word_nikud
    #             "‫קֵיסָר‬‬"
    #         ),
    #     ]
    # ),    
    # (
    #     # group_name_ru
    #     "159. Планета Земля",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Земля, земной шар",
    #             # pronunciation_word
    #             "kadur ha'ʾareʦ",
    #             # hebrew_word_nikud
    #             "כַּדוּר‬‬ ‫הָאָרֶץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "планета",
    #             # pronunciation_word
    #             "koχav 'leχet",
    #             # hebrew_word_nikud
    #             "‬כּוֹכַב‬‬ ‫לֶכֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "атмосфера",
    #             # pronunciation_word
    #             "atmos'fera",
    #             # hebrew_word_nikud
    #             "‫אַטמוֹספֶרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "география",
    #             # pronunciation_word
    #             "geʾo'grafya",
    #             # hebrew_word_nikud
    #             "‫גֵיאוֹגרַפיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "природа",
    #             # pronunciation_word
    #             "'teva",
    #             # hebrew_word_nikud
    #             "‫טֶבַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Европа",
    #             # pronunciation_word
    #             "ei'ropa",
    #             # hebrew_word_nikud
    #             "‫אֵירוֹפָּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Азия",
    #             # pronunciation_word
    #             "'asya",
    #             # hebrew_word_nikud
    #             "‫אַסיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Африка",
    #             # pronunciation_word
    #             "'afrika",
    #             # hebrew_word_nikud
    #             "‫אַפרִיקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Австралия",
    #             # pronunciation_word
    #             "ost'ralya",
    #             # hebrew_word_nikud
    #             "‫אוֹסטרַליָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Америка",
    #             # pronunciation_word
    #             "a'merika",
    #             # hebrew_word_nikud
    #             "‫אָמֶרִיקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Северная Америка",
    #             # pronunciation_word
    #             "a'merika haʦfonit",
    #             # hebrew_word_nikud
    #             "‬אָמֶרִיקָה‬‬ ‬‫הַצפוֹנִית‬"
    #         ),
    #         (
    #             # translation_word
    #             "Южная Америка",
    #             # pronunciation_word
    #             "a'merika hadromit",
    #             # hebrew_word_nikud
    #             "אָמֶרִיקָה‬‬‬ ‫הַדרוֹמִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Антарктида",
    #             # pronunciation_word
    #             "ya'beʃet an'tarktika",
    #             # hebrew_word_nikud
    #             "‬יַבֶּשֶת‬‬‬ ‫אַנטַארקטִיקָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "север",
    #             # pronunciation_word
    #             "ʦafon",
    #             # hebrew_word_nikud
    #             "‫צָפוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "юг",
    #             # pronunciation_word
    #             "darom",
    #             # hebrew_word_nikud
    #             "‬‫דָרוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "запад‬",
    #             # pronunciation_word
    #             "maʿarav",
    #             # hebrew_word_nikud
    #             "‫מַעֲרָב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "восток",
    #             # pronunciation_word
    #             "mizraχ",
    #             # hebrew_word_nikud
    #             "‬‫מִזרָח‬"
    #         ),
    #         (
    #             # translation_word
    #             "море",
    #             # pronunciation_word
    #             "yam",
    #             # hebrew_word_nikud
    #             "‫יָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "океан",
    #             # pronunciation_word
    #             "ok'yanos",
    #             # hebrew_word_nikud
    #             "‬‫אוֹקיָאנוֹס‬"
    #         ),
    #         (
    #             # translation_word
    #             "остров",
    #             # pronunciation_word
    #             "i",
    #             # hebrew_word_nikud
    #             "‫אִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полуостров",
    #             # pronunciation_word
    #             "χaʦi i",
    #             # hebrew_word_nikud
    #             "חֲצִי‬‬‬ ‫אִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "волна",
    #             # pronunciation_word
    #             "gal",
    #             # hebrew_word_nikud
    #             "‫גַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "экватор",
    #             # pronunciation_word
    #             "kav hamaʃve",
    #             # hebrew_word_nikud
    #             "קַו‬‬‬ ‫הַמַשווֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "горизонт",
    #             # pronunciation_word
    #             "'ofek",
    #             # hebrew_word_nikud
    #             "‬‫אוֹפֶק‬"
    #         ),
    #         (
    #             # translation_word
    #             "небо",
    #             # pronunciation_word
    #             "ʃa'mayim",
    #             # hebrew_word_nikud
    #             "‫שָמַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "воздух",
    #             # pronunciation_word
    #             "avir",
    #             # hebrew_word_nikud
    #             "‫אֲווִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гора",
    #             # pronunciation_word
    #             "har",
    #             # hebrew_word_nikud
    #             "‫הַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "река",
    #             # pronunciation_word
    #             "nahar",
    #             # hebrew_word_nikud
    #             "‫נָהָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лес",
    #             # pronunciation_word
    #             "'yaʿar",
    #             # hebrew_word_nikud
    #             "‫יַעַר‬‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "160. Погода",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "погода",
    #             # pronunciation_word
    #             "'mezeg avir",
    #             # hebrew_word_nikud
    #             "מֶזֶג‬‬‬ ‫אֲווִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "температура",
    #             # pronunciation_word
    #             "tempera'tura",
    #             # hebrew_word_nikud
    #             "‫טֶמפֶּרָטוּרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "влажный",
    #             # pronunciation_word
    #             "laχ",
    #             # hebrew_word_nikud
    #             "‫לַח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жара",
    #             # pronunciation_word
    #             "χom",
    #             # hebrew_word_nikud
    #             "‫חוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жаркий",
    #             # pronunciation_word
    #             "χam",
    #             # hebrew_word_nikud
    #             "‫חַם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тепло (о погоде)",
    #             # pronunciation_word
    #             "χamim",
    #             # hebrew_word_nikud
    #             "‫חָמִים‬‬"
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
    #             "холодно (о погоде)",
    #             # pronunciation_word
    #             "kar",
    #             # hebrew_word_nikud
    #             "‫קַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "солнце",
    #             # pronunciation_word
    #             "'ʃemeʃ",
    #             # hebrew_word_nikud
    #             "‫שֶמֶש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "облако",
    #             # pronunciation_word
    #             "anan",
    #             # hebrew_word_nikud
    #             "‬‫עָנָן‬"
    #         ),
    #         (
    #             # translation_word
    #             "дождь",
    #             # pronunciation_word
    #             "'geʃem",
    #             # hebrew_word_nikud
    #             "‫גֶשֶם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ливень",
    #             # pronunciation_word
    #             "mabul",
    #             # hebrew_word_nikud
    #             "‫מַבּוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "туман",
    #             # pronunciation_word
    #             "arafel",
    #             # hebrew_word_nikud
    #             "‫עֲרָפֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "снег",
    #             # pronunciation_word
    #             "'ʃeleg",
    #             # hebrew_word_nikud
    #             "‫שֶלֶג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гроза",
    #             # pronunciation_word
    #             "sufat reʿamim",
    #             # hebrew_word_nikud
    #             "סוּפַת‬‬‬ ‫רְעָמִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "молния",
    #             # pronunciation_word
    #             "barak",
    #             # hebrew_word_nikud
    #             "‫בָּרָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гром",
    #             # pronunciation_word
    #             "'raʿam",
    #             # hebrew_word_nikud
    #             "‬‫רַעַם‬"
    #         ),
    #         (
    #             # translation_word
    #             "град",
    #             # pronunciation_word
    #             "barad",
    #             # hebrew_word_nikud
    #             "‫בָּרָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ураган",
    #             # pronunciation_word
    #             "hurikan",
    #             # hebrew_word_nikud
    #             "‫הוּרִיקָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пожар",
    #             # pronunciation_word
    #             "srefa",
    #             # hebrew_word_nikud
    #             "‬‫שׂרֵיפָה‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "161. Дикие животные",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "животное",
    #             # pronunciation_word
    #             "'baʿal χayim",
    #             # hebrew_word_nikud
    #             "בַּעַל‬‬‬ ‫חַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "хищник",
    #             # pronunciation_word
    #             "χayat 'teref",
    #             # hebrew_word_nikud
    #             "‬חַייַת‬‬‬ ‫טֶרֶף‬"
    #         ),
    #         (
    #             # translation_word
    #             "белка",
    #             # pronunciation_word
    #             "snaʾi",
    #             # hebrew_word_nikud
    #             "‫סנָאִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кролик",
    #             # pronunciation_word
    #             "ʃafan",
    #             # hebrew_word_nikud
    #             "‫שָפָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мышь",
    #             # pronunciation_word
    #             "aχbar",
    #             # hebrew_word_nikud
    #             "‫עַכבָּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лошадь",
    #             # pronunciation_word
    #             "sus",
    #             # hebrew_word_nikud
    #             "‫סוּס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "медведь",
    #             # pronunciation_word
    #             "dov",
    #             # hebrew_word_nikud
    #             "‫דוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "панда",
    #             # pronunciation_word
    #             "'panda",
    #             # hebrew_word_nikud
    #             "‫פַּנדָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кот",
    #             # pronunciation_word
    #             "χatul",
    #             # hebrew_word_nikud
    #             "‫חָתוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "собака",
    #             # pronunciation_word
    #             "'kelev",
    #             # hebrew_word_nikud
    #             "‫כֶּלֶב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "домашние животные",
    #             # pronunciation_word
    #             "χayot 'bayit",
    #             # hebrew_word_nikud
    #             "חַיוֹת‬‬‬ ‫בַּיִת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "змея",
    #             # pronunciation_word
    #             "naχaʃ",
    #             # hebrew_word_nikud
    #             "‬‫נָחָש‬"
    #         ),
    #         (
    #             # translation_word
    #             "ящерица",
    #             # pronunciation_word
    #             "letaʾa",
    #             # hebrew_word_nikud
    #             "‫לְטָאָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скорпион",
    #             # pronunciation_word
    #             "akrav",
    #             # hebrew_word_nikud
    #             "‫עַקרָב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "насекомое",
    #             # pronunciation_word
    #             "χarak",
    #             # hebrew_word_nikud
    #             "‫חָרָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бабочка",
    #             # pronunciation_word
    #             "parpar",
    #             # hebrew_word_nikud
    #             "‫פַּרפַּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пчела",
    #             # pronunciation_word
    #             "dvora",
    #             # hebrew_word_nikud
    #             "‫דבוֹרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "паук",
    #             # pronunciation_word
    #             "akaviʃ",
    #             # hebrew_word_nikud
    #             "‫עַכָּבִיש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "таракан",
    #             # pronunciation_word
    #             "makak",
    #             # hebrew_word_nikud
    #             "‫מַקָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зоопарк",
    #             # pronunciation_word
    #             "gan hayot",
    #             # hebrew_word_nikud
    #             "גַן‬‬‬ ‫חַיוֹת‬‬"
    #         ),
    #     ]
    # ),  
    # (
    #     # group_name_ru
    #     "162. Растения",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "дерево",
    #             # pronunciation_word
    #             "eʦ",
    #             # hebrew_word_nikud
    #             "‫עֵץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кустарник",
    #             # pronunciation_word
    #             "'siaχ",
    #             # hebrew_word_nikud
    #             "‫שִׂיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гриб",
    #             # pronunciation_word
    #             "pitriya",
    #             # hebrew_word_nikud
    #             "‫פִּטרִייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "фрукт, плод",
    #             # pronunciation_word
    #             "pri",
    #             # hebrew_word_nikud
    #             "‫פּרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "яблоко",
    #             # pronunciation_word
    #             "ta'puaχ",
    #             # hebrew_word_nikud
    #             "‫תַפּוּח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "груша",
    #             # pronunciation_word
    #             "agas",
    #             # hebrew_word_nikud
    #             "‬‫אַגָס‬"
    #         ),
    #         (
    #             # translation_word
    #             "клубника",
    #             # pronunciation_word
    #             "tut",
    #             # hebrew_word_nikud
    #             "‫תוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вишня",
    #             # pronunciation_word
    #             "duvdevan",
    #             # hebrew_word_nikud
    #             "‫דוּבדְבָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "виноград",
    #             # pronunciation_word
    #             "anavim",
    #             # hebrew_word_nikud
    #             "‬‫עֲנָבִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "малина",
    #             # pronunciation_word
    #             "'petel",
    #             # hebrew_word_nikud
    #             "‬‫פֶּטֶל‬"
    #         ),
    #         (
    #             # translation_word
    #             "апельсин",
    #             # pronunciation_word
    #             "tapuz",
    #             # hebrew_word_nikud
    #             "‫תַפּוּז‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мандарин",
    #             # pronunciation_word
    #             "klemen'tina",
    #             # hebrew_word_nikud
    #             "‬‫קלֶמֶנטִינָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "ананас",
    #             # pronunciation_word
    #             "'ananas",
    #             # hebrew_word_nikud
    #             "‫אָנָנָס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "банан",
    #             # pronunciation_word
    #             "ba'nana",
    #             # hebrew_word_nikud
    #             "‫בַּנָנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "финик",
    #             # pronunciation_word
    #             "tamar",
    #             # hebrew_word_nikud
    #             "‫תָמָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лимон",
    #             # pronunciation_word
    #             "limon",
    #             # hebrew_word_nikud
    #             "‫לִימוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "абрикос",
    #             # pronunciation_word
    #             "'miʃmeʃ",
    #             # hebrew_word_nikud
    #             "‫מִשמֵש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "персик",
    #             # pronunciation_word
    #             "afarsek",
    #             # hebrew_word_nikud
    #             "‫אֲפַרסֵק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "киви",
    #             # pronunciation_word
    #             "'kivi",
    #             # hebrew_word_nikud
    #             "‫קִיווִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "грейпфрут",
    #             # pronunciation_word
    #             "eʃkolit",
    #             # hebrew_word_nikud
    #             "‫אֶשכּוֹלִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ягоды",
    #             # pronunciation_word
    #             "gargerim",
    #             # hebrew_word_nikud
    #             "‫גַרגֵרִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "цветок",
    #             # pronunciation_word
    #             "'peraχ",
    #             # hebrew_word_nikud
    #             "‫פֶּרַח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пшеница",
    #             # pronunciation_word
    #             "χita",
    #             # hebrew_word_nikud
    #             "‬‫חִיטָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "рожь",
    #             # pronunciation_word
    #             "ʃifon",
    #             # hebrew_word_nikud
    #             "‫שִיפוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "овёс",
    #             # pronunciation_word
    #             "ʃi'bolet ʃuʿal",
    #             # hebrew_word_nikud
    #             "שִיבּוֹלֶת‬‬‬ ‫שוּעָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ячмень",
    #             # pronunciation_word
    #             "seʿora",
    #             # hebrew_word_nikud
    #             "‫שְׂעוֹרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кукуруза",
    #             # pronunciation_word
    #             "'tiras",
    #             # hebrew_word_nikud
    #             "‫תִירָס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рис",
    #             # pronunciation_word
    #             "'orez",
    #             # hebrew_word_nikud
    #             "‫אוֹרֶז‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "овощи",
    #             # pronunciation_word
    #             "yerakot",
    #             # hebrew_word_nikud
    #             "‬‫יְרָקוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "зелень",
    #             # pronunciation_word
    #             "'yerek",
    #             # hebrew_word_nikud
    #             "‫יֶרֶק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "помидор",
    #             # pronunciation_word
    #             "agvaniya",
    #             # hebrew_word_nikud
    #             "‫עַגבָנִייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "огурец",
    #             # pronunciation_word
    #             "melafefon",
    #             # hebrew_word_nikud
    #             "‫מְלָפְפוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "морковь",
    #             # pronunciation_word
    #             "'gezer",
    #             # hebrew_word_nikud
    #             "‫גֶזֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "картофель",
    #             # pronunciation_word
    #             "ta'puaχ adama",
    #             # hebrew_word_nikud
    #             "תַפּוּח‬‬‬ ‫אֲדָמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лук",
    #             # pronunciation_word
    #             "baʦal",
    #             # hebrew_word_nikud
    #             "‫בָּצָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чеснок",
    #             # pronunciation_word
    #             "ʃum",
    #             # hebrew_word_nikud
    #             "‫שוּם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "капуста",
    #             # pronunciation_word
    #             "kruv",
    #             # hebrew_word_nikud
    #             "‫כּרוּב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "свёкла",
    #             # pronunciation_word
    #             "'selek",
    #             # hebrew_word_nikud
    #             "‫סֶלֶק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "баклажан",
    #             # pronunciation_word
    #             "χaʦil",
    #             # hebrew_word_nikud
    #             "‫חָצִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тыква",
    #             # pronunciation_word
    #             "'dlaʿat",
    #             # hebrew_word_nikud
    #             "‬‫דלַעַת‬"
    #         ),
    #         (
    #             # translation_word
    #             "шпинат",
    #             # pronunciation_word
    #             "'tered",
    #             # hebrew_word_nikud
    #             "‫תֶרֶד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "перец",
    #             # pronunciation_word
    #             "'pilpel",
    #             # hebrew_word_nikud
    #             "‫פִּלפֵּל‬‬"
    #         ),
    #     ]
    # ),   
    # (
    #     # group_name_ru
    #     "163. Страны, национальности",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Австрия",
    #             # pronunciation_word
    #             "'ostriya",
    #             # hebrew_word_nikud
    #             "‫אוֹסטרִיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Соединённые Штаты Америки",
    #             # pronunciation_word
    #             "arʦot habrit",
    #             # hebrew_word_nikud
    #             "אַרצוֹת‬‬‬ ‫הַבּרִית‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Великобритания",
    #             # pronunciation_word
    #             "bri'tanya hagdola",
    #             # hebrew_word_nikud
    #             "בּרִיטַניָה‬‬‬ ָ‫הַגדוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Канада",
    #             # pronunciation_word
    #             "'kanada",
    #             # hebrew_word_nikud
    #             "‫קָנָדָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Бельгия",
    #             # pronunciation_word
    #             "'belgya",
    #             # hebrew_word_nikud
    #             "‫בֶּלגיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Аргентина",
    #             # pronunciation_word
    #             "argen'tina",
    #             # hebrew_word_nikud
    #             "‫אַרגֶנטִינָה‬‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Германия",
    #             # pronunciation_word
    #             "ger'manya",
    #             # hebrew_word_nikud
    #             "‫גֶרמַניָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Бразилия",
    #             # pronunciation_word
    #             "brazil",
    #             # hebrew_word_nikud
    #             "‫בּרָזִיל‬"
    #         ),
    #         (
    #             # translation_word
    #             "Нидерланды",
    #             # pronunciation_word
    #             "'holand",
    #             # hebrew_word_nikud
    #             "‫הוֹלַנד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Египет",
    #             # pronunciation_word
    #             "miʦ'rayim",
    #             # hebrew_word_nikud
    #             "‫מִצרַיִם‬"
    #         ),
    #         (
    #             # translation_word
    #             "Греция",
    #             # pronunciation_word
    #             "yavan",
    #             # hebrew_word_nikud
    #             "‫יָווָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Австралия",
    #             # pronunciation_word
    #             "ost'ralya",
    #             # hebrew_word_nikud
    #             "‫אוֹסטרַליָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Дания",
    #             # pronunciation_word
    #             "'denemark",
    #             # hebrew_word_nikud
    #             "‫דֶנֶמַרק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Ирландия",
    #             # pronunciation_word
    #             "'irland",
    #             # hebrew_word_nikud
    #             "‬‫אִירלַנד‬"
    #         ),
    #         (
    #             # translation_word
    #             "Испания",
    #             # pronunciation_word
    #             "sfarad",
    #             # hebrew_word_nikud
    #             "‫ספָרַד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Италия",
    #             # pronunciation_word
    #             "i'talya",
    #             # hebrew_word_nikud
    #             "‫אִיטַליָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Норвегия",
    #             # pronunciation_word
    #             "nor'vegya",
    #             # hebrew_word_nikud
    #             "‫נוֹרבֶגיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Португалия",
    #             # pronunciation_word
    #             "portugal",
    #             # hebrew_word_nikud
    #             "‫פּוֹרטוּגָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Франция",
    #             # pronunciation_word
    #             "ʦarfat",
    #             # hebrew_word_nikud
    #             "‫צָרפַת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Швеция",
    #             # pronunciation_word
    #             "'ʃvedya",
    #             # hebrew_word_nikud
    #             "‫שבֶדיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Болгария",
    #             # pronunciation_word
    #             "bul'garya",
    #             # hebrew_word_nikud
    #             "‫בּוּלגַריָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Литва",
    #             # pronunciation_word
    #             "'lita",
    #             # hebrew_word_nikud
    #             "‫לִיטָא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Польша",
    #             # pronunciation_word
    #             "polin",
    #             # hebrew_word_nikud
    #             "‫פּוֹלִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Чехия",
    #             # pronunciation_word
    #             "'ʧeχya",
    #             # hebrew_word_nikud
    #             "‫צֶ׳כיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Беларусь",
    #             # pronunciation_word
    #             "'belarus",
    #             # hebrew_word_nikud
    #             "‫בֶּלָרוּס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Россия",
    #             # pronunciation_word
    #             "'rusya",
    #             # hebrew_word_nikud
    #             "‫רוּסיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Украина",
    #             # pronunciation_word
    #             "uk'rayna",
    #             # hebrew_word_nikud
    #             "‫אוּקרַאינָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Израиль",
    #             # pronunciation_word
    #             "yisraʾel",
    #             # hebrew_word_nikud
    #             "‬‫יִשׂרָאֵל‬"
    #         ),
    #         (
    #             # translation_word
    #             "еврей",
    #             # pronunciation_word
    #             "yehudi",
    #             # hebrew_word_nikud
    #             "‫יְהוּדִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "еврейка",
    #             # pronunciation_word
    #             "yehudiya",
    #             # hebrew_word_nikud
    #             "‫יְהוּדִיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Китай",
    #             # pronunciation_word
    #             "sin",
    #             # hebrew_word_nikud
    #             "‫סִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Турция",
    #             # pronunciation_word
    #             "'turkiya",
    #             # hebrew_word_nikud
    #             "‫טוּרקִיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Япония",
    #             # pronunciation_word
    #             "yapan",
    #             # hebrew_word_nikud
    #             "‫יַפָּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Палестина",
    #             # pronunciation_word
    #             "falastin",
    #             # hebrew_word_nikud
    #             "‫פָלַסטִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "израильтянин",
    #             # pronunciation_word
    #             "yisraʾeli",
    #             # hebrew_word_nikud
    #             "‫יִשׂרְאֵלִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "израильтянка",
    #             # pronunciation_word
    #             "yisraʾelit",
    #             # hebrew_word_nikud
    #             "‫יִשׂרְאֵלִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "израильский",
    #             # pronunciation_word
    #             "yisraʾeli",
    #             # hebrew_word_nikud
    #             "‫יִשׂרְאֵלִי‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "164. Страны. Разное",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "иностранец, иностранный",
    #             # pronunciation_word
    #             "zar",
    #             # hebrew_word_nikud
    #             "‬‫זָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "за границей",
    #             # pronunciation_word
    #             "beχul",
    #             # hebrew_word_nikud
    #             "‫בְּחוּ"ל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "эмигрант",
    #             # pronunciation_word
    #             "mehager",
    #             # hebrew_word_nikud
    #             "‬‫מְהַגֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "эмиграция",
    #             # pronunciation_word
    #             "hagira",
    #             # hebrew_word_nikud
    #             "‬‫הֲגִירָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "эмигрировать",
    #             # pronunciation_word
    #             "lehager",
    #             # hebrew_word_nikud
    #             "‫לְהַגֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мир (вся планета)",
    #             # pronunciation_word
    #             "olam",
    #             # hebrew_word_nikud
    #             "‫עוֹלָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "человечество",
    #             # pronunciation_word
    #             "enoʃut",
    #             # hebrew_word_nikud
    #             "‬‫אֱנוֹשוּת‬"
    #         ),
    #         (
    #             # translation_word
    #             "родина",
    #             # pronunciation_word
    #             "mo'ledet",
    #             # hebrew_word_nikud
    #             "‬‫מוֹלֶדֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "население",
    #             # pronunciation_word
    #             "oχlusiya",
    #             # hebrew_word_nikud
    #             "‫אוֹכלוּסִיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нация",
    #             # pronunciation_word
    #             "uma",
    #             # hebrew_word_nikud
    #             "‫אוּמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поколение",
    #             # pronunciation_word
    #             "dor",
    #             # hebrew_word_nikud
    #             "‫דוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "территория",
    #             # pronunciation_word
    #             "'ʃetaχ",
    #             # hebrew_word_nikud
    #             "‬‫שֶטַח‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "165. Мировые религии. Конфессии",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "религия",
    #             # pronunciation_word
    #             "dat",
    #             # hebrew_word_nikud
    #             "‫דָת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "религиозный",
    #             # pronunciation_word
    #             "dati",
    #             # hebrew_word_nikud
    #             "‫דָתִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "верующий (сущ.)",
    #             # pronunciation_word
    #             "maʾamin",
    #             # hebrew_word_nikud
    #             "‫מַאֲמִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "атеизм",
    #             # pronunciation_word
    #             "ateʾizm",
    #             # hebrew_word_nikud
    #             "‫אָתֵאִיזם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "атеист",
    #             # pronunciation_word
    #             "ateʾist",
    #             # hebrew_word_nikud
    #             "‫אָתֵאִיסט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Христианство",
    #             # pronunciation_word
    #             "naʦrut",
    #             # hebrew_word_nikud
    #             "‫נַצרוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "христианин",
    #             # pronunciation_word
    #             "noʦri",
    #             # hebrew_word_nikud
    #             "‫נוֹצרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Католицизм",
    #             # pronunciation_word
    #             "kaʿtoliyut",
    #             # hebrew_word_nikud
    #             "‫נוֹצרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Протестантство",
    #             # pronunciation_word
    #             "protes'tantiyut",
    #             # hebrew_word_nikud
    #             "‫פּרוֹטֶסטַנטִיוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Православие",
    #             # pronunciation_word
    #             "naʦrut orto'doksit",
    #             # hebrew_word_nikud
    #             "נַצרוּת‬‬‬ ‫אוֹרתוֹדוֹקסִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Иудаизм",
    #             # pronunciation_word
    #             "yahadut",
    #             # hebrew_word_nikud
    #             "‫יַהדוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "иудей",
    #             # pronunciation_word
    #             "yehudi, yehudiya",
    #             # hebrew_word_nikud
    #             " ‫יְהוּדִיָה‬, ‫יְהוּדִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Ислам",
    #             # pronunciation_word
    #             "islam",
    #             # hebrew_word_nikud
    #             "‫אִיסלָאם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Бог",
    #             # pronunciation_word
    #             "elohim",
    #             # hebrew_word_nikud
    #             "‫אֱלוֹהִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "грех",
    #             # pronunciation_word
    #             "χet",
    #             # hebrew_word_nikud
    #             "‫חֵטא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ад",
    #             # pronunciation_word
    #             "gehinom",
    #             # hebrew_word_nikud
    #             "‫גֵיהִינוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рай",
    #             # pronunciation_word
    #             "gan 'eden",
    #             # hebrew_word_nikud
    #             "גַן‬‬‬ ‫עֵדֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ангел",
    #             # pronunciation_word
    #             "malʾaχ",
    #             # hebrew_word_nikud
    #             "‫מַלאָך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Церковь",
    #             # pronunciation_word
    #             "knesiya",
    #             # hebrew_word_nikud
    #             "‫כּנֵסִייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "библия",
    #             # pronunciation_word
    #             "tanaχ",
    #             # hebrew_word_nikud
    #             "‫תַנַ"ך‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "166. Общие существительные",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "база (основа)",
    #             # pronunciation_word
    #             "basis",
    #             # hebrew_word_nikud
    #             "‫בָּסִיס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "баланс",
    #             # pronunciation_word
    #             "izun",
    #             # hebrew_word_nikud
    #             "‫אִיזוּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вещь",
    #             # pronunciation_word
    #             "'χefeʦ",
    #             # hebrew_word_nikud
    #             "‬‫חֶפֶץ‬"
    #         ),
    #         (
    #             # translation_word
    #             "выбор (ассортимент)",
    #             # pronunciation_word
    #             "bχina",
    #             # hebrew_word_nikud
    #             "‫בּחִינָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "идеал",
    #             # pronunciation_word
    #             "ideʾal",
    #             # hebrew_word_nikud
    #             "‫אִידֵיאָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "момент",
    #             # pronunciation_word
    #             "'rega",
    #             # hebrew_word_nikud
    #             "‬‫רֶגַע‬"
    #         ),
    #         (
    #             # translation_word
    #             "начало",
    #             # pronunciation_word
    #             "hatχala",
    #             # hebrew_word_nikud
    #             "‫הַתחָלָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "объект (предмет)",
    #             # pronunciation_word
    #             "'eʦem",
    #             # hebrew_word_nikud
    #             "‬‫עֶצֶם‬"
    #         ),
    #         (
    #             # translation_word
    #             "окончание (конец)",
    #             # pronunciation_word
    #             "sof",
    #             # hebrew_word_nikud
    #             "‫סוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "остановка (перерыв)",
    #             # pronunciation_word
    #             "hafsaka",
    #             # hebrew_word_nikud
    #             "‫הַפסָקָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "очередь (сейчас моя ~)",
    #             # pronunciation_word
    #             "tor",
    #             # hebrew_word_nikud
    #             "‫תוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ошибка",
    #             # pronunciation_word
    #             "taʿut",
    #             # hebrew_word_nikud
    #             "‫טָעוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пауза",
    #             # pronunciation_word
    #             "hafuga",
    #             # hebrew_word_nikud
    #             "‫הֲפוּגָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "польза",
    #             # pronunciation_word
    #             "to'ʿelet",
    #             # hebrew_word_nikud
    #             "‬‫תוֹעֶלֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "помощь",
    #             # pronunciation_word
    #             "ezra",
    #             # hebrew_word_nikud
    #             "‫עֶזרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "препятствие",
    #             # pronunciation_word
    #             "maχsom",
    #             # hebrew_word_nikud
    #             "‫מַחסוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пример",
    #             # pronunciation_word
    #             "dugma",
    #             # hebrew_word_nikud
    #             "‫דוּגמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "принцип",
    #             # pronunciation_word
    #             "ikaron",
    #             # hebrew_word_nikud
    #             "‫עִיקָרוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "причина",
    #             # pronunciation_word
    #             "siba",
    #             # hebrew_word_nikud
    #             "‫סִיבָּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "проблема",
    #             # pronunciation_word
    #             "beʿaya",
    #             # hebrew_word_nikud
    #             "‫בְּעָיָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "процесс",
    #             # pronunciation_word
    #             "tahaliχ",
    #             # hebrew_word_nikud
    #             "‫תַהֲלִיך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "развитие",
    #             # pronunciation_word
    #             "hitpatχut",
    #             # hebrew_word_nikud
    #             "‫הִתפַּתחוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "различие",
    #             # pronunciation_word
    #             "'ʃoni",
    #             # hebrew_word_nikud
    #             "‫שוֹנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "реакция",
    #             # pronunciation_word
    #             "tguva",
    #             # hebrew_word_nikud
    #             "‫תגוּבָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "решение (задачи)",
    #             # pronunciation_word
    #             "pitaron",
    #             # hebrew_word_nikud
    #             "‫פִּיתָרוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "риск",
    #             # pronunciation_word
    #             "sikun",
    #             # hebrew_word_nikud
    #             "‫סִיכּוּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рост (процесс)",
    #             # pronunciation_word
    #             "gidul",
    #             # hebrew_word_nikud
    #             "‬‫גִידוּל‬"
    #         ),
    #         (
    #             # translation_word
    #             "система",
    #             # pronunciation_word
    #             "ʃita",
    #             # hebrew_word_nikud
    #             "‫שִיטָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ситуация",
    #             # pronunciation_word
    #             "maʦav",
    #             # hebrew_word_nikud
    #             "‫מַצָב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "совпадение",
    #             # pronunciation_word
    #             "hatʾama",
    #             # hebrew_word_nikud
    #             "‫הַתאָמָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "способ",
    #             # pronunciation_word
    #             "'ofen",
    #             # hebrew_word_nikud
    #             "‬‫אוֹפֵן‬"
    #         ),
    #         (
    #             # translation_word
    #             "сравнение",
    #             # pronunciation_word
    #             "haʃvaʾa",
    #             # hebrew_word_nikud
    #             "‬‫הַשווָאָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "срочно",
    #             # pronunciation_word
    #             "bidχifut",
    #             # hebrew_word_nikud
    #             "‫בִּדחִיפוּת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "срочный",
    #             # pronunciation_word
    #             "daχuf",
    #             # hebrew_word_nikud
    #             "‫דָחוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стандарт",
    #             # pronunciation_word
    #             "'teken",
    #             # hebrew_word_nikud
    #             "‬‫תֶקֶן‬"
    #         ),
    #         (
    #             # translation_word
    #             "степень",
    #             # pronunciation_word
    #             "darga",
    #             # hebrew_word_nikud
    #             "‫דַרגָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стиль",
    #             # pronunciation_word
    #             "signon",
    #             # hebrew_word_nikud
    #             "‫סִגנוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тайна, секрет",
    #             # pronunciation_word
    #             "sod",
    #             # hebrew_word_nikud
    #             "‫סוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "усилие",
    #             # pronunciation_word
    #             "maʾamaʦ",
    #             # hebrew_word_nikud
    #             "‫מַאֲמָץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "факт",
    #             # pronunciation_word
    #             "uvda",
    #             # hebrew_word_nikud
    #             "‬‫עוּבדָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "часть (целого)",
    #             # pronunciation_word
    #             "'χelek",
    #             # hebrew_word_nikud
    #             "‫חֶלֶק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "элемент",
    #             # pronunciation_word
    #             "element",
    #             # hebrew_word_nikud
    #             "‫אֶלֶמֶנט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "эффект",
    #             # pronunciation_word
    #             "efekt",
    #             # hebrew_word_nikud
    #             "‫אֶפֶקט‬‬"
    #         ),
    #     ]
    # ),    
    # (
    #     # group_name_ru
    #     "167. Прилагательные 1",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "аккуратный",
    #             # pronunciation_word
    #             "kapdani",
    #             # hebrew_word_nikud
    #             "‫קַפּדָנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бедный",
    #             # pronunciation_word
    #             "ani",
    #             # hebrew_word_nikud
    #             "‬‫עָנִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "безопасный",
    #             # pronunciation_word
    #             "ba'tuaχ",
    #             # hebrew_word_nikud
    #             "‫בָּטוּח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бесплатный",
    #             # pronunciation_word
    #             "χinam",
    #             # hebrew_word_nikud
    #             "‫חִינָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "благодарный",
    #             # pronunciation_word
    #             "asir toda",
    #             # hebrew_word_nikud
    #             "אֲסִיר‬‬‬ ‫תוֹדָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "близкий",
    #             # pronunciation_word
    #             "karov",
    #             # hebrew_word_nikud
    #             "‫קָרוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "больной",
    #             # pronunciation_word
    #             "χole",
    #             # hebrew_word_nikud
    #             "‫חוֹלֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "большой",
    #             # pronunciation_word
    #             "gadol",
    #             # hebrew_word_nikud
    #             "‫גָדוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "быстрый",
    #             # pronunciation_word
    #             "mahir",
    #             # hebrew_word_nikud
    #             "‫מָהִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "важный",
    #             # pronunciation_word
    #             "χaʃuv",
    #             # hebrew_word_nikud
    #             "‫חָשוּב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вежливый",
    #             # pronunciation_word
    #             "menumas",
    #             # hebrew_word_nikud
    #             "‫מְנוּמָס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "весёлый",
    #             # pronunciation_word
    #             "sa'meaχ",
    #             # hebrew_word_nikud
    #             "‬‫שָׂמֵח‬"
    #         ),
    #         (
    #             # translation_word
    #             "вкусный",
    #             # pronunciation_word
    #             "taʿim",
    #             # hebrew_word_nikud
    #             "‫טָעִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "влажный",
    #             # pronunciation_word
    #             "laχ",
    #             # hebrew_word_nikud
    #             "‫לַח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "возможный",
    #             # pronunciation_word
    #             "efʃari",
    #             # hebrew_word_nikud
    #             "‫אֶפשָרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "внешний",
    #             # pronunciation_word
    #             "χiʦoni",
    #             # hebrew_word_nikud
    #             "‫חִיצוֹנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "внутренний",
    #             # pronunciation_word
    #             "pnimi",
    #             # hebrew_word_nikud
    #             "‫פּנִימִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "враждебный",
    #             # pronunciation_word
    #             "oyen",
    #             # hebrew_word_nikud
    #             "‫עוֹיֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "высший",
    #             # pronunciation_word
    #             "haga'voha beyoter",
    #             # hebrew_word_nikud
    #             "הַגָבוֹה‬‬‬ ‫בְּיוֹתֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "главный",
    #             # pronunciation_word
    #             "raʃi",
    #             # hebrew_word_nikud
    #             "‫רָאשִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гладкий",
    #             # pronunciation_word
    #             "χalak",
    #             # hebrew_word_nikud
    #             "‫חָלָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "глупый",
    #             # pronunciation_word
    #             "tipeʃ",
    #             # hebrew_word_nikud
    #             "‬‫טִיפֵּש‬"
    #         ),
    #         (
    #             # translation_word
    #             "голодный",
    #             # pronunciation_word
    #             "raʿev",
    #             # hebrew_word_nikud
    #             "‫רָעֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "горький",
    #             # pronunciation_word
    #             "marir",
    #             # hebrew_word_nikud
    #             "‬‫מָרִיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "горячий",
    #             # pronunciation_word
    #             "χam",
    #             # hebrew_word_nikud
    #             "‬‫חַם‬"
    #         ),
    #         (
    #             # translation_word
    #             "громкий",
    #             # pronunciation_word
    #             "ram",
    #             # hebrew_word_nikud
    #             "‫רָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "грустный",
    #             # pronunciation_word
    #             "aʦuv",
    #             # hebrew_word_nikud
    #             "‫עָצוּב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "грязный",
    #             # pronunciation_word
    #             "meluχlaχ",
    #             # hebrew_word_nikud
    #             "‫מְלוּכלָך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "густой",
    #             # pronunciation_word
    #             "samuχ",
    #             # hebrew_word_nikud
    #             "‫סָמוּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дальний",
    #             # pronunciation_word
    #             "raχok",
    #             # hebrew_word_nikud
    #             "‫רָחוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "детский",
    #             # pronunciation_word
    #             "yaldi",
    #             # hebrew_word_nikud
    #             "‫יַלדִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "длинный",
    #             # pronunciation_word
    #             "aroχ",
    #             # hebrew_word_nikud
    #             "‫אָרוֹך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "добрый",
    #             # pronunciation_word
    #             "tov",
    #             # hebrew_word_nikud
    #             "‬‫טוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "довольный",
    #             # pronunciation_word
    #             "meruʦe",
    #             # hebrew_word_nikud
    #             "‫מְרוּצָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "дорогой",
    #             # pronunciation_word
    #             "yakar",
    #             # hebrew_word_nikud
    #             "‫יָקָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жидкий",
    #             # pronunciation_word
    #             "nozli",
    #             # hebrew_word_nikud
    #             "‫נוֹזלִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жирный (о пище)",
    #             # pronunciation_word
    #             "ʃamen",
    #             # hebrew_word_nikud
    #             "‫שָמֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "заботливый",
    #             # pronunciation_word
    #             "doʾeg",
    #             # hebrew_word_nikud
    #             "‫דָוֹאֵג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "загорелый",
    #             # pronunciation_word
    #             "ʃazuf",
    #             # hebrew_word_nikud
    #             "‫שָזוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "законный",
    #             # pronunciation_word
    #             "χuki",
    #             # hebrew_word_nikud
    #             "‫חוּקִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "закрытый",
    #             # pronunciation_word
    #             "sagur",
    #             # hebrew_word_nikud
    #             "‫סָגוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "замороженный (продукт)",
    #             # pronunciation_word
    #             "kafu",
    #             # hebrew_word_nikud
    #             "‫קָפוּא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "искусственный",
    #             # pronunciation_word
    #             "melaχuti",
    #             # hebrew_word_nikud
    #             "‫מְלָאכוּתִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кислый",
    #             # pronunciation_word
    #             "χamuʦ",
    #             # hebrew_word_nikud
    #             "‫חָמוּץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "короткий",
    #             # pronunciation_word
    #             "kaʦar",
    #             # hebrew_word_nikud
    #             "‫קָצַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "красивый",
    #             # pronunciation_word
    #             "yafe",
    #             # hebrew_word_nikud
    #             "‫יָפֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "левый",
    #             # pronunciation_word
    #             "smali",
    #             # hebrew_word_nikud
    #             "‫שׂמָאלִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "правый",
    #             # pronunciation_word
    #             "yemani",
    #             # hebrew_word_nikud
    #             "‫יְמָנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лёгкий (и о грузе и простой)",
    #             # pronunciation_word
    #             "kal",
    #             # hebrew_word_nikud
    #             "‫קַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "маленький,",
    #             # pronunciation_word
    #             "katan",
    #             # hebrew_word_nikud
    #             "‫קָטַן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мёртвый",
    #             # pronunciation_word
    #             "met",
    #             # hebrew_word_nikud
    #             "‫מֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "милый (любезный)",
    #             # pronunciation_word
    #             "neχmad",
    #             # hebrew_word_nikud
    #             "‫נֶחמָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мокрый (промокший)",
    #             # pronunciation_word
    #             "ratuv",
    #             # hebrew_word_nikud
    #             "‬‫רָטוּב‬"
    #         ),
    #         (
    #             # translation_word
    #             "молодой",
    #             # pronunciation_word
    #             "ʦaʿir",
    #             # hebrew_word_nikud
    #             "‬‫צָעִיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "мягкий",
    #             # pronunciation_word
    #             "raχ",
    #             # hebrew_word_nikud
    #             "‫רַך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "настоящий (момент)",
    #             # pronunciation_word
    #             "noχeχi",
    #             # hebrew_word_nikud
    #             "‫נוֹכְחִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "невозможный",
    #             # pronunciation_word
    #             "'bilti efʃari",
    #             # hebrew_word_nikud
    #             "בִּלתִי‬‬‬ ‫אֶפשָרִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "нежный (о человеке)",
    #             # pronunciation_word
    #             "raχ",
    #             # hebrew_word_nikud
    #             "‫רַך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "необходимый",
    #             # pronunciation_word
    #             "naχuʦ",
    #             # hebrew_word_nikud
    #             "‫נָחוּץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "непонятный (~ текст)",
    #             # pronunciation_word
    #             "'bilti muvan",
    #             # hebrew_word_nikud
    #             "בִּלתִי‬‬‬ ‫מוּבָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нервный",
    #             # pronunciation_word
    #             "aʦbani",
    #             # hebrew_word_nikud
    #             "‫עַצבָּנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "новый",
    #             # pronunciation_word
    #             "χadaʃ",
    #             # hebrew_word_nikud
    #             "‫חָדָש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нормальный",
    #             # pronunciation_word
    #             "nor'mali",
    #             # hebrew_word_nikud
    #             "‫נוֹרמָלִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нужный",
    #             # pronunciation_word
    #             "daruʃ",
    #             # hebrew_word_nikud
    #             "‫דָרוּש‬‬"
    #         ),
    #     ]
    # ),  
    # (
    #     # group_name_ru
    #     "168. Прилагательные 2",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "общественный",
    #             # pronunciation_word
    #             "ʦiburi",
    #             # hebrew_word_nikud
    #             "‫צִיבּוּרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обыкновенный",
    #             # pronunciation_word
    #             "ragil",
    #             # hebrew_word_nikud
    #             "‫רָגִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обязательный",
    #             # pronunciation_word
    #             "heχreχi",
    #             # hebrew_word_nikud
    #             "‫הֶכרֵחִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ограниченный",
    #             # pronunciation_word
    #             "mugbal",
    #             # hebrew_word_nikud
    #             "‫מוּגבָּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "огромный",
    #             # pronunciation_word
    #             "anaki",
    #             # hebrew_word_nikud
    #             "‫עֲנָקִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "одинаковый",
    #             # pronunciation_word
    #             "zehe",
    #             # hebrew_word_nikud
    #             "‫זֵהֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "опасный",
    #             # pronunciation_word
    #             "mesukan",
    #             # hebrew_word_nikud
    #             "‫מְסוּכָּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "оригинальный",
    #             # pronunciation_word
    #             "mekori",
    #             # hebrew_word_nikud
    #             "‬‫מְקוֹרִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "основной",
    #             # pronunciation_word
    #             "ikari",
    #             # hebrew_word_nikud
    #             "‫עִיקָרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "острый (нож и т.п.)",
    #             # pronunciation_word
    #             "χad",
    #             # hebrew_word_nikud
    #             "‫חַד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "открытый",
    #             # pronunciation_word
    #             "pa'tuaχ",
    #             # hebrew_word_nikud
    #             "‬ּפָּתו‬‫ח‬"
    #         ),
    #         (
    #             # translation_word
    #             "отличный (хороший)",
    #             # pronunciation_word
    #             "meʦuyan",
    #             # hebrew_word_nikud
    #             "‫מְצוּיָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отрицательный",
    #             # pronunciation_word
    #             "ʃlili",
    #             # hebrew_word_nikud
    #             "‫שלִילִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "персональный",
    #             # pronunciation_word
    #             "prati",
    #             # hebrew_word_nikud
    #             "‫פּרָטִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плоский",
    #             # pronunciation_word
    #             "ʃa'tuaχ",
    #             # hebrew_word_nikud
    #             "‫שָטוּח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плохой",
    #             # pronunciation_word
    #             "ra",
    #             # hebrew_word_nikud
    #             "‫רַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полный (наполненный)",
    #             # pronunciation_word
    #             "male",
    #             # hebrew_word_nikud
    #             "‫מָלֵא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "понятный (ясный)",
    #             # pronunciation_word
    #             "barur",
    #             # hebrew_word_nikud
    #             "‫בָּרוּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "последний",
    #             # pronunciation_word
    #             "aχaron",
    #             # hebrew_word_nikud
    #             "‫אַחֲרוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "постоянный (работа, адрес)",
    #             # pronunciation_word
    #             "ka'vuʿa",
    #             # hebrew_word_nikud
    #             "‫קָבוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "похожий",
    #             # pronunciation_word
    #             "dome",
    #             # hebrew_word_nikud
    #             "‬‫דוֹמֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "правильный (верный)",
    #             # pronunciation_word
    #             "naχon",
    #             # hebrew_word_nikud
    #             "‬‫נָכוֹן‬"
    #         ),
    #         (
    #             # translation_word
    #             "превосходный",
    #             # pronunciation_word
    #             "meʦuyan",
    #             # hebrew_word_nikud
    #             "‫מְצוּיָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "приятный (голос)",
    #             # pronunciation_word
    #             "naʿim",
    #             # hebrew_word_nikud
    #             "‫נָעִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "продолжительный",
    #             # pronunciation_word
    #             "memuʃaχ",
    #             # hebrew_word_nikud
    #             "‫מְמוּשָך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прозрачный",
    #             # pronunciation_word
    #             "ʃakuf",
    #             # hebrew_word_nikud
    #             "‫שָקוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "простой",
    #             # pronunciation_word
    #             "paʃut",
    #             # hebrew_word_nikud
    #             "‫פָּשוּט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "просторный",
    #             # pronunciation_word
    #             "meruvaχ",
    #             # hebrew_word_nikud
    #             "‫מְרוּוָח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "противоположный",
    #             # pronunciation_word
    #             "negdi",
    #             # hebrew_word_nikud
    #             "‫נֶגדִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прохладный",
    #             # pronunciation_word
    #             "karir",
    #             # hebrew_word_nikud
    #             "‫קָרִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прочный",
    #             # pronunciation_word
    #             "muʦak",
    #             # hebrew_word_nikud
    #             "‫מוּצָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прошлый",
    #             # pronunciation_word
    #             "ʃeʿavar",
    #             # hebrew_word_nikud
    #             "‫שֶעָבַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прямой",
    #             # pronunciation_word
    #             "yaʃar",
    #             # hebrew_word_nikud
    #             "‫יָשָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пунктуальный",
    #             # pronunciation_word
    #             "daikan",
    #             # hebrew_word_nikud
    #             "‫דַייקָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пустой (~ бокал)",
    #             # pronunciation_word
    #             "rek",
    #             # hebrew_word_nikud
    #             "‫רֵיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "разный",
    #             # pronunciation_word
    #             "ʃone",
    #             # hebrew_word_nikud
    #             "‫שוֹנֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "редкий",
    #             # pronunciation_word
    #             "nadir",
    #             # hebrew_word_nikud
    #             "‫נָדִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рискованный",
    #             # pronunciation_word
    #             "mesukan",
    #             # hebrew_word_nikud
    #             "‫מְסוּכָּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ровный (о поверхности)",
    #             # pronunciation_word
    #             "χalak",
    #             # hebrew_word_nikud
    #             "‫חָלָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "свежий",
    #             # pronunciation_word
    #             "tari",
    #             # hebrew_word_nikud
    #             "‫טָרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "светлый (о цвете)",
    #             # pronunciation_word
    #             "bahir",
    #             # hebrew_word_nikud
    #             "‫בָּהִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "свободный",
    #             # pronunciation_word
    #             "χofʃi",
    #             # hebrew_word_nikud
    #             "‫חוֹפשִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сладкий",
    #             # pronunciation_word
    #             "matok",
    #             # hebrew_word_nikud
    #             "‫מָתוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "следующий",
    #             # pronunciation_word
    #             "haba",
    #             # hebrew_word_nikud
    #             "‬‫הַבָּא‬"
    #         ),
    #         (
    #             # translation_word
    #             "слепой",
    #             # pronunciation_word
    #             "iver",
    #             # hebrew_word_nikud
    #             "‬‫עִיווֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "сложный (вопрос и т.п.)",
    #             # pronunciation_word
    #             "mesubaχ",
    #             # hebrew_word_nikud
    #             "‫מְסוּבָּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "смуглый",
    #             # pronunciation_word
    #             "ʃaχum",
    #             # hebrew_word_nikud
    #             "‬‫שָחוּם‬"
    #         ),
    #         (
    #             # translation_word
    #             "совместимый",
    #             # pronunciation_word
    #             "toʾem",
    #             # hebrew_word_nikud
    #             "‬‫תוֹאֵם‬"
    #         ),
    #         (
    #             # translation_word
    #             "солёный",
    #             # pronunciation_word
    #             "ma'luaχ",
    #             # hebrew_word_nikud
    #             "‫מָלוּח‬"
    #         ),
    #         (
    #             # translation_word
    #             "солнечный",
    #             # pronunciation_word
    #             "ʃimʃi",
    #             # hebrew_word_nikud
    #             "‫שִמשִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "соседний",
    #             # pronunciation_word
    #             "samuχ",
    #             # hebrew_word_nikud
    #             "‫סָמוּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "специальный",
    #             # pronunciation_word
    #             "meyuχad",
    #             # hebrew_word_nikud
    #             "‫מְיוּחָד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спокойный",
    #             # pronunciation_word
    #             "ʃaket",
    #             # hebrew_word_nikud
    #             "‫שָקֵט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "старый",
    #             # pronunciation_word
    #             "yaʃan",
    #             # hebrew_word_nikud
    #             "‫יָשָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сухой",
    #             # pronunciation_word
    #             "yaveʃ",
    #             # hebrew_word_nikud
    #             "‫יָבֵש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "счастливый",
    #             # pronunciation_word
    #             "meʾuʃar",
    #             # hebrew_word_nikud
    #             "‫מְאוּשָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "твёрдый",
    #             # pronunciation_word
    #             "kaʃe",
    #             # hebrew_word_nikud
    #             "‫קָשֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тёмный(о комнате)",
    #             # pronunciation_word
    #             "χaʃuχ",
    #             # hebrew_word_nikud
    #             "‫חָשוּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тёплый",
    #             # pronunciation_word
    #             "χamim",
    #             # hebrew_word_nikud
    #             "‫חָמִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тихий",
    #             # pronunciation_word
    #             "ʃaket",
    #             # hebrew_word_nikud
    #             "‫שָקֵט‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "толстый",
    #             # pronunciation_word
    #             "ave",
    #             # hebrew_word_nikud
    #             "‫עָבֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "точный",
    #             # pronunciation_word
    #             "meduyak",
    #             # hebrew_word_nikud
    #             "‫מְדוּיָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тощий",
    #             # pronunciation_word
    #             "raze",
    #             # hebrew_word_nikud
    #             "‫רָזֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "трудный",
    #             # pronunciation_word
    #             "kaʃe",
    #             # hebrew_word_nikud
    #             "‫קָשֶה‬‬"
    #         ),
    #          (
    #             # translation_word
    #             "тяжёлый (напр. груз)",
    #             # pronunciation_word
    #             "kaved",
    #             # hebrew_word_nikud
    #             "‫כָּבֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "удовлетворённый",
    #             # pronunciation_word
    #             "mesupak",
    #             # hebrew_word_nikud
    #             "‫מְסוּפָּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "узкий",
    #             # pronunciation_word
    #             "ʦar",
    #             # hebrew_word_nikud
    #             "‬‫צַר‬"
    #         ),
    #         (
    #             # translation_word
    #             "умный",
    #             # pronunciation_word
    #             "pi'keaχ",
    #             # hebrew_word_nikud
    #             "‬‫פִּיקֵח‬"
    #         ),
    #          (
    #             # translation_word
    #             "уникальный",
    #             # pronunciation_word
    #             "meyuχad bemino",
    #             # hebrew_word_nikud
    #             "‬מְיוּחָד‬ ‬‬‫בְּמִינו‬"
    #         ),
    #         (
    #             # translation_word
    #             "усталый",
    #             # pronunciation_word
    #             "ayef",
    #             # hebrew_word_nikud
    #             "‫עָייֵף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "холодный",
    #             # pronunciation_word
    #             "kar",
    #             # hebrew_word_nikud
    #             "‫קַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "хрупкий",
    #             # pronunciation_word
    #             "ʃavir",
    #             # hebrew_word_nikud
    #             "‫שָבִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "центральный",
    #             # pronunciation_word
    #             "merkazi",
    #             # hebrew_word_nikud
    #             "‬‫מֶרכָּזִי‬
    #         (
    #             # translation_word
    #             "частный (личный)",
    #             # pronunciation_word
    #             "iʃi",
    #             # hebrew_word_nikud
    #             "‬‫אִישִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "чистый",
    #             # pronunciation_word
    #             "naki",
    #             # hebrew_word_nikud
    #             "‫נָקִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чрезмерный",
    #             # pronunciation_word
    #             "meyutar",
    #             # hebrew_word_nikud
    #             "‬‫מְיוּתָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "широкий",
    #             # pronunciation_word
    #             "raχav",
    #             # hebrew_word_nikud
    #             "‫רָחָב‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "169. Глаголы 1",
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
    #             "беспокоить (волновать)",
    #             # pronunciation_word
    #             "lehadʾig",
    #             # hebrew_word_nikud
    #             "‬‫לְהַדאִיג‬"
    #         ),
    #         (
    #             # translation_word
    #             "беспокоить (мешать)",
    #             # pronunciation_word
    #             "lehatrid",
    #             # hebrew_word_nikud
    #             "‫לְהַטרִיד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "беспокоиться",
    #             # pronunciation_word
    #             "lidʾog",
    #             # hebrew_word_nikud
    #             "‬‫לִדאוֹג‬"
    #         ),
    #         (
    #             # translation_word
    #             "бить (ударять)",
    #             # pronunciation_word
    #             "lehakot",
    #             # hebrew_word_nikud
    #             "‫לְהַכּוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "благодарить",
    #             # pronunciation_word
    #             "lehodot",
    #             # hebrew_word_nikud
    #             "‬‫לְהוֹדוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "бояться (чего-л.)",
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
    #             "бриться",
    #             # pronunciation_word
    #             "lehitga'leaχ",
    #             # hebrew_word_nikud
    #             "‫לְהִתגַלֵח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бросать (напр. камень)",
    #             # pronunciation_word
    #             "lizrok",
    #             # hebrew_word_nikud
    #             "‫לִזרוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бросать (покидать)",
    #             # pronunciation_word
    #             "laʿazov",
    #             # hebrew_word_nikud
    #             "‬‫לַעֲזוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "будить",
    #             # pronunciation_word
    #             "lehaʿir",
    #             # hebrew_word_nikud
    #             "‬‫לְהָעִיר‬"
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
    #             "быть должным",
    #             # pronunciation_word
    #             "lihyot χayav",
    #             # hebrew_word_nikud
    #             "לִהיוֹת‬‬ ‫חַייָב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "быть похожим",
    #             # pronunciation_word
    #             "lihyot dome",
    #             # hebrew_word_nikud
    #             "‬לִהיוֹת‬‬ ‫דוֹמֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "верить (думать)",
    #             # pronunciation_word
    #             "lehaʾamin",
    #             # hebrew_word_nikud
    #             "‫לְהַאֲמִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "веселиться",
    #             # pronunciation_word
    #             "lehanot",
    #             # hebrew_word_nikud
    #             "‫לֵיהָנוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "весить (иметь вес)",
    #             # pronunciation_word
    #             "liʃkol",
    #             # hebrew_word_nikud
    #             "‫לִשקוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вести машину",
    #             # pronunciation_word
    #             "linhog",
    #             # hebrew_word_nikud
    #             "‬‫לִנהוֹג‬"
    #         ),
    #         (
    #             # translation_word
    #             "вести переговоры",
    #             # pronunciation_word
    #             "laset velatet",
    #             # hebrew_word_nikud
    #             "לָשֵׂאת‬‬ ‫וְלָתֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вешать",
    #             # pronunciation_word
    #             "litlot",
    #             # hebrew_word_nikud
    #             "‫לִתלוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вздохнуть",
    #             # pronunciation_word
    #             "leheʾanaχ",
    #             # hebrew_word_nikud
    #             "‫לְהֵיאָנַח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "видеть сны",
    #             # pronunciation_word
    #             "laχalom",
    #             # hebrew_word_nikud
    #             "‫לַחֲלוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "включать (напр. радио)",
    #             # pronunciation_word
    #             "lehadlik",
    #             # hebrew_word_nikud
    #             "‫לְהַדלִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "владеть",
    #             # pronunciation_word
    #             "lihyot 'baʿal ʃel",
    #             # hebrew_word_nikud
    #             "לִהיוֹת‬‬ ‫בַּעַל‬ ‫שֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "влиять",
    #             # pronunciation_word
    #             "lehaʃ'piʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַשפִּיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "влюбиться (в ...)",
    #             # pronunciation_word
    #             "lehitʾahev",
    #             # hebrew_word_nikud
    #             "‫לְהִתאַהֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вмешиваться",
    #             # pronunciation_word
    #             "lehitʿarev",
    #             # hebrew_word_nikud
    #             "‫לְהִתעָרֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "возвращаться",
    #             # pronunciation_word
    #             "laʃuv",
    #             # hebrew_word_nikud
    #             "‫לָשוּב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "возмущаться",
    #             # pronunciation_word
    #             "lehitraʿem",
    #             # hebrew_word_nikud
    #             "‫לְהִתרַעֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "возражать",
    #             # pronunciation_word
    #             "lehitnaged",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתנַגֵד‬"
    #         ),
    #         (
    #             # translation_word
    #             "войти (в комнату и т.п.)",
    #             # pronunciation_word
    #             "lehikanes",
    #             # hebrew_word_nikud
    #             "‫לְהִיכָּנֵס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "волноваться",
    #             # pronunciation_word
    #             "lidʾog",
    #             # hebrew_word_nikud
    #             "‫לִדאוֹג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "восхищаться",
    #             # pronunciation_word
    #             "lehitpaʿel",
    #             # hebrew_word_nikud
    #             "‫לְהִתפַּעֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "врать",
    #             # pronunciation_word
    #             "leʃaker",
    #             # hebrew_word_nikud
    #             "‫לְשַקֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вспоминать",
    #             # pronunciation_word
    #             "lehizaχer",
    #             # hebrew_word_nikud
    #             "‫לְהִיזָכֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "выбирать",
    #             # pronunciation_word
    #             "livχor",
    #             # hebrew_word_nikud
    #             "‫לִבחוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "выздоравливать",
    #             # pronunciation_word
    #             "lehaχlim",
    #             # hebrew_word_nikud
    #             "‫לְהַחלִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "выйти (из дома и т.п.)",
    #             # pronunciation_word
    #             "laʦet",
    #             # hebrew_word_nikud
    #             "‫לָצֵאת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "гарантировать",
    #             # pronunciation_word
    #             "lehav'tiaχ",
    #             # hebrew_word_nikud
    #             "‫לְהַבטִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "говорить с ...",
    #             # pronunciation_word
    #             "ledaber",
    #             # hebrew_word_nikud
    #             "‫לְדַבֵּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "голосовать",
    #             # pronunciation_word
    #             "lehaʦ'biʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַצבִּיע‬‬"
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
    #             "‫לָתֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "делать",
    #             # pronunciation_word
    #             "laʿasot",
    #             # hebrew_word_nikud
    #             "‫לַעֲשׂוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "делать прививки",
    #             # pronunciation_word
    #             "leχasen",
    #             # hebrew_word_nikud
    #             "‫לְחַסֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "добавлять",
    #             # pronunciation_word
    #             "lehosif",
    #             # hebrew_word_nikud
    #             "‫לְהוֹסִיף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "доверять",
    #             # pronunciation_word
    #             "liv'toaχ",
    #             # hebrew_word_nikud
    #             "‬‫לִבטוֹח‬"
    #         ),
    #         (
    #             # translation_word
    #             "доказывать",
    #             # pronunciation_word
    #             "leho'χiaχ",
    #             # hebrew_word_nikud
    #             "‫לְהוֹכִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "достигать (напр. ~ полюса)",
    #             # pronunciation_word
    #             "lehasig",
    #             # hebrew_word_nikud
    #             "‫לְהַשִׂיג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "достигать (результата)",
    #             # pronunciation_word
    #             "lehasig",
    #             # hebrew_word_nikud
    #             "‬‫לְהַשִׂיג‬"
    #         ),
    #         (
    #             # translation_word
    #             "драться (в драке)",
    #             # pronunciation_word
    #             "lehitkotet",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתקוֹטֵט‬"
    #         ),
    #         (
    #             # translation_word
    #             "дрожать",
    #             # pronunciation_word
    #             "lirʿod",
    #             # hebrew_word_nikud
    #             "‫לִרעוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "думать",
    #             # pronunciation_word
    #             "laχʃov",
    #             # hebrew_word_nikud
    #             "‬‫לַחשוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "дышать",
    #             # pronunciation_word
    #             "linʃom",
    #             # hebrew_word_nikud
    #             "‫לִנשוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ехать",
    #             # pronunciation_word
    #             "lin'soʿa",
    #             # hebrew_word_nikud
    #             "‬‫לִנסוֹע‬"
    #         ),
    #     ]
    # ),  
    # (
    #     # group_name_ru
    #     "170. Глаголы 2",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "жаловаться",
    #             # pronunciation_word
    #             "lehitlonen",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתלוֹנֵן‬"
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
    #             "жениться",
    #             # pronunciation_word
    #             "lehitχaten",
    #             # hebrew_word_nikud
    #             "‫לְהִתחַתֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жечь, сжигать",
    #             # pronunciation_word
    #             "lisrof",
    #             # hebrew_word_nikud
    #             "‬‫לִשׂרוֹף‬"
    #         ),
    #         (
    #             # translation_word
    #             "жить (проживать)",
    #             # pronunciation_word
    #             "lagur",
    #             # hebrew_word_nikud
    #             "‬‫לָגוּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "жить (существовать)",
    #             # pronunciation_word
    #             "liχyot",
    #             # hebrew_word_nikud
    #             "‫לִחיוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "забыть",
    #             # pronunciation_word
    #             "liʃ'koaχ",
    #             # hebrew_word_nikud
    #             "‫לִשכּוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "завидовать",
    #             # pronunciation_word
    #             "lekane",
    #             # hebrew_word_nikud
    #             "‫לְקַנֵא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зависеть (от ...)",
    #             # pronunciation_word
    #             "lihyot talui be...",
    #             # hebrew_word_nikud
    #             "לִהיוֹת‬‬ ‫תָלוּי‬ ‫ב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "завтракать",
    #             # pronunciation_word
    #             "leʾeχol aruχat 'boker",
    #             # hebrew_word_nikud
    #             "‬לֶאֱכוֹל‬‬ ‫אֲרוּחַת‬ ‫בּוֹקֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "заказывать (в ресторане)",
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
    #             "‫לְסַייֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "закрывать",
    #             # pronunciation_word
    #             "lisgor",
    #             # hebrew_word_nikud
    #             "‫לִסגוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "замечать (увидеть)",
    #             # pronunciation_word
    #             "lasim lev",
    #             # hebrew_word_nikud
    #             "לָשִׂים‬‬ ‫לֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "замолчать",
    #             # pronunciation_word
    #             "lehiʃtatek",
    #             # hebrew_word_nikud
    #             "‫לְהִשתַתֵק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "занимать (деньги)",
    #             # pronunciation_word
    #             "lilvot",
    #             # hebrew_word_nikud
    #             "‫לִלווֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "записывать",
    #             # pronunciation_word
    #             "lirʃom",
    #             # hebrew_word_nikud
    #             "‬‫לִרשוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "запомнить",
    #             # pronunciation_word
    #             "lizkor",
    #             # hebrew_word_nikud
    #             "‫לִזכּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "запрещать",
    #             # pronunciation_word
    #             "leʾesor",
    #             # hebrew_word_nikud
    #             "‫לֶאֱסוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "заразиться чем-л.",
    #             # pronunciation_word
    #             "lehibadek",
    #             # hebrew_word_nikud
    #             "‫לְהִידָבֵק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "защищаться",
    #             # pronunciation_word
    #             "lehitgonen",
    #             # hebrew_word_nikud
    #             "‫לְהִתגוֹנֵן‬‬"
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
    #             "знакомить (кого-л. с кем-л.)",
    #             # pronunciation_word
    #             "lehaʦig",
    #             # hebrew_word_nikud
    #             "‬‫לְהַצִיג‬"
    #         ),
    #         (
    #             # translation_word
    #             "знакомиться (с кем-л.)",
    #             # pronunciation_word
    #             "lehakir",
    #             # hebrew_word_nikud
    #             "‫לְהַכִּיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "знать (кого-л.)",
    #             # pronunciation_word
    #             "lehakir et",
    #             # hebrew_word_nikud
    #             "‬לְהַכִּיר‬‬ ‫אֶת‬"
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
    #             "значить",
    #             # pronunciation_word
    #             "lomar",
    #             # hebrew_word_nikud
    #             "‫לוֹמַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "играть (в игру)",
    #             # pronunciation_word
    #             "lesaχek",
    #             # hebrew_word_nikud
    #             "‬‫לְשַׂחֵק‬"
    #         ),
    #         (
    #             # translation_word
    #             "идти",
    #             # pronunciation_word
    #             "la'leχet",
    #             # hebrew_word_nikud
    #             "‫לָלֶכֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "избегать",
    #             # pronunciation_word
    #             "lehimana",
    #             # hebrew_word_nikud
    #             "‫לְהִימָנַע‬‬"
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
    #             "изменить (поменять)",
    #             # pronunciation_word
    #             "leʃanot",
    #             # hebrew_word_nikud
    #             "‬‫לְשַנוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "изучать",
    #             # pronunciation_word
    #             "lilmod",
    #             # hebrew_word_nikud
    #             "‬‫לִלמוֹד‬"
    #         ),
    #         (
    #             # translation_word
    #             "иметь",
    #             # pronunciation_word
    #             "lehaχzik",
    #             # hebrew_word_nikud
    #             "‫לְהַחזִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "имитировать",
    #             # pronunciation_word
    #             "leχakot",
    #             # hebrew_word_nikud
    #             "‫לְחַקוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "импортировать",
    #             # pronunciation_word
    #             "leyabe",
    #             # hebrew_word_nikud
    #             "‫לְייַבֵּא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "интересоваться",
    #             # pronunciation_word
    #             "lehitʿanyen",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתעַנייֵן‬"
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
    #             "искать",
    #             # pronunciation_word
    #             "leχapes",
    #             # hebrew_word_nikud
    #             "‫לְחַפֵּש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "испачкаться",
    #             # pronunciation_word
    #             "lehitlaχleχ",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתלַכלֵך‬"
    #         ),
    #         (
    #             # translation_word
    #             "исчезнуть",
    #             # pronunciation_word
    #             "leheʿalem",
    #             # hebrew_word_nikud
    #             "‫לְהֵיעָלֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "класть, положить",
    #             # pronunciation_word
    #             "lasim",
    #             # hebrew_word_nikud
    #             "‬‫לָשִׂים‬"
    #         ),
    #         (
    #             # translation_word
    #             "компенсировать",
    #             # pronunciation_word
    #             "lefaʦot",
    #             # hebrew_word_nikud
    #             "‫לְפַצוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "компрометировать",
    #             # pronunciation_word
    #             "lehavʾiʃ et reχo",
    #             # hebrew_word_nikud
    #             "לְהַבאִיש‬ ‫אֶת‬ ‬‫רֵיחו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "конкурировать",
    #             # pronunciation_word
    #             "lehitχarot",
    #             # hebrew_word_nikud
    #             "‫לְהִתחָרוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "консультироваться с ...",
    #             # pronunciation_word
    #             "lehityaʿeʦ im",
    #             # hebrew_word_nikud
    #             "לְהִתייַעֵץ‬ ‬‫עִם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "контролировать",
    #             # pronunciation_word
    #             "liʃlot",
    #             # hebrew_word_nikud
    #             "‬‫לִשלוֹט‬"
    #         ),
    #         (
    #             # translation_word
    #             "концентрироваться",
    #             # pronunciation_word
    #             "lehitrakez",
    #             # hebrew_word_nikud
    #             "‫לְהִתרַכֵּז‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кормить",
    #             # pronunciation_word
    #             "lehaʾaχil",
    #             # hebrew_word_nikud
    #             "‫לְהַאֲכִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "красть",
    #             # pronunciation_word
    #             "lignov",
    #             # hebrew_word_nikud
    #             "‫לִגנוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кричать",
    #             # pronunciation_word
    #             "liʦʿok",
    #             # hebrew_word_nikud
    #             "‫לִצעוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "купать",
    #             # pronunciation_word
    #             "lirχoʦ",
    #             # hebrew_word_nikud
    #             "‫לִרחוֹץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "купаться (в море и т.п.)",
    #             # pronunciation_word
    #             "lehitraχeʦ",
    #             # hebrew_word_nikud
    #             "‫לְהִתרַחֵץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кушать, есть",
    #             # pronunciation_word
    #             "leʾeχol",
    #             # hebrew_word_nikud
    #             "‫לֶאֱכוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лежать (о предмете)",
    #             # pronunciation_word
    #             "lihyot munaχ",
    #             # hebrew_word_nikud
    #             "לִהיוֹת‬‬ ‫מוּנָח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лежать (о человеке)",
    #             # pronunciation_word
    #             "liʃkav",
    #             # hebrew_word_nikud
    #             "‫לִשכַּב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "летать",
    #             # pronunciation_word
    #             "laʿuf",
    #             # hebrew_word_nikud
    #             "‫לָעוּף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лечить (болезнь)",
    #             # pronunciation_word
    #             "letapel be...",
    #             # hebrew_word_nikud
    #             "לְטַפֵּל‬ ‬ְּ‫ב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ловить",
    #             # pronunciation_word
    #             "litfos",
    #             # hebrew_word_nikud
    #             "‫לִתפוֹס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ложиться спать",
    #             # pronunciation_word
    #             "liʃkav liʃon",
    #             # hebrew_word_nikud
    #             "לִשכַּב‬ ‬‫לִישוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ломать",
    #             # pronunciation_word
    #             "liʃbor",
    #             # hebrew_word_nikud
    #             "‫לִשבּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "льстить",
    #             # pronunciation_word
    #             "lehaχnif",
    #             # hebrew_word_nikud
    #             "‫לְהַחנִיף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "любить",
    #             # pronunciation_word
    #             "leʾehov",
    #             # hebrew_word_nikud
    #             "‫לֶאֱהוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "менять",
    #             # pronunciation_word
    #             "lehaχlif",
    #             # hebrew_word_nikud
    #             "‬‫לְהַחלִיף‬"
    #         ),
    #         (
    #             # translation_word
    #             "мечтать",
    #             # pronunciation_word
    #             "laχalom",
    #             # hebrew_word_nikud
    #             "‫לַחֲלוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "молчать",
    #             # pronunciation_word
    #             "liʃtok",
    #             # hebrew_word_nikud
    #             "‫לִשתוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мочь",
    #             # pronunciation_word
    #             "yaχol",
    #             # hebrew_word_nikud
    #             "‫יָכוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мстить",
    #             # pronunciation_word
    #             "linkom",
    #             # hebrew_word_nikud
    #             "‬‫לִנקוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "мыть",
    #             # pronunciation_word
    #             "liʃtof",
    #             # hebrew_word_nikud
    #             "‬‫לִשטוֹף‬"
    #         ),
    #         (
    #             # translation_word
    #             "мыться",
    #             # pronunciation_word
    #             "lehitraχeʦ",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתרַחֵץ‬"
    #         ),
    #     ]
    # ), 
    # (
    #     # group_name_ru
    #     "171. Глаголы 3",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "наблюдать",
    #             # pronunciation_word
    #             "liʦpot,",
    #             # hebrew_word_nikud
    #             "‬‫לִצפּוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "нагревать",
    #             # pronunciation_word
    #             "leχamem",
    #             # hebrew_word_nikud
    #             "‫לְחַמֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "называть",
    #             # pronunciation_word
    #             "likro",
    #             # hebrew_word_nikud
    #             "‫לִקרוֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "наказывать",
    #             # pronunciation_word
    #             "lehaʿaniʃ",
    #             # hebrew_word_nikud
    #             "‫לְהַעֲנִיש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "намекать",
    #             # pronunciation_word
    #             "lirmoz",
    #             # hebrew_word_nikud
    #             "‫לִרמוֹז‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нанимать (работника)",
    #             # pronunciation_word
    #             "lehaʿasik",
    #             # hebrew_word_nikud
    #             "‫לְהַעֲסִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "напоминать",
    #             # pronunciation_word
    #             "lehazkir",
    #             # hebrew_word_nikud
    #             "‬‫לְהַזכִּיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "наследовать",
    #             # pronunciation_word
    #             "la'reʃet",
    #             # hebrew_word_nikud
    #             "‫לָרֶשֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "насмехаться",
    #             # pronunciation_word
    #             "lilʿog",
    #             # hebrew_word_nikud
    #             "‫לִלעוֹג‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "находить",
    #             # pronunciation_word
    #             "limʦo",
    #             # hebrew_word_nikud
    #             "‬‫לִמצוֹא‬"
    #         ),
    #         (
    #             # translation_word
    #             "начинать",
    #             # pronunciation_word
    #             "lehatχil",
    #             # hebrew_word_nikud
    #             "‬‫לְהַתחִיל‬"
    #         ),
    #         (
    #             # translation_word
    #             "нравиться",
    #             # pronunciation_word
    #             "limʦo χen beʿei'nayim",
    #             # hebrew_word_nikud
    #             "‬לִמצוֹא‬ ‫חֵן‬ ‬‫בְּעֵינַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "нюхать",
    #             # pronunciation_word
    #             "leha'riaχ",
    #             # hebrew_word_nikud
    #             "‫לְהָרִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обвинять",
    #             # pronunciation_word
    #             "lehaʾaʃim",
    #             # hebrew_word_nikud
    #             "‫לְהַאֲשִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обедать",
    #             # pronunciation_word
    #             "leʾeχol aruχat ʦaha'rayim",
    #             # hebrew_word_nikud
    #             "לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‬‫צָהֳרַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обещать",
    #             # pronunciation_word
    #             "lehav'tiaχ",
    #             # hebrew_word_nikud
    #             "‫לְהַבטִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обижать",
    #             # pronunciation_word
    #             "lif'goʿa",
    #             # hebrew_word_nikud
    #             "‬‫לִפגוֹע‬"
    #         ),
    #         (
    #             # translation_word
    #             "обманывать",
    #             # pronunciation_word
    #             "leramot",
    #             # hebrew_word_nikud
    #             "‫לְרַמוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обнимать",
    #             # pronunciation_word
    #             "leχabek",
    #             # hebrew_word_nikud
    #             "‫לְחַבֵּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обращаться (к кому-л.)",
    #             # pronunciation_word
    #             "lifnot el",
    #             # hebrew_word_nikud
    #             "לִפנוֹת‬‬ ‫אֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обучать",
    #             # pronunciation_word
    #             "lelamed",
    #             # hebrew_word_nikud
    #             "‫לְלַמֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "объяснять",
    #             # pronunciation_word
    #             "lehasbir",
    #             # hebrew_word_nikud
    #             "‬‫לְהַסבִּיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "ограничивать",
    #             # pronunciation_word
    #             "lehagbil",
    #             # hebrew_word_nikud
    #             "‬‫לְהַגבִּיל‬"
    #         ),
    #         (
    #             # translation_word
    #             "ожидать",
    #             # pronunciation_word
    #             "leʦapot",
    #             # hebrew_word_nikud
    #             "‫לְצַפּוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "означать",
    #             # pronunciation_word
    #             "lomar",
    #             # hebrew_word_nikud
    #             "‫לוֹמַר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "оскорблять",
    #             # pronunciation_word
    #             "lehaʿaliv",
    #             # hebrew_word_nikud
    #             "‫לְהַעֲלִיב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "оставлять (забыть)",
    #             # pronunciation_word
    #             "lehaʃʾir",
    #             # hebrew_word_nikud
    #             "‫לְהַשאִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "останавливаться",
    #             # pronunciation_word
    #             "laʿaʦor",
    #             # hebrew_word_nikud
    #             "‬‫לַעֲצוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "отвечать",
    #             # pronunciation_word
    #             "laʿanot",
    #             # hebrew_word_nikud
    #             "‫לְעַנוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отдыхать",
    #             # pronunciation_word
    #             "la'nuaχ",
    #             # hebrew_word_nikud
    #             "‬‫לָנוּח‬"
    #         ),
    #         (
    #             # translation_word
    #             "отказывать",
    #             # pronunciation_word
    #             "lesarev",
    #             # hebrew_word_nikud
    #             "‫לְסָרֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отличаться",
    #             # pronunciation_word
    #             "lehibadel",
    #             # hebrew_word_nikud
    #             "‫לְהִיבָּדֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отменить",
    #             # pronunciation_word
    #             "levatel",
    #             # hebrew_word_nikud
    #             "‫לְבַטֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отрезать",
    #             # pronunciation_word
    #             "laχtoχ",
    #             # hebrew_word_nikud
    #             "‫לַחתוֹך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отрицать",
    #             # pronunciation_word
    #             "liʃlol",
    #             # hebrew_word_nikud
    #             "‫לִשלוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "охранять",
    #             # pronunciation_word
    #             "liʃmor",
    #             # hebrew_word_nikud
    #             "‬‫לִשמוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "очаровывать",
    #             # pronunciation_word
    #             "lehaksim",
    #             # hebrew_word_nikud
    #             "‫לְהַקסִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "очищать",
    #             # pronunciation_word
    #             "lenakot",
    #             # hebrew_word_nikud
    #             "‬‫לְנַקוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "ошибаться",
    #             # pronunciation_word
    #             "litʿot",
    #             # hebrew_word_nikud
    #             "‫לִטעוֹת‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "172. Глаголы 4",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "пахнуть",
    #             # pronunciation_word
    #             "leha'riaχ",
    #             # hebrew_word_nikud
    #             "‫לְהָרִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переделывать",
    #             # pronunciation_word
    #             "laʿasot meχadaʃ",
    #             # hebrew_word_nikud
    #             "לַעֲשׂוֹת‬‬ ‫מֵחָדָש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "писать",
    #             # pronunciation_word
    #             "liχtov",
    #             # hebrew_word_nikud
    #             "‬‫לִכתוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "пить",
    #             # pronunciation_word
    #             "liʃtot",
    #             # hebrew_word_nikud
    #             "‫לִשתוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плавать",
    #             # pronunciation_word
    #             "lisχot",
    #             # hebrew_word_nikud
    #             "‬‫לִשׂחוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "плакать",
    #             # pronunciation_word
    #             "livkot",
    #             # hebrew_word_nikud
    #             "‫לִבכּוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "планировать",
    #             # pronunciation_word
    #             "letaχnen",
    #             # hebrew_word_nikud
    #             "‬‫לְתַכנֵן‬"
    #         ),
    #         (
    #             # translation_word
    #             "платить",
    #             # pronunciation_word
    #             "leʃalem",
    #             # hebrew_word_nikud
    #             "‫לְשַלֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "плевать",
    #             # pronunciation_word
    #             "lirok",
    #             # hebrew_word_nikud
    #             "‫לִירוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поворачивать",
    #             # pronunciation_word
    #             "lifnot",
    #             # hebrew_word_nikud
    #             "‫לִפנוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "повторять",
    #             # pronunciation_word
    #             "laχazor al",
    #             # hebrew_word_nikud
    #             "לַחֲזוֹר‬‬ ‫עַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подготовить",
    #             # pronunciation_word
    #             "lehaχin",
    #             # hebrew_word_nikud
    #             "‬‫לְהָכִין‬"
    #         ),
    #         (
    #             # translation_word
    #             "подозревать",
    #             # pronunciation_word
    #             "laχʃod",
    #             # hebrew_word_nikud
    #             "‬‫לַחשוֹד‬"
    #         ),
    #         (
    #             # translation_word
    #             "подписывать",
    #             # pronunciation_word
    #             "laχtom",
    #             # hebrew_word_nikud
    #             "‫לַחתוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подслушивать",
    #             # pronunciation_word
    #             "lehaʾazin be'seter",
    #             # hebrew_word_nikud
    #             "לְהַאֲזִין‬‬ ‫בְּסֵתֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подсматривать",
    #             # pronunciation_word
    #             "lehaʦiʦ",
    #             # hebrew_word_nikud
    #             "‫לְהָצִיץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подчиняться",
    #             # pronunciation_word
    #             "leʦayet",
    #             # hebrew_word_nikud
    #             "‫לְצַייֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поздравлять",
    #             # pronunciation_word
    #             "levareχ",
    #             # hebrew_word_nikud
    #             "‫לְבָרֵך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "показывать",
    #             # pronunciation_word
    #             "leharʾot",
    #             # hebrew_word_nikud
    #             "‬‫לְהַראוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "покупать",
    #             # pronunciation_word
    #             "liknot",
    #             # hebrew_word_nikud
    #             "‬‫לִקנוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "пользоваться (чем-л.)",
    #             # pronunciation_word
    #             "lehiʃtameʃ be...",
    #             # hebrew_word_nikud
    #             "‬לְהִשתַמֵש‬‬ ְּ‫ב‬"
    #         ),
    #         (
    #             # translation_word
    #             "помнить",
    #             # pronunciation_word
    #             "lizkor",
    #             # hebrew_word_nikud
    #             "‫לִזכּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "помогать",
    #             # pronunciation_word
    #             "laʿazor",
    #             # hebrew_word_nikud
    #             "‫לַעֲזוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "понимать",
    #             # pronunciation_word
    #             "lehavin",
    #             # hebrew_word_nikud
    #             "‬‫לְהָבִין‬"
    #         ),
    #         (
    #             # translation_word
    #             "починить (машину, крышу)",
    #             # pronunciation_word
    #             "letaken",
    #             # hebrew_word_nikud
    #             "‬‫לְתַקֵן‬"
    #         ),
    #         (
    #             # translation_word
    #             "предлагать",
    #             # pronunciation_word
    #             "leha'ʦiʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַצִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предполагать",
    #             # pronunciation_word
    #             "leʃaʿer",
    #             # hebrew_word_nikud
    #             "‫לְשַעֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предупреждать",
    #             # pronunciation_word
    #             "lehazhir",
    #             # hebrew_word_nikud
    #             "‬‫לְהַזהִיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "презирать",
    #             # pronunciation_word
    #             "lezalzel be...",
    #             # hebrew_word_nikud
    #             "‬לְזַלזֵל‬‬ ‫ב‬"
    #         ),
    #         (
    #             # translation_word
    #             "прибывать",
    #             # pronunciation_word
    #             "leha'giʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַגִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "приводить в порядок",
    #             # pronunciation_word
    #             "lesader",
    #             # hebrew_word_nikud
    #             "‫לְסַדֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "приглашать",
    #             # pronunciation_word
    #             "lehazmin",
    #             # hebrew_word_nikud
    #             "‫לְהַזמִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "признавать (ошибку)",
    #             # pronunciation_word
    #             "lehakir be...",
    #             # hebrew_word_nikud
    #             "לְהַכִּיר‬‬ ְּ‫ב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "признаваться",
    #             # pronunciation_word
    #             "lehodot be...",
    #             # hebrew_word_nikud
    #             "‬לְהוֹדוֹת‬‬ ‫ב‬"
    #         ),
    #         (
    #             # translation_word
    #             "принуждать",
    #             # pronunciation_word
    #             "lehaχ'riaχ",
    #             # hebrew_word_nikud
    #             "‫לְהַכרִיח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "продавать",
    #             # pronunciation_word
    #             "limkor",
    #             # hebrew_word_nikud
    #             "‫לִמכּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "просить",
    #             # pronunciation_word
    #             "levakeʃ",
    #             # hebrew_word_nikud
    #             "‫לְבַקֵש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "протестовать",
    #             # pronunciation_word
    #             "limχot",
    #             # hebrew_word_nikud
    #             "‬‫לִמחוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "прощать",
    #             # pronunciation_word
    #             "lis'loaχ",
    #             # hebrew_word_nikud
    #             "‫לִסלוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "работать",
    #             # pronunciation_word
    #             "laʿavod",
    #             # hebrew_word_nikud
    #             "‬‫לַעֲבוֹד‬"
    #         ),
    #         (
    #             # translation_word
    #             "развлекать",
    #             # pronunciation_word
    #             "levader",
    #             # hebrew_word_nikud
    #             "‬‫לְבַדֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "раздражаться",
    #             # pronunciation_word
    #             "lehitragez",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתרַגֵז‬"
    #         ),
    #         (
    #             # translation_word
    #             "разрешать (позволять)",
    #             # pronunciation_word
    #             "leharʃot",
    #             # hebrew_word_nikud
    #             "‫לְהַרשוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рассказывать",
    #             # pronunciation_word
    #             "lesaper",
    #             # hebrew_word_nikud
    #             "‬‫לְסַפֵּר‬"
    #         ),
    #         (
    #             # translation_word
    #             "рассчитывать на ...",
    #             # pronunciation_word
    #             "lismoχ al",
    #             # hebrew_word_nikud
    #             "‬לִסמוֹך‬‬ ‫עַל‬"
    #         ),
    #         (
    #             # translation_word
    #             "рвать",
    #             # pronunciation_word
    #             "liktof",
    #             # hebrew_word_nikud
    #             "‫לִקטוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рекламировать",
    #             # pronunciation_word
    #             "lefarsem",
    #             # hebrew_word_nikud
    #             "‫לְפַרסֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "решать (принимать решение)",
    #             # pronunciation_word
    #             "lehaχlit",
    #             # hebrew_word_nikud
    #             "‫לְהַחלִיט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "решить (задачу)",
    #             # pronunciation_word
    #             "liftor",
    #             # hebrew_word_nikud
    #             "‫לִפתוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рисковать",
    #             # pronunciation_word
    #             "la'kaχat sikun",
    #             # hebrew_word_nikud
    #             "לָקַחַת‬‬ ‫סִיכּוּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ругать",
    #             # pronunciation_word
    #             "linzof",
    #             # hebrew_word_nikud
    #             "‫לִנזוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "руководить",
    #             # pronunciation_word
    #             "lenahel",
    #             # hebrew_word_nikud
    #             "‫לְנַהֵל‬‬"
    #         ),
    #     ]
    # ),    
    # (
    #     # group_name_ru
    #     "173. Глаголы 5",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "светиться (блестеть)",
    #             # pronunciation_word
    #             "lizhor",
    #             # hebrew_word_nikud
    #             "‫לִזהוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "связывать",
    #             # pronunciation_word
    #             "likʃor",
    #             # hebrew_word_nikud
    #             "‫לִקשוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сердиться (на ...)",
    #             # pronunciation_word
    #             "lehitragez",
    #             # hebrew_word_nikud
    #             "‫לְהִתרַגֵז‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сесть",
    #             # pronunciation_word
    #             "lehityaʃev",
    #             # hebrew_word_nikud
    #             "‫לְהִתייַשֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сидеть",
    #             # pronunciation_word
    #             "la'ʃevet",
    #             # hebrew_word_nikud
    #             "‬‫לָשֶבֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "сказать",
    #             # pronunciation_word
    #             "lomar",
    #             # hebrew_word_nikud
    #             "‬‫לוֹמַר‬"
    #         ),
    #         (
    #             # translation_word
    #             "скучать",
    #             # pronunciation_word
    #             "lehiʃtaʿamem",
    #             # hebrew_word_nikud
    #             "‫לְהִשתַעֲמֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слушать",
    #             # pronunciation_word
    #             "lehakʃiv",
    #             # hebrew_word_nikud
    #             "‫לְהַקשִיב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слышать",
    #             # pronunciation_word
    #             "liʃ'moʿa",
    #             # hebrew_word_nikud
    #             "‫לִשמוֹע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "смеяться",
    #             # pronunciation_word
    #             "liʦχok",
    #             # hebrew_word_nikud
    #             "‬‫לִצחוֹק‬"
    #         ),
    #         (
    #             # translation_word
    #             "смотреть",
    #             # pronunciation_word
    #             "lehistakel",
    #             # hebrew_word_nikud
    #             "‫לְהִסתַכֵּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "снимать (~ квартиру)",
    #             # pronunciation_word
    #             "liskor",
    #             # hebrew_word_nikud
    #             "‫לִשׂכּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "советовать",
    #             # pronunciation_word
    #             "leyaʿeʦ",
    #             # hebrew_word_nikud
    #             "‫לְייַעֵץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "соглашаться",
    #             # pronunciation_word
    #             "lehaskim",
    #             # hebrew_word_nikud
    #             "‫לְהַסכִּים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "создать",
    #             # pronunciation_word
    #             "liʦor",
    #             # hebrew_word_nikud
    #             "‫לִיצוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сомневаться",
    #             # pronunciation_word
    #             "lefakpek",
    #             # hebrew_word_nikud
    #             "‫לְפַקפֵּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сотрудничать",
    #             # pronunciation_word
    #             "leʃatef peʿula",
    #             # hebrew_word_nikud
    #             "לְשַתֵף‬ ‬‫פְּעוּלָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сохранять",
    #             # pronunciation_word
    #             "leʃamer",
    #             # hebrew_word_nikud
    #             "‫לְשַמֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спасать",
    #             # pronunciation_word
    #             "lehaʦil",
    #             # hebrew_word_nikud
    #             "‫לְהַצִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сравнивать",
    #             # pronunciation_word
    #             "lehaʃvot",
    #             # hebrew_word_nikud
    #             "‫לְהַשווֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "становиться (сделаться)",
    #             # pronunciation_word
    #             "lahafoχ le...",
    #             # hebrew_word_nikud
    #             "לַהֲפוֹך‬‬ ‫ל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стирать (бельё)",
    #             # pronunciation_word
    #             "leχabes",
    #             # hebrew_word_nikud
    #             "‬‫לְכַבֵּס‬"
    #         ),
    #         (
    #             # translation_word
    #             "стоить",
    #             # pronunciation_word
    #             "laʿalot",
    #             # hebrew_word_nikud
    #             "‫לַעֲלוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "страдать",
    #             # pronunciation_word
    #             "lisbol",
    #             # hebrew_word_nikud
    #             "‫לִסבּוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стрелять",
    #             # pronunciation_word
    #             "lirot",
    #             # hebrew_word_nikud
    #             "‬‫לִירוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "стремиться (желать)",
    #             # pronunciation_word
    #             "liʃʾof",
    #             # hebrew_word_nikud
    #             "‫לִשאוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "существовать",
    #             # pronunciation_word
    #             "lehitkayem",
    #             # hebrew_word_nikud
    #             "‫לְהִתקַייֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сушить",
    #             # pronunciation_word
    #             "leyabeʃ",
    #             # hebrew_word_nikud
    #             "‫לְייַבֵּש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "терпеть (боль и т.п.)",
    #             # pronunciation_word
    #             "lisbol",
    #             # hebrew_word_nikud
    #             "‫לִסבּוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "терять",
    #             # pronunciation_word
    #             "leʾabed",
    #             # hebrew_word_nikud
    #             "‫לְאַבֵּד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "торопиться",
    #             # pronunciation_word
    #             "lemaher",
    #             # hebrew_word_nikud
    #             "‫לְמַהֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "требовать",
    #             # pronunciation_word
    #             "lidroʃ",
    #             # hebrew_word_nikud
    #             "‫לִדרוֹש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тренироваться",
    #             # pronunciation_word
    #             "lehitʾamen",
    #             # hebrew_word_nikud
    #             "‫לְהִתאַמֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "тушить ",
    #             # pronunciation_word
    #             "leχabot",
    #             # hebrew_word_nikud
    #             "‬‫לְכַבּוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "убеждать",
    #             # pronunciation_word
    #             "leʃaχ'neʿa",
    #             # hebrew_word_nikud
    #             "‬‫לְשַכנֵע‬"
    #         ),
    #         (
    #             # translation_word
    #             "убивать",
    #             # pronunciation_word
    #             "laharog",
    #             # hebrew_word_nikud
    #             "‬‫לַהֲרוֹג‬"
    #         ),
    #         (
    #             # translation_word
    #             "убирать (наводить порядок)",
    #             # pronunciation_word
    #             "lesader",
    #             # hebrew_word_nikud
    #             "‫לְסַדֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "удивлять",
    #             # pronunciation_word
    #             "lehaf'tiʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַפתִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "удовлетворять",
    #             # pronunciation_word
    #             "lesapek",
    #             # hebrew_word_nikud
    #             "‫לְסַפֵּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "уезжать",
    #             # pronunciation_word
    #             "laʿazov",
    #             # hebrew_word_nikud
    #             "‫לַעֲזוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ужинать",
    #             # pronunciation_word
    #             "leʾeχol aruχat 'erev",
    #             # hebrew_word_nikud
    #             "לֶאֱכוֹל‬‬ ‫אֲרוּחַת‬ ‫עֶרֶב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "украшать (дом и т.п.)",
    #             # pronunciation_word
    #             "lekaʃet",
    #             # hebrew_word_nikud
    #             "‫לְקַשֵט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "улыбаться",
    #             # pronunciation_word
    #             "leχayeχ",
    #             # hebrew_word_nikud
    #             "‬‫לְחַייֵך‬"
    #         ),
    #         (
    #             # translation_word
    #             "уменьшать",
    #             # pronunciation_word
    #             "lehaktin",
    #             # hebrew_word_nikud
    #             "‫לְהַקטִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "упрекать",
    #             # pronunciation_word
    #             "linzof",
    #             # hebrew_word_nikud
    #             "‫לִנזוֹף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "успокаивать",
    #             # pronunciation_word
    #             "lehar'giʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַרגִיע‬"
    #         ),
    #         (
    #             # translation_word
    #             "уступать",
    #             # pronunciation_word
    #             "levater",
    #             # hebrew_word_nikud
    #             "‫לְווַתֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "участвовать",
    #             # pronunciation_word
    #             "lehiʃtatef",
    #             # hebrew_word_nikud
    #             "‫לְהִשתַתֵף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "фотографировать",
    #             # pronunciation_word
    #             "leʦalem",
    #             # hebrew_word_nikud
    #             "‫לְצַלֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "хвастаться",
    #             # pronunciation_word
    #             "lehitravrev",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתרַברֵב‬"
    #         ),
    #         (
    #             # translation_word
    #             "хотеть",
    #             # pronunciation_word
    #             "lirʦot",
    #             # hebrew_word_nikud
    #             "‫לִרצוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "хранить",
    #             # pronunciation_word
    #             "liʃmor",
    #             # hebrew_word_nikud
    #             "‫לִשמוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чистить",
    #             # pronunciation_word
    #             "lenakot",
    #             # hebrew_word_nikud
    #             "‬‫לְנַקוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "читать",
    #             # pronunciation_word
    #             "likro",
    #             # hebrew_word_nikud
    #             "‫לִקרוֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чувствовать (опасность)",
    #             # pronunciation_word
    #             "laχuʃ",
    #             # hebrew_word_nikud
    #             "‬‫לָחוּש‬"
    #         ),
    #         (
    #             # translation_word
    #             "шутить",
    #             # pronunciation_word
    #             "lehitba'deaχ",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתבַּדֵח‬"
    #         ),
    #     ]
    # ),    
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