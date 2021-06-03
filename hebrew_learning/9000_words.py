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
    #     "11. Самые важные глаголы - 2",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "контролировать",
    #             # pronunciation_word
    #             "liʃlot",
    #             # hebrew_word_nikud
    #             "‫לִשלוֹט‬‬"
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
    #             "купаться (в море и т.п.)",
    #             # pronunciation_word
    #             "lehitraχeʦ",
    #             # hebrew_word_nikud
    #             "‫לְהִתרַחֵץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лететь",
    #             # pronunciation_word
    #             "laʿuf",
    #             # hebrew_word_nikud
    #             "‬‫לָעוּף‬"
    #         ),
    #         (
    #             # translation_word
    #             "ловить",
    #             # pronunciation_word
    #             "litfos",
    #             # hebrew_word_nikud
    #             "‬‫לִתפוֹס‬"
    #         ),
    #         (
    #             # translation_word
    #             "ломать",
    #             # pronunciation_word
    #             "liʃbor",
    #             # hebrew_word_nikud
    #             "‬‫לִשבּוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "любить (кого-л.)",
    #             # pronunciation_word
    #             "leʾehov",
    #             # hebrew_word_nikud
    #             "‫לֶאֱהוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "молиться",
    #             # pronunciation_word
    #             "lehitpalel",
    #             # hebrew_word_nikud
    #             "‫לְהִתפַּלֵל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "молчать",
    #             # pronunciation_word
    #             "liʃtok",
    #             # hebrew_word_nikud
    #             "‬‫לִשתוֹק‬"
    #         ),
    #         (
    #             # translation_word
    #             "мочь",
    #             # pronunciation_word
    #             "yaχol",
    #             # hebrew_word_nikud
    #             "‬‫יָכוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "наблюдать",
    #             # pronunciation_word
    #             "liʦpot,",
    #             # hebrew_word_nikud
    #             "‫לִצפּוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "наблюдать",
    #             # pronunciation_word
    #             "lehaʃkif",
    #             # hebrew_word_nikud
    #             "‫לְהַשקִיף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "надеяться",
    #             # pronunciation_word
    #             "lekavot",
    #             # hebrew_word_nikud
    #             "‫לְקַווֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "наказывать",
    #             # pronunciation_word
    #             "lehaʿaniʃ",
    #             # hebrew_word_nikud
    #             "‬‫לְהַעֲנִיש‬"
    #         ),
    #         (
    #             # translation_word
    #             "настаивать (упорствовать)",
    #             # pronunciation_word
    #             "lehitʿakeʃ",
    #             # hebrew_word_nikud
    #             "‫לְהִתעַקֵש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "находить",
    #             # pronunciation_word
    #             "limʦo",
    #             # hebrew_word_nikud
    #             "‫לִמצוֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "начинать",
    #             # pronunciation_word
    #             "lehatχil",
    #             # hebrew_word_nikud
    #             "‫לְהַתחִיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "недооценивать",
    #             # pronunciation_word
    #             "lehamʿit be'ʿereχ",
    #             # hebrew_word_nikud
    #             "‬לְהַמעִיט‬ ‫בְּעֵרֶך‬"
    #         ),
    #         (
    #             # translation_word
    #             "нравиться",
    #             # pronunciation_word
    #             "limʦo χen beʿei'nayim",
    #             # hebrew_word_nikud
    #             "‬לִמצוֹא‬ ‫חֵן‬ ‫בְּעֵינַיִים‬"
    #         ),
    #         (
    #             # translation_word
    #             "обедать",
    #             # pronunciation_word
    #             "leʾeχol aruχat ʦaha'rayim",
    #             # hebrew_word_nikud
    #             "לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‫צָהֳרַיִים‬‬"
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
    #             "обманывать",
    #             # pronunciation_word
    #             "leramot",
    #             # hebrew_word_nikud
    #             "‫לְרַמוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "обсуждать",
    #             # pronunciation_word
    #             "ladun",
    #             # hebrew_word_nikud
    #             "‬‫לָדוּן‬"
    #         ),
    #         (
    #             # translation_word
    #             "объединять",
    #             # pronunciation_word
    #             "leʾaχed",
    #             # hebrew_word_nikud
    #             "‫לְאַחֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "объяснять",
    #             # pronunciation_word
    #             "lehasbir",
    #             # hebrew_word_nikud
    #             "‫לְהַסבִּיר‬‬"
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
    #             "освобождать (город)",
    #             # pronunciation_word
    #             "leʃaχrer",
    #             # hebrew_word_nikud
    #             "‬‫לְשַחרֵר‬"
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
    #             "останавливаться",
    #             # pronunciation_word
    #             "laʿaʦor",
    #             # hebrew_word_nikud
    #             "‫לַעֲצוֹר‬‬"
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
    #             "отгадать",
    #             # pronunciation_word
    #             "lenaχeʃ",
    #             # hebrew_word_nikud
    #             "‬‫לְנַחֵש‬"
    #         ),
    #         (
    #             # translation_word
    #             "отказываться",
    #             # pronunciation_word
    #             "lesarev",
    #             # hebrew_word_nikud
    #             "‬‫לְסָרֵב‬"
    #         ),
    #         (
    #             # translation_word
    #             "открывать (дверь и т.п.)",
    #             # pronunciation_word
    #             "lif'toaχ",
    #             # hebrew_word_nikud
    #             "‫‫לִפתו‬ח‬‫‬"
    #         ),
    #         (
    #             # translation_word
    #             "отправлять",
    #             # pronunciation_word
    #             "liʃ'loaχ",
    #             # hebrew_word_nikud
    #             "‫לִשלוֹח‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "охотиться",
    #             # pronunciation_word
    #             "laʦud",
    #             # hebrew_word_nikud
    #             "‫לָצוּד‬‬"
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
    #     "12. Самые важные глаголы - 3",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "падать",
    #             # pronunciation_word
    #             "lipol",
    #             # hebrew_word_nikud
    #             "‫לִיפּוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "переводить (текст)",
    #             # pronunciation_word
    #             "letargem",
    #             # hebrew_word_nikud
    #             "‬‫לְתַרגֵם‬"
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
    #             "‫לְתַכנֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "платить",
    #             # pronunciation_word
    #             "leʃalem",
    #             # hebrew_word_nikud
    #             "‬‫לְשַלֵם‬"
    #         ),
    #         (
    #             # translation_word
    #             "поворачивать",
    #             # pronunciation_word
    #             "lifnot",
    #             # hebrew_word_nikud
    #             "‬‫לִפנוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "повторять",
    #             # pronunciation_word
    #             "laχazor al",
    #             # hebrew_word_nikud
    #             "לַחֲזוֹר‬ ‫עַל‬‬"
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
    #             "подсказать (отгадку)",
    #             # pronunciation_word
    #             "lirmoz",
    #             # hebrew_word_nikud
    #             "‬‫לִרמוֹז‬"
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
    #             "предвидеть (ожидать)",
    #             # pronunciation_word
    #             "laχazot",
    #             # hebrew_word_nikud
    #             "‫לַחֲזוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предлагать",
    #             # pronunciation_word
    #             "leha'ʦiʿa",
    #             # hebrew_word_nikud
    #             "‬‫לְהַצִיע‬"
    #         ),
    #         (
    #             # translation_word
    #             "предпочитать",
    #             # pronunciation_word
    #             "lehaʿadif",
    #             # hebrew_word_nikud
    #             "‫לְהַעֲדִיף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "предупреждать",
    #             # pronunciation_word
    #             "lehazhir",
    #             # hebrew_word_nikud
    #             "‫לְהַזהִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прекращать",
    #             # pronunciation_word
    #             "lehafsik",
    #             # hebrew_word_nikud
    #             "‫לְהַפסִיק‬‬"
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
    #             "приезжать",
    #             # pronunciation_word
    #             "leha'giʿa",
    #             # hebrew_word_nikud
    #             "‫לְהַגִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "приказывать",
    #             # pronunciation_word
    #             "lifkod",
    #             # hebrew_word_nikud
    #             "‫לִפקוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "принадлежать",
    #             # pronunciation_word
    #             "lehiʃtayeχ",
    #             # hebrew_word_nikud
    #             "‫לְהִשתַייֵך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пробовать (пытаться)",
    #             # pronunciation_word
    #             "lenasot",
    #             # hebrew_word_nikud
    #             "‬‫לְנַסוֹת‬"
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
    #             "продолжать",
    #             # pronunciation_word
    #             "lehamʃiχ",
    #             # hebrew_word_nikud
    #             "‫לְהַמשִיך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "произносить (слово)",
    #             # pronunciation_word
    #             "levate",
    #             # hebrew_word_nikud
    #             "‬‫לְבַטֵא‬"
    #         ),
    #         (
    #             # translation_word
    #             "пропускать (занятия и т.п.)",
    #             # pronunciation_word
    #             "lehaχsir",
    #             # hebrew_word_nikud
    #             "‫לְהַחסִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "просить",
    #             # pronunciation_word
    #             "levakeʃ",
    #             # hebrew_word_nikud
    #             "‬‫לְבַקֵש‬"
    #         ),
    #         (
    #             # translation_word
    #             "прощать",
    #             # pronunciation_word
    #             "lis'loaχ",
    #             # hebrew_word_nikud
    #             "‬‫לִסלוֹח‬"
    #         ),
    #         (
    #             # translation_word
    #             "прятать",
    #             # pronunciation_word
    #             "lehastir",
    #             # hebrew_word_nikud
    #             "‫לְהַסתִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "путать (ошибаться)",
    #             # pronunciation_word
    #             "lehitbalbel",
    #             # hebrew_word_nikud
    #             "‫לְהִתבַּלבֵּל‬"
    #         ),
    #         (
    #             # translation_word
    #             "работать",
    #             # pronunciation_word
    #             "laʿavod",
    #             # hebrew_word_nikud
    #             "‫לַעֲבוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "разрешать",
    #             # pronunciation_word
    #             "leharʃot",
    #             # hebrew_word_nikud
    #             "‫לְהַרשוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рассчитывать на …",
    #             # pronunciation_word
    #             "lismoχ al",
    #             # hebrew_word_nikud
    #             "לִסמוֹך‬ ‫עַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "резервировать",
    #             # pronunciation_word
    #             "lehazmin meroʃ",
    #             # hebrew_word_nikud
    #             "‬לְהַזמִין‬ ‫מֵרֹאש‬"
    #         ),
    #         (
    #             # translation_word
    #             "рекомендовать",
    #             # pronunciation_word
    #             "lehamliʦ",
    #             # hebrew_word_nikud
    #             "‬‫לְהַמלִיץ‬"
    #         ),
    #         (
    #             # translation_word
    #             "ронять",
    #             # pronunciation_word
    #             "lehapil",
    #             # hebrew_word_nikud
    #             "‫לְהַפִּיל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ругать",
    #             # pronunciation_word
    #             "linzof",
    #             # hebrew_word_nikud
    #             "‬‫לִנזוֹף‬"
    #         ),
    #         (
    #             # translation_word
    #             "руководить (чем-л.)",
    #             # pronunciation_word
    #             "lenahel",
    #             # hebrew_word_nikud
    #             "‬‫לְנַהֵל‬"
    #         ),
    #         (
    #             # translation_word
    #             "рыть",
    #             # pronunciation_word
    #             "laχpor",
    #             # hebrew_word_nikud
    #             "‬‫לַחפּוֹר‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "13. Самые важные глаголы - 4",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "садиться",
    #             # pronunciation_word
    #             "lehityaʃev",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתייַשֵב‬"
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
    #             "следовать за …",
    #             # pronunciation_word
    #             "laʿakov aχarei",
    #             # hebrew_word_nikud
    #             "לַעֲקוֹב‬ ‫אַחֲרֵי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слышать",
    #             # pronunciation_word
    #             "liʃ'moʿa",
    #             # hebrew_word_nikud
    #             "‬‫לִשמוֹע‬"
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
    #             "снимать (напр. квартиру)",
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
    #             "‬‫לְייַעֵץ‬"
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
    #             "сожалеть",
    #             # pronunciation_word
    #             "lehiʦtaʿer",
    #             # hebrew_word_nikud
    #             "‬‫לְהִצטַעֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "создать",
    #             # pronunciation_word
    #             "liʦor",
    #             # hebrew_word_nikud
    #             "‬‫לִיצוֹר‬"
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
    #             "сохранять",
    #             # pronunciation_word
    #             "liʃmor",
    #             # hebrew_word_nikud
    #             "‫לִשמוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спасать",
    #             # pronunciation_word
    #             "lehaʦil",
    #             # hebrew_word_nikud
    #             "‬‫לְהַצִיל‬"
    #         ),
    #         (
    #             # translation_word
    #             "спрашивать",
    #             # pronunciation_word
    #             "liʃʾol",
    #             # hebrew_word_nikud
    #             "‫לִשאוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "спускаться",
    #             # pronunciation_word
    #             "la'redet",
    #             # hebrew_word_nikud
    #             "‫לָרֶדֶת‬‬"
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
    #             "стоить",
    #             # pronunciation_word
    #             "laʿalot",
    #             # hebrew_word_nikud
    #             "‬‫לַעֲלוֹת‬"
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
    #             "существовать",
    #             # pronunciation_word
    #             "lehitkayem",
    #             # hebrew_word_nikud
    #             "‬‫לְהִתקַייֵם‬"
    #         ),
    #         (
    #             # translation_word
    #             "считать (подсчитывать)",
    #             # pronunciation_word
    #             "lispor",
    #             # hebrew_word_nikud
    #             "‫לִספּוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "торопиться",
    #             # pronunciation_word
    #             "lemaher",
    #             # hebrew_word_nikud
    #             "‬‫לְמַהֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "требовать",
    #             # pronunciation_word
    #             "lidroʃ",
    #             # hebrew_word_nikud
    #             "‬‫לִדרוֹש‬"
    #         ),
    #         (
    #             # translation_word
    #             "требоваться",
    #             # pronunciation_word
    #             "lehidareʃ",
    #             # hebrew_word_nikud
    #             "‬‫לְהִידָרֵש‬"
    #         ),
    #         (
    #             # translation_word
    #             "трогать",
    #             # pronunciation_word
    #             "la'gaʿat",
    #             # hebrew_word_nikud
    #             "‫לָגַעַת‬‬"
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
    #             "угрожать",
    #             # pronunciation_word
    #             "leʾayem",
    #             # hebrew_word_nikud
    #             "‫לְאַייֵם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "удивляться",
    #             # pronunciation_word
    #             "lehitpale",
    #             # hebrew_word_nikud
    #             "‫לְהִתפַּלֵא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ужинать",
    #             # pronunciation_word
    #             "leʾeχol aruχat 'erev",
    #             # hebrew_word_nikud
    #             "‬לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‫עֶרֶב‬"
    #         ),
    #         (
    #             # translation_word
    #             "украшать",
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
    #             "‫לְחַייֵך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "упоминать",
    #             # pronunciation_word
    #             "lehazkir",
    #             # hebrew_word_nikud
    #             "‫לְהַזכִּיר‬‬"
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
    #             "хотеть есть",
    #             # pronunciation_word
    #             "lihyot raʿev",
    #             # hebrew_word_nikud
    #             "‬לִהיוֹת‬ ‫רָעֵב‬"
    #         ),
    #         (
    #             # translation_word
    #             "хотеть пить",
    #             # pronunciation_word
    #             "lihyot ʦame",
    #             # hebrew_word_nikud
    #             "‬לִהיוֹת‬ ‫צָמֵא‬"
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
    #             "шутить",
    #             # pronunciation_word
    #             "lehitba'deaχ",
    #             # hebrew_word_nikud
    #             "‫לְהִתבַּדֵח‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "14. Цвета",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "цвет",
    #             # pronunciation_word
    #             "'ʦeva",
    #             # hebrew_word_nikud
    #             "‬‫צֶבַע‬"
    #         ),
    #         (
    #             # translation_word
    #             "радуга",
    #             # pronunciation_word
    #             "'keʃet",
    #             # hebrew_word_nikud
    #             "‬‫קֶשֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "белый",
    #             # pronunciation_word
    #             "lavan",
    #             # hebrew_word_nikud
    #             "‫לָבָן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чёрный",
    #             # pronunciation_word
    #             "ʃaχor",
    #             # hebrew_word_nikud
    #             "‬‫שָחוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "серый",
    #             # pronunciation_word
    #             "afor",
    #             # hebrew_word_nikud
    #             "‫אֲפוֹר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зелёный",
    #             # pronunciation_word
    #             "yarok",
    #             # hebrew_word_nikud
    #             "‫יָרוֹק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "жёлтый",
    #             # pronunciation_word
    #             "ʦahov",
    #             # hebrew_word_nikud
    #             "‫צָהוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "красный",
    #             # pronunciation_word
    #             "adom",
    #             # hebrew_word_nikud
    #             "‫אָדוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "синий",
    #             # pronunciation_word
    #             "kaχol",
    #             # hebrew_word_nikud
    #             "‬‫כָּחוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "голубой",
    #             # pronunciation_word
    #             "taχol",
    #             # hebrew_word_nikud
    #             "‬‫תָכוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "розовый",
    #             # pronunciation_word
    #             "varod",
    #             # hebrew_word_nikud
    #             "‫וָרוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "оранжевый",
    #             # pronunciation_word
    #             "katom",
    #             # hebrew_word_nikud
    #             "‬‫כָּתוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "фиолетовый",
    #             # pronunciation_word
    #             "segol",
    #             # hebrew_word_nikud
    #             "‬‫סֶגוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "коричневый",
    #             # pronunciation_word
    #             "χum",
    #             # hebrew_word_nikud
    #             "‫חוּם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "золотой",
    #             # pronunciation_word
    #             "zahov",
    #             # hebrew_word_nikud
    #             "‬‫זָהוֹב‬"
    #         ),
    #         (
    #             # translation_word
    #             "серебристый",
    #             # pronunciation_word
    #             "kasuf",
    #             # hebrew_word_nikud
    #             "‬‫כָּסוּף‬"
    #         ),
    #         (
    #             # translation_word
    #             "светлый",
    #             # pronunciation_word
    #             "bahir",
    #             # hebrew_word_nikud
    #             "‬‫בָּהִיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "тёмный",
    #             # pronunciation_word
    #             "kehe",
    #             # hebrew_word_nikud
    #             "‬‫כֵּהֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "яркий",
    #             # pronunciation_word
    #             "bohek",
    #             # hebrew_word_nikud
    #             "‫בּוֹהֵק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "цветной (карандаш, (фильм))",
    #             # pronunciation_word
    #             "ʦivʿoni",
    #             # hebrew_word_nikud
    #             "‫צִבעוֹנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "чёрно-белый",
    #             # pronunciation_word
    #             "ʃaχor lavan",
    #             # hebrew_word_nikud
    #             "‬‫שָחוֹר־לָבָן‬"
    #         ),
    #         (
    #             # translation_word
    #             "разноцветный",
    #             # pronunciation_word
    #             "sasgoni",
    #             # hebrew_word_nikud
    #             "‬‫סַסגוֹנִי‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "15. Вопросы",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Кто?",
    #             # pronunciation_word
    #             "mi?",
    #             # hebrew_word_nikud
    #             "?‫מִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Что?",
    #             # pronunciation_word
    #             "ma?",
    #             # hebrew_word_nikud
    #             "‬?‫מָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Где?",
    #             # pronunciation_word
    #             "'eifo?",
    #             # hebrew_word_nikud
    #             "‬?‫אֵיפֹה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Куда?",
    #             # pronunciation_word
    #             "leʾan?",
    #             # hebrew_word_nikud
    #             "‬?‫לְאָן‬"
    #         ),
    #         (
    #             # translation_word
    #             "Откуда?",
    #             # pronunciation_word
    #             "me'ʾeifo?",
    #             # hebrew_word_nikud
    #             "?‫מֵאֵיפֹה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Когда?",
    #             # pronunciation_word
    #             "matai?",
    #             # hebrew_word_nikud
    #             "?‫מָתַי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Зачем?",
    #             # pronunciation_word
    #             "'lama?",
    #             # hebrew_word_nikud
    #             "‬?‫לָמָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Почему?",
    #             # pronunciation_word
    #             "ma'duʿa?",
    #             # hebrew_word_nikud
    #             "?ַ‫מַדוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Для чего?",
    #             # pronunciation_word
    #             "biʃvil ma?",
    #             # hebrew_word_nikud
    #             "‬בִּשבִיל‬ ‫מָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Как?",
    #             # pronunciation_word
    #             "eiχ",
    #             # hebrew_word_nikud
    #             "‫אֵיך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Как?",
    #             # pronunciation_word
    #             "keiʦad",
    #             # hebrew_word_nikud
    #             "‫כֵּיצַד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Какой? Который?",
    #             # pronunciation_word
    #             "'eize?",
    #             # hebrew_word_nikud
    #             "‬?‫אֵיזֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Кому?",
    #             # pronunciation_word
    #             "lemi?",
    #             # hebrew_word_nikud
    #             "‬?‫לְמִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "О ком?",
    #             # pronunciation_word
    #             "al mi?",
    #             # hebrew_word_nikud
    #             "עַל‬ ‫מִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "О чём?",
    #             # pronunciation_word
    #             "al ma?",
    #             # hebrew_word_nikud
    #             "‬עַל‬ ‫מַה‬"
    #         ),
    #         (
    #             # translation_word
    #             "С кем?",
    #             # pronunciation_word
    #             "im mi?",
    #             # hebrew_word_nikud
    #             "עִם‬ ‫מִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "Сколько?",
    #             # pronunciation_word
    #             "'kama?",
    #             # hebrew_word_nikud
    #             "‬?‫כַּמָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "Чей? Чья? Чьи?",
    #             # pronunciation_word
    #             "ʃel mi?",
    #             # hebrew_word_nikud
    #             "שֶל‬ ‫מִי‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "16. Основные предлоги",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "с … (с кем-л.)",
    #             # pronunciation_word
    #             "im",
    #             # hebrew_word_nikud
    #             "‬‫עִם‬"
    #         ),
    #         (
    #             # translation_word
    #             "без",
    #             # pronunciation_word
    #             "bli",
    #             # hebrew_word_nikud
    #             "‫בּלִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "без",
    #             # pronunciation_word
    #             "lelo",
    #             # hebrew_word_nikud
    #             "‫לְלֹא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "в (предлог движения)",
    #             # pronunciation_word
    #             "le…",
    #             # hebrew_word_nikud
    #             "‬…ְ‫ל‬"
    #         ),
    #         (
    #             # translation_word
    #             "о (говорить о …)",
    #             # pronunciation_word
    #             "al",
    #             # hebrew_word_nikud
    #             "‫עַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "перед (во времени, в пространстве)",
    #             # pronunciation_word
    #             "lifnei",
    #             # hebrew_word_nikud
    #             "‬‫לִפנֵי‬"
    #         ),
    #         (
    #             # translation_word
    #             "под (внизу)",
    #             # pronunciation_word
    #             "mi'taχat le…",
    #             # hebrew_word_nikud
    #             "מִתַחַת‬ ‫ל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "над (наверху)",
    #             # pronunciation_word
    #             "meʿal",
    #             # hebrew_word_nikud
    #             "‫מֵעַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "на (на чём-то)",
    #             # pronunciation_word
    #             "al",
    #             # hebrew_word_nikud
    #             "‫עַל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "из (откуда-то, о материале)",
    #             # pronunciation_word
    #             "mi, me",
    #             # hebrew_word_nikud
    #             "‬מ‬"
    #         ),
    #         (
    #             # translation_word
    #             "через … (о времени)",
    #             # pronunciation_word
    #             "toχ",
    #             # hebrew_word_nikud
    #             "‫תוֹך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "через (о препятствии)",
    #             # pronunciation_word
    #             "'dereχ",
    #             # hebrew_word_nikud
    #             "‬‫דֶרֶך‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "17. Вводные и служебные слова. Наречия - 1",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "здесь",
    #             # pronunciation_word
    #             "po",
    #             # hebrew_word_nikud
    #             "‫פֹּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "здесь",
    #             # pronunciation_word
    #             "kan",
    #             # hebrew_word_nikud
    #             "‫כָּאן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "там",
    #             # pronunciation_word
    #             "ʃam",
    #             # hebrew_word_nikud
    #             "‫שָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "где-то",
    #             # pronunciation_word
    #             "'eifo ʃehu",
    #             # hebrew_word_nikud
    #             "‬אֵיפֹה‬ ‫שֶהוּא‬"
    #         ),
    #         (
    #             # translation_word
    #             "нигде",
    #             # pronunciation_word
    #             "beʃum makom",
    #             # hebrew_word_nikud
    #             "‬בְּשוּם‬ ‫מָקוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "у … (около)",
    #             # pronunciation_word
    #             "leyad …",
    #             # hebrew_word_nikud
    #             "‫לְיַד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "у окна",
    #             # pronunciation_word
    #             "leyad haχalon",
    #             # hebrew_word_nikud
    #             "לְיַד‬ ‫הַחַלוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сюда",
    #             # pronunciation_word
    #             "'hena",
    #             # hebrew_word_nikud
    #             "‬‫הֵנָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "сюда",
    #             # pronunciation_word
    #             "lekan",
    #             # hebrew_word_nikud
    #             "‫לְכָאן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "туда",
    #             # pronunciation_word
    #             "leʃam",
    #             # hebrew_word_nikud
    #             "‫לְשָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "отсюда",
    #             # pronunciation_word
    #             "mikan",
    #             # hebrew_word_nikud
    #             "‫מִכָּאן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "оттуда",
    #             # pronunciation_word
    #             "miʃam",
    #             # hebrew_word_nikud
    #             "‬‫מִשָם‬"
    #         ),
    #         (
    #             # translation_word
    #             "близко",
    #             # pronunciation_word
    #             "karov",
    #             # hebrew_word_nikud
    #             "‫קָרוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "далеко",
    #             # pronunciation_word
    #             "raχok",
    #             # hebrew_word_nikud
    #             "‬‫רָחוֹק‬"
    #         ),
    #         (
    #             # translation_word
    #             "около (рядом)",
    #             # pronunciation_word
    #             "leyad",
    #             # hebrew_word_nikud
    #             "‬‫לְיַד‬"
    #         ),
    #         (
    #             # translation_word
    #             "недалеко (ехать, идти)",
    #             # pronunciation_word
    #             "lo raχok",
    #             # hebrew_word_nikud
    #             "‬לֹא‬ ‫רָחוֹק‬"
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
    #             "слева",
    #             # pronunciation_word
    #             "mismol",
    #             # hebrew_word_nikud
    #             "‫מִשׂמֹאל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "налево",
    #             # pronunciation_word
    #             "'smola",
    #             # hebrew_word_nikud
    #             "‫שׂמֹאלָה‬‬"
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
    #             "справа",
    #             # pronunciation_word
    #             "miyamin",
    #             # hebrew_word_nikud
    #             "‫מִיָמִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "направо",
    #             # pronunciation_word
    #             "ya'mina",
    #             # hebrew_word_nikud
    #             "‬‫יָמִינָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "спереди",
    #             # pronunciation_word
    #             "mika'dima",
    #             # hebrew_word_nikud
    #             "‬‫מִקָדִימָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "передний",
    #             # pronunciation_word
    #             "kidmi",
    #             # hebrew_word_nikud
    #             "‬‫קִדמִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "вперёд (движение)",
    #             # pronunciation_word
    #             "ka'dima",
    #             # hebrew_word_nikud
    #             "‫קָדִימָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сзади (находиться, подойти)",
    #             # pronunciation_word
    #             "meʾaχor",
    #             # hebrew_word_nikud
    #             "‬‫מֵאָחוֹר‬"
    #         ),
    #         (
    #             # translation_word
    #             "назад (движение)",
    #             # pronunciation_word
    #             "a'χora",
    #             # hebrew_word_nikud
    #             "‫אָחוֹרָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "середина",
    #             # pronunciation_word
    #             "'emʦa",
    #             # hebrew_word_nikud
    #             "‫אֶמצַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "посередине",
    #             # pronunciation_word
    #             "ba'ʾemʦa",
    #             # hebrew_word_nikud
    #             "‫בָּאֶמצַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сбоку (со стороны)",
    #             # pronunciation_word
    #             "mehaʦad",
    #             # hebrew_word_nikud
    #             "‫מֵהַצַד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "везде",
    #             # pronunciation_word
    #             "beχol makom",
    #             # hebrew_word_nikud
    #             "בְּכָל‬ ‫מָקוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вокруг",
    #             # pronunciation_word
    #             "misaviv",
    #             # hebrew_word_nikud
    #             "‬‫מִסָבִיב‬"
    #         ),
    #         (
    #             # translation_word
    #             "изнутри",
    #             # pronunciation_word
    #             "mibifnim",
    #             # hebrew_word_nikud
    #             "‫מִבִּפנִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "куда-то",
    #             # pronunciation_word
    #             "leʾan ʃehu",
    #             # hebrew_word_nikud
    #             "לְאָן‬ ‬‫שֶהוּא‬"
    #         ),
    #         (
    #             # translation_word
    #             "обратно",
    #             # pronunciation_word
    #             "baχazara",
    #             # hebrew_word_nikud
    #             "‬‫בַּחֲזָרָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "во-первых",
    #             # pronunciation_word
    #             "reʃit",
    #             # hebrew_word_nikud
    #             "‫רֵאשִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "во-вторых",
    #             # pronunciation_word
    #             "ʃenit",
    #             # hebrew_word_nikud
    #             "‫שֵנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "в-третьих",
    #             # pronunciation_word
    #             "ʃliʃit",
    #             # hebrew_word_nikud
    #             "‫שלִִישִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "заново",
    #             # pronunciation_word
    #             "meχadaʃ",
    #             # hebrew_word_nikud
    #             "‬‫מֵחָדָש‬"
    #         ),
    #         (
    #             # translation_word
    #             "никогда",
    #             # pronunciation_word
    #             "af 'paʿam",
    #             # hebrew_word_nikud
    #             "אַף‬ ‫פַּעַם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "никогда",
    #             # pronunciation_word
    #             "meʿolam",
    #             # hebrew_word_nikud
    #             "‬‫מֵעוֹלָם‬"
    #         ),
    #         (
    #             # translation_word
    #             "опять",
    #             # pronunciation_word
    #             "ʃuv",
    #             # hebrew_word_nikud
    #             "‬‫שוּב‬"
    #         ),
    #         (
    #             # translation_word
    #             "теперь",
    #             # pronunciation_word
    #             "aχʃav",
    #             # hebrew_word_nikud
    #             "‬‫עַכשָיו‬"
    #         ),
    #         (
    #             # translation_word
    #             "теперь",
    #             # pronunciation_word
    #             "kaʿet",
    #             # hebrew_word_nikud
    #             "‫כָּעֵת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "часто",
    #             # pronunciation_word
    #             "leʿitim krovot",
    #             # hebrew_word_nikud
    #             "‬לְעִיתִים‬ ‫קרוֹבוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "тогда",
    #             # pronunciation_word
    #             "az",
    #             # hebrew_word_nikud
    #             "‬‫אָז‬"
    #         ),
    #         (
    #             # translation_word
    #             "срочно",
    #             # pronunciation_word
    #             "bidχifut",
    #             # hebrew_word_nikud
    #             "‬‫בִּדחִיפוּת‬"
    #         ),
    #         (
    #             # translation_word
    #             "обычно",
    #             # pronunciation_word
    #             "be'dereχ klal",
    #             # hebrew_word_nikud
    #             "בְּדֶרֶך‬ ‫כּלָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кстати, …",
    #             # pronunciation_word
    #             "'dereχ 'agav",
    #             # hebrew_word_nikud
    #             "‬דֶרֶך‬ ‫אַגַב‬"
    #         ),
    #         (
    #             # translation_word
    #             "возможно",
    #             # pronunciation_word
    #             "efʃari",
    #             # hebrew_word_nikud
    #             "‫אֶפשָרִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вероятно",
    #             # pronunciation_word
    #             "kanirʾe",
    #             # hebrew_word_nikud
    #             "‫כַּנִראֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "может быть",
    #             # pronunciation_word
    #             "ulai",
    #             # hebrew_word_nikud
    #             "‫אוּלַי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кроме того, …",
    #             # pronunciation_word
    #             "χuʦ mize …",
    #             # hebrew_word_nikud
    #             "חוּץ‬ ‫מִזֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поэтому …",
    #             # pronunciation_word
    #             "laχen",
    #             # hebrew_word_nikud
    #             "‬‫לָכֵן‬"
    #         ),
    #         (
    #             # translation_word
    #             "несмотря на …",
    #             # pronunciation_word
    #             "lamrot …",
    #             # hebrew_word_nikud
    #             "‬‫לַמרוֹת‬"
    #         ),
    #         (
    #             # translation_word
    #             "благодаря …",
    #             # pronunciation_word
    #             "hodot le…",
    #             # hebrew_word_nikud
    #             "‬הוֹדוֹת‬ ‫ל‬"
    #         ),
    #         (
    #             # translation_word
    #             "что (союз)",
    #             # pronunciation_word
    #             "ʃe",
    #             # hebrew_word_nikud
    #             "‫ש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "что-то, что-нибудь",
    #             # pronunciation_word
    #             "'maʃehu",
    #             # hebrew_word_nikud
    #             "‫מַשֶהו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ничего",
    #             # pronunciation_word
    #             "klum",
    #             # hebrew_word_nikud
    #             "‬‫כּלוּם‬"
    #         ),
    #         (
    #             # translation_word
    #             "кто-то, кто-нибудь (м.р.)",
    #             # pronunciation_word
    #             "'miʃehu",
    #             # hebrew_word_nikud
    #             "‫מִישֶהו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кто-то, кто-нибудь (ж.р.)",
    #             # pronunciation_word
    #             "'miʃehi",
    #             # hebrew_word_nikud
    #             "‫מִישֶהִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "никто (м.р.)",
    #             # pronunciation_word
    #             "af eχad",
    #             # hebrew_word_nikud
    #             "‬אַף‬ ‫אֶחָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "никто (ж.р.)",
    #             # pronunciation_word
    #             "af aχat",
    #             # hebrew_word_nikud
    #             "‬אַף‬ ‫אַחַת‬"
    #         ),
    #         (
    #             # translation_word
    #             "никуда",
    #             # pronunciation_word
    #             "leʃum makom",
    #             # hebrew_word_nikud
    #             "לְשוּם‬ ‫מָקוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "так",
    #             # pronunciation_word
    #             "kol kaχ",
    #             # hebrew_word_nikud
    #             "‫כָּל־כָּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "также, тоже",
    #             # pronunciation_word
    #             "gam",
    #             # hebrew_word_nikud
    #             "‫גַם‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "18. Вводные и служебные слова. Наречия - 2",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "Почему?",
    #             # pronunciation_word
    #             "ma'duʿa?",
    #             # hebrew_word_nikud
    #             "?ַ‫מַדוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "почему-то",
    #             # pronunciation_word
    #             "miʃum ma",
    #             # hebrew_word_nikud
    #             "‫מִשוּם־מָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "потому, что …",
    #             # pronunciation_word
    #             "miʃum ʃe",
    #             # hebrew_word_nikud
    #             "מִשוּם‬ ‫ש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зачем-то",
    #             # pronunciation_word
    #             "lematara 'kolʃehi",
    #             # hebrew_word_nikud
    #             "לְמַטָרָה‬ ‫כָּלשֶהִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "и",
    #             # pronunciation_word
    #             "ve …",
    #             # hebrew_word_nikud
    #             "‬ְ‫ו‬"
    #         ),
    #         (
    #             # translation_word
    #             "или",
    #             # pronunciation_word
    #             "o",
    #             # hebrew_word_nikud
    #             "‬‫או‬"
    #         ),
    #         (
    #             # translation_word
    #             "но",
    #             # pronunciation_word
    #             "ulam",
    #             # hebrew_word_nikud
    #             "‫אוּלָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "но",
    #             # pronunciation_word
    #             "aval",
    #             # hebrew_word_nikud
    #             "‫אֲבָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "для (предлог)",
    #             # pronunciation_word
    #             "biʃvil",
    #             # hebrew_word_nikud
    #             "‬‫בִּשבִיל‬"
    #         ),
    #         (
    #             # translation_word
    #             "слишком",
    #             # pronunciation_word
    #             "yoter midai",
    #             # hebrew_word_nikud
    #             "‬‫מִדַי‬ ‫יוֹתֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "только",
    #             # pronunciation_word
    #             "rak",
    #             # hebrew_word_nikud
    #             "‬‫רַק‬"
    #         ),
    #         (
    #             # translation_word
    #             "точно",
    #             # pronunciation_word
    #             "bediyuk",
    #             # hebrew_word_nikud
    #             "‬‫בְּדִיוּק‬"
    #         ),
    #         (
    #             # translation_word
    #             "около (~ 10 кг), приблизительно",
    #             # pronunciation_word
    #             "be'ʿereχ",
    #             # hebrew_word_nikud
    #             "‬‫בְּעֵרֶך‬"
    #         ),
    #         (
    #             # translation_word
    #             "почти",
    #             # pronunciation_word
    #             "kimʿat",
    #             # hebrew_word_nikud
    #             "‫כִּמעַט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "другой (второй), другой (иной)",
    #             # pronunciation_word
    #             "aχer",
    #             # hebrew_word_nikud
    #             "‫אַחֵר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "каждый",
    #             # pronunciation_word
    #             "kol",
    #             # hebrew_word_nikud
    #             "‫כֹּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "любой",
    #             # pronunciation_word
    #             "kolʃehu",
    #             # hebrew_word_nikud
    #             "‫כָּלשֶהו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "много",
    #             # pronunciation_word
    #             "harbe",
    #             # hebrew_word_nikud
    #             "‬‫הַרבֵּה‬"
    #         ),
    #         (
    #             # translation_word
    #             "все (все люди)",
    #             # pronunciation_word
    #             "kulam",
    #             # hebrew_word_nikud
    #             "‫כּוּלָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вручную",
    #             # pronunciation_word
    #             "bayad",
    #             # hebrew_word_nikud
    #             "‬‫בַּיָד‬"
    #         ),
    #         (
    #             # translation_word
    #             "вряд ли",
    #             # pronunciation_word
    #             "safek im",
    #             # hebrew_word_nikud
    #             "‫אִם‬ ‫סָפֵק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "наверное (вероятно)",
    #             # pronunciation_word
    #             "karov levadai",
    #             # hebrew_word_nikud
    #             "‫לְווַדַאי‬ ‫קָרוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нарочно (намеренно, специально)",
    #             # pronunciation_word
    #             "'davka",
    #             # hebrew_word_nikud
    #             "‫דַווקָא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "случайно",
    #             # pronunciation_word
    #             "bemikre",
    #             # hebrew_word_nikud
    #             "‫בְּמִקרֶה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "очень",
    #             # pronunciation_word
    #             "meʾod",
    #             # hebrew_word_nikud
    #             "‫מְאוֹד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "например",
    #             # pronunciation_word
    #             "lemaʃal",
    #             # hebrew_word_nikud
    #             "‬‫לְמָשָל‬"
    #         ),
    #         (
    #             # translation_word
    #             "между",
    #             # pronunciation_word
    #             "bein",
    #             # hebrew_word_nikud
    #             "‬‫בֵּין‬"
    #         ),
    #         (
    #             # translation_word
    #             "среди",
    #             # pronunciation_word
    #             "be'kerev",
    #             # hebrew_word_nikud
    #             "‬‫בְּקֶרֶב‬"
    #         ),
    #         (
    #             # translation_word
    #             "столько",
    #             # pronunciation_word
    #             "kol kaχ harbe",
    #             # hebrew_word_nikud
    #             "כָּל־כָּך‬ ‫הַרבֵּה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "особенно",
    #             # pronunciation_word
    #             "bimyuχad",
    #             # hebrew_word_nikud
    #             "‬‫בִּמיוּחָד‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "19. Противоположности",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "богатый",
    #             # pronunciation_word
    #             "aʃir",
    #             # hebrew_word_nikud
    #             "‬‫עָשִיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "бедный",
    #             # pronunciation_word
    #             "ani",
    #             # hebrew_word_nikud
    #             "‫עָנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "больной",
    #             # pronunciation_word
    #             "χole",
    #             # hebrew_word_nikud
    #             "‬‫חוֹלֶה‬"
    #         ),
    #         (
    #             # translation_word
    #             "здоровый",
    #             # pronunciation_word
    #             "bari",
    #             # hebrew_word_nikud
    #             "‫בָּרִיא‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "большой",
    #             # pronunciation_word
    #             "gadol",
    #             # hebrew_word_nikud
    #             "‬‫גָדוֹל‬"
    #         ),
    #         (
    #             # translation_word
    #             "маленький",
    #             # pronunciation_word
    #             "katan",
    #             # hebrew_word_nikud
    #             "‫קָטַן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "быстро",
    #             # pronunciation_word
    #             "maher",
    #             # hebrew_word_nikud
    #             "‬‫מַהֵר‬"
    #         ),
    #         (
    #             # translation_word
    #             "медленно",
    #             # pronunciation_word
    #             "leʾat",
    #             # hebrew_word_nikud
    #             "‬‫לְאַט‬"
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
    #             "медленный",
    #             # pronunciation_word
    #             "iti",
    #             # hebrew_word_nikud
    #             "‫אִיטִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "весёлый",
    #             # pronunciation_word
    #             "sa'meaχ",
    #             # hebrew_word_nikud
    #             "‫שָׂמֵח‬‬"
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
    #             "вместе",
    #             # pronunciation_word
    #             "be'yaχad",
    #             # hebrew_word_nikud
    #             "‬‫בְּיַחַד‬"
    #         ),
    #         (
    #             # translation_word
    #             "отдельно",
    #             # pronunciation_word
    #             "levad",
    #             # hebrew_word_nikud
    #             "‫לְבַד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вслух",
    #             # pronunciation_word
    #             "bekol ram",
    #             # hebrew_word_nikud
    #             "בְּקוֹל‬ ‫רָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "про себя (не вслух)",
    #             # pronunciation_word
    #             "belev",
    #             # hebrew_word_nikud
    #             "‫בְּלֵב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "про себя (не вслух)",
    #             # pronunciation_word
    #             "be'ʃeket",
    #             # hebrew_word_nikud
    #             "‫בְּשֶקֶט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "высокий",
    #             # pronunciation_word
    #             "ga'voha",
    #             # hebrew_word_nikud
    #             "‬‫גָבוֹה‬"
    #         ),
    #         (
    #             # translation_word
    #             "низкий",
    #             # pronunciation_word
    #             "namuχ",
    #             # hebrew_word_nikud
    #             "‫נָמוּך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "глубокий",
    #             # pronunciation_word
    #             "amok",
    #             # hebrew_word_nikud
    #             "‬‫עָמוֹק‬"
    #         ),
    #         (
    #             # translation_word
    #             "мелкий",
    #             # pronunciation_word
    #             "radud",
    #             # hebrew_word_nikud
    #             "‫רָדוּד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "да",
    #             # pronunciation_word
    #             "ken",
    #             # hebrew_word_nikud
    #             "‫כֵּן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "нет",
    #             # pronunciation_word
    #             "lo",
    #             # hebrew_word_nikud
    #             "‬‫לֹא‬"
    #         ),
    #         (
    #             # translation_word
    #             "далёкий",
    #             # pronunciation_word
    #             "raχok",
    #             # hebrew_word_nikud
    #             "‬‫רָחוֹק‬"
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
    #             "длинный",
    #             # pronunciation_word
    #             "aroχ",
    #             # hebrew_word_nikud
    #             "‬‫אָרוֹך‬"
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
    #             "добрый",
    #             # pronunciation_word
    #             "tov lev",
    #             # hebrew_word_nikud
    #             "‬טוֹב‬ ‫לֵב‬"
    #         ),
    #         (
    #             # translation_word
    #             "злой",
    #             # pronunciation_word
    #             "raʃa",
    #             # hebrew_word_nikud
    #             "‫רָשָע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "женатый",
    #             # pronunciation_word
    #             "nasui",
    #             # hebrew_word_nikud
    #             "‫נָשׂוּי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "холостой",
    #             # pronunciation_word
    #             "ravak",
    #             # hebrew_word_nikud
    #             "‬‫רַווָק‬"
    #         ),
    #         (
    #             # translation_word
    #             "конец",
    #             # pronunciation_word
    #             "sof",
    #             # hebrew_word_nikud
    #             "‬‫סוֹף‬"
    #         ),
    #         (
    #             # translation_word
    #             "начало",
    #             # pronunciation_word
    #             "hatχala",
    #             # hebrew_word_nikud
    #             "‬‫הַתחָלָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "левый",
    #             # pronunciation_word
    #             "smali",
    #             # hebrew_word_nikud
    #             "‬‫שׂמָאלִי‬"
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
    #             "первый",
    #             # pronunciation_word
    #             "riʃon",
    #             # hebrew_word_nikud
    #             "‫רִאשוֹן‬‬"
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
    #             "прямой",
    #             # pronunciation_word
    #             "yaʃar",
    #             # hebrew_word_nikud
    #             "‬‫יָשָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "кривой",
    #             # pronunciation_word
    #             "meʿukal",
    #             # hebrew_word_nikud
    #             "‫מְעוּקָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рай",
    #             # pronunciation_word
    #             "gan 'eden",
    #             # hebrew_word_nikud
    #             "גַן‬ ‫עֵדֶן‬‬"
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
    #             "сильный",
    #             # pronunciation_word
    #             "χazak",
    #             # hebrew_word_nikud
    #             "‫חָזָק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "слабый",
    #             # pronunciation_word
    #             "χalaʃ",
    #             # hebrew_word_nikud
    #             "‬‫חַלָש‬"
    #         ),
    #         (
    #             # translation_word
    #             "старый",
    #             # pronunciation_word
    #             "zaken",
    #             # hebrew_word_nikud
    #             "‬‫זָקֵן‬"
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
    #             "старый",
    #             # pronunciation_word
    #             "yaʃan",
    #             # hebrew_word_nikud
    #             "‬‫יָשָן‬"
    #         ),
    #         (
    #             # translation_word
    #             "новый",
    #             # pronunciation_word
    #             "χadaʃ",
    #             # hebrew_word_nikud
    #             "‬‫חָדָש‬"
    #         ),
    #         (
    #             # translation_word
    #             "твёрдый",
    #             # pronunciation_word
    #             "kaʃe",
    #             # hebrew_word_nikud
    #             "‬‫קָשֶה‬"
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
    #             "тёплый",
    #             # pronunciation_word
    #             "χamim",
    #             # hebrew_word_nikud
    #             "‬‫חָמִים‬"
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
    #             "толстый",
    #             # pronunciation_word
    #             "ʃamen",
    #             # hebrew_word_nikud
    #             "‫שָמֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "худой",
    #             # pronunciation_word
    #             "raze",
    #             # hebrew_word_nikud
    #             "‬‫רָזֶה‬"
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
    #             "широкий",
    #             # pronunciation_word
    #             "raχav",
    #             # hebrew_word_nikud
    #             "‬‫רָחָב‬"
    #         ),
    #         (
    #             # translation_word
    #             "хороший",
    #             # pronunciation_word
    #             "tov",
    #             # hebrew_word_nikud
    #             "‫טוֹב‬‬"
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
    #             "храбрый",
    #             # pronunciation_word
    #             "amiʦ",
    #             # hebrew_word_nikud
    #             "‫אַמִיץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "трусливый",
    #             # pronunciation_word
    #             "paχdani",
    #             # hebrew_word_nikud
    #             "‫פַּחדָנִי‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "20. Дни недели",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "понедельник",
    #             # pronunciation_word
    #             "yom ʃeni",
    #             # hebrew_word_nikud
    #             "‬יום‬ ‫שֵנִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "вторник",
    #             # pronunciation_word
    #             "yom ʃliʃi",
    #             # hebrew_word_nikud
    #             "יוֹם‬ ‫שלִישִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "среда",
    #             # pronunciation_word
    #             "yom reviʿi",
    #             # hebrew_word_nikud
    #             "יוֹם‬ ‫רְבִיעִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "четверг",
    #             # pronunciation_word
    #             "yom χamiʃi",
    #             # hebrew_word_nikud
    #             "‬יוֹם‬ ‫חֲמִישִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "пятница",
    #             # pronunciation_word
    #             "yom ʃiʃi",
    #             # hebrew_word_nikud
    #             "יוֹם‬ ‫שִישִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "суббота",
    #             # pronunciation_word
    #             "ʃabat",
    #             # hebrew_word_nikud
    #             "‬‫שַבָּת‬"
    #         ),
    #         (
    #             # translation_word
    #             "воскресенье",
    #             # pronunciation_word
    #             "yom riʃon",
    #             # hebrew_word_nikud
    #             "יוֹם‬ ‫רִאשוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сегодня",
    #             # pronunciation_word
    #             "hayom",
    #             # hebrew_word_nikud
    #             "‬‫הַיוֹם‬"
    #         ),
    #         (
    #             # translation_word
    #             "завтра",
    #             # pronunciation_word
    #             "maχar",
    #             # hebrew_word_nikud
    #             "‬‫מָחָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "послезавтра",
    #             # pronunciation_word
    #             "maχara'tayim",
    #             # hebrew_word_nikud
    #             "‫מָחֳרָתַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вчера",
    #             # pronunciation_word
    #             "etmol",
    #             # hebrew_word_nikud
    #             "‫אֶתמוֹל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "позавчера",
    #             # pronunciation_word
    #             "ʃilʃom",
    #             # hebrew_word_nikud
    #             "‫שִלשוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "день",
    #             # pronunciation_word
    #             "yom",
    #             # hebrew_word_nikud
    #             "‫יוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рабочий день",
    #             # pronunciation_word
    #             "yom avoda",
    #             # hebrew_word_nikud
    #             "יום‬ ‫עֲבוֹדָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "праздничный день",
    #             # pronunciation_word
    #             "yom χag",
    #             # hebrew_word_nikud
    #             "‬יוֹם‬ ‫חַג‬"
    #         ),
    #         (
    #             # translation_word
    #             "выходной день",
    #             # pronunciation_word
    #             "yom menuχa",
    #             # hebrew_word_nikud
    #             "יום‬ ‫מְנוּחָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "выходные",
    #             # pronunciation_word
    #             "sof ʃa'vuʿa",
    #             # hebrew_word_nikud
    #             "סוֹף‬ ‫שָבוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "весь день",
    #             # pronunciation_word
    #             "kol hayom",
    #             # hebrew_word_nikud
    #             "כָּל‬ ‫הַיוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ежедневно",
    #             # pronunciation_word
    #             "midei yom",
    #             # hebrew_word_nikud
    #             "מִדֵי‬ ‫יוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "неделя",
    #             # pronunciation_word
    #             "ʃa'vua",
    #             # hebrew_word_nikud
    #             "‬‫שָבוּע‬"
    #         ),
    #         (
    #             # translation_word
    #             "еженедельно",
    #             # pronunciation_word
    #             "kol ʃa'vuʿa",
    #             # hebrew_word_nikud
    #             "‬כָּל‬ ‫שָבוּע‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "21. Часы. Время суток",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "утро",
    #             # pronunciation_word
    #             "'boker",
    #             # hebrew_word_nikud
    #             "‫בּוֹקֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "утром",
    #             # pronunciation_word
    #             "ba'boker",
    #             # hebrew_word_nikud
    #             "‫בַּבּוֹקֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полдень",
    #             # pronunciation_word
    #             "ʦaha'rayim",
    #             # hebrew_word_nikud
    #             "‫צָהֳרַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "после обеда",
    #             # pronunciation_word
    #             "aχar haʦaha'rayim",
    #             # hebrew_word_nikud
    #             "אַחַר‬ ‫הַצָהֳרַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "вечер",
    #             # pronunciation_word
    #             "'erev",
    #             # hebrew_word_nikud
    #             "‬‫עֶרֶב‬"
    #         ),
    #         (
    #             # translation_word
    #             "вечером",
    #             # pronunciation_word
    #             "ba'ʿerev",
    #             # hebrew_word_nikud
    #             "‫בַּעֶרֶב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ночь",
    #             # pronunciation_word
    #             "'laila",
    #             # hebrew_word_nikud
    #             "‫לַילָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ночью",
    #             # pronunciation_word
    #             "ba'laila",
    #             # hebrew_word_nikud
    #             "‬‫בַּלַילָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "полночь",
    #             # pronunciation_word
    #             "χaʦot",
    #             # hebrew_word_nikud
    #             "‫חֲצוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "секунда",
    #             # pronunciation_word
    #             "ʃniya",
    #             # hebrew_word_nikud
    #             "‫שנִייָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "минута",
    #             # pronunciation_word
    #             "daka",
    #             # hebrew_word_nikud
    #             "‬‫דַקָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "час",
    #             # pronunciation_word
    #             "ʃaʿa",
    #             # hebrew_word_nikud
    #             "‫שָעָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полчаса",
    #             # pronunciation_word
    #             "χaʦi ʃaʿa",
    #             # hebrew_word_nikud
    #             "חֲצִי‬ ‫שָעָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "15 минут",
    #             # pronunciation_word
    #             "'reva ʃaʿa",
    #             # hebrew_word_nikud
    #             "רֶבַע‬ ‫שָעָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сутки",
    #             # pronunciation_word
    #             "yemama",
    #             # hebrew_word_nikud
    #             "‬‫יְמָמָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "восход солнца",
    #             # pronunciation_word
    #             "zriχa",
    #             # hebrew_word_nikud
    #             "‫זרִיחָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "закат",
    #             # pronunciation_word
    #             "ʃkiʿa",
    #             # hebrew_word_nikud
    #             "‫שקִיעָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "22. Месяцы. Времена года",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "январь",
    #             # pronunciation_word
    #             "'yanuʾar",
    #             # hebrew_word_nikud
    #             "‫יָנוּאָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "февраль",
    #             # pronunciation_word
    #             "'februʾar",
    #             # hebrew_word_nikud
    #             "‫פֶבּרוּאָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "март",
    #             # pronunciation_word
    #             "merʦ",
    #             # hebrew_word_nikud
    #             "‫מֶרץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "апрель",
    #             # pronunciation_word
    #             "april",
    #             # hebrew_word_nikud
    #             "‬‫אַפּרִיל‬"
    #         ),
    #         (
    #             # translation_word
    #             "май",
    #             # pronunciation_word
    #             "mai",
    #             # hebrew_word_nikud
    #             "‫מַאי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "июнь",
    #             # pronunciation_word
    #             "'yuni",
    #             # hebrew_word_nikud
    #             "‫יוּנִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "июль",
    #             # pronunciation_word
    #             "'yuli",
    #             # hebrew_word_nikud
    #             "‫יוּלִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "август",
    #             # pronunciation_word
    #             "'ogust",
    #             # hebrew_word_nikud
    #             "‫אוֹגוּסט‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сентябрь",
    #             # pronunciation_word
    #             "sep'tember",
    #             # hebrew_word_nikud
    #             "‫סֶפּטֶמבֶּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "октябрь",
    #             # pronunciation_word
    #             "ok'tober",
    #             # hebrew_word_nikud
    #             "‫אוֹקטוֹבֶּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ноябрь",
    #             # pronunciation_word
    #             "no'vember",
    #             # hebrew_word_nikud
    #             "‫נוֹבֶמבֶּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "декабрь",
    #             # pronunciation_word
    #             "de'ʦember",
    #             # hebrew_word_nikud
    #             "‫דֶצֶמבֶּר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "весна",
    #             # pronunciation_word
    #             "aviv",
    #             # hebrew_word_nikud
    #             "‫אָבִיב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "весной",
    #             # pronunciation_word
    #             "baʾaviv",
    #             # hebrew_word_nikud
    #             "‬‫בַּאָבִיב‬"
    #         ),
    #         (
    #             # translation_word
    #             "весенний",
    #             # pronunciation_word
    #             "avivi",
    #             # hebrew_word_nikud
    #             "‫אֲבִיבִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лето",
    #             # pronunciation_word
    #             "'kayiʦ",
    #             # hebrew_word_nikud
    #             "‫קַיִץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "летом",
    #             # pronunciation_word
    #             "ba'kayiʦ",
    #             # hebrew_word_nikud
    #             "‫בַּקַיִץ‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "летний",
    #             # pronunciation_word
    #             "keʦi",
    #             # hebrew_word_nikud
    #             "‫קֵיצִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "осень",
    #             # pronunciation_word
    #             "stav",
    #             # hebrew_word_nikud
    #             "‬‫סתָיו‬"
    #         ),
    #         (
    #             # translation_word
    #             "осенью",
    #             # pronunciation_word
    #             "bestav",
    #             # hebrew_word_nikud
    #             "‫בְּסתָיו‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "осенний",
    #             # pronunciation_word
    #             "stavi",
    #             # hebrew_word_nikud
    #             "‫סתָווִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зима",
    #             # pronunciation_word
    #             "'χoref",
    #             # hebrew_word_nikud
    #             "‫חוֹרֶף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "зимой",
    #             # pronunciation_word
    #             "ba'χoref",
    #             # hebrew_word_nikud
    #             "‬‫בַּחוֹרֶף‬"
    #         ),
    #         (
    #             # translation_word
    #             "зимний",
    #             # pronunciation_word
    #             "χorpi",
    #             # hebrew_word_nikud
    #             "‫חוֹרפִּי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "месяц",
    #             # pronunciation_word
    #             "'χodeʃ",
    #             # hebrew_word_nikud
    #             "‫חוֹדֶש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "год",
    #             # pronunciation_word
    #             "ʃana",
    #             # hebrew_word_nikud
    #             "‬‫שָנָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "дата",
    #             # pronunciation_word
    #             "taʾariχ",
    #             # hebrew_word_nikud
    #             "‫תַאֲרִיך‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "календарь",
    #             # pronunciation_word
    #             "'luaχ ʃana",
    #             # hebrew_word_nikud
    #             "לוּח‬ ‫שָנָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "полгода, полугодие",
    #             # pronunciation_word
    #             "χaʦi ʃana",
    #             # hebrew_word_nikud
    #             "‬חֲצִי‬ ‫שָנָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "век (столетие)",
    #             # pronunciation_word
    #             "'meʾa",
    #             # hebrew_word_nikud
    #             "‬‫מֵאָה‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "23. Время. Разное",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "время",
    #             # pronunciation_word
    #             "zman",
    #             # hebrew_word_nikud
    #             "‫זמַן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "будущее (сущ.)",
    #             # pronunciation_word
    #             "atid",
    #             # hebrew_word_nikud
    #             "‬‫עָתִיד‬"
    #         ),
    #         (
    #             # translation_word
    #             "прошлое (сущ.)",
    #             # pronunciation_word
    #             "avar",
    #             # hebrew_word_nikud
    #             "‫עָבָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "сейчас",
    #             # pronunciation_word
    #             "kayom",
    #             # hebrew_word_nikud
    #             "‫כַּיוֹם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "скоро",
    #             # pronunciation_word
    #             "bekarov",
    #             # hebrew_word_nikud
    #             "‫בְּקָרוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "заранее",
    #             # pronunciation_word
    #             "meroʃ",
    #             # hebrew_word_nikud
    #             "‫מֵרֹאש‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "долго",
    #             # pronunciation_word
    #             "zman rav",
    #             # hebrew_word_nikud
    #             "זמַן‬ ‫רַב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "недолго",
    #             # pronunciation_word
    #             "lo zman rav",
    #             # hebrew_word_nikud
    #             "לֹא‬ ‫זמַן‬ ‫רַב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "рано (~ проснуться)",
    #             # pronunciation_word
    #             "mukdam",
    #             # hebrew_word_nikud
    #             "‫מוּקדָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "поздно (~ встать)",
    #             # pronunciation_word
    #             "meʾuχar",
    #             # hebrew_word_nikud
    #             "‫מְאוּחָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "навсегда",
    #             # pronunciation_word
    #             "la'neʦaχ",
    #             # hebrew_word_nikud
    #             "‫לָנֶצַח‬"
    #         ),
    #         (
    #             # translation_word
    #             "одновременно",
    #             # pronunciation_word
    #             "bo zmanit",
    #             # hebrew_word_nikud
    #             "בּו‬ ‫זמַנִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "временный",
    #             # pronunciation_word
    #             "zmani",
    #             # hebrew_word_nikud
    #             "‬‫זמַנִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "иногда",
    #             # pronunciation_word
    #             "lifʿamim",
    #             # hebrew_word_nikud
    #             "‫לִפעָמִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "редко",
    #             # pronunciation_word
    #             "leʿitim reχokot",
    #             # hebrew_word_nikud
    #             "לְעִיתִים‬ ‫רְחוֹקוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "часто",
    #             # pronunciation_word
    #             "leʿitim krovot",
    #             # hebrew_word_nikud
    #             "לְעִיתִים‬ ‫קרוֹבוֹת‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "24. Линии и формы",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "квадрат",
    #             # pronunciation_word
    #             "ri'buʿa",
    #             # hebrew_word_nikud
    #             "‫רִיבּוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "круг",
    #             # pronunciation_word
    #             "maʿagal",
    #             # hebrew_word_nikud
    #             "‫מַעֲגָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "круг",
    #             # pronunciation_word
    #             "igul",
    #             # hebrew_word_nikud
    #             "‫עִיגוּל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "прямоугольник",
    #             # pronunciation_word
    #             "malben",
    #             # hebrew_word_nikud
    #             "‬‫מַלבֵּן‬"
    #         ),
    #         (
    #             # translation_word
    #             "горизонтальный",
    #             # pronunciation_word
    #             "ofki",
    #             # hebrew_word_nikud
    #             "‬‫אוֹפקִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "вертикальный",
    #             # pronunciation_word
    #             "anaχi",
    #             # hebrew_word_nikud
    #             "‫אֲנָכִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "линия, черта",
    #             # pronunciation_word
    #             "kav",
    #             # hebrew_word_nikud
    #             "‬‫קַו‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "25. Меры измерения",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "вес",
    #             # pronunciation_word
    #             "miʃkal",
    #             # hebrew_word_nikud
    #             "‫מִשקָל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "длина",
    #             # pronunciation_word
    #             "'oreχ",
    #             # hebrew_word_nikud
    #             "‬‫אוֹרֶך‬"
    #         ),
    #         (
    #             # translation_word
    #             "ширина",
    #             # pronunciation_word
    #             "'roχav",
    #             # hebrew_word_nikud
    #             "‬‫רוֹחַב‬"
    #         ),
    #         (
    #             # translation_word
    #             "высота",
    #             # pronunciation_word
    #             "'gova",
    #             # hebrew_word_nikud
    #             "‫גוֹבַה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "глубина",
    #             # pronunciation_word
    #             "'omek",
    #             # hebrew_word_nikud
    #             "‬‫עוֹמֶק‬"
    #         ),
    #         (
    #             # translation_word
    #             "объём",
    #             # pronunciation_word
    #             "'nefaχ",
    #             # hebrew_word_nikud
    #             "‬‫נֶפַח‬"
    #         ),
    #         (
    #             # translation_word
    #             "площадь",
    #             # pronunciation_word
    #             "'ʃetaχ",
    #             # hebrew_word_nikud
    #             "‬‫שֶטַח‬"
    #         ),
    #         (
    #             # translation_word
    #             "грамм",
    #             # pronunciation_word
    #             "gram",
    #             # hebrew_word_nikud
    #             "‬‫גרָם‬"
    #         ),
    #         (
    #             # translation_word
    #             "килограмм",
    #             # pronunciation_word
    #             "kilogram",
    #             # hebrew_word_nikud
    #             "‫קִילוֹגרָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "метр",
    #             # pronunciation_word
    #             "'meter",
    #             # hebrew_word_nikud
    #             "‫מֶטֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "километр",
    #             # pronunciation_word
    #             "kilo'meter",
    #             # hebrew_word_nikud
    #             "‬‫קִילוֹמֶטֶר‬"
    #         ),
    #         (
    #             # translation_word
    #             "квадратный метр",
    #             # pronunciation_word
    #             "'meter ra'vuʿa",
    #             # hebrew_word_nikud
    #             "מֶטֶר‬ ‫רָבוּע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "литр",
    #             # pronunciation_word
    #             "litr",
    #             # hebrew_word_nikud
    #             "‫לִיטר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "количество",
    #             # pronunciation_word
    #             "kamut",
    #             # hebrew_word_nikud
    #             "‬‫כַּמוּת‬"
    #         ),
    #         (
    #             # translation_word
    #             "немного",
    #             # pronunciation_word
    #             "kʦat",
    #             # hebrew_word_nikud
    #             "‬‫קצָת‬"
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
    #             "штука",
    #             # pronunciation_word
    #             "yeχida",
    #             # hebrew_word_nikud
    #             "‬‫יְחִידָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "размер (предмета)",
    #             # pronunciation_word
    #             "'godel",
    #             # hebrew_word_nikud
    #             "‫גוֹדֶל‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "минимальный",
    #             # pronunciation_word
    #             "mini'mali",
    #             # hebrew_word_nikud
    #             "‬‫מִינִימָאלִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "средний",
    #             # pronunciation_word
    #             "memuʦa",
    #             # hebrew_word_nikud
    #             "‬‫מְמוּצָע‬"
    #         ),
    #         (
    #             # translation_word
    #             "максимальный",
    #             # pronunciation_word
    #             "maksi'mali",
    #             # hebrew_word_nikud
    #             "‫מַקסִימָלִי‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "26. Ёмкости",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "банка (стеклянная)",
    #             # pronunciation_word
    #             "ʦin'ʦenet",
    #             # hebrew_word_nikud
    #             "‫צִנצֶנֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "банка (жестяная)",
    #             # pronunciation_word
    #             "paχit",
    #             # hebrew_word_nikud
    #             "‬‫פַּחִית‬"
    #         ),
    #         (
    #             # translation_word
    #             "ведро",
    #             # pronunciation_word
    #             "dli",
    #             # hebrew_word_nikud
    #             "‬‫דלִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "бочка",
    #             # pronunciation_word
    #             "χavit",
    #             # hebrew_word_nikud
    #             "‬‫חָבִית‬"
    #         ),
    #         (
    #             # translation_word
    #             "таз",
    #             # pronunciation_word
    #             "gigit",
    #             # hebrew_word_nikud
    #             "‫גִיגִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кружка, чашка",
    #             # pronunciation_word
    #             "'sefel",
    #             # hebrew_word_nikud
    #             "‬‫סֵפֶל‬"
    #         ),
    #         (
    #             # translation_word
    #             "блюдце",
    #             # pronunciation_word
    #             "taχtit",
    #             # hebrew_word_nikud
    #             "‫תַחתִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стакан",
    #             # pronunciation_word
    #             "kos",
    #             # hebrew_word_nikud
    #             "‫כּוֹס‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бокал",
    #             # pronunciation_word
    #             "ga'viʿa",
    #             # hebrew_word_nikud
    #             "‫גָבִיע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кастрюля",
    #             # pronunciation_word
    #             "sir",
    #             # hebrew_word_nikud
    #             "‫סִיר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бутылка",
    #             # pronunciation_word
    #             "bakbuk",
    #             # hebrew_word_nikud
    #             "‫בַּקבּוּק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ваза",
    #             # pronunciation_word
    #             "agartal",
    #             # hebrew_word_nikud
    #             "‬‫אֲגַרטָל‬"
    #         ),
    #         (
    #             # translation_word
    #             "тюбик",
    #             # pronunciation_word
    #             "ʃfo'feret",
    #             # hebrew_word_nikud
    #             "‫שפוֹפֶרֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пакет (мешок)",
    #             # pronunciation_word
    #             "sakit",
    #             # hebrew_word_nikud
    #             "‫שַׂקִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "коробка",
    #             # pronunciation_word
    #             "kufsa",
    #             # hebrew_word_nikud
    #             "‬‫קוּפסָה‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "27. Материалы",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "материал",
    #             # pronunciation_word
    #             "'χomer",
    #             # hebrew_word_nikud
    #             "‫חוֹמֶר‬‬"
    #         ),
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
    #             "деревянный",
    #             # pronunciation_word
    #             "meʿeʦ",
    #             # hebrew_word_nikud
    #             "‬‫מֵעֵץ‬"
    #         ),
    #         (
    #             # translation_word
    #             "стекло",
    #             # pronunciation_word
    #             "zχuχit",
    #             # hebrew_word_nikud
    #             "‫זכוּכִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "стеклянный",
    #             # pronunciation_word
    #             "mizχuχit",
    #             # hebrew_word_nikud
    #             "‫מִזכוּכִית‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "камень",
    #             # pronunciation_word
    #             "'even",
    #             # hebrew_word_nikud
    #             "‫אֶבֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "каменный",
    #             # pronunciation_word
    #             "me'ʾeven",
    #             # hebrew_word_nikud
    #             "‫מֵאֶבֶן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пластик, пластмасса",
    #             # pronunciation_word
    #             "'plastik",
    #             # hebrew_word_nikud
    #             "‫פּלַסטִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "пластмассовый",
    #             # pronunciation_word
    #             "mi'plastik",
    #             # hebrew_word_nikud
    #             "‫מִפּלַסטִיק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "резина",
    #             # pronunciation_word
    #             "'gumi",
    #             # hebrew_word_nikud
    #             "‫גוּמִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "резиновый",
    #             # pronunciation_word
    #             "mi'gumi",
    #             # hebrew_word_nikud
    #             "‬‫מִגוּמִי‬"
    #         ),
    #         (
    #             # translation_word
    #             "ткань",
    #             # pronunciation_word
    #             "bad",
    #             # hebrew_word_nikud
    #             "‬‫בַּד‬"
    #         ),
    #         (
    #             # translation_word
    #             "из ткани",
    #             # pronunciation_word
    #             "mibad",
    #             # hebrew_word_nikud
    #             "‫מִבַּד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бумага",
    #             # pronunciation_word
    #             "neyar",
    #             # hebrew_word_nikud
    #             "‫נְייָר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "бумажный",
    #             # pronunciation_word
    #             "mineyar",
    #             # hebrew_word_nikud
    #             "‬‫מִנְייָר‬"
    #         ),
    #         (
    #             # translation_word
    #             "картон",
    #             # pronunciation_word
    #             "karton",
    #             # hebrew_word_nikud
    #             "‫קַרטוֹן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "картонный",
    #             # pronunciation_word
    #             "mikarton",
    #             # hebrew_word_nikud
    #             "‬‫מִקַרטוֹן‬"
    #         ),
    #         (
    #             # translation_word
    #             "целлофан",
    #             # pronunciation_word
    #             "ʦelofan",
    #             # hebrew_word_nikud
    #             "‬‫צֶלוֹפָן‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "28. Металлы",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "металл",
    #             # pronunciation_word
    #             "ma'teχet",
    #             # hebrew_word_nikud
    #             "‬‫מַתֶכֶת‬"
    #         ),
    #         (
    #             # translation_word
    #             "металлический",
    #             # pronunciation_word
    #             "mataχti",
    #             # hebrew_word_nikud
    #             "‫מַתַכתִי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "золото",
    #             # pronunciation_word
    #             "zahav",
    #             # hebrew_word_nikud
    #             "‬‫זָהָב‬"
    #         ),
    #         (
    #             # translation_word
    #             "золотой",
    #             # pronunciation_word
    #             "mizahav",
    #             # hebrew_word_nikud
    #             "‬‫מִזָהָב‬"
    #         ),
    #         (
    #             # translation_word
    #             "золотой",
    #             # pronunciation_word
    #             "zahov",
    #             # hebrew_word_nikud
    #             "‫זָהוֹב‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "серебро",
    #             # pronunciation_word
    #             "'kesef",
    #             # hebrew_word_nikud
    #             "‫כֶּסֶף‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "серебряный",
    #             # pronunciation_word
    #             "kaspi",
    #             # hebrew_word_nikud
    #             "‫כַּספִּי‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "железо",
    #             # pronunciation_word
    #             "barzel",
    #             # hebrew_word_nikud
    #             "‬‫בַּרזֶל‬"
    #         ),
    #         (
    #             # translation_word
    #             "железный",
    #             # pronunciation_word
    #             "mibarzel",
    #             # hebrew_word_nikud
    #             "‫מִבַּרזֶל‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "29. Человек. Общие понятия",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "человек",
    #             # pronunciation_word
    #             "ben adam",
    #             # hebrew_word_nikud
    #             "בֶּן‬ ‫אָדָם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мужчина",
    #             # pronunciation_word
    #             "'gever",
    #             # hebrew_word_nikud
    #             "‫גֶבֶר‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "женщина",
    #             # pronunciation_word
    #             "iʃa",
    #             # hebrew_word_nikud
    #             "‫אִשָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ребёнок, мальчик",
    #             # pronunciation_word
    #             "'yeled",
    #             # hebrew_word_nikud
    #             "‬‫יֶלֶד‬"
    #         ),
    #         (
    #             # translation_word
    #             "девочка",
    #             # pronunciation_word
    #             "yalda",
    #             # hebrew_word_nikud
    #             "‫יַלדָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "подросток",
    #             # pronunciation_word
    #             "",
    #             # hebrew_word_nikud
    #             "'naʿar‬"
    #         ),
    #         (
    #             # translation_word
    #             "старик",
    #             # pronunciation_word
    #             "zaken",
    #             # hebrew_word_nikud
    #             "‫זָקֵן‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "старая женщина",
    #             # pronunciation_word
    #             "zkena",
    #             # hebrew_word_nikud
    #             "‫זקֵנָה‬‬"
    #         ),
    #     ]
    # ),
    # (
    #     # group_name_ru
    #     "30. Анатомия",
    #     # words
    #     [
    #         (
    #             # translation_word
    #             "сердце",
    #             # pronunciation_word
    #             "lev",
    #             # hebrew_word_nikud
    #             "‬‫לֵב‬"
    #         ),
    #         (
    #             # translation_word
    #             "кровь",
    #             # pronunciation_word
    #             "dam",
    #             # hebrew_word_nikud
    #             "‬‫דָם‬"
    #         ),
    #         (
    #             # translation_word
    #             "вена",
    #             # pronunciation_word
    #             "vrid",
    #             # hebrew_word_nikud
    #             "‬‫ורִיד‬"
    #         ),
    #         (
    #             # translation_word
    #             "мозг",
    #             # pronunciation_word
    #             "'moaχ",
    #             # hebrew_word_nikud
    #             "‬‫מוֹח‬"
    #         ),
    #         (
    #             # translation_word
    #             "нервы",
    #             # pronunciation_word
    #             "aʦabim",
    #             # hebrew_word_nikud
    #             "‬‫עֲצַבִּים‬"
    #         ),
    #         (
    #             # translation_word
    #             "позвоночник",
    #             # pronunciation_word
    #             "amud haʃidra",
    #             # hebrew_word_nikud
    #             "‬עַמוּד‬ ‫הַשִדרָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "желудок",
    #             # pronunciation_word
    #             "keiva",
    #             # hebrew_word_nikud
    #             "‫קֵיבָה‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кишечник",
    #             # pronunciation_word
    #             "me'ʿayim",
    #             # hebrew_word_nikud
    #             "‫מֵעַיִים‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "печень",
    #             # pronunciation_word
    #             "kaved",
    #             # hebrew_word_nikud
    #             "‫כָּבֵד‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "почка",
    #             # pronunciation_word
    #             "kilya",
    #             # hebrew_word_nikud
    #             "‬‫כִּליָה‬"
    #         ),
    #         (
    #             # translation_word
    #             "кость",
    #             # pronunciation_word
    #             "'eʦem",
    #             # hebrew_word_nikud
    #             "‫עֶצֶם‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "ребро",
    #             # pronunciation_word
    #             "'ʦela",
    #             # hebrew_word_nikud
    #             "‫צֶלַע‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "череп",
    #             # pronunciation_word
    #             "gul'golet",
    #             # hebrew_word_nikud
    #             "‫גוּלגוֹלֶת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "мышца",
    #             # pronunciation_word
    #             "ʃrir",
    #             # hebrew_word_nikud
    #             "‬‫שרִיר‬"
    #         ),
    #         (
    #             # translation_word
    #             "сустав",
    #             # pronunciation_word
    #             "'perek",
    #             # hebrew_word_nikud
    #             "‫פֶּרֶק‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "лёгкие",
    #             # pronunciation_word
    #             "reʾot",
    #             # hebrew_word_nikud
    #             "‫רֵיאוֹת‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "половые органы",
    #             # pronunciation_word
    #             "evrei min",
    #             # hebrew_word_nikud
    #             "אֶברֵי‬ ‫מִין‬‬"
    #         ),
    #         (
    #             # translation_word
    #             "кожа",
    #             # pronunciation_word
    #             "or",
    #             # hebrew_word_nikud
    #             "‬‫עוֹר‬"
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