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
    (
        # group_name_ru
        "1. Местоимения",
        # words
        [
            (
                # translation_word
                "я",
                # pronunciation_word
                "ani",
                # hebrew_word_nikud
                "‫אֲנִי‬‬"
            ),
            (
                # translation_word
                "ты (муж. род)",
                # pronunciation_word
                "ata",
                # hebrew_word_nikud
                "‬‫אַתָה‬"
            ),
            (
                # translation_word
                "ты (жен. род)",
                # pronunciation_word
                "at",
                # hebrew_word_nikud
                "‫אַת‬‬"
            ),
            (
                # translation_word
                "он",
                # pronunciation_word
                "hu",
                # hebrew_word_nikud
                "‫הוּא‬‬"
            ),
            (
                # translation_word
                "она",
                # pronunciation_word
                "hi",
                # hebrew_word_nikud
                "‬‫הִיא‬"
            ),
            (
                # translation_word
                "мы",
                # pronunciation_word
                "a'naχnu",
                # hebrew_word_nikud
                "‫אֲנַחנו‬‬"
            ),
            (
                # translation_word
                "вы (муж. род)",
                # pronunciation_word
                "atem",
                # hebrew_word_nikud
                "‫אַתֶם‬‬"
            ),
            (
                # translation_word
                "вы (жен. род)",
                # pronunciation_word
                "aten",
                # hebrew_word_nikud
                "‬‫אַתֶן‬"
            ),
            (
                # translation_word
                "Вы (вежл. форма, ед., муж. род)",
                # pronunciation_word
                "ata",
                # hebrew_word_nikud
                "‬‫אַתָה‬"
            ),
            (
                # translation_word
                "Вы (вежл. форма, ед., жен. род)",
                # pronunciation_word
                "at",
                # hebrew_word_nikud
                "‬‫אַת‬"
            ),
            (
                # translation_word
                "Вы (вежл. форма, мн., муж. род)",
                # pronunciation_word
                "atem",
                # hebrew_word_nikud
                "‫אַתֶם‬‬"
            ),
            (
                # translation_word
                "Вы (вежл. форма, мн., жен. род",
                # pronunciation_word
                "aten",
                # hebrew_word_nikud
                "‬‫אַתֶן‬"
            ),
            (
                # translation_word
                "они (муж. род)",
                # pronunciation_word
                "hem",
                # hebrew_word_nikud
                "‬‫הֵם‬"
            ),
            (
                # translation_word
                "они (жен. род)",
                # pronunciation_word
                "hen",
                # hebrew_word_nikud
                "‬‫הֵן‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "2. Приветствия. Прощания. Извинения. Благодарность",
        # words
        [
            (
                # translation_word
                "Здравствуй!",
                # pronunciation_word
                "ʃalom!",
                # hebrew_word_nikud
                "‬!‫שָלוֹם‬"
            ),
            (
                # translation_word
                "Здравствуйте!",
                # pronunciation_word
                "ʃalom!",
                # hebrew_word_nikud
                "!‫שָלוֹם‬‬"
            ),
            (
                # translation_word
                "Доброе утро!",
                # pronunciation_word
                "'boker tov!",
                # hebrew_word_nikud
                "בּוֹקֶר‬ ‫טוֹב‬"
            ),
            (
                # translation_word
                "Добрый день!",
                # pronunciation_word
                "ʦaha'rayim tovim!",
                # hebrew_word_nikud
                "צָהֳרַיִים‬ ‫טוֹבִים‬‬‬"
            ),
            (
                # translation_word
                "Добрый вечер!",
                # pronunciation_word
                "'erev tov!",
                # hebrew_word_nikud
                "‬‬עֶרֶב‬ ‫טוֹב‬"
            ),
            (
                # translation_word
                "здороваться, приветствовать",
                # pronunciation_word
                "lomar ʃalom",
                # hebrew_word_nikud
                "‬‫‬לוֹמַר‬ ‫שָלוֹם‬"
            ),
            (
                # translation_word
                "Привет!",
                # pronunciation_word
                "hai!",
                # hebrew_word_nikud
                "!‫הַיי‬‬"
            ),
            (
                # translation_word
                "привет, приветствие",
                # pronunciation_word
                "ahlan",
                # hebrew_word_nikud
                "‬‫אַהלַן‬"
            ),
            (
                # translation_word
                "Как дела? (к муж.)",
                # pronunciation_word
                "ma ʃlomχa?",
                # hebrew_word_nikud
                "‬‬‬מַה‬ ‫שלוֹמך‬"
            ),
            (
                # translation_word
                "Как дела? (у тебя)",
                # pronunciation_word
                "ma niʃma?",
                # hebrew_word_nikud
                "‬‬מַה‬ ‫נִשמָע‬"
            ),
            (
                # translation_word
                "Что нового?",
                # pronunciation_word
                "ma χadaʃ?",
                # hebrew_word_nikud
                "‬‬מַה‬ ‫חָדָש‬"
            ),
            (
                # translation_word
                "До свидания! (на «Вы»)",
                # pronunciation_word
                "lehitraʾot!",
                # hebrew_word_nikud
                "‬‬‫לְהִתרָאוֹת‬"
            ),
            (
                # translation_word
                "До свидания! Пока! (на «ты»)",
                # pronunciation_word
                "bai!",
                # hebrew_word_nikud
                "‬!‫בַּי‬"
            ),
            (
                # translation_word
                "До скорой встречи!",
                # pronunciation_word
                "lehitraʾot bekarov!",
                # hebrew_word_nikud
                "לְהִתרָאוֹת‬ ‫בְּקָרוֹב‬‬‬"
            ),
            (
                # translation_word
                "прощаться",
                # pronunciation_word
                "lomar lehitraʾot",
                # hebrew_word_nikud
                "‬‬לוֹמַר‬ ‫לְהִתרָאוֹת‬"
            ),
            (
                # translation_word
                "Спасибо!",
                # pronunciation_word
                "toda!",
                # hebrew_word_nikud
                "‬!‫תוֹדָה‬"
            ),
            (
                # translation_word
                "Большое спасибо!",
                # pronunciation_word
                "toda raba!",
                # hebrew_word_nikud
                "‬‬תוֹדָה‬ ‫רַבָּה‬"
            ),
            (
                # translation_word
                "Пожалуйста (ответ)",
                # pronunciation_word
                "bevakaʃa",
                # hebrew_word_nikud
                "‬‫בְּבַקָשָה‬"
            ),
            (
                # translation_word
                "Не стоит благодарности",
                # pronunciation_word
                "al lo davar",
                # hebrew_word_nikud
                "עַל‬ ‫לֹא‬ ‫דָבָר‬"
            ),
            (
                # translation_word
                "Не за что",
                # pronunciation_word
                "ein beʿad ma",
                # hebrew_word_nikud
                "‬אֵין‬ ‫בְּעַד‬ ‫מָה‬"
            ),
            (
                # translation_word
                "Извини! Извините!",
                # pronunciation_word
                "sliχa!",
                # hebrew_word_nikud
                "!‫סלִיחָה‬‬"
            ),
            (
                # translation_word
                "извинять",
                # pronunciation_word
                "lis'loaχ",
                # hebrew_word_nikud
                "‬‫לִסלוֹח‬"
            ),
            (
                # translation_word
                "извиняться",
                # pronunciation_word
                "lehitnaʦel",
                # hebrew_word_nikud
                "‬‫לְהִתנַצֵל‬"
            ),
            (
                # translation_word
                "Мои извинения. (м.р.)",
                # pronunciation_word
                "ani mitnaʦel",
                # hebrew_word_nikud
                "‬אֲנִי‬ ‫מִתנַצֵל‬"
            ),
            (
                # translation_word
                "Мои извинения. (ж.р.)",
                # pronunciation_word
                "ani mitna'ʦelet",
                # hebrew_word_nikud
                "אֲנִי‬ ‫מִתנַצֵלֶת‬‬"
            ),
            (
                # translation_word
                "Простите! (м.р.)",
                # pronunciation_word
                "ani miʦtaʿer",
                # hebrew_word_nikud
                "‬"
            ),
            (
                # translation_word
                "Простите!(ж.р.)",
                # pronunciation_word
                "ani miʦta'ʿeret",
                # hebrew_word_nikud
                "‬אֲנִי‬ ‫מִצטַעֵרֶת‬"
            ),
            (
                # translation_word
                "прощать (кого-л.)",
                # pronunciation_word
                "lis'loaχ",
                # hebrew_word_nikud
                "‫לִסלוֹח‬‬"
            ),
            (
                # translation_word
                "Ничего страшного (ответ)",
                # pronunciation_word
                "lo nora",
                # hebrew_word_nikud
                "לֹא‬ ‫נוֹרָא‬‬"
            ),
            (
                # translation_word
                "пожалуйста (при просьбе)",
                # pronunciation_word
                "bevakaʃa",
                # hebrew_word_nikud
                "‫בְּבַקָשָה‬‬"
            ),
            (
                # translation_word
                "Не забудьте! (м.р.)",
                # pronunciation_word
                "al tiʃkaχ!",
                # hebrew_word_nikud
                "אַל‬ ‫תִשכַּח‬‬"
            ),
            (
                # translation_word
                "Конечно!",
                # pronunciation_word
                "'betaχ!",
                # hebrew_word_nikud
                "‫בֶּטַח‬‬"
            ),
            (
                # translation_word
                "Конечно нет!",
                # pronunciation_word
                "'betaχ ʃelo!",
                # hebrew_word_nikud
                "בֶּטַח‬ ‫שֶלֹא‬‬"
            ),
            (
                # translation_word
                "Согласен!",
                # pronunciation_word
                "okei!",
                # hebrew_word_nikud
                "‫אוֹקֵיי‬‬"
            ),
            (
                # translation_word
                "Хватит!",
                # pronunciation_word
                "maspik!",
                # hebrew_word_nikud
                "‫מַספִּיק‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "3. Обращения",
        # words
        [
            (
                # translation_word
                "Извините! (обращение)",
                # pronunciation_word
                "sliχa!",
                # hebrew_word_nikud
                "‬!‫סלִיחָה‬"
            ),
            (
                # translation_word
                "господин",
                # pronunciation_word
                "adon",
                # hebrew_word_nikud
                "‫אָדוֹן‬‬"
            ),
            (
                # translation_word
                "госпожа",
                # pronunciation_word
                "gvirti",
                # hebrew_word_nikud
                "‬‫גבִרתִי‬"
            ),
            (
                # translation_word
                "девушка",
                # pronunciation_word
                "'gveret",
                # hebrew_word_nikud
                "‫גבֶרֶת‬‬"
            ),
            (
                # translation_word
                "молодой человек",
                # pronunciation_word
                "baχur ʦaʿir",
                # hebrew_word_nikud
                "בָּחוּר‬ ‫צָעִיר‬‬"
            ),
            (
                # translation_word
                "мальчик",
                # pronunciation_word
                "'yeled",
                # hebrew_word_nikud
                "‫יֶלֶד‬‬"
            ),
            (
                # translation_word
                "девочка",
                # pronunciation_word
                "yalda",
                # hebrew_word_nikud
                "‫יַלדָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "4. Числа от 1 до 100",
        # words
        [
            (
                # translation_word
                "0 ноль",
                # pronunciation_word
                "'efes",
                # hebrew_word_nikud
                "‬‫אֶפֶס‬"
            ),
            (
                # translation_word
                "1 один",
                # pronunciation_word
                "eχad",
                # hebrew_word_nikud
                "‬‫אֶחָד‬"
            ),
            (
                # translation_word
                "1 одна",
                # pronunciation_word
                "aχat",
                # hebrew_word_nikud
                "‬‫אַחַת‬"
            ),
            (
                # translation_word
                "2 два",
                # pronunciation_word
                "'ʃtayim",
                # hebrew_word_nikud
                "‬‫שתַיִים‬"
            ),
            (
                # translation_word
                "3 три",
                # pronunciation_word
                "ʃaloʃ",
                # hebrew_word_nikud
                "‬‫שָלוֹש‬"
            ),
            (
                # translation_word
                "4 четыре",
                # pronunciation_word
                "arba",
                # hebrew_word_nikud
                "‬‫אַרבַּע‬"
            ),
            (
                # translation_word
                "5 пять",
                # pronunciation_word
                "χameʃ",
                # hebrew_word_nikud
                "‬‫חָמֵש‬"
            ),
            (
                # translation_word
                "6 шесть",
                # pronunciation_word
                "ʃeʃ",
                # hebrew_word_nikud
                "‬‫שֵש‬"
            ),
            (
                # translation_word
                "7 семь",
                # pronunciation_word
                "'ʃeva",
                # hebrew_word_nikud
                "‫שֶבַע‬‬"
            ),
            (
                # translation_word
                "8 восемь",
                # pronunciation_word
                "'ʃmone",
                # hebrew_word_nikud
                "‬‫שמוֹנֶה‬"
            ),
            (
                # translation_word
                "9 девять",
                # pronunciation_word
                "'teʃa",
                # hebrew_word_nikud
                "‬‫תֵשַע‬"
            ),
            (
                # translation_word
                "10 десять",
                # pronunciation_word
                "'eser",
                # hebrew_word_nikud
                "‫עֶשֶׂר‬‬"
            ),
            (
                # translation_word
                "11 одиннадцать",
                # pronunciation_word
                "aχat esre",
                # hebrew_word_nikud
                "‬‫אַחַת־עֶשׂרֵה‬"
            ),
            (
                # translation_word
                "12 двенадцать",
                # pronunciation_word
                "ʃteim esre",
                # hebrew_word_nikud
                "‫שתֵים־עֶשֹרֵה‬‬"
            ),
            (
                # translation_word
                "13 тринадцать",
                # pronunciation_word
                "ʃloʃ esre",
                # hebrew_word_nikud
                "‫שלוֹש־עֶשֹרֵה‬‬"
            ),
            (
                # translation_word
                "14 четырнадцать",
                # pronunciation_word
                "arba esre",
                # hebrew_word_nikud
                "‬‫אַרְבַּע־עֶשֹרֵה‬"
            ),
            (
                # translation_word
                "15 пятнадцать",
                # pronunciation_word
                "χameʃ esre",
                # hebrew_word_nikud
                "‬‫חֲמֵש־עֶשֹרֵה‬"
            ),
            (
                # translation_word
                "16 шестнадцать",
                # pronunciation_word
                "ʃeʃ esre",
                # hebrew_word_nikud
                "‫שֵש־עֶשֹרֵה‬‬"
            ),
            (
                # translation_word
                "17 семнадцать",
                # pronunciation_word
                "ʃva esre",
                # hebrew_word_nikud
                "‬‫שבַע־עֶשֹרֵה‬"
            ),
            (
                # translation_word
                "18 восемнадцать",
                # pronunciation_word
                "ʃmone esre",
                # hebrew_word_nikud
                "‫שמוֹנֶה־עֶשֹרֵה‬‬"
            ),
            (
                # translation_word
                "19 девятнадцать",
                # pronunciation_word
                "tʃa esre",
                # hebrew_word_nikud
                "‬‫תשַע־עֶשֹרֵה‬"
            ),
            (
                # translation_word
                "20 двадцать",
                # pronunciation_word
                "esrim",
                # hebrew_word_nikud
                "‬‫עֶשׂרִים‬"
            ),
            (
                # translation_word
                "21 двадцать один",
                # pronunciation_word
                "esrim veʾeχad",
                # hebrew_word_nikud
                "‬עֶשׂרִים‬ ‫וְאֶחָד‬"
            ),
            (
                # translation_word
                "22 двадцать два",
                # pronunciation_word
                "esrim u'ʃnayim",
                # hebrew_word_nikud
                "עֶשׂרִים‬ ‫וּשנַיִים‬‬"
            ),
            (
                # translation_word
                "23 двадцать три",
                # pronunciation_word
                "esrim uʃloʃa",
                # hebrew_word_nikud
                "עֶשׂרִים‬ ‫וּשלוֹשָה‬‬"
            ),
            (
                # translation_word
                "30 тридцать",
                # pronunciation_word
                "ʃloʃim",
                # hebrew_word_nikud
                "‫שלוֹשִים‬‬"
            ),
            (
                # translation_word
                "31 тридцать один",
                # pronunciation_word
                "ʃloʃim veʾeχad",
                # hebrew_word_nikud
                "‬שלוֹשִים‬ ‫וְאֶחָד‬"
            ),
            (
                # translation_word
                "32 тридцать два",
                # pronunciation_word
                "ʃloʃim u'ʃnayim",
                # hebrew_word_nikud
                "שלוֹשִים‬ ‫וּשנַיִים‬‬"
            ),
            (
                # translation_word
                "33 тридцать три",
                # pronunciation_word
                "ʃloʃim uʃloʃa",
                # hebrew_word_nikud
                "שלוֹשִים‬ ‫וּשלוֹשָה‬‬"
            ),
            (
                # translation_word
                "40 сорок",
                # pronunciation_word
                "arbaʿim",
                # hebrew_word_nikud
                "‬‫אַרבָּעִים‬"
            ),
            (
                # translation_word
                "41 сорок один",
                # pronunciation_word
                "arbaʿim veʾeχad",
                # hebrew_word_nikud
                "אַרבָּעִים‬ ‫וְאֶחָד‬‬"
            ),
            (
                # translation_word
                "42 сорок два",
                # pronunciation_word
                "arbaʿim u'ʃnayim",
                # hebrew_word_nikud
                "אַרבָּעִים‬ ‫וּשנַיִים‬‬"
            ),
            (
                # translation_word
                "43 сорок три",
                # pronunciation_word
                "arbaʿim uʃloʃa",
                # hebrew_word_nikud
                "אַרבָּעִים‬ ‫וּשלוֹשָה‬‬"
            ),
            (
                # translation_word
                "50 пятьдесят",
                # pronunciation_word
                "χamiʃim",
                # hebrew_word_nikud
                "‫חֲמִישִים‬‬"
            ),
            (
                # translation_word
                "51 пятьдесят один",
                # pronunciation_word
                "χamiʃim veʾeχad",
                # hebrew_word_nikud
                "חֲמִישִים‬ ‫וְאֶחָד‬‬"
            ),
            (
                # translation_word
                "52 пятьдесят два",
                # pronunciation_word
                "χamiʃim u'ʃnayim",
                # hebrew_word_nikud
                "‬חֲמִישִים‬ ‫וּשנַיִים‬"
            ),
            (
                # translation_word
                "53 пятьдесят три",
                # pronunciation_word
                "χamiʃim uʃloʃa",
                # hebrew_word_nikud
                "‬חֲמִישִים‬ ‫וּשלוֹשָה‬"
            ),
            (
                # translation_word
                "60 шестьдесят",
                # pronunciation_word
                "ʃiʃim",
                # hebrew_word_nikud
                "‫שִישִים‬‬"
            ),
            (
                # translation_word
                "61 шестьдесят один",
                # pronunciation_word
                "ʃiʃim veʾeχad",
                # hebrew_word_nikud
                "שִישִים‬ ‫וְאֶחָד‬‬"
            ),
            (
                # translation_word
                "62 шестьдесят два",
                # pronunciation_word
                "ʃiʃim u'ʃnayim",
                # hebrew_word_nikud
                "‬שִישִים‬ ‫וּשנַיִים‬"
            ),
            (
                # translation_word
                "63 шестьдесят три",
                # pronunciation_word
                "ʃiʃim uʃloʃa",
                # hebrew_word_nikud
                "‬שִישִים‬ ‫וּשלוֹשָה‬"
            ),
            (
                # translation_word
                "70 семьдесят",
                # pronunciation_word
                "ʃivʿim",
                # hebrew_word_nikud
                "‬‫שִבעִים‬"
            ),
            (
                # translation_word
                "71 семьдесят один",
                # pronunciation_word
                "ʃivʿim veʾeχad",
                # hebrew_word_nikud
                "שִבעִים‬ ‫וְאֶחָד‬‬"
            ),
            (
                # translation_word
                "72 семьдесят два",
                # pronunciation_word
                "ʃivʿim u'ʃnayim",
                # hebrew_word_nikud
                "שִבעִים‬ ‫וּשנַיִים‬‬"
            ),
            (
                # translation_word
                "73 семьдесят три",
                # pronunciation_word
                "ʃivʿim uʃloʃa",
                # hebrew_word_nikud
                "שִבעִים‬ ‫וּשלוֹשָה‬‬"
            ),
            (
                # translation_word
                "80 восемьдесят",
                # pronunciation_word
                "ʃmonim",
                # hebrew_word_nikud
                "‬‫שמוֹנִים‬"
            ),
            (
                # translation_word
                "81 восемьдесят один",
                # pronunciation_word
                "ʃmonim veʾeχad",
                # hebrew_word_nikud
                "‬שמוֹנִים‬ ‫וְאֶחָד‬"
            ),
            (
                # translation_word
                "82 восемьдесят два",
                # pronunciation_word
                "ʃmonim u'ʃnayim",
                # hebrew_word_nikud
                "‬שמוֹנִים‬ ‫וּשנַיִים‬"
            ),
            (
                # translation_word
                "83 восемьдесят три",
                # pronunciation_word
                "ʃmonim uʃloʃa",
                # hebrew_word_nikud
                "‬שמוֹנִים‬ ‫וּשלוֹשָה‬"
            ),
            (
                # translation_word
                "90 девяносто",
                # pronunciation_word
                "tiʃʿim",
                # hebrew_word_nikud
                "‫תִשעִים‬‬"
            ),
            (
                # translation_word
                "91 девяносто один",
                # pronunciation_word
                "tiʃʿim veʾeχad",
                # hebrew_word_nikud
                "‬תִשעִים‬ ‫וְאֶחָד‬"
            ),
            (
                # translation_word
                "92 девяносто два",
                # pronunciation_word
                "tiʃʿim u'ʃayim",
                # hebrew_word_nikud
                "תִשעִים‬ ‫וּשנַיִים‬‬"
            ),
            (
                # translation_word
                "93 девяносто три",
                # pronunciation_word
                "tiʃʿim uʃloʃa",
                # hebrew_word_nikud
                "‬תִשעִים‬ ‫וּשלוֹשָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "5. Числа от 100",
        # words
        [
            (
                # translation_word
                "100 сто",
                # pronunciation_word
                "'meʾa",
                # hebrew_word_nikud
                "‬‫מֵאָה‬"
            ),
            (
                # translation_word
                "200 двести",
                # pronunciation_word
                "ma'tayim",
                # hebrew_word_nikud
                "‫מָאתַיִים‬‬"
            ),
            (
                # translation_word
                "300 триста",
                # pronunciation_word
                "ʃloʃ meʾot",
                # hebrew_word_nikud
                "‬שלוֹש‬ ‫מֵאוֹת‬"
            ),
            (
                # translation_word
                "400 четыреста",
                # pronunciation_word
                "arba meʾot",
                # hebrew_word_nikud
                "אַרבַּע‬ ‫מֵאוֹת‬‬"
            ),
            (
                # translation_word
                "500 пятьсот",
                # pronunciation_word
                "χameʃ meʾot",
                # hebrew_word_nikud
                "חָמֵש‬ ‫מֵאוֹת‬‬"
            ),
            (
                # translation_word
                "600 шестьсот",
                # pronunciation_word
                "ʃeʃ meʾot",
                # hebrew_word_nikud
                "‬שֵש‬ ‫מֵאוֹת‬"
            ),
            (
                # translation_word
                "700 семьсот",
                # pronunciation_word
                "ʃva meʾot",
                # hebrew_word_nikud
                "‬שבַע‬ ‫מֵאוֹת‬"
            ),
            (
                # translation_word
                "800 восемьсот",
                # pronunciation_word
                "ʃmone meʾot",
                # hebrew_word_nikud
                "‬שמוֹנֶה‬ ‫מֵאוֹת‬"
            ),
            (
                # translation_word
                "900 девятьсот",
                # pronunciation_word
                "tʃa meʾot",
                # hebrew_word_nikud
                "תשַע‬ ‫מֵאוֹת‬‬"
            ),
            (
                # translation_word
                "1000 тысяча",
                # pronunciation_word
                "'elef",
                # hebrew_word_nikud
                "‬‫אֶלֶף‬"
            ),
            (
                # translation_word
                "2000 две тысячи",
                # pronunciation_word
                "al'payim",
                # hebrew_word_nikud
                "‫אַלפַּיִים‬‬"
            ),
            (
                # translation_word
                "3000 три тысячи",
                # pronunciation_word
                "'ʃloʃet alafim",
                # hebrew_word_nikud
                "‬שלוֹשֶת‬ ‫אֲלָפִים‬"
            ),
            (
                # translation_word
                "10000 десять тысяч",
                # pronunciation_word
                "a'seret alafim",
                # hebrew_word_nikud
                "עֲשֶׂרֶת‬ ‫אֲלָפִים‬‬"
            ),
            (
                # translation_word
                "100000 сто тысяч",
                # pronunciation_word
                "'meʾa 'elef",
                # hebrew_word_nikud
                "‬מֵאָה‬ ‫אֶלֶף‬"
            ),
            (
                # translation_word
                "миллион",
                # pronunciation_word
                "milyon",
                # hebrew_word_nikud
                "‫מִיליוֹן‬‬"
            ),
            (
                # translation_word
                "миллиард",
                # pronunciation_word
                "milyard",
                # hebrew_word_nikud
                "‬‫מִיליַארד‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "6. Числа. Порядковые числительные",
        # words
        [
            (
                # translation_word
                "первый",
                # pronunciation_word
                "riʃon",
                # hebrew_word_nikud
                "‫רִאשוֹן‬‬"
            ),
            (
                # translation_word
                "второй",
                # pronunciation_word
                "ʃeni",
                # hebrew_word_nikud
                "‫שֵנִי‬‬"
            ),
            (
                # translation_word
                "третий",
                # pronunciation_word
                "ʃliʃi",
                # hebrew_word_nikud
                "‬‫שלִישִי‬"
            ),
            (
                # translation_word
                "четвёртый",
                # pronunciation_word
                "reviʿi",
                # hebrew_word_nikud
                "‬‫רְבִיעִי‬"
            ),
            (
                # translation_word
                "пятый",
                # pronunciation_word
                "χamiʃi",
                # hebrew_word_nikud
                "‫חֲמִישִי‬‬"
            ),
            (
                # translation_word
                "шестой",
                # pronunciation_word
                "ʃiʃi",
                # hebrew_word_nikud
                "‬‫שִישִי‬"
            ),
            (
                # translation_word
                "седьмой",
                # pronunciation_word
                "ʃviʿi",
                # hebrew_word_nikud
                "‬‫שבִיעִי‬"
            ),
            (
                # translation_word
                "восьмой",
                # pronunciation_word
                "ʃmini",
                # hebrew_word_nikud
                "‬‫שמִינִי‬"
            ),
            (
                # translation_word
                "девятый",
                # pronunciation_word
                "tʃiʿi",
                # hebrew_word_nikud
                "‬‫תשִיעִי‬"
            ),
            (
                # translation_word
                "десятый",
                # pronunciation_word
                "asiri",
                # hebrew_word_nikud
                "‫עֲשִׂירִי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "7. Числа. Дроби",
        # words
        [
            (
                # translation_word
                "дробь",
                # pronunciation_word
                "'ʃever",
                # hebrew_word_nikud
                "‫שֶבֶר‬‬"
            ),
            (
                # translation_word
                "одна вторая",
                # pronunciation_word
                "χeʦi",
                # hebrew_word_nikud
                "‬‫חֵצִי‬"
            ),
            (
                # translation_word
                "одна третья",
                # pronunciation_word
                "ʃliʃ",
                # hebrew_word_nikud
                "‬‫שלִיש‬"
            ),
            (
                # translation_word
                "одна четвёртая",
                # pronunciation_word
                "'reva",
                # hebrew_word_nikud
                "‫רֶבַע‬‬"
            ),
            (
                # translation_word
                "одна восьмая",
                # pronunciation_word
                "ʃminit",
                # hebrew_word_nikud
                "‫שמִינִית‬‬"
            ),
            (
                # translation_word
                "одна десятая",
                # pronunciation_word
                "asirit",
                # hebrew_word_nikud
                "‫עֲשִׂירִית‬‬"
            ),
            (
                # translation_word
                "две третьих",
                # pronunciation_word
                "ʃnei ʃliʃim",
                # hebrew_word_nikud
                "‬שנֵי‬ ‫שלִישִים‬"
            ),
            (
                # translation_word
                "три четвёртых",
                # pronunciation_word
                "'ʃloʃet rivʿei",
                # hebrew_word_nikud
                "שלוֹשֶת‬ ‫רִבעֵי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "8. Числа. Математические действия",
        # words
        [
            (
                # translation_word
                "вычитание",
                # pronunciation_word
                "χisur",
                # hebrew_word_nikud
                "‬‫חִיסוּר‬"
            ),
            (
                # translation_word
                "вычитать",
                # pronunciation_word
                "leχaser",
                # hebrew_word_nikud
                "‬‫לְחַסֵר‬"
            ),
            (
                # translation_word
                "деление",
                # pronunciation_word
                "χiluk",
                # hebrew_word_nikud
                "‫חִילוּק‬‬"
            ),
            (
                # translation_word
                "делить",
                # pronunciation_word
                "leχalek",
                # hebrew_word_nikud
                "‬‫לְחַלֵק‬"
            ),
            (
                # translation_word
                "сложение",
                # pronunciation_word
                "χibur",
                # hebrew_word_nikud
                "‬‫חִיבּוּר‬"
            ),
            (
                # translation_word
                "сложить (матем.)",
                # pronunciation_word
                "leχaber",
                # hebrew_word_nikud
                "‫לְחַבֵּר‬‬"
            ),
            (
                # translation_word
                "прибавлять",
                # pronunciation_word
                "leχaber",
                # hebrew_word_nikud
                "‫לְחַבֵּר‬‬"
            ),
            (
                # translation_word
                "умножение",
                # pronunciation_word
                "kefel",
                # hebrew_word_nikud
                "‫כֶּפֶל‬‬"
            ),
            (
                # translation_word
                "умножать",
                # pronunciation_word
                "lehaχpil",
                # hebrew_word_nikud
                "‬‫לְהַכפִּיל‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "9. Числа. Разное",
        # words
        [
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
                "число",
                # pronunciation_word
                "mispar",
                # hebrew_word_nikud
                "‫מִספָּר‬‬"
            ),
            (
                # translation_word
                "числительное",
                # pronunciation_word
                "ʃem mispar",
                # hebrew_word_nikud
                "שֵם‬ ‫מִספָּר‬‬"
            ),
            (
                # translation_word
                "минус",
                # pronunciation_word
                "'minus",
                # hebrew_word_nikud
                "‬‫מִינוּס‬"
            ),
            (
                # translation_word
                "плюс",
                # pronunciation_word
                "plus",
                # hebrew_word_nikud
                "‬‫פּלוּס‬"
            ),
            (
                # translation_word
                "формула",
                # pronunciation_word
                "nusχa",
                # hebrew_word_nikud
                "‫נוּסחָה‬‬"
            ),
            (
                # translation_word
                "вычисление",
                # pronunciation_word
                "χiʃuv",
                # hebrew_word_nikud
                "‬‫חִישוּב‬"
            ),
            (
                # translation_word
                "считать",
                # pronunciation_word
                "lispor",
                # hebrew_word_nikud
                "‫לִספּוֹר‬‬"
            ),
            (
                # translation_word
                "подсчитывать",
                # pronunciation_word
                "leχaʃev",
                # hebrew_word_nikud
                "‬‫לְחַשֵב‬"
            ),
            (
                # translation_word
                "сравнивать",
                # pronunciation_word
                "lehaʃvot",
                # hebrew_word_nikud
                "‬‫לְהַשווֹת‬"
            ),
            (
                # translation_word
                "Сколько?",
                # pronunciation_word
                "kama?",
                # hebrew_word_nikud
                "‬?‫כַּמָה‬"
            ),
            (
                # translation_word
                "сумма",
                # pronunciation_word
                "sχum",
                # hebrew_word_nikud
                "‬‫סכוּם‬"
            ),
            (
                # translation_word
                "результат",
                # pronunciation_word
                "toʦaʾa",
                # hebrew_word_nikud
                "‬‫תוֹצָאָה‬"
            ),
            (
                # translation_word
                "остаток",
                # pronunciation_word
                "ʃeʾerit",
                # hebrew_word_nikud
                "‫שְאֵרִית‬‬"
            ),
            (
                # translation_word
                "несколько",
                # pronunciation_word
                "'kama",
                # hebrew_word_nikud
                "‫כַּמָה‬‬"
            ),
            (
                # translation_word
                "мало (неисч.)",
                # pronunciation_word
                "kʦat",
                # hebrew_word_nikud
                "‫קצָת‬‬"
            ),
            (
                # translation_word
                "немного",
                # pronunciation_word
                "meʿat",
                # hebrew_word_nikud
                "‫מְעַט‬‬"
            ),
            (
                # translation_word
                "остальное",
                # pronunciation_word
                "ʃeʾar",
                # hebrew_word_nikud
                "‫שְאָר‬‬"
            ),
            (
                # translation_word
                "полтора",
                # pronunciation_word
                "eχad va'χeʦi",
                # hebrew_word_nikud
                "‬אֶחָד‬ ‫וָחֵצִי‬"
            ),
            (
                # translation_word
                "дюжина",
                # pronunciation_word
                "tresar",
                # hebrew_word_nikud
                "‫תרֵיסָר‬‬"
            ),
            (
                # translation_word
                "пополам (на 2 части)",
                # pronunciation_word
                "'χeʦi 'χeʦi",
                # hebrew_word_nikud
                "‬‫חֵצִי‬ ‫חֵצִי‬"
            ),
            (
                # translation_word
                "поровну",
                # pronunciation_word
                "ʃave beʃave",
                # hebrew_word_nikud
                "‬שָווֶה‬ ‫בְּשָווֶה‬"
            ),
            (
                # translation_word
                "половина",
                # pronunciation_word
                "'χeʦi",
                # hebrew_word_nikud
                "‫חֵצִי‬‬"
            ),
            (
                # translation_word
                "раз",
                # pronunciation_word
                "paʿam",
                # hebrew_word_nikud
                "‫פַּעַם‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "10. Самые важные глаголы - 1",
        # words
        [
            (
                # translation_word
                "бежать",
                # pronunciation_word
                "laruʦ",
                # hebrew_word_nikud
                "‫לָרוּץ‬‬"
            ),
            (
                # translation_word
                "бояться",
                # pronunciation_word
                "lefaχed",
                # hebrew_word_nikud
                "‫לְפַחֵד‬‬"
            ),
            (
                # translation_word
                "брать",
                # pronunciation_word
                "la'kaχat",
                # hebrew_word_nikud
                "‫לָקַחַת‬‬"
            ),
            (
                # translation_word
                "быть",
                # pronunciation_word
                "lihyot",
                # hebrew_word_nikud
                "‫לִהיוֹת‬‬"
            ),
            (
                # translation_word
                "видеть",
                # pronunciation_word
                "lirʾot",
                # hebrew_word_nikud
                "‬‫לִראוֹת‬"
            ),
            (
                # translation_word
                "владеть",
                # pronunciation_word
                "lihyot 'baʿal ʃel",
                # hebrew_word_nikud
                "‬לִהיוֹת‬ ‫בַּעַל‬ ‫שֶל‬"
            ),
            (
                # translation_word
                "возражать",
                # pronunciation_word
                "lehitnaged",
                # hebrew_word_nikud
                "‫לְהִתנַגֵד‬‬"
            ),
            (
                # translation_word
                "входить (в комнату и т.п.)",
                # pronunciation_word
                "lehikanes",
                # hebrew_word_nikud
                "‬‫לְהִיכָּנֵס‬"
            ),
            (
                # translation_word
                "выбирать",
                # pronunciation_word
                "livχor",
                # hebrew_word_nikud
                "‬‫לִבחוֹר‬"
            ),
            (
                # translation_word
                "выходить (из дома)",
                # pronunciation_word
                "laʦet",
                # hebrew_word_nikud
                "‫לָצֵאת‬‬"
            ),
            (
                # translation_word
                "говорить (разговаривать)",
                # pronunciation_word
                "ledaber",
                # hebrew_word_nikud
                "‬‫לְדַבֵּר‬"
            ),
            (
                # translation_word
                "готовить (обед)",
                # pronunciation_word
                "levaʃel",
                # hebrew_word_nikud
                "‫לְבַשֵל‬‬"
            ),
            (
                # translation_word
                "давать",
                # pronunciation_word
                "latet",
                # hebrew_word_nikud
                "‬‫לָתֵת‬"
            ),
            (
                # translation_word
                "делать",
                # pronunciation_word
                "laʿasot",
                # hebrew_word_nikud
                "‬‫לַעֲשׂוֹת‬"
            ),
            (
                # translation_word
                "доверять",
                # pronunciation_word
                "liv'toaχ",
                # hebrew_word_nikud
                "‫לִבטוֹח‬‬"
            ),
            (
                # translation_word
                "думать",
                # pronunciation_word
                "laχʃov",
                # hebrew_word_nikud
                "‫לַחשוֹב‬‬"
            ),
            (
                # translation_word
                "жаловаться",
                # pronunciation_word
                "lehitlonen",
                # hebrew_word_nikud
                "‫לְהִתלוֹנֵן‬‬"
            ),
            (
                # translation_word
                "ждать",
                # pronunciation_word
                "lehamtin",
                # hebrew_word_nikud
                "‫לְהַמתִין‬‬"
            ),
            (
                # translation_word
                "забывать",
                # pronunciation_word
                "liʃ'koaχ",
                # hebrew_word_nikud
                "‫לִשכּוֹח‬‬"
            ),
            (
                # translation_word
                "завтракать",
                # pronunciation_word
                "leʾeχol aruχat 'boker",
                # hebrew_word_nikud
                "‬לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‫בּוֹקֶר‬"
            ),
            (
                # translation_word
                "заказывать",
                # pronunciation_word
                "lehazmin",
                # hebrew_word_nikud
                "‬‫לְהַזמִין‬"
            ),
            (
                # translation_word
                "заканчивать",
                # pronunciation_word
                "lesayem",
                # hebrew_word_nikud
                "‬‫לְסַייֵם‬"
            ),
            (
                # translation_word
                "замечать (увидеть)",
                # pronunciation_word
                "lasim lev",
                # hebrew_word_nikud
                "לָשִׂים‬ ‫לֵב‬‬"
            ),
            (
                # translation_word
                "записывать",
                # pronunciation_word
                "lirʃom",
                # hebrew_word_nikud
                "‫לִרשוֹם‬‬"
            ),
            (
                # translation_word
                "защищать (страну)",
                # pronunciation_word
                "lehagen",
                # hebrew_word_nikud
                "‬‫לְהָגֵן‬"
            ),
            (
                # translation_word
                "звать (на помощь и т.п.)",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "знать (кого-л.)",
                # pronunciation_word
                "lehakir et",
                # hebrew_word_nikud
                "לְהַכִּיר‬ ‫אֶת‬‬"
            ),
            (
                # translation_word
                "знать (что-л.)",
                # pronunciation_word
                "la'daʿat",
                # hebrew_word_nikud
                "‬‫לָדַעַת‬"
            ),
            (
                # translation_word
                "играть",
                # pronunciation_word
                "lesaχek",
                # hebrew_word_nikud
                "‫לְשַׂחֵק‬‬"
            ),
            (
                # translation_word
                "идти",
                # pronunciation_word
                "la'leχet",
                # hebrew_word_nikud
                "‬‫לָלֶכֶת‬"
            ),
            (
                # translation_word
                "извинять",
                # pronunciation_word
                "lis'loaχ",
                # hebrew_word_nikud
                "‬‫לִסלוֹח‬"
            ),
            (
                # translation_word
                "извиняться",
                # pronunciation_word
                "lehitnaʦel",
                # hebrew_word_nikud
                "‫לְהִתנַצֵל‬‬"
            ),
            (
                # translation_word
                "изменить (поменять)",
                # pronunciation_word
                "leʃanot",
                # hebrew_word_nikud
                "‫לְשַנוֹת‬‬"
            ),
            (
                # translation_word
                "изучать",
                # pronunciation_word
                "lilmod",
                # hebrew_word_nikud
                "‫לִלמוֹד‬‬"
            ),
            (
                # translation_word
                "иметь",
                # pronunciation_word
                "lehaχzik",
                # hebrew_word_nikud
                "‬‫לְהַחזִיק‬"
            ),
            (
                # translation_word
                "интересоваться",
                # pronunciation_word
                "lehitʿanyen be…",
                # hebrew_word_nikud
                "‬לְהִתעַנייֵן‬ ‫ב‬"
            ),
            (
                # translation_word
                "информировать",
                # pronunciation_word
                "leho'dia",
                # hebrew_word_nikud
                "‫לְהוֹדִיע‬‬"
            ),
            (
                # translation_word
                "искать …",
                # pronunciation_word
                "leχapes",
                # hebrew_word_nikud
                "‫לְחַפֵּש‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "11. Самые важные глаголы - 2",
        # words
        [
            (
                # translation_word
                "контролировать",
                # pronunciation_word
                "liʃlot",
                # hebrew_word_nikud
                "‫לִשלוֹט‬‬"
            ),
            (
                # translation_word
                "красть",
                # pronunciation_word
                "lignov",
                # hebrew_word_nikud
                "‫לִגנוֹב‬‬"
            ),
            (
                # translation_word
                "кричать",
                # pronunciation_word
                "liʦʿok",
                # hebrew_word_nikud
                "‫לִצעוֹק‬‬"
            ),
            (
                # translation_word
                "купаться (в море и т.п.)",
                # pronunciation_word
                "lehitraχeʦ",
                # hebrew_word_nikud
                "‫לְהִתרַחֵץ‬‬"
            ),
            (
                # translation_word
                "лететь",
                # pronunciation_word
                "laʿuf",
                # hebrew_word_nikud
                "‬‫לָעוּף‬"
            ),
            (
                # translation_word
                "ловить",
                # pronunciation_word
                "litfos",
                # hebrew_word_nikud
                "‬‫לִתפוֹס‬"
            ),
            (
                # translation_word
                "ломать",
                # pronunciation_word
                "liʃbor",
                # hebrew_word_nikud
                "‬‫לִשבּוֹר‬"
            ),
            (
                # translation_word
                "любить (кого-л.)",
                # pronunciation_word
                "leʾehov",
                # hebrew_word_nikud
                "‫לֶאֱהוֹב‬‬"
            ),
            (
                # translation_word
                "молиться",
                # pronunciation_word
                "lehitpalel",
                # hebrew_word_nikud
                "‫לְהִתפַּלֵל‬‬"
            ),
            (
                # translation_word
                "молчать",
                # pronunciation_word
                "liʃtok",
                # hebrew_word_nikud
                "‬‫לִשתוֹק‬"
            ),
            (
                # translation_word
                "мочь",
                # pronunciation_word
                "yaχol",
                # hebrew_word_nikud
                "‬‫יָכוֹל‬"
            ),
            (
                # translation_word
                "наблюдать",
                # pronunciation_word
                "liʦpot,",
                # hebrew_word_nikud
                "‫לִצפּוֹת‬‬"
            ),
            (
                # translation_word
                "наблюдать",
                # pronunciation_word
                "lehaʃkif",
                # hebrew_word_nikud
                "‫לְהַשקִיף‬‬"
            ),
            (
                # translation_word
                "надеяться",
                # pronunciation_word
                "lekavot",
                # hebrew_word_nikud
                "‫לְקַווֹת‬‬"
            ),
            (
                # translation_word
                "наказывать",
                # pronunciation_word
                "lehaʿaniʃ",
                # hebrew_word_nikud
                "‬‫לְהַעֲנִיש‬"
            ),
            (
                # translation_word
                "настаивать (упорствовать)",
                # pronunciation_word
                "lehitʿakeʃ",
                # hebrew_word_nikud
                "‫לְהִתעַקֵש‬‬"
            ),
            (
                # translation_word
                "находить",
                # pronunciation_word
                "limʦo",
                # hebrew_word_nikud
                "‫לִמצוֹא‬‬"
            ),
            (
                # translation_word
                "начинать",
                # pronunciation_word
                "lehatχil",
                # hebrew_word_nikud
                "‫לְהַתחִיל‬‬"
            ),
            (
                # translation_word
                "недооценивать",
                # pronunciation_word
                "lehamʿit be'ʿereχ",
                # hebrew_word_nikud
                "‬לְהַמעִיט‬ ‫בְּעֵרֶך‬"
            ),
            (
                # translation_word
                "нравиться",
                # pronunciation_word
                "limʦo χen beʿei'nayim",
                # hebrew_word_nikud
                "‬לִמצוֹא‬ ‫חֵן‬ ‫בְּעֵינַיִים‬"
            ),
            (
                # translation_word
                "обедать",
                # pronunciation_word
                "leʾeχol aruχat ʦaha'rayim",
                # hebrew_word_nikud
                "לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‫צָהֳרַיִים‬‬"
            ),
            (
                # translation_word
                "обещать",
                # pronunciation_word
                "lehav'tiaχ",
                # hebrew_word_nikud
                "‫לְהַבטִיח‬‬"
            ),
            (
                # translation_word
                "обманывать",
                # pronunciation_word
                "leramot",
                # hebrew_word_nikud
                "‫לְרַמוֹת‬‬"
            ),
            (
                # translation_word
                "обсуждать",
                # pronunciation_word
                "ladun",
                # hebrew_word_nikud
                "‬‫לָדוּן‬"
            ),
            (
                # translation_word
                "объединять",
                # pronunciation_word
                "leʾaχed",
                # hebrew_word_nikud
                "‫לְאַחֵד‬‬"
            ),
            (
                # translation_word
                "объяснять",
                # pronunciation_word
                "lehasbir",
                # hebrew_word_nikud
                "‫לְהַסבִּיר‬‬"
            ),
            (
                # translation_word
                "означать",
                # pronunciation_word
                "lomar",
                # hebrew_word_nikud
                "‫לוֹמַר‬‬"
            ),
            (
                # translation_word
                "освобождать (город)",
                # pronunciation_word
                "leʃaχrer",
                # hebrew_word_nikud
                "‬‫לְשַחרֵר‬"
            ),
            (
                # translation_word
                "оскорблять",
                # pronunciation_word
                "lehaʿaliv",
                # hebrew_word_nikud
                "‫לְהַעֲלִיב‬‬"
            ),
            (
                # translation_word
                "останавливаться",
                # pronunciation_word
                "laʿaʦor",
                # hebrew_word_nikud
                "‫לַעֲצוֹר‬‬"
            ),
            (
                # translation_word
                "отвечать",
                # pronunciation_word
                "laʿanot",
                # hebrew_word_nikud
                "‫לְעַנוֹת‬‬"
            ),
            (
                # translation_word
                "отгадать",
                # pronunciation_word
                "lenaχeʃ",
                # hebrew_word_nikud
                "‬‫לְנַחֵש‬"
            ),
            (
                # translation_word
                "отказываться",
                # pronunciation_word
                "lesarev",
                # hebrew_word_nikud
                "‬‫לְסָרֵב‬"
            ),
            (
                # translation_word
                "открывать (дверь и т.п.)",
                # pronunciation_word
                "lif'toaχ",
                # hebrew_word_nikud
                "‫‫לִפתו‬ח‬‫‬"
            ),
            (
                # translation_word
                "отправлять",
                # pronunciation_word
                "liʃ'loaχ",
                # hebrew_word_nikud
                "‫לִשלוֹח‬‬"
            ),
            (
                # translation_word
                "охотиться",
                # pronunciation_word
                "laʦud",
                # hebrew_word_nikud
                "‫לָצוּד‬‬"
            ),
            (
                # translation_word
                "ошибаться",
                # pronunciation_word
                "litʿot",
                # hebrew_word_nikud
                "‫לִטעוֹת‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "12. Самые важные глаголы - 3",
        # words
        [
            (
                # translation_word
                "падать",
                # pronunciation_word
                "lipol",
                # hebrew_word_nikud
                "‫לִיפּוֹל‬‬"
            ),
            (
                # translation_word
                "переводить (текст)",
                # pronunciation_word
                "letargem",
                # hebrew_word_nikud
                "‬‫לְתַרגֵם‬"
            ),
            (
                # translation_word
                "писать",
                # pronunciation_word
                "liχtov",
                # hebrew_word_nikud
                "‬‫לִכתוֹב‬"
            ),
            (
                # translation_word
                "плавать",
                # pronunciation_word
                "lisχot",
                # hebrew_word_nikud
                "‬‫לִשׂחוֹת‬"
            ),
            (
                # translation_word
                "плакать",
                # pronunciation_word
                "livkot",
                # hebrew_word_nikud
                "‫לִבכּוֹת‬‬"
            ),
            (
                # translation_word
                "планировать",
                # pronunciation_word
                "letaχnen",
                # hebrew_word_nikud
                "‫לְתַכנֵן‬‬"
            ),
            (
                # translation_word
                "платить",
                # pronunciation_word
                "leʃalem",
                # hebrew_word_nikud
                "‬‫לְשַלֵם‬"
            ),
            (
                # translation_word
                "поворачивать",
                # pronunciation_word
                "lifnot",
                # hebrew_word_nikud
                "‬‫לִפנוֹת‬"
            ),
            (
                # translation_word
                "повторять",
                # pronunciation_word
                "laχazor al",
                # hebrew_word_nikud
                "לַחֲזוֹר‬ ‫עַל‬‬"
            ),
            (
                # translation_word
                "подписывать",
                # pronunciation_word
                "laχtom",
                # hebrew_word_nikud
                "‫לַחתוֹם‬‬"
            ),
            (
                # translation_word
                "подсказать (отгадку)",
                # pronunciation_word
                "lirmoz",
                # hebrew_word_nikud
                "‬‫לִרמוֹז‬"
            ),
            (
                # translation_word
                "показывать",
                # pronunciation_word
                "leharʾot",
                # hebrew_word_nikud
                "‬‫לְהַראוֹת‬"
            ),
            (
                # translation_word
                "помогать",
                # pronunciation_word
                "laʿazor",
                # hebrew_word_nikud
                "‫לַעֲזוֹר‬‬"
            ),
            (
                # translation_word
                "понимать",
                # pronunciation_word
                "lehavin",
                # hebrew_word_nikud
                "‬‫לְהָבִין‬"
            ),
            (
                # translation_word
                "предвидеть (ожидать)",
                # pronunciation_word
                "laχazot",
                # hebrew_word_nikud
                "‫לַחֲזוֹת‬‬"
            ),
            (
                # translation_word
                "предлагать",
                # pronunciation_word
                "leha'ʦiʿa",
                # hebrew_word_nikud
                "‬‫לְהַצִיע‬"
            ),
            (
                # translation_word
                "предпочитать",
                # pronunciation_word
                "lehaʿadif",
                # hebrew_word_nikud
                "‫לְהַעֲדִיף‬‬"
            ),
            (
                # translation_word
                "предупреждать",
                # pronunciation_word
                "lehazhir",
                # hebrew_word_nikud
                "‫לְהַזהִיר‬‬"
            ),
            (
                # translation_word
                "прекращать",
                # pronunciation_word
                "lehafsik",
                # hebrew_word_nikud
                "‫לְהַפסִיק‬‬"
            ),
            (
                # translation_word
                "приглашать",
                # pronunciation_word
                "lehazmin",
                # hebrew_word_nikud
                "‬‫לְהַזמִין‬"
            ),
            (
                # translation_word
                "приезжать",
                # pronunciation_word
                "leha'giʿa",
                # hebrew_word_nikud
                "‫לְהַגִיע‬‬"
            ),
            (
                # translation_word
                "приказывать",
                # pronunciation_word
                "lifkod",
                # hebrew_word_nikud
                "‫לִפקוֹד‬‬"
            ),
            (
                # translation_word
                "принадлежать",
                # pronunciation_word
                "lehiʃtayeχ",
                # hebrew_word_nikud
                "‫לְהִשתַייֵך‬‬"
            ),
            (
                # translation_word
                "пробовать (пытаться)",
                # pronunciation_word
                "lenasot",
                # hebrew_word_nikud
                "‬‫לְנַסוֹת‬"
            ),
            (
                # translation_word
                "продавать",
                # pronunciation_word
                "limkor",
                # hebrew_word_nikud
                "‫לִמכּוֹר‬‬"
            ),
            (
                # translation_word
                "продолжать",
                # pronunciation_word
                "lehamʃiχ",
                # hebrew_word_nikud
                "‫לְהַמשִיך‬‬"
            ),
            (
                # translation_word
                "произносить (слово)",
                # pronunciation_word
                "levate",
                # hebrew_word_nikud
                "‬‫לְבַטֵא‬"
            ),
            (
                # translation_word
                "пропускать (занятия и т.п.)",
                # pronunciation_word
                "lehaχsir",
                # hebrew_word_nikud
                "‫לְהַחסִיר‬‬"
            ),
            (
                # translation_word
                "просить",
                # pronunciation_word
                "levakeʃ",
                # hebrew_word_nikud
                "‬‫לְבַקֵש‬"
            ),
            (
                # translation_word
                "прощать",
                # pronunciation_word
                "lis'loaχ",
                # hebrew_word_nikud
                "‬‫לִסלוֹח‬"
            ),
            (
                # translation_word
                "прятать",
                # pronunciation_word
                "lehastir",
                # hebrew_word_nikud
                "‫לְהַסתִיר‬‬"
            ),
            (
                # translation_word
                "путать (ошибаться)",
                # pronunciation_word
                "lehitbalbel",
                # hebrew_word_nikud
                "‫לְהִתבַּלבֵּל‬"
            ),
            (
                # translation_word
                "работать",
                # pronunciation_word
                "laʿavod",
                # hebrew_word_nikud
                "‫לַעֲבוֹד‬‬"
            ),
            (
                # translation_word
                "разрешать",
                # pronunciation_word
                "leharʃot",
                # hebrew_word_nikud
                "‫לְהַרשוֹת‬‬"
            ),
            (
                # translation_word
                "рассчитывать на …",
                # pronunciation_word
                "lismoχ al",
                # hebrew_word_nikud
                "לִסמוֹך‬ ‫עַל‬‬"
            ),
            (
                # translation_word
                "резервировать",
                # pronunciation_word
                "lehazmin meroʃ",
                # hebrew_word_nikud
                "‬לְהַזמִין‬ ‫מֵרֹאש‬"
            ),
            (
                # translation_word
                "рекомендовать",
                # pronunciation_word
                "lehamliʦ",
                # hebrew_word_nikud
                "‬‫לְהַמלִיץ‬"
            ),
            (
                # translation_word
                "ронять",
                # pronunciation_word
                "lehapil",
                # hebrew_word_nikud
                "‫לְהַפִּיל‬‬"
            ),
            (
                # translation_word
                "ругать",
                # pronunciation_word
                "linzof",
                # hebrew_word_nikud
                "‬‫לִנזוֹף‬"
            ),
            (
                # translation_word
                "руководить (чем-л.)",
                # pronunciation_word
                "lenahel",
                # hebrew_word_nikud
                "‬‫לְנַהֵל‬"
            ),
            (
                # translation_word
                "рыть",
                # pronunciation_word
                "laχpor",
                # hebrew_word_nikud
                "‬‫לַחפּוֹר‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "13. Самые важные глаголы - 4",
        # words
        [
            (
                # translation_word
                "садиться",
                # pronunciation_word
                "lehityaʃev",
                # hebrew_word_nikud
                "‬‫לְהִתייַשֵב‬"
            ),
            (
                # translation_word
                "сказать",
                # pronunciation_word
                "lomar",
                # hebrew_word_nikud
                "‬‫לוֹמַר‬"
            ),
            (
                # translation_word
                "следовать за …",
                # pronunciation_word
                "laʿakov aχarei",
                # hebrew_word_nikud
                "לַעֲקוֹב‬ ‫אַחֲרֵי‬‬"
            ),
            (
                # translation_word
                "слышать",
                # pronunciation_word
                "liʃ'moʿa",
                # hebrew_word_nikud
                "‬‫לִשמוֹע‬"
            ),
            (
                # translation_word
                "смеяться",
                # pronunciation_word
                "liʦχok",
                # hebrew_word_nikud
                "‬‫לִצחוֹק‬"
            ),
            (
                # translation_word
                "снимать (напр. квартиру)",
                # pronunciation_word
                "liskor",
                # hebrew_word_nikud
                "‫לִשׂכּוֹר‬‬"
            ),
            (
                # translation_word
                "советовать",
                # pronunciation_word
                "leyaʿeʦ",
                # hebrew_word_nikud
                "‬‫לְייַעֵץ‬"
            ),
            (
                # translation_word
                "соглашаться",
                # pronunciation_word
                "lehaskim",
                # hebrew_word_nikud
                "‫לְהַסכִּים‬‬"
            ),
            (
                # translation_word
                "сожалеть",
                # pronunciation_word
                "lehiʦtaʿer",
                # hebrew_word_nikud
                "‬‫לְהִצטַעֵר‬"
            ),
            (
                # translation_word
                "создать",
                # pronunciation_word
                "liʦor",
                # hebrew_word_nikud
                "‬‫לִיצוֹר‬"
            ),
            (
                # translation_word
                "сомневаться",
                # pronunciation_word
                "lefakpek",
                # hebrew_word_nikud
                "‫לְפַקפֵּק‬‬"
            ),
            (
                # translation_word
                "сохранять",
                # pronunciation_word
                "liʃmor",
                # hebrew_word_nikud
                "‫לִשמוֹר‬‬"
            ),
            (
                # translation_word
                "спасать",
                # pronunciation_word
                "lehaʦil",
                # hebrew_word_nikud
                "‬‫לְהַצִיל‬"
            ),
            (
                # translation_word
                "спрашивать",
                # pronunciation_word
                "liʃʾol",
                # hebrew_word_nikud
                "‫לִשאוֹל‬‬"
            ),
            (
                # translation_word
                "спускаться",
                # pronunciation_word
                "la'redet",
                # hebrew_word_nikud
                "‫לָרֶדֶת‬‬"
            ),
            (
                # translation_word
                "сравнивать",
                # pronunciation_word
                "lehaʃvot",
                # hebrew_word_nikud
                "‫לְהַשווֹת‬‬"
            ),
            (
                # translation_word
                "стоить",
                # pronunciation_word
                "laʿalot",
                # hebrew_word_nikud
                "‬‫לַעֲלוֹת‬"
            ),
            (
                # translation_word
                "стрелять",
                # pronunciation_word
                "lirot",
                # hebrew_word_nikud
                "‬‫לִירוֹת‬"
            ),
            (
                # translation_word
                "существовать",
                # pronunciation_word
                "lehitkayem",
                # hebrew_word_nikud
                "‬‫לְהִתקַייֵם‬"
            ),
            (
                # translation_word
                "считать (подсчитывать)",
                # pronunciation_word
                "lispor",
                # hebrew_word_nikud
                "‫לִספּוֹר‬‬"
            ),
            (
                # translation_word
                "торопиться",
                # pronunciation_word
                "lemaher",
                # hebrew_word_nikud
                "‬‫לְמַהֵר‬"
            ),
            (
                # translation_word
                "требовать",
                # pronunciation_word
                "lidroʃ",
                # hebrew_word_nikud
                "‬‫לִדרוֹש‬"
            ),
            (
                # translation_word
                "требоваться",
                # pronunciation_word
                "lehidareʃ",
                # hebrew_word_nikud
                "‬‫לְהִידָרֵש‬"
            ),
            (
                # translation_word
                "трогать",
                # pronunciation_word
                "la'gaʿat",
                # hebrew_word_nikud
                "‫לָגַעַת‬‬"
            ),
            (
                # translation_word
                "убивать",
                # pronunciation_word
                "laharog",
                # hebrew_word_nikud
                "‬‫לַהֲרוֹג‬"
            ),
            (
                # translation_word
                "угрожать",
                # pronunciation_word
                "leʾayem",
                # hebrew_word_nikud
                "‫לְאַייֵם‬‬"
            ),
            (
                # translation_word
                "удивляться",
                # pronunciation_word
                "lehitpale",
                # hebrew_word_nikud
                "‫לְהִתפַּלֵא‬‬"
            ),
            (
                # translation_word
                "ужинать",
                # pronunciation_word
                "leʾeχol aruχat 'erev",
                # hebrew_word_nikud
                "‬לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‫עֶרֶב‬"
            ),
            (
                # translation_word
                "украшать",
                # pronunciation_word
                "lekaʃet",
                # hebrew_word_nikud
                "‫לְקַשֵט‬‬"
            ),
            (
                # translation_word
                "улыбаться",
                # pronunciation_word
                "leχayeχ",
                # hebrew_word_nikud
                "‫לְחַייֵך‬‬"
            ),
            (
                # translation_word
                "упоминать",
                # pronunciation_word
                "lehazkir",
                # hebrew_word_nikud
                "‫לְהַזכִּיר‬‬"
            ),
            (
                # translation_word
                "участвовать",
                # pronunciation_word
                "lehiʃtatef",
                # hebrew_word_nikud
                "‫לְהִשתַתֵף‬‬"
            ),
            (
                # translation_word
                "хвастаться",
                # pronunciation_word
                "lehitravrev",
                # hebrew_word_nikud
                "‬‫לְהִתרַברֵב‬"
            ),
            (
                # translation_word
                "хотеть",
                # pronunciation_word
                "lirʦot",
                # hebrew_word_nikud
                "‫לִרצוֹת‬‬"
            ),
            (
                # translation_word
                "хотеть есть",
                # pronunciation_word
                "lihyot raʿev",
                # hebrew_word_nikud
                "‬לִהיוֹת‬ ‫רָעֵב‬"
            ),
            (
                # translation_word
                "хотеть пить",
                # pronunciation_word
                "lihyot ʦame",
                # hebrew_word_nikud
                "‬לִהיוֹת‬ ‫צָמֵא‬"
            ),
            (
                # translation_word
                "читать",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "шутить",
                # pronunciation_word
                "lehitba'deaχ",
                # hebrew_word_nikud
                "‫לְהִתבַּדֵח‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "14. Цвета",
        # words
        [
            (
                # translation_word
                "цвет",
                # pronunciation_word
                "'ʦeva",
                # hebrew_word_nikud
                "‬‫צֶבַע‬"
            ),
            (
                # translation_word
                "радуга",
                # pronunciation_word
                "'keʃet",
                # hebrew_word_nikud
                "‬‫קֶשֶת‬"
            ),
            (
                # translation_word
                "белый",
                # pronunciation_word
                "lavan",
                # hebrew_word_nikud
                "‫לָבָן‬‬"
            ),
            (
                # translation_word
                "чёрный",
                # pronunciation_word
                "ʃaχor",
                # hebrew_word_nikud
                "‬‫שָחוֹר‬"
            ),
            (
                # translation_word
                "серый",
                # pronunciation_word
                "afor",
                # hebrew_word_nikud
                "‫אֲפוֹר‬‬"
            ),
            (
                # translation_word
                "зелёный",
                # pronunciation_word
                "yarok",
                # hebrew_word_nikud
                "‫יָרוֹק‬‬"
            ),
            (
                # translation_word
                "жёлтый",
                # pronunciation_word
                "ʦahov",
                # hebrew_word_nikud
                "‫צָהוֹב‬‬"
            ),
            (
                # translation_word
                "красный",
                # pronunciation_word
                "adom",
                # hebrew_word_nikud
                "‫אָדוֹם‬‬"
            ),
            (
                # translation_word
                "синий",
                # pronunciation_word
                "kaχol",
                # hebrew_word_nikud
                "‬‫כָּחוֹל‬"
            ),
            (
                # translation_word
                "голубой",
                # pronunciation_word
                "taχol",
                # hebrew_word_nikud
                "‬‫תָכוֹל‬"
            ),
            (
                # translation_word
                "розовый",
                # pronunciation_word
                "varod",
                # hebrew_word_nikud
                "‫וָרוֹד‬‬"
            ),
            (
                # translation_word
                "оранжевый",
                # pronunciation_word
                "katom",
                # hebrew_word_nikud
                "‬‫כָּתוֹם‬"
            ),
            (
                # translation_word
                "фиолетовый",
                # pronunciation_word
                "segol",
                # hebrew_word_nikud
                "‬‫סֶגוֹל‬"
            ),
            (
                # translation_word
                "коричневый",
                # pronunciation_word
                "χum",
                # hebrew_word_nikud
                "‫חוּם‬‬"
            ),
            (
                # translation_word
                "золотой",
                # pronunciation_word
                "zahov",
                # hebrew_word_nikud
                "‬‫זָהוֹב‬"
            ),
            (
                # translation_word
                "серебристый",
                # pronunciation_word
                "kasuf",
                # hebrew_word_nikud
                "‬‫כָּסוּף‬"
            ),
            (
                # translation_word
                "светлый",
                # pronunciation_word
                "bahir",
                # hebrew_word_nikud
                "‬‫בָּהִיר‬"
            ),
            (
                # translation_word
                "тёмный",
                # pronunciation_word
                "kehe",
                # hebrew_word_nikud
                "‬‫כֵּהֶה‬"
            ),
            (
                # translation_word
                "яркий",
                # pronunciation_word
                "bohek",
                # hebrew_word_nikud
                "‫בּוֹהֵק‬‬"
            ),
            (
                # translation_word
                "цветной (карандаш, (фильм))",
                # pronunciation_word
                "ʦivʿoni",
                # hebrew_word_nikud
                "‫צִבעוֹנִי‬‬"
            ),
            (
                # translation_word
                "чёрно-белый",
                # pronunciation_word
                "ʃaχor lavan",
                # hebrew_word_nikud
                "‬‫שָחוֹר־לָבָן‬"
            ),
            (
                # translation_word
                "разноцветный",
                # pronunciation_word
                "sasgoni",
                # hebrew_word_nikud
                "‬‫סַסגוֹנִי‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "15. Вопросы",
        # words
        [
            (
                # translation_word
                "Кто?",
                # pronunciation_word
                "mi?",
                # hebrew_word_nikud
                "?‫מִי‬‬"
            ),
            (
                # translation_word
                "Что?",
                # pronunciation_word
                "ma?",
                # hebrew_word_nikud
                "‬?‫מָה‬"
            ),
            (
                # translation_word
                "Где?",
                # pronunciation_word
                "'eifo?",
                # hebrew_word_nikud
                "‬?‫אֵיפֹה‬"
            ),
            (
                # translation_word
                "Куда?",
                # pronunciation_word
                "leʾan?",
                # hebrew_word_nikud
                "‬?‫לְאָן‬"
            ),
            (
                # translation_word
                "Откуда?",
                # pronunciation_word
                "me'ʾeifo?",
                # hebrew_word_nikud
                "?‫מֵאֵיפֹה‬‬"
            ),
            (
                # translation_word
                "Когда?",
                # pronunciation_word
                "matai?",
                # hebrew_word_nikud
                "?‫מָתַי‬‬"
            ),
            (
                # translation_word
                "Зачем?",
                # pronunciation_word
                "'lama?",
                # hebrew_word_nikud
                "‬?‫לָמָה‬"
            ),
            (
                # translation_word
                "Почему?",
                # pronunciation_word
                "ma'duʿa?",
                # hebrew_word_nikud
                "?ַ‫מַדוּע‬‬"
            ),
            (
                # translation_word
                "Для чего?",
                # pronunciation_word
                "biʃvil ma?",
                # hebrew_word_nikud
                "‬בִּשבִיל‬ ‫מָה‬"
            ),
            (
                # translation_word
                "Как?",
                # pronunciation_word
                "eiχ",
                # hebrew_word_nikud
                "‫אֵיך‬‬"
            ),
            (
                # translation_word
                "Как?",
                # pronunciation_word
                "keiʦad",
                # hebrew_word_nikud
                "‫כֵּיצַד‬‬"
            ),
            (
                # translation_word
                "Какой? Который?",
                # pronunciation_word
                "'eize?",
                # hebrew_word_nikud
                "‬?‫אֵיזֶה‬"
            ),
            (
                # translation_word
                "Кому?",
                # pronunciation_word
                "lemi?",
                # hebrew_word_nikud
                "‬?‫לְמִי‬"
            ),
            (
                # translation_word
                "О ком?",
                # pronunciation_word
                "al mi?",
                # hebrew_word_nikud
                "עַל‬ ‫מִי‬‬"
            ),
            (
                # translation_word
                "О чём?",
                # pronunciation_word
                "al ma?",
                # hebrew_word_nikud
                "‬עַל‬ ‫מַה‬"
            ),
            (
                # translation_word
                "С кем?",
                # pronunciation_word
                "im mi?",
                # hebrew_word_nikud
                "עִם‬ ‫מִי‬‬"
            ),
            (
                # translation_word
                "Сколько?",
                # pronunciation_word
                "'kama?",
                # hebrew_word_nikud
                "‬?‫כַּמָה‬"
            ),
            (
                # translation_word
                "Чей? Чья? Чьи?",
                # pronunciation_word
                "ʃel mi?",
                # hebrew_word_nikud
                "שֶל‬ ‫מִי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "16. Основные предлоги",
        # words
        [
            (
                # translation_word
                "с … (с кем-л.)",
                # pronunciation_word
                "im",
                # hebrew_word_nikud
                "‬‫עִם‬"
            ),
            (
                # translation_word
                "без",
                # pronunciation_word
                "bli",
                # hebrew_word_nikud
                "‫בּלִי‬"
            ),
            (
                # translation_word
                "без",
                # pronunciation_word
                "lelo",
                # hebrew_word_nikud
                "‫לְלֹא‬‬"
            ),
            (
                # translation_word
                "в (предлог движения)",
                # pronunciation_word
                "le…",
                # hebrew_word_nikud
                "‬…ְ‫ל‬"
            ),
            (
                # translation_word
                "о (говорить о …)",
                # pronunciation_word
                "al",
                # hebrew_word_nikud
                "‫עַל‬‬"
            ),
            (
                # translation_word
                "перед (во времени, в пространстве)",
                # pronunciation_word
                "lifnei",
                # hebrew_word_nikud
                "‬‫לִפנֵי‬"
            ),
            (
                # translation_word
                "под (внизу)",
                # pronunciation_word
                "mi'taχat le…",
                # hebrew_word_nikud
                "מִתַחַת‬ ‫ל‬‬"
            ),
            (
                # translation_word
                "над (наверху)",
                # pronunciation_word
                "meʿal",
                # hebrew_word_nikud
                "‫מֵעַל‬‬"
            ),
            (
                # translation_word
                "на (на чём-то)",
                # pronunciation_word
                "al",
                # hebrew_word_nikud
                "‫עַל‬‬"
            ),
            (
                # translation_word
                "из (откуда-то, о материале)",
                # pronunciation_word
                "mi, me",
                # hebrew_word_nikud
                "‬מ‬"
            ),
            (
                # translation_word
                "через … (о времени)",
                # pronunciation_word
                "toχ",
                # hebrew_word_nikud
                "‫תוֹך‬‬"
            ),
            (
                # translation_word
                "через (о препятствии)",
                # pronunciation_word
                "'dereχ",
                # hebrew_word_nikud
                "‬‫דֶרֶך‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "17. Вводные и служебные слова. Наречия - 1",
        # words
        [
            (
                # translation_word
                "здесь",
                # pronunciation_word
                "po",
                # hebrew_word_nikud
                "‫פֹּה‬‬"
            ),
            (
                # translation_word
                "здесь",
                # pronunciation_word
                "kan",
                # hebrew_word_nikud
                "‫כָּאן‬‬"
            ),
            (
                # translation_word
                "там",
                # pronunciation_word
                "ʃam",
                # hebrew_word_nikud
                "‫שָם‬‬"
            ),
            (
                # translation_word
                "где-то",
                # pronunciation_word
                "'eifo ʃehu",
                # hebrew_word_nikud
                "‬אֵיפֹה‬ ‫שֶהוּא‬"
            ),
            (
                # translation_word
                "нигде",
                # pronunciation_word
                "beʃum makom",
                # hebrew_word_nikud
                "‬בְּשוּם‬ ‫מָקוֹם‬"
            ),
            (
                # translation_word
                "у … (около)",
                # pronunciation_word
                "leyad …",
                # hebrew_word_nikud
                "‫לְיַד‬‬"
            ),
            (
                # translation_word
                "у окна",
                # pronunciation_word
                "leyad haχalon",
                # hebrew_word_nikud
                "לְיַד‬ ‫הַחַלוֹן‬‬"
            ),
            (
                # translation_word
                "сюда",
                # pronunciation_word
                "'hena",
                # hebrew_word_nikud
                "‬‫הֵנָה‬"
            ),
            (
                # translation_word
                "сюда",
                # pronunciation_word
                "lekan",
                # hebrew_word_nikud
                "‫לְכָאן‬‬"
            ),
            (
                # translation_word
                "туда",
                # pronunciation_word
                "leʃam",
                # hebrew_word_nikud
                "‫לְשָם‬‬"
            ),
            (
                # translation_word
                "отсюда",
                # pronunciation_word
                "mikan",
                # hebrew_word_nikud
                "‫מִכָּאן‬‬"
            ),
            (
                # translation_word
                "оттуда",
                # pronunciation_word
                "miʃam",
                # hebrew_word_nikud
                "‬‫מִשָם‬"
            ),
            (
                # translation_word
                "близко",
                # pronunciation_word
                "karov",
                # hebrew_word_nikud
                "‫קָרוֹב‬‬"
            ),
            (
                # translation_word
                "далеко",
                # pronunciation_word
                "raχok",
                # hebrew_word_nikud
                "‬‫רָחוֹק‬"
            ),
            (
                # translation_word
                "около (рядом)",
                # pronunciation_word
                "leyad",
                # hebrew_word_nikud
                "‬‫לְיַד‬"
            ),
            (
                # translation_word
                "недалеко (ехать, идти)",
                # pronunciation_word
                "lo raχok",
                # hebrew_word_nikud
                "‬לֹא‬ ‫רָחוֹק‬"
            ),
            (
                # translation_word
                "левый",
                # pronunciation_word
                "smali",
                # hebrew_word_nikud
                "‫שׂמָאלִי‬‬"
            ),
            (
                # translation_word
                "слева",
                # pronunciation_word
                "mismol",
                # hebrew_word_nikud
                "‫מִשׂמֹאל‬‬"
            ),
            (
                # translation_word
                "налево",
                # pronunciation_word
                "'smola",
                # hebrew_word_nikud
                "‫שׂמֹאלָה‬‬"
            ),
            (
                # translation_word
                "правый",
                # pronunciation_word
                "yemani",
                # hebrew_word_nikud
                "‫יְמָנִי‬‬"
            ),
            (
                # translation_word
                "справа",
                # pronunciation_word
                "miyamin",
                # hebrew_word_nikud
                "‫מִיָמִין‬‬"
            ),
            (
                # translation_word
                "направо",
                # pronunciation_word
                "ya'mina",
                # hebrew_word_nikud
                "‬‫יָמִינָה‬"
            ),
            (
                # translation_word
                "спереди",
                # pronunciation_word
                "mika'dima",
                # hebrew_word_nikud
                "‬‫מִקָדִימָה‬"
            ),
            (
                # translation_word
                "передний",
                # pronunciation_word
                "kidmi",
                # hebrew_word_nikud
                "‬‫קִדמִי‬"
            ),
            (
                # translation_word
                "вперёд (движение)",
                # pronunciation_word
                "ka'dima",
                # hebrew_word_nikud
                "‫קָדִימָה‬‬"
            ),
            (
                # translation_word
                "сзади (находиться, подойти)",
                # pronunciation_word
                "meʾaχor",
                # hebrew_word_nikud
                "‬‫מֵאָחוֹר‬"
            ),
            (
                # translation_word
                "назад (движение)",
                # pronunciation_word
                "a'χora",
                # hebrew_word_nikud
                "‫אָחוֹרָה‬‬"
            ),
            (
                # translation_word
                "середина",
                # pronunciation_word
                "'emʦa",
                # hebrew_word_nikud
                "‫אֶמצַע‬‬"
            ),
            (
                # translation_word
                "посередине",
                # pronunciation_word
                "ba'ʾemʦa",
                # hebrew_word_nikud
                "‫בָּאֶמצַע‬‬"
            ),
            (
                # translation_word
                "сбоку (со стороны)",
                # pronunciation_word
                "mehaʦad",
                # hebrew_word_nikud
                "‫מֵהַצַד‬‬"
            ),
            (
                # translation_word
                "везде",
                # pronunciation_word
                "beχol makom",
                # hebrew_word_nikud
                "בְּכָל‬ ‫מָקוֹם‬‬"
            ),
            (
                # translation_word
                "вокруг",
                # pronunciation_word
                "misaviv",
                # hebrew_word_nikud
                "‬‫מִסָבִיב‬"
            ),
            (
                # translation_word
                "изнутри",
                # pronunciation_word
                "mibifnim",
                # hebrew_word_nikud
                "‫מִבִּפנִים‬‬"
            ),
            (
                # translation_word
                "куда-то",
                # pronunciation_word
                "leʾan ʃehu",
                # hebrew_word_nikud
                "לְאָן‬ ‬‫שֶהוּא‬"
            ),
            (
                # translation_word
                "обратно",
                # pronunciation_word
                "baχazara",
                # hebrew_word_nikud
                "‬‫בַּחֲזָרָה‬"
            ),
            (
                # translation_word
                "во-первых",
                # pronunciation_word
                "reʃit",
                # hebrew_word_nikud
                "‫רֵאשִית‬‬"
            ),
            (
                # translation_word
                "во-вторых",
                # pronunciation_word
                "ʃenit",
                # hebrew_word_nikud
                "‫שֵנִית‬‬"
            ),
            (
                # translation_word
                "в-третьих",
                # pronunciation_word
                "ʃliʃit",
                # hebrew_word_nikud
                "‫שלִִישִית‬‬"
            ),
            (
                # translation_word
                "заново",
                # pronunciation_word
                "meχadaʃ",
                # hebrew_word_nikud
                "‬‫מֵחָדָש‬"
            ),
            (
                # translation_word
                "никогда",
                # pronunciation_word
                "af 'paʿam",
                # hebrew_word_nikud
                "אַף‬ ‫פַּעַם‬‬"
            ),
            (
                # translation_word
                "никогда",
                # pronunciation_word
                "meʿolam",
                # hebrew_word_nikud
                "‬‫מֵעוֹלָם‬"
            ),
            (
                # translation_word
                "опять",
                # pronunciation_word
                "ʃuv",
                # hebrew_word_nikud
                "‬‫שוּב‬"
            ),
            (
                # translation_word
                "теперь",
                # pronunciation_word
                "aχʃav",
                # hebrew_word_nikud
                "‬‫עַכשָיו‬"
            ),
            (
                # translation_word
                "теперь",
                # pronunciation_word
                "kaʿet",
                # hebrew_word_nikud
                "‫כָּעֵת‬‬"
            ),
            (
                # translation_word
                "часто",
                # pronunciation_word
                "leʿitim krovot",
                # hebrew_word_nikud
                "‬לְעִיתִים‬ ‫קרוֹבוֹת‬"
            ),
            (
                # translation_word
                "тогда",
                # pronunciation_word
                "az",
                # hebrew_word_nikud
                "‬‫אָז‬"
            ),
            (
                # translation_word
                "срочно",
                # pronunciation_word
                "bidχifut",
                # hebrew_word_nikud
                "‬‫בִּדחִיפוּת‬"
            ),
            (
                # translation_word
                "обычно",
                # pronunciation_word
                "be'dereχ klal",
                # hebrew_word_nikud
                "בְּדֶרֶך‬ ‫כּלָל‬‬"
            ),
            (
                # translation_word
                "кстати, …",
                # pronunciation_word
                "'dereχ 'agav",
                # hebrew_word_nikud
                "‬דֶרֶך‬ ‫אַגַב‬"
            ),
            (
                # translation_word
                "возможно",
                # pronunciation_word
                "efʃari",
                # hebrew_word_nikud
                "‫אֶפשָרִי‬‬"
            ),
            (
                # translation_word
                "вероятно",
                # pronunciation_word
                "kanirʾe",
                # hebrew_word_nikud
                "‫כַּנִראֶה‬‬"
            ),
            (
                # translation_word
                "может быть",
                # pronunciation_word
                "ulai",
                # hebrew_word_nikud
                "‫אוּלַי‬‬"
            ),
            (
                # translation_word
                "кроме того, …",
                # pronunciation_word
                "χuʦ mize …",
                # hebrew_word_nikud
                "חוּץ‬ ‫מִזֶה‬‬"
            ),
            (
                # translation_word
                "поэтому …",
                # pronunciation_word
                "laχen",
                # hebrew_word_nikud
                "‬‫לָכֵן‬"
            ),
            (
                # translation_word
                "несмотря на …",
                # pronunciation_word
                "lamrot …",
                # hebrew_word_nikud
                "‬‫לַמרוֹת‬"
            ),
            (
                # translation_word
                "благодаря …",
                # pronunciation_word
                "hodot le…",
                # hebrew_word_nikud
                "‬הוֹדוֹת‬ ‫ל‬"
            ),
            (
                # translation_word
                "что (союз)",
                # pronunciation_word
                "ʃe",
                # hebrew_word_nikud
                "‫ש‬‬"
            ),
            (
                # translation_word
                "что-то, что-нибудь",
                # pronunciation_word
                "'maʃehu",
                # hebrew_word_nikud
                "‫מַשֶהו‬‬"
            ),
            (
                # translation_word
                "ничего",
                # pronunciation_word
                "klum",
                # hebrew_word_nikud
                "‬‫כּלוּם‬"
            ),
            (
                # translation_word
                "кто-то, кто-нибудь (м.р.)",
                # pronunciation_word
                "'miʃehu",
                # hebrew_word_nikud
                "‫מִישֶהו‬‬"
            ),
            (
                # translation_word
                "кто-то, кто-нибудь (ж.р.)",
                # pronunciation_word
                "'miʃehi",
                # hebrew_word_nikud
                "‫מִישֶהִי‬‬"
            ),
            (
                # translation_word
                "никто (м.р.)",
                # pronunciation_word
                "af eχad",
                # hebrew_word_nikud
                "‬אַף‬ ‫אֶחָד‬"
            ),
            (
                # translation_word
                "никто (ж.р.)",
                # pronunciation_word
                "af aχat",
                # hebrew_word_nikud
                "‬אַף‬ ‫אַחַת‬"
            ),
            (
                # translation_word
                "никуда",
                # pronunciation_word
                "leʃum makom",
                # hebrew_word_nikud
                "לְשוּם‬ ‫מָקוֹם‬‬"
            ),
            (
                # translation_word
                "так",
                # pronunciation_word
                "kol kaχ",
                # hebrew_word_nikud
                "‫כָּל־כָּך‬‬"
            ),
            (
                # translation_word
                "также, тоже",
                # pronunciation_word
                "gam",
                # hebrew_word_nikud
                "‫גַם‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "18. Вводные и служебные слова. Наречия - 2",
        # words
        [
            (
                # translation_word
                "Почему?",
                # pronunciation_word
                "ma'duʿa?",
                # hebrew_word_nikud
                "?ַ‫מַדוּע‬‬"
            ),
            (
                # translation_word
                "почему-то",
                # pronunciation_word
                "miʃum ma",
                # hebrew_word_nikud
                "‫מִשוּם־מָה‬‬"
            ),
            (
                # translation_word
                "потому, что …",
                # pronunciation_word
                "miʃum ʃe",
                # hebrew_word_nikud
                "מִשוּם‬ ‫ש‬‬"
            ),
            (
                # translation_word
                "зачем-то",
                # pronunciation_word
                "lematara 'kolʃehi",
                # hebrew_word_nikud
                "לְמַטָרָה‬ ‫כָּלשֶהִי‬‬"
            ),
            (
                # translation_word
                "и",
                # pronunciation_word
                "ve …",
                # hebrew_word_nikud
                "‬ְ‫ו‬"
            ),
            (
                # translation_word
                "или",
                # pronunciation_word
                "o",
                # hebrew_word_nikud
                "‬‫או‬"
            ),
            (
                # translation_word
                "но",
                # pronunciation_word
                "ulam",
                # hebrew_word_nikud
                "‫אוּלָם‬‬"
            ),
            (
                # translation_word
                "но",
                # pronunciation_word
                "aval",
                # hebrew_word_nikud
                "‫אֲבָל‬‬"
            ),
            (
                # translation_word
                "для (предлог)",
                # pronunciation_word
                "biʃvil",
                # hebrew_word_nikud
                "‬‫בִּשבִיל‬"
            ),
            (
                # translation_word
                "слишком",
                # pronunciation_word
                "yoter midai",
                # hebrew_word_nikud
                "‬‫מִדַי‬ ‫יוֹתֵר‬"
            ),
            (
                # translation_word
                "только",
                # pronunciation_word
                "rak",
                # hebrew_word_nikud
                "‬‫רַק‬"
            ),
            (
                # translation_word
                "точно",
                # pronunciation_word
                "bediyuk",
                # hebrew_word_nikud
                "‬‫בְּדִיוּק‬"
            ),
            (
                # translation_word
                "около (~ 10 кг), приблизительно",
                # pronunciation_word
                "be'ʿereχ",
                # hebrew_word_nikud
                "‬‫בְּעֵרֶך‬"
            ),
            (
                # translation_word
                "почти",
                # pronunciation_word
                "kimʿat",
                # hebrew_word_nikud
                "‫כִּמעַט‬‬"
            ),
            (
                # translation_word
                "другой (второй), другой (иной)",
                # pronunciation_word
                "aχer",
                # hebrew_word_nikud
                "‫אַחֵר‬‬"
            ),
            (
                # translation_word
                "каждый",
                # pronunciation_word
                "kol",
                # hebrew_word_nikud
                "‫כֹּל‬‬"
            ),
            (
                # translation_word
                "любой",
                # pronunciation_word
                "kolʃehu",
                # hebrew_word_nikud
                "‫כָּלשֶהו‬‬"
            ),
            (
                # translation_word
                "много",
                # pronunciation_word
                "harbe",
                # hebrew_word_nikud
                "‬‫הַרבֵּה‬"
            ),
            (
                # translation_word
                "все (все люди)",
                # pronunciation_word
                "kulam",
                # hebrew_word_nikud
                "‫כּוּלָם‬‬"
            ),
            (
                # translation_word
                "вручную",
                # pronunciation_word
                "bayad",
                # hebrew_word_nikud
                "‬‫בַּיָד‬"
            ),
            (
                # translation_word
                "вряд ли",
                # pronunciation_word
                "safek im",
                # hebrew_word_nikud
                "‫אִם‬ ‫סָפֵק‬‬"
            ),
            (
                # translation_word
                "наверное (вероятно)",
                # pronunciation_word
                "karov levadai",
                # hebrew_word_nikud
                "‫לְווַדַאי‬ ‫קָרוֹב‬‬"
            ),
            (
                # translation_word
                "нарочно (намеренно, специально)",
                # pronunciation_word
                "'davka",
                # hebrew_word_nikud
                "‫דַווקָא‬‬"
            ),
            (
                # translation_word
                "случайно",
                # pronunciation_word
                "bemikre",
                # hebrew_word_nikud
                "‫בְּמִקרֶה‬‬"
            ),
            (
                # translation_word
                "очень",
                # pronunciation_word
                "meʾod",
                # hebrew_word_nikud
                "‫מְאוֹד‬‬"
            ),
            (
                # translation_word
                "например",
                # pronunciation_word
                "lemaʃal",
                # hebrew_word_nikud
                "‬‫לְמָשָל‬"
            ),
            (
                # translation_word
                "между",
                # pronunciation_word
                "bein",
                # hebrew_word_nikud
                "‬‫בֵּין‬"
            ),
            (
                # translation_word
                "среди",
                # pronunciation_word
                "be'kerev",
                # hebrew_word_nikud
                "‬‫בְּקֶרֶב‬"
            ),
            (
                # translation_word
                "столько",
                # pronunciation_word
                "kol kaχ harbe",
                # hebrew_word_nikud
                "כָּל־כָּך‬ ‫הַרבֵּה‬‬"
            ),
            (
                # translation_word
                "особенно",
                # pronunciation_word
                "bimyuχad",
                # hebrew_word_nikud
                "‬‫בִּמיוּחָד‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "19. Противоположности",
        # words
        [
            (
                # translation_word
                "богатый",
                # pronunciation_word
                "aʃir",
                # hebrew_word_nikud
                "‬‫עָשִיר‬"
            ),
            (
                # translation_word
                "бедный",
                # pronunciation_word
                "ani",
                # hebrew_word_nikud
                "‫עָנִי‬‬"
            ),
            (
                # translation_word
                "больной",
                # pronunciation_word
                "χole",
                # hebrew_word_nikud
                "‬‫חוֹלֶה‬"
            ),
            (
                # translation_word
                "здоровый",
                # pronunciation_word
                "bari",
                # hebrew_word_nikud
                "‫בָּרִיא‬‬"
            ),
            (
                # translation_word
                "большой",
                # pronunciation_word
                "gadol",
                # hebrew_word_nikud
                "‬‫גָדוֹל‬"
            ),
            (
                # translation_word
                "маленький",
                # pronunciation_word
                "katan",
                # hebrew_word_nikud
                "‫קָטַן‬‬"
            ),
            (
                # translation_word
                "быстро",
                # pronunciation_word
                "maher",
                # hebrew_word_nikud
                "‬‫מַהֵר‬"
            ),
            (
                # translation_word
                "медленно",
                # pronunciation_word
                "leʾat",
                # hebrew_word_nikud
                "‬‫לְאַט‬"
            ),
            (
                # translation_word
                "быстрый",
                # pronunciation_word
                "mahir",
                # hebrew_word_nikud
                "‫מָהִיר‬‬"
            ),
            (
                # translation_word
                "медленный",
                # pronunciation_word
                "iti",
                # hebrew_word_nikud
                "‫אִיטִי‬‬"
            ),
            (
                # translation_word
                "весёлый",
                # pronunciation_word
                "sa'meaχ",
                # hebrew_word_nikud
                "‫שָׂמֵח‬‬"
            ),
            (
                # translation_word
                "грустный",
                # pronunciation_word
                "aʦuv",
                # hebrew_word_nikud
                "‫עָצוּב‬‬"
            ),
            (
                # translation_word
                "вместе",
                # pronunciation_word
                "be'yaχad",
                # hebrew_word_nikud
                "‬‫בְּיַחַד‬"
            ),
            (
                # translation_word
                "отдельно",
                # pronunciation_word
                "levad",
                # hebrew_word_nikud
                "‫לְבַד‬‬"
            ),
            (
                # translation_word
                "вслух",
                # pronunciation_word
                "bekol ram",
                # hebrew_word_nikud
                "בְּקוֹל‬ ‫רָם‬‬"
            ),
            (
                # translation_word
                "про себя (не вслух)",
                # pronunciation_word
                "belev",
                # hebrew_word_nikud
                "‫בְּלֵב‬‬"
            ),
            (
                # translation_word
                "про себя (не вслух)",
                # pronunciation_word
                "be'ʃeket",
                # hebrew_word_nikud
                "‫בְּשֶקֶט‬‬"
            ),
            (
                # translation_word
                "высокий",
                # pronunciation_word
                "ga'voha",
                # hebrew_word_nikud
                "‬‫גָבוֹה‬"
            ),
            (
                # translation_word
                "низкий",
                # pronunciation_word
                "namuχ",
                # hebrew_word_nikud
                "‫נָמוּך‬‬"
            ),
            (
                # translation_word
                "глубокий",
                # pronunciation_word
                "amok",
                # hebrew_word_nikud
                "‬‫עָמוֹק‬"
            ),
            (
                # translation_word
                "мелкий",
                # pronunciation_word
                "radud",
                # hebrew_word_nikud
                "‫רָדוּד‬‬"
            ),
            (
                # translation_word
                "да",
                # pronunciation_word
                "ken",
                # hebrew_word_nikud
                "‫כֵּן‬‬"
            ),
            (
                # translation_word
                "нет",
                # pronunciation_word
                "lo",
                # hebrew_word_nikud
                "‬‫לֹא‬"
            ),
            (
                # translation_word
                "далёкий",
                # pronunciation_word
                "raχok",
                # hebrew_word_nikud
                "‬‫רָחוֹק‬"
            ),
            (
                # translation_word
                "близкий",
                # pronunciation_word
                "karov",
                # hebrew_word_nikud
                "‫קָרוֹב‬‬"
            ),
            (
                # translation_word
                "длинный",
                # pronunciation_word
                "aroχ",
                # hebrew_word_nikud
                "‬‫אָרוֹך‬"
            ),
            (
                # translation_word
                "короткий",
                # pronunciation_word
                "kaʦar",
                # hebrew_word_nikud
                "‫קָצַר‬‬"
            ),
            (
                # translation_word
                "добрый",
                # pronunciation_word
                "tov lev",
                # hebrew_word_nikud
                "‬טוֹב‬ ‫לֵב‬"
            ),
            (
                # translation_word
                "злой",
                # pronunciation_word
                "raʃa",
                # hebrew_word_nikud
                "‫רָשָע‬‬"
            ),
            (
                # translation_word
                "женатый",
                # pronunciation_word
                "nasui",
                # hebrew_word_nikud
                "‫נָשׂוּי‬‬"
            ),
            (
                # translation_word
                "холостой",
                # pronunciation_word
                "ravak",
                # hebrew_word_nikud
                "‬‫רַווָק‬"
            ),
            (
                # translation_word
                "конец",
                # pronunciation_word
                "sof",
                # hebrew_word_nikud
                "‬‫סוֹף‬"
            ),
            (
                # translation_word
                "начало",
                # pronunciation_word
                "hatχala",
                # hebrew_word_nikud
                "‬‫הַתחָלָה‬"
            ),
            (
                # translation_word
                "левый",
                # pronunciation_word
                "smali",
                # hebrew_word_nikud
                "‬‫שׂמָאלִי‬"
            ),
            (
                # translation_word
                "правый",
                # pronunciation_word
                "yemani",
                # hebrew_word_nikud
                "‫יְמָנִי‬‬"
            ),
            (
                # translation_word
                "первый",
                # pronunciation_word
                "riʃon",
                # hebrew_word_nikud
                "‫רִאשוֹן‬‬"
            ),
            (
                # translation_word
                "последний",
                # pronunciation_word
                "aχaron",
                # hebrew_word_nikud
                "‫אַחֲרוֹן‬‬"
            ),
            (
                # translation_word
                "прямой",
                # pronunciation_word
                "yaʃar",
                # hebrew_word_nikud
                "‬‫יָשָר‬"
            ),
            (
                # translation_word
                "кривой",
                # pronunciation_word
                "meʿukal",
                # hebrew_word_nikud
                "‫מְעוּקָל‬‬"
            ),
            (
                # translation_word
                "рай",
                # pronunciation_word
                "gan 'eden",
                # hebrew_word_nikud
                "גַן‬ ‫עֵדֶן‬‬"
            ),
            (
                # translation_word
                "ад",
                # pronunciation_word
                "gehinom",
                # hebrew_word_nikud
                "‫גֵיהִינוֹם‬‬"
            ),
            (
                # translation_word
                "сильный",
                # pronunciation_word
                "χazak",
                # hebrew_word_nikud
                "‫חָזָק‬‬"
            ),
            (
                # translation_word
                "слабый",
                # pronunciation_word
                "χalaʃ",
                # hebrew_word_nikud
                "‬‫חַלָש‬"
            ),
            (
                # translation_word
                "старый",
                # pronunciation_word
                "zaken",
                # hebrew_word_nikud
                "‬‫זָקֵן‬"
            ),
            (
                # translation_word
                "молодой",
                # pronunciation_word
                "ʦaʿir",
                # hebrew_word_nikud
                "‬‫צָעִיר‬"
            ),
            (
                # translation_word
                "старый",
                # pronunciation_word
                "yaʃan",
                # hebrew_word_nikud
                "‬‫יָשָן‬"
            ),
            (
                # translation_word
                "новый",
                # pronunciation_word
                "χadaʃ",
                # hebrew_word_nikud
                "‬‫חָדָש‬"
            ),
            (
                # translation_word
                "твёрдый",
                # pronunciation_word
                "kaʃe",
                # hebrew_word_nikud
                "‬‫קָשֶה‬"
            ),
            (
                # translation_word
                "мягкий",
                # pronunciation_word
                "raχ",
                # hebrew_word_nikud
                "‫רַך‬‬"
            ),
            (
                # translation_word
                "тёплый",
                # pronunciation_word
                "χamim",
                # hebrew_word_nikud
                "‬‫חָמִים‬"
            ),
            (
                # translation_word
                "холодный",
                # pronunciation_word
                "kar",
                # hebrew_word_nikud
                "‫קַר‬‬"
            ),
            (
                # translation_word
                "толстый",
                # pronunciation_word
                "ʃamen",
                # hebrew_word_nikud
                "‫שָמֵן‬‬"
            ),
            (
                # translation_word
                "худой",
                # pronunciation_word
                "raze",
                # hebrew_word_nikud
                "‬‫רָזֶה‬"
            ),
            (
                # translation_word
                "узкий",
                # pronunciation_word
                "ʦar",
                # hebrew_word_nikud
                "‬‫צַר‬"
            ),
            (
                # translation_word
                "широкий",
                # pronunciation_word
                "raχav",
                # hebrew_word_nikud
                "‬‫רָחָב‬"
            ),
            (
                # translation_word
                "хороший",
                # pronunciation_word
                "tov",
                # hebrew_word_nikud
                "‫טוֹב‬‬"
            ),
            (
                # translation_word
                "плохой",
                # pronunciation_word
                "ra",
                # hebrew_word_nikud
                "‫רַע‬‬"
            ),
            (
                # translation_word
                "храбрый",
                # pronunciation_word
                "amiʦ",
                # hebrew_word_nikud
                "‫אַמִיץ‬‬"
            ),
            (
                # translation_word
                "трусливый",
                # pronunciation_word
                "paχdani",
                # hebrew_word_nikud
                "‫פַּחדָנִי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "20. Дни недели",
        # words
        [
            (
                # translation_word
                "понедельник",
                # pronunciation_word
                "yom ʃeni",
                # hebrew_word_nikud
                "‬יום‬ ‫שֵנִי‬"
            ),
            (
                # translation_word
                "вторник",
                # pronunciation_word
                "yom ʃliʃi",
                # hebrew_word_nikud
                "יוֹם‬ ‫שלִישִי‬‬"
            ),
            (
                # translation_word
                "среда",
                # pronunciation_word
                "yom reviʿi",
                # hebrew_word_nikud
                "יוֹם‬ ‫רְבִיעִי‬‬"
            ),
            (
                # translation_word
                "четверг",
                # pronunciation_word
                "yom χamiʃi",
                # hebrew_word_nikud
                "‬יוֹם‬ ‫חֲמִישִי‬"
            ),
            (
                # translation_word
                "пятница",
                # pronunciation_word
                "yom ʃiʃi",
                # hebrew_word_nikud
                "יוֹם‬ ‫שִישִי‬‬"
            ),
            (
                # translation_word
                "суббота",
                # pronunciation_word
                "ʃabat",
                # hebrew_word_nikud
                "‬‫שַבָּת‬"
            ),
            (
                # translation_word
                "воскресенье",
                # pronunciation_word
                "yom riʃon",
                # hebrew_word_nikud
                "יוֹם‬ ‫רִאשוֹן‬‬"
            ),
            (
                # translation_word
                "сегодня",
                # pronunciation_word
                "hayom",
                # hebrew_word_nikud
                "‬‫הַיוֹם‬"
            ),
            (
                # translation_word
                "завтра",
                # pronunciation_word
                "maχar",
                # hebrew_word_nikud
                "‬‫מָחָר‬"
            ),
            (
                # translation_word
                "послезавтра",
                # pronunciation_word
                "maχara'tayim",
                # hebrew_word_nikud
                "‫מָחֳרָתַיִים‬‬"
            ),
            (
                # translation_word
                "вчера",
                # pronunciation_word
                "etmol",
                # hebrew_word_nikud
                "‫אֶתמוֹל‬‬"
            ),
            (
                # translation_word
                "позавчера",
                # pronunciation_word
                "ʃilʃom",
                # hebrew_word_nikud
                "‫שִלשוֹם‬‬"
            ),
            (
                # translation_word
                "день",
                # pronunciation_word
                "yom",
                # hebrew_word_nikud
                "‫יוֹם‬‬"
            ),
            (
                # translation_word
                "рабочий день",
                # pronunciation_word
                "yom avoda",
                # hebrew_word_nikud
                "יום‬ ‫עֲבוֹדָה‬‬"
            ),
            (
                # translation_word
                "праздничный день",
                # pronunciation_word
                "yom χag",
                # hebrew_word_nikud
                "‬יוֹם‬ ‫חַג‬"
            ),
            (
                # translation_word
                "выходной день",
                # pronunciation_word
                "yom menuχa",
                # hebrew_word_nikud
                "יום‬ ‫מְנוּחָה‬‬"
            ),
            (
                # translation_word
                "выходные",
                # pronunciation_word
                "sof ʃa'vuʿa",
                # hebrew_word_nikud
                "סוֹף‬ ‫שָבוּע‬‬"
            ),
            (
                # translation_word
                "весь день",
                # pronunciation_word
                "kol hayom",
                # hebrew_word_nikud
                "כָּל‬ ‫הַיוֹם‬‬"
            ),
            (
                # translation_word
                "ежедневно",
                # pronunciation_word
                "midei yom",
                # hebrew_word_nikud
                "מִדֵי‬ ‫יוֹם‬‬"
            ),
            (
                # translation_word
                "неделя",
                # pronunciation_word
                "ʃa'vua",
                # hebrew_word_nikud
                "‬‫שָבוּע‬"
            ),
            (
                # translation_word
                "еженедельно",
                # pronunciation_word
                "kol ʃa'vuʿa",
                # hebrew_word_nikud
                "‬כָּל‬ ‫שָבוּע‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "21. Часы. Время суток",
        # words
        [
            (
                # translation_word
                "утро",
                # pronunciation_word
                "'boker",
                # hebrew_word_nikud
                "‫בּוֹקֶר‬‬"
            ),
            (
                # translation_word
                "утром",
                # pronunciation_word
                "ba'boker",
                # hebrew_word_nikud
                "‫בַּבּוֹקֶר‬‬"
            ),
            (
                # translation_word
                "полдень",
                # pronunciation_word
                "ʦaha'rayim",
                # hebrew_word_nikud
                "‫צָהֳרַיִים‬‬"
            ),
            (
                # translation_word
                "после обеда",
                # pronunciation_word
                "aχar haʦaha'rayim",
                # hebrew_word_nikud
                "אַחַר‬ ‫הַצָהֳרַיִים‬‬"
            ),
            (
                # translation_word
                "вечер",
                # pronunciation_word
                "'erev",
                # hebrew_word_nikud
                "‬‫עֶרֶב‬"
            ),
            (
                # translation_word
                "вечером",
                # pronunciation_word
                "ba'ʿerev",
                # hebrew_word_nikud
                "‫בַּעֶרֶב‬‬"
            ),
            (
                # translation_word
                "ночь",
                # pronunciation_word
                "'laila",
                # hebrew_word_nikud
                "‫לַילָה‬‬"
            ),
            (
                # translation_word
                "ночью",
                # pronunciation_word
                "ba'laila",
                # hebrew_word_nikud
                "‬‫בַּלַילָה‬"
            ),
            (
                # translation_word
                "полночь",
                # pronunciation_word
                "χaʦot",
                # hebrew_word_nikud
                "‫חֲצוֹת‬‬"
            ),
            (
                # translation_word
                "секунда",
                # pronunciation_word
                "ʃniya",
                # hebrew_word_nikud
                "‫שנִייָה‬‬"
            ),
            (
                # translation_word
                "минута",
                # pronunciation_word
                "daka",
                # hebrew_word_nikud
                "‬‫דַקָה‬"
            ),
            (
                # translation_word
                "час",
                # pronunciation_word
                "ʃaʿa",
                # hebrew_word_nikud
                "‫שָעָה‬‬"
            ),
            (
                # translation_word
                "полчаса",
                # pronunciation_word
                "χaʦi ʃaʿa",
                # hebrew_word_nikud
                "חֲצִי‬ ‫שָעָה‬‬"
            ),
            (
                # translation_word
                "15 минут",
                # pronunciation_word
                "'reva ʃaʿa",
                # hebrew_word_nikud
                "רֶבַע‬ ‫שָעָה‬‬"
            ),
            (
                # translation_word
                "сутки",
                # pronunciation_word
                "yemama",
                # hebrew_word_nikud
                "‬‫יְמָמָה‬"
            ),
            (
                # translation_word
                "восход солнца",
                # pronunciation_word
                "zriχa",
                # hebrew_word_nikud
                "‫זרִיחָה‬‬"
            ),
            (
                # translation_word
                "закат",
                # pronunciation_word
                "ʃkiʿa",
                # hebrew_word_nikud
                "‫שקִיעָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "22. Месяцы. Времена года",
        # words
        [
            (
                # translation_word
                "январь",
                # pronunciation_word
                "'yanuʾar",
                # hebrew_word_nikud
                "‫יָנוּאָר‬‬"
            ),
            (
                # translation_word
                "февраль",
                # pronunciation_word
                "'februʾar",
                # hebrew_word_nikud
                "‫פֶבּרוּאָר‬‬"
            ),
            (
                # translation_word
                "март",
                # pronunciation_word
                "merʦ",
                # hebrew_word_nikud
                "‫מֶרץ‬‬"
            ),
            (
                # translation_word
                "апрель",
                # pronunciation_word
                "april",
                # hebrew_word_nikud
                "‬‫אַפּרִיל‬"
            ),
            (
                # translation_word
                "май",
                # pronunciation_word
                "mai",
                # hebrew_word_nikud
                "‫מַאי‬‬"
            ),
            (
                # translation_word
                "июнь",
                # pronunciation_word
                "'yuni",
                # hebrew_word_nikud
                "‫יוּנִי‬‬"
            ),
            (
                # translation_word
                "июль",
                # pronunciation_word
                "'yuli",
                # hebrew_word_nikud
                "‫יוּלִי‬‬"
            ),
            (
                # translation_word
                "август",
                # pronunciation_word
                "'ogust",
                # hebrew_word_nikud
                "‫אוֹגוּסט‬‬"
            ),
            (
                # translation_word
                "сентябрь",
                # pronunciation_word
                "sep'tember",
                # hebrew_word_nikud
                "‫סֶפּטֶמבֶּר‬‬"
            ),
            (
                # translation_word
                "октябрь",
                # pronunciation_word
                "ok'tober",
                # hebrew_word_nikud
                "‫אוֹקטוֹבֶּר‬‬"
            ),
            (
                # translation_word
                "ноябрь",
                # pronunciation_word
                "no'vember",
                # hebrew_word_nikud
                "‫נוֹבֶמבֶּר‬‬"
            ),
            (
                # translation_word
                "декабрь",
                # pronunciation_word
                "de'ʦember",
                # hebrew_word_nikud
                "‫דֶצֶמבֶּר‬‬"
            ),
            (
                # translation_word
                "весна",
                # pronunciation_word
                "aviv",
                # hebrew_word_nikud
                "‫אָבִיב‬‬"
            ),
            (
                # translation_word
                "весной",
                # pronunciation_word
                "baʾaviv",
                # hebrew_word_nikud
                "‬‫בַּאָבִיב‬"
            ),
            (
                # translation_word
                "весенний",
                # pronunciation_word
                "avivi",
                # hebrew_word_nikud
                "‫אֲבִיבִי‬‬"
            ),
            (
                # translation_word
                "лето",
                # pronunciation_word
                "'kayiʦ",
                # hebrew_word_nikud
                "‫קַיִץ‬‬"
            ),
            (
                # translation_word
                "летом",
                # pronunciation_word
                "ba'kayiʦ",
                # hebrew_word_nikud
                "‫בַּקַיִץ‬‬"
            ),
            (
                # translation_word
                "летний",
                # pronunciation_word
                "keʦi",
                # hebrew_word_nikud
                "‫קֵיצִי‬‬"
            ),
            (
                # translation_word
                "осень",
                # pronunciation_word
                "stav",
                # hebrew_word_nikud
                "‬‫סתָיו‬"
            ),
            (
                # translation_word
                "осенью",
                # pronunciation_word
                "bestav",
                # hebrew_word_nikud
                "‫בְּסתָיו‬‬"
            ),
            (
                # translation_word
                "осенний",
                # pronunciation_word
                "stavi",
                # hebrew_word_nikud
                "‫סתָווִי‬‬"
            ),
            (
                # translation_word
                "зима",
                # pronunciation_word
                "'χoref",
                # hebrew_word_nikud
                "‫חוֹרֶף‬‬"
            ),
            (
                # translation_word
                "зимой",
                # pronunciation_word
                "ba'χoref",
                # hebrew_word_nikud
                "‬‫בַּחוֹרֶף‬"
            ),
            (
                # translation_word
                "зимний",
                # pronunciation_word
                "χorpi",
                # hebrew_word_nikud
                "‫חוֹרפִּי‬‬"
            ),
            (
                # translation_word
                "месяц",
                # pronunciation_word
                "'χodeʃ",
                # hebrew_word_nikud
                "‫חוֹדֶש‬‬"
            ),
            (
                # translation_word
                "год",
                # pronunciation_word
                "ʃana",
                # hebrew_word_nikud
                "‬‫שָנָה‬"
            ),
            (
                # translation_word
                "дата",
                # pronunciation_word
                "taʾariχ",
                # hebrew_word_nikud
                "‫תַאֲרִיך‬‬"
            ),
            (
                # translation_word
                "календарь",
                # pronunciation_word
                "'luaχ ʃana",
                # hebrew_word_nikud
                "לוּח‬ ‫שָנָה‬‬"
            ),
            (
                # translation_word
                "полгода, полугодие",
                # pronunciation_word
                "χaʦi ʃana",
                # hebrew_word_nikud
                "‬חֲצִי‬ ‫שָנָה‬"
            ),
            (
                # translation_word
                "век (столетие)",
                # pronunciation_word
                "'meʾa",
                # hebrew_word_nikud
                "‬‫מֵאָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "23. Время. Разное",
        # words
        [
            (
                # translation_word
                "время",
                # pronunciation_word
                "zman",
                # hebrew_word_nikud
                "‫זמַן‬‬"
            ),
            (
                # translation_word
                "будущее (сущ.)",
                # pronunciation_word
                "atid",
                # hebrew_word_nikud
                "‬‫עָתִיד‬"
            ),
            (
                # translation_word
                "прошлое (сущ.)",
                # pronunciation_word
                "avar",
                # hebrew_word_nikud
                "‫עָבָר‬‬"
            ),
            (
                # translation_word
                "сейчас",
                # pronunciation_word
                "kayom",
                # hebrew_word_nikud
                "‫כַּיוֹם‬‬"
            ),
            (
                # translation_word
                "скоро",
                # pronunciation_word
                "bekarov",
                # hebrew_word_nikud
                "‫בְּקָרוֹב‬‬"
            ),
            (
                # translation_word
                "заранее",
                # pronunciation_word
                "meroʃ",
                # hebrew_word_nikud
                "‫מֵרֹאש‬‬"
            ),
            (
                # translation_word
                "долго",
                # pronunciation_word
                "zman rav",
                # hebrew_word_nikud
                "זמַן‬ ‫רַב‬‬"
            ),
            (
                # translation_word
                "недолго",
                # pronunciation_word
                "lo zman rav",
                # hebrew_word_nikud
                "לֹא‬ ‫זמַן‬ ‫רַב‬‬"
            ),
            (
                # translation_word
                "рано (~ проснуться)",
                # pronunciation_word
                "mukdam",
                # hebrew_word_nikud
                "‫מוּקדָם‬‬"
            ),
            (
                # translation_word
                "поздно (~ встать)",
                # pronunciation_word
                "meʾuχar",
                # hebrew_word_nikud
                "‫מְאוּחָר‬‬"
            ),
            (
                # translation_word
                "навсегда",
                # pronunciation_word
                "la'neʦaχ",
                # hebrew_word_nikud
                "‫לָנֶצַח‬"
            ),
            (
                # translation_word
                "одновременно",
                # pronunciation_word
                "bo zmanit",
                # hebrew_word_nikud
                "בּו‬ ‫זמַנִית‬‬"
            ),
            (
                # translation_word
                "временный",
                # pronunciation_word
                "zmani",
                # hebrew_word_nikud
                "‬‫זמַנִי‬"
            ),
            (
                # translation_word
                "иногда",
                # pronunciation_word
                "lifʿamim",
                # hebrew_word_nikud
                "‫לִפעָמִים‬‬"
            ),
            (
                # translation_word
                "редко",
                # pronunciation_word
                "leʿitim reχokot",
                # hebrew_word_nikud
                "לְעִיתִים‬ ‫רְחוֹקוֹת‬‬"
            ),
            (
                # translation_word
                "часто",
                # pronunciation_word
                "leʿitim krovot",
                # hebrew_word_nikud
                "לְעִיתִים‬ ‫קרוֹבוֹת‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "24. Линии и формы",
        # words
        [
            (
                # translation_word
                    "квадрат",
                # pronunciation_word
                "ri'buʿa",
                # hebrew_word_nikud
                "‫רִיבּוּע‬‬"
            ),
            (
                # translation_word
                "круг",
                # pronunciation_word
                "maʿagal",
                # hebrew_word_nikud
                "‫מַעֲגָל‬‬"
            ),
            (
                # translation_word
                "круг",
                # pronunciation_word
                "igul",
                # hebrew_word_nikud
                "‫עִיגוּל‬‬"
            ),
            (
                # translation_word
                "прямоугольник",
                # pronunciation_word
                "malben",
                # hebrew_word_nikud
                "‬‫מַלבֵּן‬"
            ),
            (
                # translation_word
                "горизонтальный",
                # pronunciation_word
                "ofki",
                # hebrew_word_nikud
                "‬‫אוֹפקִי‬"
            ),
            (
                # translation_word
                "вертикальный",
                # pronunciation_word
                "anaχi",
                # hebrew_word_nikud
                "‫אֲנָכִי‬‬"
            ),
            (
                # translation_word
                "линия, черта",
                # pronunciation_word
                "kav",
                # hebrew_word_nikud
                "‬‫קַו‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "25. Меры измерения",
        # words
        [
            (
                # translation_word
                "вес",
                # pronunciation_word
                "miʃkal",
                # hebrew_word_nikud
                "‫מִשקָל‬‬"
            ),
            (
                # translation_word
                "длина",
                # pronunciation_word
                "'oreχ",
                # hebrew_word_nikud
                "‬‫אוֹרֶך‬"
            ),
            (
                # translation_word
                "ширина",
                # pronunciation_word
                "'roχav",
                # hebrew_word_nikud
                "‬‫רוֹחַב‬"
            ),
            (
                # translation_word
                "высота",
                # pronunciation_word
                "'gova",
                # hebrew_word_nikud
                "‫גוֹבַה‬‬"
            ),
            (
                # translation_word
                "глубина",
                # pronunciation_word
                "'omek",
                # hebrew_word_nikud
                "‬‫עוֹמֶק‬"
            ),
            (
                # translation_word
                "объём",
                # pronunciation_word
                "'nefaχ",
                # hebrew_word_nikud
                "‬‫נֶפַח‬"
            ),
            (
                # translation_word
                "площадь",
                # pronunciation_word
                "'ʃetaχ",
                # hebrew_word_nikud
                "‬‫שֶטַח‬"
            ),
            (
                # translation_word
                "грамм",
                # pronunciation_word
                "gram",
                # hebrew_word_nikud
                "‬‫גרָם‬"
            ),
            (
                # translation_word
                "килограмм",
                # pronunciation_word
                "kilogram",
                # hebrew_word_nikud
                "‫קִילוֹגרָם‬‬"
            ),
            (
                # translation_word
                "метр",
                # pronunciation_word
                "'meter",
                # hebrew_word_nikud
                "‫מֶטֶר‬‬"
            ),
            (
                # translation_word
                "километр",
                # pronunciation_word
                "kilo'meter",
                # hebrew_word_nikud
                "‬‫קִילוֹמֶטֶר‬"
            ),
            (
                # translation_word
                "квадратный метр",
                # pronunciation_word
                "'meter ra'vuʿa",
                # hebrew_word_nikud
                "מֶטֶר‬ ‫רָבוּע‬‬"
            ),
            (
                # translation_word
                "литр",
                # pronunciation_word
                "litr",
                # hebrew_word_nikud
                "‫לִיטר‬‬"
            ),
            (
                # translation_word
                "количество",
                # pronunciation_word
                "kamut",
                # hebrew_word_nikud
                "‬‫כַּמוּת‬"
            ),
            (
                # translation_word
                "немного",
                # pronunciation_word
                "kʦat",
                # hebrew_word_nikud
                "‬‫קצָת‬"
            ),
            (
                # translation_word
                "половина",
                # pronunciation_word
                "'χeʦi",
                # hebrew_word_nikud
                "‫חֵצִי‬‬"
            ),
            (
                # translation_word
                "штука",
                # pronunciation_word
                "yeχida",
                # hebrew_word_nikud
                "‬‫יְחִידָה‬"
            ),
            (
                # translation_word
                "размер (предмета)",
                # pronunciation_word
                "'godel",
                # hebrew_word_nikud
                "‫גוֹדֶל‬‬"
            ),
            (
                # translation_word
                "минимальный",
                # pronunciation_word
                "mini'mali",
                # hebrew_word_nikud
                "‬‫מִינִימָאלִי‬"
            ),
            (
                # translation_word
                "средний",
                # pronunciation_word
                "memuʦa",
                # hebrew_word_nikud
                "‬‫מְמוּצָע‬"
            ),
            (
                # translation_word
                "максимальный",
                # pronunciation_word
                "maksi'mali",
                # hebrew_word_nikud
                "‫מַקסִימָלִי‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "26. Ёмкости",
        # words
        [
            (
                # translation_word
                "банка (стеклянная)",
                # pronunciation_word
                "ʦin'ʦenet",
                # hebrew_word_nikud
                "‫צִנצֶנֶת‬‬"
            ),
            (
                # translation_word
                "банка (жестяная)",
                # pronunciation_word
                "paχit",
                # hebrew_word_nikud
                "‬‫פַּחִית‬"
            ),
            (
                # translation_word
                "ведро",
                # pronunciation_word
                "dli",
                # hebrew_word_nikud
                "‬‫דלִי‬"
            ),
            (
                # translation_word
                "бочка",
                # pronunciation_word
                "χavit",
                # hebrew_word_nikud
                "‬‫חָבִית‬"
            ),
            (
                # translation_word
                "таз",
                # pronunciation_word
                "gigit",
                # hebrew_word_nikud
                "‫גִיגִית‬‬"
            ),
            (
                # translation_word
                "кружка, чашка",
                # pronunciation_word
                "'sefel",
                # hebrew_word_nikud
                "‬‫סֵפֶל‬"
            ),
            (
                # translation_word
                "блюдце",
                # pronunciation_word
                "taχtit",
                # hebrew_word_nikud
                "‫תַחתִית‬‬"
            ),
            (
                # translation_word
                "стакан",
                # pronunciation_word
                "kos",
                # hebrew_word_nikud
                "‫כּוֹס‬‬"
            ),
            (
                # translation_word
                "бокал",
                # pronunciation_word
                "ga'viʿa",
                # hebrew_word_nikud
                "‫גָבִיע‬‬"
            ),
            (
                # translation_word
                "кастрюля",
                # pronunciation_word
                "sir",
                # hebrew_word_nikud
                "‫סִיר‬‬"
            ),
            (
                # translation_word
                "бутылка",
                # pronunciation_word
                "bakbuk",
                # hebrew_word_nikud
                "‫בַּקבּוּק‬‬"
            ),
            (
                # translation_word
                "ваза",
                # pronunciation_word
                "agartal",
                # hebrew_word_nikud
                "‬‫אֲגַרטָל‬"
            ),
            (
                # translation_word
                "тюбик",
                # pronunciation_word
                "ʃfo'feret",
                # hebrew_word_nikud
                "‫שפוֹפֶרֶת‬‬"
            ),
            (
                # translation_word
                "пакет (мешок)",
                # pronunciation_word
                "sakit",
                # hebrew_word_nikud
                "‫שַׂקִית‬‬"
            ),
            (
                # translation_word
                "коробка",
                # pronunciation_word
                "kufsa",
                # hebrew_word_nikud
                "‬‫קוּפסָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "27. Материалы",
        # words
        [
            (
                # translation_word
                "материал",
                # pronunciation_word
                "'χomer",
                # hebrew_word_nikud
                "‫חוֹמֶר‬‬"
            ),
            (
                # translation_word
                "дерево",
                # pronunciation_word
                "eʦ",
                # hebrew_word_nikud
                "‫עֵץ‬‬"
            ),
            (
                # translation_word
                "деревянный",
                # pronunciation_word
                "meʿeʦ",
                # hebrew_word_nikud
                "‬‫מֵעֵץ‬"
            ),
            (
                # translation_word
                "стекло",
                # pronunciation_word
                "zχuχit",
                # hebrew_word_nikud
                "‫זכוּכִית‬‬"
            ),
            (
                # translation_word
                "стеклянный",
                # pronunciation_word
                "mizχuχit",
                # hebrew_word_nikud
                "‫מִזכוּכִית‬‬"
            ),
            (
                # translation_word
                "камень",
                # pronunciation_word
                "'even",
                # hebrew_word_nikud
                "‫אֶבֶן‬‬"
            ),
            (
                # translation_word
                "каменный",
                # pronunciation_word
                "me'ʾeven",
                # hebrew_word_nikud
                "‫מֵאֶבֶן‬‬"
            ),
            (
                # translation_word
                "пластик, пластмасса",
                # pronunciation_word
                "'plastik",
                # hebrew_word_nikud
                "‫פּלַסטִיק‬‬"
            ),
            (
                # translation_word
                "пластмассовый",
                # pronunciation_word
                "mi'plastik",
                # hebrew_word_nikud
                "‫מִפּלַסטִיק‬‬"
            ),
            (
                # translation_word
                "резина",
                # pronunciation_word
                "'gumi",
                # hebrew_word_nikud
                "‫גוּמִי‬‬"
            ),
            (
                # translation_word
                "резиновый",
                # pronunciation_word
                "mi'gumi",
                # hebrew_word_nikud
                "‬‫מִגוּמִי‬"
            ),
            (
                # translation_word
                "ткань",
                # pronunciation_word
                "bad",
                # hebrew_word_nikud
                "‬‫בַּד‬"
            ),
            (
                # translation_word
                "из ткани",
                # pronunciation_word
                "mibad",
                # hebrew_word_nikud
                "‫מִבַּד‬‬"
            ),
            (
                # translation_word
                "бумага",
                # pronunciation_word
                "neyar",
                # hebrew_word_nikud
                "‫נְייָר‬‬"
            ),
            (
                # translation_word
                "бумажный",
                # pronunciation_word
                "mineyar",
                # hebrew_word_nikud
                "‬‫מִנְייָר‬"
            ),
            (
                # translation_word
                "картон",
                # pronunciation_word
                "karton",
                # hebrew_word_nikud
                "‫קַרטוֹן‬‬"
            ),
            (
                # translation_word
                "картонный",
                # pronunciation_word
                "mikarton",
                # hebrew_word_nikud
                "‬‫מִקַרטוֹן‬"
            ),
            (
                # translation_word
                "целлофан",
                # pronunciation_word
                "ʦelofan",
                # hebrew_word_nikud
                "‬‫צֶלוֹפָן‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "28. Металлы",
        # words
        [
            (
                # translation_word
                "металл",
                # pronunciation_word
                "ma'teχet",
                # hebrew_word_nikud
                "‬‫מַתֶכֶת‬"
            ),
            (
                # translation_word
                "металлический",
                # pronunciation_word
                "mataχti",
                # hebrew_word_nikud
                "‫מַתַכתִי‬‬"
            ),
            (
                # translation_word
                "золото",
                # pronunciation_word
                "zahav",
                # hebrew_word_nikud
                "‬‫זָהָב‬"
            ),
            (
                # translation_word
                "золотой",
                # pronunciation_word
                "mizahav",
                # hebrew_word_nikud
                "‬‫מִזָהָב‬"
            ),
            (
                # translation_word
                "золотой",
                # pronunciation_word
                "zahov",
                # hebrew_word_nikud
                "‫זָהוֹב‬‬"
            ),
            (
                # translation_word
                "серебро",
                # pronunciation_word
                "'kesef",
                # hebrew_word_nikud
                "‫כֶּסֶף‬‬"
            ),
            (
                # translation_word
                "серебряный",
                # pronunciation_word
                "kaspi",
                # hebrew_word_nikud
                "‫כַּספִּי‬‬"
            ),
            (
                # translation_word
                "железо",
                # pronunciation_word
                "barzel",
                # hebrew_word_nikud
                "‬‫בַּרזֶל‬"
            ),
            (
                # translation_word
                "железный",
                # pronunciation_word
                "mibarzel",
                # hebrew_word_nikud
                "‫מִבַּרזֶל‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "29. Человек. Общие понятия",
        # words
        [
            (
                # translation_word
                "человек",
                # pronunciation_word
                "ben adam",
                # hebrew_word_nikud
                "בֶּן‬ ‫אָדָם‬‬"
            ),
            (
                # translation_word
                "мужчина",
                # pronunciation_word
                "'gever",
                # hebrew_word_nikud
                "‫גֶבֶר‬‬"
            ),
            (
                # translation_word
                "женщина",
                # pronunciation_word
                "iʃa",
                # hebrew_word_nikud
                "‫אִשָה‬‬"
            ),
            (
                # translation_word
                "ребёнок, мальчик",
                # pronunciation_word
                "'yeled",
                # hebrew_word_nikud
                "‬‫יֶלֶד‬"
            ),
            (
                # translation_word
                "девочка",
                # pronunciation_word
                "yalda",
                # hebrew_word_nikud
                "‫יַלדָה‬‬"
            ),
            (
                # translation_word
                "подросток",
                # pronunciation_word
                "'naʿar",
                # hebrew_word_nikud
                "‬‫נַעַר‬"
            ),
            (
                # translation_word
                "старик",
                # pronunciation_word
                "zaken",
                # hebrew_word_nikud
                "‫זָקֵן‬‬"
            ),
            (
                # translation_word
                "старая женщина",
                # pronunciation_word
                "zkena",
                # hebrew_word_nikud
                "‫זקֵנָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru    
        "30. Анатомия",
        # words
        [
            (
                # translation_word
                "сердце",
                # pronunciation_word
                "lev",
                # hebrew_word_nikud
                "‬‫לֵב‬"
            ),
            (
                # translation_word
                "кровь",
                # pronunciation_word
                "dam",
                # hebrew_word_nikud
                "‬‫דָם‬"
            ),
            (
                # translation_word
                "вена",
                # pronunciation_word
                "vrid",
                # hebrew_word_nikud
                "‬‫ורִיד‬"
            ),
            (
                # translation_word
                "мозг",
                # pronunciation_word
                "'moaχ",
                # hebrew_word_nikud
                "‬‫מוֹח‬"
            ),
            (
                # translation_word
                "нервы",
                # pronunciation_word
                "aʦabim",
                # hebrew_word_nikud
                "‬‫עֲצַבִּים‬"
            ),
            (
                # translation_word
                "позвоночник",
                # pronunciation_word
                "amud haʃidra",
                # hebrew_word_nikud
                "‬עַמוּד‬ ‫הַשִדרָה‬"
            ),
            (
                # translation_word
                "желудок",
                # pronunciation_word
                "keiva",
                # hebrew_word_nikud
                "‫קֵיבָה‬‬"
            ),
            (
                # translation_word
                "кишечник",
                # pronunciation_word
                "me'ʿayim",
                # hebrew_word_nikud
                "‫מֵעַיִים‬‬"
            ),
            (
                # translation_word
                "печень",
                # pronunciation_word
                "kaved",
                # hebrew_word_nikud
                "‫כָּבֵד‬‬"
            ),
            (
                # translation_word
                "почка",
                # pronunciation_word
                "kilya",
                # hebrew_word_nikud
                "‬‫כִּליָה‬"
            ),
            (
                # translation_word
                "кость",
                # pronunciation_word
                "'eʦem",
                # hebrew_word_nikud
                "‫עֶצֶם‬‬"
            ),
            (
                # translation_word
                "ребро",
                # pronunciation_word
                "'ʦela",
                # hebrew_word_nikud
                "‫צֶלַע‬‬"
            ),
            (
                # translation_word
                "череп",
                # pronunciation_word
                "gul'golet",
                # hebrew_word_nikud
                "‫גוּלגוֹלֶת‬‬"
            ),
            (
                # translation_word
                "мышца",
                # pronunciation_word
                "ʃrir",
                # hebrew_word_nikud
                "‬‫שרִיר‬"
            ),
            (
                # translation_word
                "сустав",
                # pronunciation_word
                "'perek",
                # hebrew_word_nikud
                "‫פֶּרֶק‬‬"
            ),
            (
                # translation_word
                "лёгкие",
                # pronunciation_word
                "reʾot",
                # hebrew_word_nikud
                "‫רֵיאוֹת‬‬"
            ),
            (
                # translation_word
                "половые органы",
                # pronunciation_word
                "evrei min",
                # hebrew_word_nikud
                "אֶברֵי‬ ‫מִין‬‬"
            ),
            (
                # translation_word
                "кожа",
                # pronunciation_word
                "or",
                # hebrew_word_nikud
                "‬‫עוֹר‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "31. Голова",
        # words
        [
            (
                # translation_word
                "голова",
                # pronunciation_word
                "roʃ",
                # hebrew_word_nikud
                "‫רֹאש‬‬"
            ),
            (
                # translation_word
                "лицо",
                # pronunciation_word
                "panim",
                # hebrew_word_nikud
                "‬‫פָּנִים‬"
            ),
            (
                # translation_word
                "нос",
                # pronunciation_word
                "af",
                # hebrew_word_nikud
                "‬‫אַף‬"
            ),
            (
                # translation_word
                "рот",
                # pronunciation_word
                "pe",
                # hebrew_word_nikud
                "‬‫פֶּה‬"
            ),
            (
                # translation_word
                "глаз",
                # pronunciation_word
                "'ayin",
                # hebrew_word_nikud
                "‫עַיִן‬‬"
            ),
            (
                # translation_word
                "глаза",
                # pronunciation_word
                "ei'nayim",
                # hebrew_word_nikud
                "‬‫עֵינַיִים‬"
            ),
            (
                # translation_word
                "бровь",
                # pronunciation_word
                "gaba",
                # hebrew_word_nikud
                "‫גַבָּה‬‬"
            ),
            (
                # translation_word
                "язык",
                # pronunciation_word
                "laʃon",
                # hebrew_word_nikud
                "‫לָשוֹן‬‬"
            ),
            (
                # translation_word
                "зуб",
                # pronunciation_word
                "ʃen",
                # hebrew_word_nikud
                "‫שֵן‬‬"
            ),
            (
                # translation_word
                "губы",
                # pronunciation_word
                "sfa'tayim",
                # hebrew_word_nikud
                "‬‫שׂפָתַיִים‬"
            ),
            (
                # translation_word
                "десна",
                # pronunciation_word
                "χani'χayim",
                # hebrew_word_nikud
                "‬‫חֲנִיכַיִים‬"
            ),
            (
                # translation_word
                "подбородок",
                # pronunciation_word
                "santer",
                # hebrew_word_nikud
                "‫סַנטֵר‬‬"
            ),
            (
                # translation_word
                "щека",
                # pronunciation_word
                "'leχi",
                # hebrew_word_nikud
                "‫לֶחִי‬‬"
            ),
            (
                # translation_word
                "лоб",
                # pronunciation_word
                "'meʦaχ",
                # hebrew_word_nikud
                "‬‫מֵצַח‬"
            ),
            (
                # translation_word
                "ухо",
                # pronunciation_word
                "'ozen",
                # hebrew_word_nikud
                "‬‫אוֹזֶן‬"
            ),
            (
                # translation_word
                "шея",
                # pronunciation_word
                "ʦavar",
                # hebrew_word_nikud
                "‫צַווָאר‬‬"
            ),
            (
                # translation_word
                "волосы",
                # pronunciation_word
                "seʿar",
                # hebrew_word_nikud
                "‫שֵׂיעָר‬‬"
            ),
            (
                # translation_word
                "стрижка (причёска)",
                # pronunciation_word
                "tis'poret",
                # hebrew_word_nikud
                "‫תִספּוֹרֶת‬"
            ),
            (
                # translation_word
                "усы",
                # pronunciation_word
                "safam",
                # hebrew_word_nikud
                "‫שָׂפָם‬‬"
            ),
            (
                # translation_word
                "борода",
                # pronunciation_word
                "zakan",
                # hebrew_word_nikud
                "‬‫זָקָן‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "32. Тело",
        # words
        [
            (
                # translation_word
                "кисть руки, ладонь",
                # pronunciation_word
                "kaf yad",
                # hebrew_word_nikud
                "‬כַּף‬ ‫יָד‬"
            ),
            (
                # translation_word
                "рука (вся)",
                # pronunciation_word
                "yad",
                # hebrew_word_nikud
                "‬‫יָד‬"
            ),
            (
                # translation_word
                "палец",
                # pronunciation_word
                "'eʦba",
                # hebrew_word_nikud
                "‫אֶצבַּע‬‬"
            ),
            (
                # translation_word
                "палец (ноги)",
                # pronunciation_word
                "'bohen",
                # hebrew_word_nikud
                "‬‫בּוֹהֶן‬"
            ),
            (
                # translation_word
                "ноготь",
                # pronunciation_word
                "ʦi'poren",
                # hebrew_word_nikud
                "‬‫צִיפּוֹרֶן‬"
            ),
            (
                # translation_word
                "предплечье",
                # pronunciation_word
                "ama",
                # hebrew_word_nikud
                "‬‫אַמָּה‬"
            ),
            (
                # translation_word
                "локоть",
                # pronunciation_word
                "marpek",
                # hebrew_word_nikud
                "‬‫מַרפֵּק‬"
            ),
            (
                # translation_word
                "плечо",
                # pronunciation_word
                "katef",
                # hebrew_word_nikud
                "‫כָּתֵף‬‬"
            ),
            (
                # translation_word
                "нога (выше ступни)",
                # pronunciation_word
                "'regel",
                # hebrew_word_nikud
                "‬‫רֶגֶל‬"
            ),
            (
                # translation_word
                "ступня",
                # pronunciation_word
                "kaf 'regel",
                # hebrew_word_nikud
                "‬כַּף‬ ‫רֶגֶל‬"
            ),
            (
                # translation_word
                "колено",
                # pronunciation_word
                "'bereχ",
                # hebrew_word_nikud
                "‬‫בֶּרֶך‬"
            ),
            (
                # translation_word
                "тело",
                # pronunciation_word
                "guf",
                # hebrew_word_nikud
                "‫גוּף‬‬"
            ),
            (
                # translation_word
                "живот",
                # pronunciation_word
                "'beten",
                # hebrew_word_nikud
                "‬‫בֶּטֶן‬"
            ),
            (
                # translation_word
                "грудь (мужская)",
                # pronunciation_word
                "χaze",
                # hebrew_word_nikud
                "‫חָזֶה‬‬"
            ),
            (
                # translation_word
                "грудь (женская)",
                # pronunciation_word
                "ʃad",
                # hebrew_word_nikud
                "‬‫שָד‬"
            ),
            (
                # translation_word
                "спина",
                # pronunciation_word
                "gav",
                # hebrew_word_nikud
                "‫גַב‬‬"
            ),
            (
                # translation_word
                "пупок",
                # pronunciation_word
                "tabur",
                # hebrew_word_nikud
                "‫טַבּוּר‬‬"
            ),
            (
                # translation_word
                "ягодицы",
                # pronunciation_word
                "aχo'rayim",
                # hebrew_word_nikud
                "‫אֲחוֹרַיִים‬‬"
            ),
            (
                # translation_word
                "зад",
                # pronunciation_word
                "yaʃvan",
                # hebrew_word_nikud
                "‫יַשבָן‬‬"
            ),
            (
                # translation_word
                "родинка",
                # pronunciation_word
                "nekudat χen",
                # hebrew_word_nikud
                "נְקוּדַת‬ ‫חֵן‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "33. Верхняя одежда",
        # words
        [
            (
                # translation_word
                "одежда",
                # pronunciation_word
                "bgadim",
                # hebrew_word_nikud
                "‫בּגָדִים‬‬"
            ),
            (
                # translation_word
                "пальто",
                # pronunciation_word
                "meʿil",
                # hebrew_word_nikud
                "‫מְעִיל‬‬"
            ),
            (
                # translation_word
                "шуба",
                # pronunciation_word
                "meʿil parva",
                # hebrew_word_nikud
                "‬מְעִיל‬ ‫פַּרווָה‬"
            ),
            (
                # translation_word
                "куртка",
                # pronunciation_word
                "meʿil kaʦar",
                # hebrew_word_nikud
                "מְעִיל‬ ‫קָצָר‬‬"
            ),
            (
                # translation_word
                "плащ непромокаемый",
                # pronunciation_word
                "meʿil 'geʃem",
                # hebrew_word_nikud
                "‬מְעִיל‬ ‫גֶשֶם‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "34. Одежда",
        # words
        [
            (
                # translation_word
                "рубашка, блузка",
                # pronunciation_word
                "χulʦa",
                # hebrew_word_nikud
                "‫חוּלצָה‬‬"
            ),
            (
                # translation_word
                "брюки",
                # pronunciation_word
                "miχna'sayim",
                # hebrew_word_nikud
                "‬‫מִכנָסַיִים‬"
            ),
            (
                # translation_word
                "джинсы",
                # pronunciation_word
                "miχnesei 'ʤins",
                # hebrew_word_nikud
                "מִכנְסֵי‬ ‫גִ׳ינְס‬‬"
            ),
            (
                # translation_word
                "пиджак",
                # pronunciation_word
                "ʒaket",
                # hebrew_word_nikud
                "‫זָ׳קֶט‬‬"
            ),
            (
                # translation_word
                "костюм (мужской)",
                # pronunciation_word
                "χalifa",
                # hebrew_word_nikud
                "‬‫חֲלִיפָה‬"
            ),
            (
                # translation_word
                "платье",
                # pronunciation_word
                "simla",
                # hebrew_word_nikud
                "‬‫שִׂמלָה‬"
            ),
            (
                # translation_word
                "юбка",
                # pronunciation_word
                "χaʦaʾit",
                # hebrew_word_nikud
                "‫חֲצָאִית‬‬"
            ),
            (
                # translation_word
                "кофта (шерстяная)",
                # pronunciation_word
                "ʒaket 'ʦemer",
                # hebrew_word_nikud
                "‬זָ׳קֶט‬ ‫צֶמֶר‬"
            ),
            (
                # translation_word
                "футболка",
                # pronunciation_word
                "ti ʃert",
                # hebrew_word_nikud
                "‬טִי‬ ‫שֶרט‬"
            ),
            (
                # translation_word
                "шорты",
                # pronunciation_word
                "miχna'sayim kʦarim",
                # hebrew_word_nikud
                "מִכנָסַיִים‬ ‫קצָרִים‬‬"
            ),
            (
                # translation_word
                "пижама",
                # pronunciation_word
                "pi'ʤama",
                # hebrew_word_nikud
                "‫פִּיגָ׳מָה‬‬"
            ),
            (
                # translation_word
                "свитер",
                # pronunciation_word
                "'sveder",
                # hebrew_word_nikud
                "‫סוֶודֶר‬‬"
            ),
            (
                # translation_word
                "форма (униформа)",
                # pronunciation_word
                "madim",
                # hebrew_word_nikud
                "‬‫מַדִים‬"
            ),
            (
                # translation_word
                "рабочая одежда",
                # pronunciation_word
                "bigdei avoda",
                # hebrew_word_nikud
                "בִּגדֵי‬ ‫עֲבוֹדָה‬‬"
            ),
            (
                # translation_word
                "халат",
                # pronunciation_word
                "χaluk",
                # hebrew_word_nikud
                "‬‫חָלוּק‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "35. Одежда. Бельё",
        # words
        [
            (
                # translation_word
                "бельё (одежда)",
                # pronunciation_word
                "levanim",
                # hebrew_word_nikud
                "‬‫לְבָנִים‬"
            ),
            (
                # translation_word
                "трусы мужские, женское бельё (трусики)",
                # pronunciation_word
                "taχtonim",
                # hebrew_word_nikud
                "‫תַחתוֹנִים‬‬"
            ),
            (
                # translation_word
                "майка",
                # pronunciation_word
                "gufiya",
                # hebrew_word_nikud
                "‫גוּפִייָה‬‬"
            ),
            (
                # translation_word
                "носки",
                # pronunciation_word
                "gar'bayim",
                # hebrew_word_nikud
                "‫גַרבַּיִים‬‬"
            ),
            (
                # translation_word
                "бюстгальтер",
                # pronunciation_word
                "χaziya",
                # hebrew_word_nikud
                "‬‫חֲזִייָה‬"
            ),
            (
                # translation_word
                "колготки",
                # pronunciation_word
                "garbonim",
                # hebrew_word_nikud
                "‫גַרבּוֹנִים‬‬"
            ),
            (
                # translation_word
                "купальник",
                # pronunciation_word
                "'beged yam",
                # hebrew_word_nikud
                "‬בֶּגֶד‬ ‫יָם‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "36. Головной убор",
        # words
        [
            (
                # translation_word
                "шапка",
                # pronunciation_word
                "'kova",
                # hebrew_word_nikud
                "‫כּוֹבַע‬‬"
            ),
            (
                # translation_word
                "кепка",
                # pronunciation_word
                "'kova miʦχiya",
                # hebrew_word_nikud
                "‬כּוֹבַע‬ ‫מִצחִייָה‬"
            ),
            (
                # translation_word
                "капюшон",
                # pronunciation_word
                "bardas",
                # hebrew_word_nikud
                "‫בַּרדָס‬‬"
            ),
            (
                # translation_word
                "каска",
                # pronunciation_word
                "kasda",
                # hebrew_word_nikud
                "‫קַסדָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "37. Обувь",
        # words
        [
            (
                # translation_word
                "обувь",
                # pronunciation_word
                "hanʿala",
                # hebrew_word_nikud
                "‫הַנְעָלָה‬‬"
            ),
            (
                # translation_word
                "ботинки, туфли",
                # pronunciation_word
                "naʿa'layim",
                # hebrew_word_nikud
                "‬‫נַעֲלַיִים‬"
            ),
            (
                # translation_word
                "сапоги",
                # pronunciation_word
                "maga'fayim",
                # hebrew_word_nikud
                "‫מַגָפַיִים‬‬"
            ),
            (
                # translation_word
                "кроссовки, кеды",
                # pronunciation_word
                "naʿalei sport",
                # hebrew_word_nikud
                "נַעֲלֵי‬ ‫ספּוֹרט‬‬"
            ),
            (
                # translation_word
                "сандалии",
                # pronunciation_word
                "sandalim",
                # hebrew_word_nikud
                "‫סַנדָלִים‬‬"
            ),
            (
                # translation_word
                "шнурок",
                # pronunciation_word
                "sroχ",
                # hebrew_word_nikud
                "‫שׂרוֹך‬‬"
            ),
            (
                # translation_word
                "рожок (для обуви)",
                # pronunciation_word
                "kaf naʿa'layim",
                # hebrew_word_nikud
                "‬כַּף‬ ‫נַעֲלַיִים‬"
            ),
            (
                # translation_word
                "крем для обуви",
                # pronunciation_word
                "miʃχat naʿa'layim",
                # hebrew_word_nikud
                "מִשחַת‬ ‫נַעֲלַיִים‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "38. Ткани. Материалы",
        # words
        [
            (
                # translation_word
                "хлопок",
                # pronunciation_word
                "kutna",
                # hebrew_word_nikud
                "‫כּוּתנָה‬‬"
            ),
            (
                # translation_word
                "из хлопка",
                # pronunciation_word
                "mikutna",
                # hebrew_word_nikud
                "‫מִכּוּתנָה‬‬"
            ),
            (
                # translation_word
                "лён",
                # pronunciation_word
                "piʃtan",
                # hebrew_word_nikud
                "‫פִּשתָן‬‬"
            ),
            (
                # translation_word
                "из льна",
                # pronunciation_word
                "mipiʃtan",
                # hebrew_word_nikud
                "‬‫מִפִּשתָן‬"
            ),
            (
                # translation_word
                "шёлк",
                # pronunciation_word
                "'meʃi",
                # hebrew_word_nikud
                "‬‫מֶשִי‬"
            ),
            (
                # translation_word
                "шёлковый",
                # pronunciation_word
                "miʃyi",
                # hebrew_word_nikud
                "‫מִשיִי‬‬"
            ),
            (
                # translation_word
                "шерсть",
                # pronunciation_word
                "'ʦemer",
                # hebrew_word_nikud
                "‬‫צֶמֶר‬"
            ),
            (
                # translation_word
                "шерстяной",
                # pronunciation_word
                "ʦamri",
                # hebrew_word_nikud
                "‬‫צַמרִי‬"
            ),
            (
                # translation_word
                "полиэстер",
                # pronunciation_word
                "poli'ʾester",
                # hebrew_word_nikud
                "‫פּוֹלִיאֶסטֶר‬‬"
            ),
            (
                # translation_word
                "полиэстровый",
                # pronunciation_word
                "mipoli'ʾester",
                # hebrew_word_nikud
                "‫מִפּוֹלִיאֶסטֶר‬‬"
            ),
            (
                # translation_word
                "кожа",
                # pronunciation_word
                "or",
                # hebrew_word_nikud
                "‫עוֹר‬‬"
            ),
            (
                # translation_word
                "из кожи",
                # pronunciation_word
                "meʿor",
                # hebrew_word_nikud
                "‫מֵעוֹר‬‬"
            ),
            (
                # translation_word
                "мех",
                # pronunciation_word
                "parva",
                # hebrew_word_nikud
                "‫פַּרווָה‬‬"
            ),
            (
                # translation_word
                "меховой",
                # pronunciation_word
                "miparva",
                # hebrew_word_nikud
                "‫מִפַּרווָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "39. Аксессуары (одежда)",
        # words
        [
            (
                # translation_word
                "перчатки, варежки",
                # pronunciation_word
                "kfafot",
                # hebrew_word_nikud
                "‫כּפָפוֹת‬‬"
            ),
            (
                # translation_word
                "шарф",
                # pronunciation_word
                "ʦaʿif",
                # hebrew_word_nikud
                "‬‫צָעִיף‬"
            ),
            (
                # translation_word
                "очки",
                # pronunciation_word
                "miʃka'fayim",
                # hebrew_word_nikud
                "‫מִשקָפַיִים‬‬"
            ),
            (
                # translation_word
                "зонт",
                # pronunciation_word
                "mitriya",
                # hebrew_word_nikud
                "‫מִטרִייָה‬‬"
            ),
            (
                # translation_word
                "галстук",
                # pronunciation_word
                "aniva",
                # hebrew_word_nikud
                "‫עֲנִיבָה‬‬"
            ),
            (
                # translation_word
                "расчёска",
                # pronunciation_word
                "masrek",
                # hebrew_word_nikud
                "‫מַסרֵק‬‬"
            ),
            (
                # translation_word
                "пояс (ремень)",
                # pronunciation_word
                "χagora",
                # hebrew_word_nikud
                "‫חֲגוֹרָה‬‬"
            ),
            (
                # translation_word
                "сумка, сумочка (женская)",
                # pronunciation_word
                "tik",
                # hebrew_word_nikud
                "‫תִיק‬‬"
            ),
            (
                # translation_word
                "рюкзак",
                # pronunciation_word
                "tarmil",
                # hebrew_word_nikud
                "‬‫תַרמִיל‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "40. Одежда. Разное",
        # words
        [
            (
                # translation_word
                "воротник",
                # pronunciation_word
                "ʦavaron",
                # hebrew_word_nikud
                "‫צַווָארוֹן‬‬"
            ),
            (
                # translation_word
                "карман",
                # pronunciation_word
                "kis",
                # hebrew_word_nikud
                "‬‫כִּיס‬"
            ),
            (
                # translation_word
                "рукав",
                # pronunciation_word
                "ʃarvul",
                # hebrew_word_nikud
                "‫שַרווּל‬‬"
            ),
            (
                # translation_word
                "вешалка",
                # pronunciation_word
                "mitle",
                # hebrew_word_nikud
                "‫מִתלֶה‬‬"
            ),
            (
                # translation_word
                "ширинка",
                # pronunciation_word
                "χanut",
                # hebrew_word_nikud
                "‫חֲנוּת‬‬"
            ),
            (
                # translation_word
                "молния (застежка)",
                # pronunciation_word
                "roχsan",
                # hebrew_word_nikud
                "‫רוֹכסָן‬‬"
            ),
            (
                # translation_word
                "пятно",
                # pronunciation_word
                "'ketem",
                # hebrew_word_nikud
                "‬‫כֶּתֶם‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "41. Предметы личной гигиены. Косметика",
        # words
        [
            (
                # translation_word
                "зубная паста",
                # pronunciation_word
                "miʃχat ʃi'nayim",
                # hebrew_word_nikud
                "מִשחַת‬ ‫שִינַיִים‬"
            ),
            (
                # translation_word
                "зубная щётка",
                # pronunciation_word
                "miv'reʃet ʃi'nayim",
                # hebrew_word_nikud
                "‬‬מִברֶשֶת‬ ‫שִינַיִים‬"
            ),
            (
                # translation_word
                "чистить зубы",
                # pronunciation_word
                "leʦaχ'ʦeaχ ʃi'nayim",
                # hebrew_word_nikud
                "‬לְצַחצֵח‬ ‫שִינַיִים‬"
            ),
            (
                # translation_word
                "бритва",
                # pronunciation_word
                "'taʿar",
                # hebrew_word_nikud
                "‬‫תַעַר‬"
            ),
            (
                # translation_word
                "крем для бритья",
                # pronunciation_word
                "keʦef gi'luaχ",
                # hebrew_word_nikud
                "קֶצֵף‬ ‫גִילוּח‬‬"
            ),
            (
                # translation_word
                "бриться",
                # pronunciation_word
                "lehitga'leaχ",
                # hebrew_word_nikud
                "‫לְהִתגַלֵח‬‬"
            ),
            (
                # translation_word
                "мыло",
                # pronunciation_word
                "sabon",
                # hebrew_word_nikud
                "‬‫סַבּוֹן‬"
            ),
            (
                # translation_word
                "шампунь",
                # pronunciation_word
                "ʃampu",
                # hebrew_word_nikud
                "‫שַמפּו‬‬"
            ),
            (
                # translation_word
                "ножницы",
                # pronunciation_word
                "mispa'rayim",
                # hebrew_word_nikud
                "‬‫מִספָּרַיִים‬"
            ),
            (
                # translation_word
                "пилочка для ногтей",
                # pronunciation_word
                "pʦira",
                # hebrew_word_nikud
                "‬‫פּצִירָה‬"
            ),
            (
                # translation_word
                "косметика",
                # pronunciation_word
                "tamrukim",
                # hebrew_word_nikud
                "‬‫תַמרוּקִים‬"
            ),
            (
                # translation_word
                "маска (косметич.)",
                # pronunciation_word
                "maseχa",
                # hebrew_word_nikud
                "‬‫מַסֵכָה‬"
            ),
            (
                # translation_word
                "духи",
                # pronunciation_word
                "'bosem",
                # hebrew_word_nikud
                "‬‫בּוֹשֶׂם‬"
            ),
            (
                # translation_word
                "тени для век",
                # pronunciation_word
                "ʦlalit",
                # hebrew_word_nikud
                "‬‫צלָלִית‬"
            ),
            (
                # translation_word
                "карандаш для глаз",
                # pronunciation_word
                "ai 'lainer",
                # hebrew_word_nikud
                "אַי‬ ‫לַיינֶר‬‬"
            ),
            (
                # translation_word
                "тушь для ресниц",
                # pronunciation_word
                "'maskara",
                # hebrew_word_nikud
                "‫מַסקָרָה‬‬"
            ),
            (
                # translation_word
                "губная помада",
                # pronunciation_word
                "sfaton",
                # hebrew_word_nikud
                "‫שׂפָתוֹן‬‬"
            ),
            (
                # translation_word
                "лак для ногтей",
                # pronunciation_word
                "'laka leʦipor'nayim",
                # hebrew_word_nikud
                "לַכָּה‬ ‫לְצִיפּוֹרנַיִים‬‬"
            ),
            (
                # translation_word
                "дезодорант",
                # pronunciation_word
                "deʾodo'rant",
                # hebrew_word_nikud
                "‫דֶאוֹדוֹרַנט‬‬"
            ),
            (
                # translation_word
                "крем",
                # pronunciation_word
                "krem",
                # hebrew_word_nikud
                "‫קרֶם‬‬"
            ),
            (
                # translation_word
                "туалетная бумага",
                # pronunciation_word
                "neyar tuʾalet",
                # hebrew_word_nikud
                "נְייַר‬ ‫טוּאָלֶט‬"
            ),
            (
                # translation_word
                "фен",
                # pronunciation_word
                "meyabeʃ seʿar",
                # hebrew_word_nikud
                "מְייַבֵּש‬ ‫שֵׂיעָר‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "42. Украшения. Драгоценности",
        # words
        [
            (
                # translation_word
                "драгоценности",
                # pronunciation_word
                "taχʃitim",
                # hebrew_word_nikud
                "‫תַכשִיטִים‬‬"
            ),
            (
                # translation_word
                "кольцо",
                # pronunciation_word
                "ta'baʿat",
                # hebrew_word_nikud
                "‫טַבַּעַת‬‬"
            ),
            (
                # translation_word
                "серьги",
                # pronunciation_word
                "agilim",
                # hebrew_word_nikud
                "‬‫עָגִילִים‬"
            ),
            (
                # translation_word
                "бриллиант",
                # pronunciation_word
                "yahalom",
                # hebrew_word_nikud
                "‬‫יַהֲלוֹם‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "43. Часы",
        # words
        [
            (
                # translation_word
                "часы (наручные)",
                # pronunciation_word
                "ʃeʿon yad",
                # hebrew_word_nikud
                "שְעוֹן‬ ‫יָד‬‬"
            ),
            (
                # translation_word
                "батарейка",
                # pronunciation_word
                "solela",
                # hebrew_word_nikud
                "‬‫סוֹלְלָה‬"
            ),
            (
                # translation_word
                "часы настенные",
                # pronunciation_word
                "ʃeʿon kir",
                # hebrew_word_nikud
                "שְעוֹן‬ ‫קִיר‬‬"
            ),
            (
                # translation_word
                "будильник",
                # pronunciation_word
                "ʃaʿon meʿorer",
                # hebrew_word_nikud
                "‬שָעוֹן‬ ‫מְעוֹרֵר‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "44. Продукты",
        # words
        [
            (
                # translation_word
                "мясо",
                # pronunciation_word
                "basar",
                # hebrew_word_nikud
                "‬‫בָּשָׂר‬"
            ),
            (
                # translation_word
                "цыплёнок",
                # pronunciation_word
                "pargit",
                # hebrew_word_nikud
                "‬‫פַּרגִית‬"
            ),
            (
                # translation_word
                "индейка",
                # pronunciation_word
                "'hodu",
                # hebrew_word_nikud
                "‬‫הוֹדו‬"
            ),
            (
                # translation_word
                "свинина",
                # pronunciation_word
                "basar χazir",
                # hebrew_word_nikud
                "בָּשָׂר‬ ‫חֲזִיר‬‬"
            ),
            (
                # translation_word
                "телятина",
                # pronunciation_word
                "basar 'egel",
                # hebrew_word_nikud
                "בָּשָׂר‬ ‫עֵגֶל‬‬"
            ),
            (
                # translation_word
                "баранина",
                # pronunciation_word
                "basar 'keves",
                # hebrew_word_nikud
                "בָּשָׂר‬ ‫כֶּבֶש‬‬"
            ),
            (
                # translation_word
                "говядина",
                # pronunciation_word
                "bakar",
                # hebrew_word_nikud
                "‫בָּקָר‬‬"
            ),
            (
                # translation_word
                "кролик",
                # pronunciation_word
                "arnav",
                # hebrew_word_nikud
                "‬‫אַרנָב‬"
            ),
            (
                # translation_word
                "колбаса",
                # pronunciation_word
                "naknik",
                # hebrew_word_nikud
                "‫נַקנִיק‬‬"
            ),
            (
                # translation_word
                "сосиска",
                # pronunciation_word
                "naknikiya",
                # hebrew_word_nikud
                "‫נַקנִיקִייָה‬‬"
            ),
            (
                # translation_word
                "паштет",
                # pronunciation_word
                "pate",
                # hebrew_word_nikud
                "‫פָּטֶה‬‬"
            ),
            (
                # translation_word
                "печень",
                # pronunciation_word
                "kaved",
                # hebrew_word_nikud
                "‫כָּבֵד‬‬"
            ),
            (
                # translation_word
                "фарш",
                # pronunciation_word
                "basar taχun",
                # hebrew_word_nikud
                "‬בָּשָׂר‬ ‫טָחוּן‬"
            ),
            (
                # translation_word
                "яйцо",
                # pronunciation_word
                "beiʦa",
                # hebrew_word_nikud
                "‫בֵּיצָה‬‬"
            ),
            (
                # translation_word
                "яйца",
                # pronunciation_word
                "beiʦim",
                # hebrew_word_nikud
                "‬‫בֵּיצִים‬"
            ),
            (
                # translation_word
                "рыба",
                # pronunciation_word
                "dag",
                # hebrew_word_nikud
                "‬‫דָג‬"
            ),
            (
                # translation_word
                "хлеб",
                # pronunciation_word
                "'leχem",
                # hebrew_word_nikud
                "‫לֶחֶם‬‬"
            ),
            (
                # translation_word
                "сыр",
                # pronunciation_word
                "gvina",
                # hebrew_word_nikud
                "‫גבִינָה‬‬"
            ),
            (
                # translation_word
                "сахар",
                # pronunciation_word
                "sukar",
                # hebrew_word_nikud
                "‬‫סוּכָּר‬"
            ),
            (
                # translation_word
                "соль",
                # pronunciation_word
                "'melaχ",
                # hebrew_word_nikud
                "‫מֶלַח‬‬"
            ),
            (
                # translation_word
                "рис",
                # pronunciation_word
                "'orez",
                # hebrew_word_nikud
                "‬‫אוֹרֶז‬"
            ),
            (
                # translation_word
                "макароны",
                # pronunciation_word
                "'pasta",
                # hebrew_word_nikud
                "‫פַּסטָה‬‬"
            ),
            (
                # translation_word
                "сливочное масло",
                # pronunciation_word
                "χemʾa",
                # hebrew_word_nikud
                "‫חֶמאָה‬‬"
            ),
            (
                # translation_word
                "подсолнечное масло",
                # pronunciation_word
                "'ʃemen χamaniyot",
                # hebrew_word_nikud
                "שֶמֶן‬ ‫חַמָנִיוֹת‬‬"
            ),
            (
                # translation_word
                "оливки",
                # pronunciation_word
                "zeitim",
                # hebrew_word_nikud
                "‫זֵיתִים‬‬"
            ),
            (
                # translation_word
                "масло оливковое",
                # pronunciation_word
                "'ʃemen 'zayit",
                # hebrew_word_nikud
                "שֶמֶן‬ ‫זַיִת‬‬"
            ),
            (
                # translation_word
                "молоко",
                # pronunciation_word
                "χalav",
                # hebrew_word_nikud
                "‬‫חָלָב‬"
            ),
            (
                # translation_word
                "сгущённое молоко",
                # pronunciation_word
                "χalav merukaz",
                # hebrew_word_nikud
                "‬חָלָב‬ ‫מְרוּכָּז‬"
            ),
            (
                # translation_word
                "йогурт",
                # pronunciation_word
                "'yogurt",
                # hebrew_word_nikud
                "‫יוֹגוּרט‬‬"
            ),
            (
                # translation_word
                "сметана, сливки",
                # pronunciation_word
                "ʃa'menet",
                # hebrew_word_nikud
                "‫שַמֶנֶת‬‬"
            ),
            (
                # translation_word
                "мука",
                # pronunciation_word
                "'kemaχ",
                # hebrew_word_nikud
                "‬‫קֶמַח‬"
            ),
            (
                # translation_word
                "консервы",
                # pronunciation_word
                "ʃimurim",
                # hebrew_word_nikud
                "‫שִימוּרִים‬‬"
            ),
            (
                # translation_word
                "мёд",
                # pronunciation_word
                "dvaʃ",
                # hebrew_word_nikud
                "‬‫דבַש‬"
            ),
            (
                # translation_word
                "джем, варенье",
                # pronunciation_word
                "riba",
                # hebrew_word_nikud
                "‬‫רִיבָּה‬"
            ),
            (
                # translation_word
                "жевательная резинка",
                # pronunciation_word
                "'mastik",
                # hebrew_word_nikud
                "‫מַסטִיק‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "45. Напитки",
        # words
        [
            (
                # translation_word
                "вода",
                # pronunciation_word
                "'mayim",
                # hebrew_word_nikud
                "‫מַיִם‬‬"
            ),
            (
                # translation_word
                "питьевая вода",
                # pronunciation_word
                "mei ʃtiya",
                # hebrew_word_nikud
                "מֵי‬ ‫שתִייָה‬‬"
            ),
            (
                # translation_word
                "минеральная вода",
                # pronunciation_word
                "'mayim mine'raliyim",
                # hebrew_word_nikud
                "‬מַיִם‬ ‫מִינֶרָלִייִם‬"
            ),
            (
                # translation_word
                "без газа",
                # pronunciation_word
                "lo mugaz",
                # hebrew_word_nikud
                "‬לֹא‬ ‫מוּגָז‬"
            ),
            (
                # translation_word
                "с газом, газированный",
                # pronunciation_word
                "mugaz",
                # hebrew_word_nikud
                "‫מוּגָז‬‬"
            ),
            (
                # translation_word
                "вино",
                # pronunciation_word
                "'yayin",
                # hebrew_word_nikud
                "‫יַיִן‬‬"
            ),
            (
                # translation_word
                "шампанское",
                # pronunciation_word
                "ʃam'panya",
                # hebrew_word_nikud
                "‫שַמפַּניָה‬‬"
            ),
            (
                # translation_word
                "водка",
                # pronunciation_word
                "'vodka",
                # hebrew_word_nikud
                "‫ווֹדקָה‬‬"
            ),
            (
                # translation_word
                "кофе",
                # pronunciation_word
                "kafe",
                # hebrew_word_nikud
                "‬‫קָפֶה‬"
            ),
            (
                # translation_word
                "молоко",
                # pronunciation_word
                "χalav",
                # hebrew_word_nikud
                "‬‫חָלָב‬"
            ),
            (
                # translation_word
                "сок",
                # pronunciation_word
                "miʦ",
                # hebrew_word_nikud
                "‫מִיץ‬‬"
            ),
            (
                # translation_word
                "томатный сок",
                # pronunciation_word
                "miʦ agvaniyot",
                # hebrew_word_nikud
                "מִיץ‬ ‫עַגבָנִיוֹת‬‬"
            ),
            (
                # translation_word
                "апельсиновый сок",
                # pronunciation_word
                "miʦ tapuzim",
                # hebrew_word_nikud
                "מִיץ‬ ‫תַפּוּזִים‬‬"
            ),
            (
                # translation_word
                "пиво",
                # pronunciation_word
                "'bira",
                # hebrew_word_nikud
                "‫בִּירָה‬‬"
            ),
            (
                # translation_word
                "чай",
                # pronunciation_word
                "te",
                # hebrew_word_nikud
                "‬‫תֵה‬"
            ),
            (
                # translation_word
                "чёрный чай",
                # pronunciation_word
                "te ʃaχor",
                # hebrew_word_nikud
                "תֵה‬ ‫שָחוֹר‬‬"
            ),
            (
                # translation_word
                "зелёный чай",
                # pronunciation_word
                "te yarok",
                # hebrew_word_nikud
                "תֵה‬ ‫יָרוֹק‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "46. Овощи",
        # words
        [
            (
                # translation_word
                "овощи",
                # pronunciation_word
                "yerakot",
                # hebrew_word_nikud
                "‫יְרָקוֹת‬‬"
            ),
            (
                # translation_word
                "зелень",
                # pronunciation_word
                "'yerek",
                # hebrew_word_nikud
                "‬‫יֶרֶק‬"
            ),
            (
                # translation_word
                "помидор",
                # pronunciation_word
                "agvaniya",
                # hebrew_word_nikud
                "‫עַגבָנִייָה‬‬"
            ),
            (
                # translation_word
                "огурец",
                # pronunciation_word
                "melafefon",
                # hebrew_word_nikud
                "‫מְלָפְפוֹן‬‬"
            ),
            (
                # translation_word
                "морковь",
                # pronunciation_word
                "'gezer",
                # hebrew_word_nikud
                "‫גֶזֶר‬‬"
            ),
            (
                # translation_word
                "картофель",
                # pronunciation_word
                "ta'puaχ adama",
                # hebrew_word_nikud
                "‬תַפּוּח‬ ‬‬‫אֲדָמָה‬"
            ),
            (
                # translation_word
                "лук",
                # pronunciation_word
                "baʦal",
                # hebrew_word_nikud
                "‬‫בָּצָל‬"
            ),
            (
                # translation_word
                "чеснок",
                # pronunciation_word
                "ʃum",
                # hebrew_word_nikud
                "‬‫שוּם‬"
            ),
            (
                # translation_word
                "капуста",
                # pronunciation_word
                "kruv",
                # hebrew_word_nikud
                "‫כּרוּב‬‬"
            ),
            (
                # translation_word
                "цветная капуста",
                # pronunciation_word
                "kruvit",
                # hebrew_word_nikud
                "‫כּרוּבִית‬‬"
            ),
            (
                # translation_word
                "брюссельская капуста",
                # pronunciation_word
                "kruv niʦanim",
                # hebrew_word_nikud
                "כּרוּב‬ ‬‬‫נִצָנִים‬‬"
            ),
            (
                # translation_word
                "брокколи",
                # pronunciation_word
                "'brokoli",
                # hebrew_word_nikud
                "‫בּרוֹקוֹלִי‬‬"
            ),
            (
                # translation_word
                "свёкла",
                # pronunciation_word
                "'selek",
                # hebrew_word_nikud
                "‫סֶלֶק‬‬"
            ),
            (
                # translation_word
                "баклажан",
                # pronunciation_word
                "χaʦil",
                # hebrew_word_nikud
                "‫חָצִיל‬‬"
            ),
            (
                # translation_word
                "кабачок",
                # pronunciation_word
                "kiʃu",
                # hebrew_word_nikud
                "‫קִישוּא‬‬"
            ),
            (
                # translation_word
                "тыква",
                # pronunciation_word
                "'dlaʿat",
                # hebrew_word_nikud
                "‫דלַעַת‬‬"
            ),
            (
                # translation_word
                "репа",
                # pronunciation_word
                "'lefet",
                # hebrew_word_nikud
                "‫לֶפֶת‬‬"
            ),
            (
                # translation_word
                "петрушка",
                # pronunciation_word
                "petro'zilya",
                # hebrew_word_nikud
                "‫פֶּטרוֹזִיליָה‬‬"
            ),
            (
                # translation_word
                "укроп",
                # pronunciation_word
                "ʃamir",
                # hebrew_word_nikud
                "‬‫שָמִיר‬"
            ),
            (
                # translation_word
                "салат (латук)",
                # pronunciation_word
                "'χasa",
                # hebrew_word_nikud
                "‫חַסָה‬‬"
            ),
    (
                # translation_word
                "сельдерей",
                # pronunciation_word
                "'seleri",
                # hebrew_word_nikud
                "‫סֶלֶרִי‬‬"
            ),
            (
                # translation_word
                "спаржа",
                # pronunciation_word
                "aspa'ragos",
                # hebrew_word_nikud
                "‫אַספָּרָגוֹס‬‬"
            ),
            (
                # translation_word
                "шпинат",
                # pronunciation_word
                "'tered",
                # hebrew_word_nikud
                "‫תֶרֶד‬‬"
            ),
            (
                # translation_word
                "горох",
                # pronunciation_word
                "afuna",
                # hebrew_word_nikud
                "‫אֲפוּנָה‬‬"
            ),
            (
                # translation_word
                "бобы",
                # pronunciation_word
                "pol",
                # hebrew_word_nikud
                "‫פּוֹל‬‬"
            ),
            (
                # translation_word
                "кукуруза",
                # pronunciation_word
                "'tiras",
                # hebrew_word_nikud
                "‬‫תִירָס‬"
            ),
            (
                # translation_word
                "фасоль",
                # pronunciation_word
                "ʃʿuʿit",
                # hebrew_word_nikud
                "‬‫שְעוּעִית‬"
            ),
            (
                # translation_word
                "перец",
                # pronunciation_word
                "'pilpel",
                # hebrew_word_nikud
                "‫פִּלפֵּל‬‬"
            ),
            (
                # translation_word
                "редис",
                # pronunciation_word
                "ʦnonit",
                # hebrew_word_nikud
                "‬‫צנוֹנִית‬"
            ),
            (
                # translation_word
                "артишок",
                # pronunciation_word
                "artiʃok",
                # hebrew_word_nikud
                "‫אַרטִישוֹק‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "47. Фрукты. Орехи",
        # words
        [
            (
                # translation_word
                "фрукт",
                # pronunciation_word
                "pri",
                # hebrew_word_nikud
                "‬‫פּרִי‬"
            ),
            (
                # translation_word
                "яблоко",
                # pronunciation_word
                "ta'puaχ",
                # hebrew_word_nikud
                "‫תַפּוּח‬‬"
            ),
            (
                # translation_word
                "груша",
                # pronunciation_word
                "agas",
                # hebrew_word_nikud
                "‬‫אַגָס‬"
            ),
            (
                # translation_word
                "лимон",
                # pronunciation_word
                "limon",
                # hebrew_word_nikud
                "‫לִימוֹן‬‬"
            ),
            (
                # translation_word
                "апельсин",
                # pronunciation_word
                "tapuz",
                # hebrew_word_nikud
                "‫תַפּוּז‬‬"
            ),
            (
                # translation_word
                "клубника",
                # pronunciation_word
                "tut sade",
                # hebrew_word_nikud
                "תוּת‬‬‬ ‫שָׂדֶה‬‬"
            ),
            (
                # translation_word
                "мандарин",
                # pronunciation_word
                "klemen'tina",
                # hebrew_word_nikud
                "‫קלֶמֶנטִינָה‬‬"
            ),
            (
                # translation_word
                "слива",
                # pronunciation_word
                "ʃezif",
                # hebrew_word_nikud
                "‫שְזִיף‬‬"
            ),
            (
                # translation_word
                "персик",
                # pronunciation_word
                "afarsek",
                # hebrew_word_nikud
                "‫אֲפַרסֵק‬‬"
            ),
            (
                # translation_word
                "абрикос",
                # pronunciation_word
                "'miʃmeʃ",
                # hebrew_word_nikud
                "‫מִשמֵש‬‬"
            ),
            (
                # translation_word
                "малина",
                # pronunciation_word
                "'petel",
                # hebrew_word_nikud
                "‬‫פֶּטֶל‬"
            ),
            (
                # translation_word
                "ананас",
                # pronunciation_word
                "'ananas",
                # hebrew_word_nikud
                "‬‫אָנָנָס‬"
            ),
            (
                # translation_word
                "банан",
                # pronunciation_word
                "ba'nana",
                # hebrew_word_nikud
                "‫בַּנָנָה‬‬"
            ),
            (
                # translation_word
                "арбуз",
                # pronunciation_word
                "ava'tiaχ",
                # hebrew_word_nikud
                "‫אֲבַטִיח‬‬"
            ),
            (
                # translation_word
                "виноград",
                # pronunciation_word
                "anavim",
                # hebrew_word_nikud
                "‫עֲנָבִים‬‬"
            ),
            (
                # translation_word
                "вишня",
                # pronunciation_word
                "duvdevan",
                # hebrew_word_nikud
                "‫דוּבדְבָן‬‬"
            ),
            (
                # translation_word
                "черешня",
                # pronunciation_word
                "gudgedan",
                # hebrew_word_nikud
                "‫גוּדגְדָן‬‬"
            ),
            (
                # translation_word
                "дыня",
                # pronunciation_word
                "melon",
                # hebrew_word_nikud
                "‫מֶלוֹן‬‬"
            ),
            (
                # translation_word
                "грейпфрут",
                # pronunciation_word
                "eʃkolit",
                # hebrew_word_nikud
                "‬‫אֶשכּוֹלִית‬"
            ),
            (
                # translation_word
                "авокадо",
                # pronunciation_word
                "avo'kado",
                # hebrew_word_nikud
                "‫אָבוֹקָדו‬‬"
            ),
            (
                # translation_word
                "папайя",
                # pronunciation_word
                "pa'paya",
                # hebrew_word_nikud
                "‫פַּפָּאיָה‬‬"
            ),
            (
                # translation_word
                "манго",
                # pronunciation_word
                "'mango",
                # hebrew_word_nikud
                "‬‫מַנגו‬"
            ),
            (
                # translation_word
                "гранат",
                # pronunciation_word
                "rimon",
                # hebrew_word_nikud
                "‫רִימוֹן‬‬‬"
            ),
            (
                # translation_word
                "крыжовник",
                # pronunciation_word
                "χazarzar",
                # hebrew_word_nikud
                "‫חֲזַרזָר‬‬"
            ),
            (
                # translation_word
                "черника",
                # pronunciation_word
                "uχmanit",
                # hebrew_word_nikud
                "‫אוּכמָנִית‬‬"
            ),
            (
                # translation_word
                "изюм",
                # pronunciation_word
                "ʦimukim",
                # hebrew_word_nikud
                "‫צִימוּקִים‬‬"
            ),
            (
                # translation_word
                "финик",
                # pronunciation_word
                "tamar",
                # hebrew_word_nikud
                "‫תָמָר‬‬"
            ),
            (
                # translation_word
                "арахис",
                # pronunciation_word
                "botnim",
                # hebrew_word_nikud
                "‬‫בּוֹטנִים‬"
            ),
            (
                # translation_word
                "миндаль",
                # pronunciation_word
                "ʃaked",
                # hebrew_word_nikud
                "‫שָקֵד‬‬"
            ),
            (
                # translation_word
                "орех (грецкий)",
                # pronunciation_word
                "egoz 'meleχ",
                # hebrew_word_nikud
                "אֱגוֹז‬‬‬ ‫מֶלֶך‬‬"
            ),
            (
                # translation_word
                "орех (лесной)",
                # pronunciation_word
                "egoz ilsar",
                # hebrew_word_nikud
                "אֱגוֹז‬‬‬ ‫אִלְסָר‬‬"
            ),
            (
                # translation_word
                "орех кокосовый",
                # pronunciation_word
                "'kokus",
                # hebrew_word_nikud
                "‫קוֹקוּס‬‬"
            ),
            (
                # translation_word
                "фисташки",
                # pronunciation_word
                "'fistuk",
                # hebrew_word_nikud
                "‫פִיסטוּק‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "48. Сладости. Хлеб",
        # words
        [
            (
                # translation_word
                "кондитерские изделия",
                # pronunciation_word
                "muʦrei kondi'torya",
                # hebrew_word_nikud
                "מוּצרֵי‬‬‬ ‫קוֹנדִיטוֹריָה‬‬"
            ),
            (
                # translation_word
                "хлеб",
                # pronunciation_word
                "'leχem",
                # hebrew_word_nikud
                "‫לֶחֶם‬‬"
            ),
            (
                # translation_word
                "печенье",
                # pronunciation_word
                "ugiya",
                # hebrew_word_nikud
                "‫עוּגִיָּה‬‬"
            ),
            (
                # translation_word
                "шоколад",
                # pronunciation_word
                "'ʃokolad",
                # hebrew_word_nikud
                "‫שוֹקוֹלָד‬‬"
            ),
            (
                # translation_word
                "шоколадный",
                # pronunciation_word
                "mi'ʃokolad",
                # hebrew_word_nikud
                "‫מִשוֹקוֹלָד‬‬"
            ),
            (
                # translation_word
                "конфета",
                # pronunciation_word
                "sukariya",
                # hebrew_word_nikud
                "‫סוּכָּרִייָה‬‬"
            ),
            (
                # translation_word
                "пирожное",
                # pronunciation_word
                "uga",
                # hebrew_word_nikud
                "‬‫עוּגָה‬"
            ),
            (
                # translation_word
                "торт",
                # pronunciation_word
                "uga",
                # hebrew_word_nikud
                "‫עוּגָה‬‬"
            ),
            (
                # translation_word
                "пирог",
                # pronunciation_word
                "pai",
                # hebrew_word_nikud
                "‬‫פַּאי‬"
            ),
            (
                # translation_word
                "начинка",
                # pronunciation_word
                "milui",
                # hebrew_word_nikud
                "‫מִילוּי‬‬"
            ),
            (
                # translation_word
                "варенье",
                # pronunciation_word
                "riba",
                # hebrew_word_nikud
                "‫רִיבָּה‬‬"
            ),
            (
                # translation_word
                "мармелад",
                # pronunciation_word
                "marme'lada",
                # hebrew_word_nikud
                "‫מַרְמֶלָדָה‬‬"
            ),
            (
                # translation_word
                "вафли",
                # pronunciation_word
                "'vaflim",
                # hebrew_word_nikud
                "‫וַפלִים‬‬"
            ),
            (
                # translation_word
                "мороженое",
                # pronunciation_word
                "'glida",
                # hebrew_word_nikud
                "‬‫גלִידָה‬"
            ),
            (
                # translation_word
                "пудинг",
                # pronunciation_word
                "'puding",
                # hebrew_word_nikud
                "‫פּוּדִינג‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "49. Блюда",
        # words
        [
            (
                # translation_word
                "кухня (национальная)",
                # pronunciation_word
                "mitbaχ",
                # hebrew_word_nikud
                "‫מִטבָּח‬‬"
            ),
            (
                # translation_word
                "рецепт",
                # pronunciation_word
                "matkon",
                # hebrew_word_nikud
                "‫מַתכּוֹן‬‬"
            ),
            (
                # translation_word
                "порция",
                # pronunciation_word
                "mana",
                # hebrew_word_nikud
                "‬‫מָנָה‬"
            ),
            (
                # translation_word
                "салат",
                # pronunciation_word
                "salat",
                # hebrew_word_nikud
                "‬‫סָלָט‬"
            ),
            (
                # translation_word
                "суп",
                # pronunciation_word
                "marak",
                # hebrew_word_nikud
                "‫מָרָק‬‬"
            ),
            (
                # translation_word
                "бутерброд",
                # pronunciation_word
                "kariχ",
                # hebrew_word_nikud
                "‫כָּרִיך‬‬"
            ),
            (
                # translation_word
                "яичница",
                # pronunciation_word
                "beiʦat ain",
                # hebrew_word_nikud
                "בֵּיצַת‬‬‬ ‫עַיִן‬‬"
            ),
            (
                # translation_word
                "гамбургер",
                # pronunciation_word
                "'hamburger",
                # hebrew_word_nikud
                "‫הַמבּוּרגֶר‬‬"
            ),
            (
                # translation_word
                "бифштекс",
                # pronunciation_word
                "steik",
                # hebrew_word_nikud
                "‫סטֵייק‬‬"
            ),
            (
                # translation_word
                "гарнир",
                # pronunciation_word
                "to'sefet",
                # hebrew_word_nikud
                "‫תוֹסֶפֶת‬‬"
            ),
            (
                # translation_word
                "спагетти",
                # pronunciation_word
                "spa'geti",
                # hebrew_word_nikud
                "‫ספָּגֶטִי‬‬"
            ),
            (
                # translation_word
                "пицца",
                # pronunciation_word
                "'piʦa",
                # hebrew_word_nikud
                "‫פִּיצָה‬‬"
            ),
            (
                # translation_word
                "картофельное пюре",
                # pronunciation_word
                "meχit tapuχei adama",
                # hebrew_word_nikud
                "מְחִית‬ ‫תַפּוּחֵי‬ ‬‬‫אֲדָמָה‬‬"
            ),
            (
                # translation_word
                "каша",
                # pronunciation_word
                "daysa",
                # hebrew_word_nikud
                "‫דַייסָה‬‬"
            ),
            (
                # translation_word
                "омлет",
                # pronunciation_word
                "χavita",
                # hebrew_word_nikud
                "‫חֲבִיתָה‬‬"
            ),
            (
                # translation_word
                "жареный",
                # pronunciation_word
                "metugan",
                # hebrew_word_nikud
                "‫מְטוּגָן‬‬"
            ),
            (
                # translation_word
                "замороженный",
                # pronunciation_word
                "kafu",
                # hebrew_word_nikud
                "‫קָפוּא‬‬"
            ),
            (
                # translation_word
                "маринованный",
                # pronunciation_word
                "kavuʃ",
                # hebrew_word_nikud
                "‫כָּבוּש‬‬"
            ),
            (
                # translation_word
                "сладкий",
                # pronunciation_word
                "matok",
                # hebrew_word_nikud
                "‫מָתוֹק‬‬"
            ),
            (
                # translation_word
                "солёный",
                # pronunciation_word
                "ma'luaχ",
                # hebrew_word_nikud
                "‫מָלוּח‬‬"
            ),
            (
                # translation_word
                "холодный",
                # pronunciation_word
                "kar",
                # hebrew_word_nikud
                "‫קַר‬‬"
            ),
            (
                # translation_word
                "горячий",
                # pronunciation_word
                "χam",
                # hebrew_word_nikud
                "‫חַם‬‬"
            ),
            (
                # translation_word
                "горький",
                # pronunciation_word
                "marir",
                # hebrew_word_nikud
                "‫מָרִיר‬"
            ),
            (
                # translation_word
                "вкусный",
                # pronunciation_word
                "taʿim",
                # hebrew_word_nikud
                "‫טָעִים‬‬"
            ),
            (
                # translation_word
                "варить (готовить)",
                # pronunciation_word
                "levaʃel be'mayim rotχim",
                # hebrew_word_nikud
                "לְבַשֵל‬‬‬ ‫בְּמַיִם‬ ‫רוֹתחִים‬‬"
            ),
            (
                # translation_word
                "готовить (ужин)",
                # pronunciation_word
                "levaʃel",
                # hebrew_word_nikud
                "‫לְבַשֵל‬‬"
            ),
            (
                # translation_word
                "жарить",
                # pronunciation_word
                "letagen",
                # hebrew_word_nikud
                "‫לְטַגֵן‬‬"
            ),
            (
                # translation_word
                "разогревать",
                # pronunciation_word
                "leχamem",
                # hebrew_word_nikud
                "‫לְחַמֵם‬‬"
            ),
            (
                # translation_word
                "солить",
                # pronunciation_word
                "leham'liaχ",
                # hebrew_word_nikud
                "‬‫לְהַמלִיח‬"
            ),
            (
                # translation_word
                "чистить (картошку и т.п.)",
                # pronunciation_word
                "lekalef",
                # hebrew_word_nikud
                "‫לְקַלֵף‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "50. Приправы. Специи",
        # words
        [
            (
                # translation_word
                "соль",
                # pronunciation_word
                "'melaχ",
                # hebrew_word_nikud
                "‫מֶלַח‬‬"
            ),
            (
                # translation_word
                "солёный",
                # pronunciation_word
                "ma'luaχ",
                # hebrew_word_nikud
                "ּ‫מָלו‫ַח‬‬‬"
            ),
            (
                # translation_word
                "солить",
                # pronunciation_word
                "leham'liaχ",
                # hebrew_word_nikud
                "‬‫לְהַמלִי‬‫ח‬"
            ),
            (
                # translation_word
                "чёрный перец",
                # pronunciation_word
                "'pilpel ʃaχor",
                # hebrew_word_nikud
                "פִּלפֵּל‬ ‬‬‫שָחוֹר‬‬"
            ),
            (
                # translation_word
                "красный перец",
                # pronunciation_word
                "'pilpel adom",
                # hebrew_word_nikud
                "פִּלפֵּל‬ ‬‬‫אָדוֹם‬‬"
            ),
            (
                # translation_word
                "горчица",
                # pronunciation_word
                "χardal",
                # hebrew_word_nikud
                "‫חַרדָל‬‬"
            ),
            (
                # translation_word
                "приправа, соус",
                # pronunciation_word
                "'rotev",
                # hebrew_word_nikud
                "‫רוֹטֶב‬‬"
            ),
            (
                # translation_word
                "уксус",
                # pronunciation_word
                "'χomeʦ",
                # hebrew_word_nikud
                "‬‫חוֹמֶץ‬"
            ),
            (
                # translation_word
                "имбирь",
                # pronunciation_word
                "'ʤinʤer",
                # hebrew_word_nikud
                "‫גִ׳ינגֶ׳ר‬‬"
            ),
            (
                # translation_word
                "корица",
                # pronunciation_word
                "kinamon",
                # hebrew_word_nikud
                "‬‫קִינָמוֹן‬"
            ),
            (
                # translation_word
                "паприка",
                # pronunciation_word
                "'paprika",
                # hebrew_word_nikud
                "‫פַּפּרִיקָה‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "51. Приём пищи",
        # words
        [
            (
                # translation_word
                "еда",
                # pronunciation_word
                "'oχel",
                # hebrew_word_nikud
                "‬‫אוֹכֶל‬"
            ),
            (
                # translation_word
                "есть",
                # pronunciation_word
                "leʾeχol",
                # hebrew_word_nikud
                "‫לֶאֱכוֹל‬‬"
            ),
            (
                # translation_word
                "завтрак",
                # pronunciation_word
                "aruχat 'boker",
                # hebrew_word_nikud
                "‬אֲרוּחַת‬ ‬‬‫בּוֹקֶר‬"
            ),
            (
                # translation_word
                "обед",
                # pronunciation_word
                "aruχat ʦaha'rayim",
                # hebrew_word_nikud
                "אֲרוּחַת‬ ‬‬‫צָהֳרַיִים‬‬"
            ),
            (
                # translation_word
                "ужин",
                # pronunciation_word
                "aruχat 'erev",
                # hebrew_word_nikud
                "‬אֲרוּחַת‬ ‬‬‫עֶרֶב‬"
            ),
            (
                # translation_word
                "аппетит",
                # pronunciation_word
                "teʾavon",
                # hebrew_word_nikud
                "‫תֵיאָבוֹן‬‬"
            ),
            (
                # translation_word
                "Приятного аппетита!",
                # pronunciation_word
                "beteiʾavon!",
                # hebrew_word_nikud
                "!‫בְּתֵיאָבוֹן‬‬"
            ),
            (
                # translation_word
                "открывать (банку и т.п.)",
                # pronunciation_word
                "lif'toaχ",
                # hebrew_word_nikud
                "‫לִפתוֹח‬‬"
            ),
            (
                # translation_word
                "кипеть",
                # pronunciation_word
                "lir'toaχ",
                # hebrew_word_nikud
                "‬‫לִרתוֹח‬"
            ),
            (
                # translation_word
                "охладить",
                # pronunciation_word
                "lekarer",
                # hebrew_word_nikud
                "‬‫לְקָרֵר‬"
            ),
            (
                # translation_word
                "вкус",
                # pronunciation_word
                "'taʿam",
                # hebrew_word_nikud
                "‫טַעַם‬‬"
            ),
            (
                # translation_word
                "привкус",
                # pronunciation_word
                "'taʿam levai",
                # hebrew_word_nikud
                "‬טַעַם‬ ‬‬‫לְווַאי‬"
            ),
            (
                # translation_word
                "худеть",
                # pronunciation_word
                "lirzot",
                # hebrew_word_nikud
                "‫לִרזוֹת‬‬"
            ),
            (
                # translation_word
                "диета",
                # pronunciation_word
                "di'ʾeta",
                # hebrew_word_nikud
                "‫דִיאֶטָה‬‬"
            ),
            (
                # translation_word
                "витамин",
                # pronunciation_word
                "vitamin",
                # hebrew_word_nikud
                "‫וִיטָמִין‬‬"
            ),
            (
                # translation_word
                "вегетарианец",
                # pronunciation_word
                "ʦimχoni",
                # hebrew_word_nikud
                "‫צִמחוֹנִי‬‬"
            ),
            (
                # translation_word
                "жиры",
                # pronunciation_word
                "ʃumanim",
                # hebrew_word_nikud
                "‫שוּמָנִים‬‬"
            ),
            (
                # translation_word
                "белки",
                # pronunciation_word
                "χelbonim",
                # hebrew_word_nikud
                "‬‫חֶלבּוֹנִים‬"
            ),
            (
                # translation_word
                "углеводы",
                # pronunciation_word
                "paχmema",
                # hebrew_word_nikud
                "‫פַּחמֵימָה‬‬"
            ),
            (
                # translation_word
                "кусок",
                # pronunciation_word
                "χatiχa",
                # hebrew_word_nikud
                "‫חֲתִיכָה‬‬"
            ),
            (
                # translation_word
                "крошка (хлеба и т.п.)",
                # pronunciation_word
                "perur",
                # hebrew_word_nikud
                "‫פֵּירוּר‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "52. Сервировка стола",
        # words
        [
            (
                # translation_word
                "ложка",
                # pronunciation_word
                "kaf",
                # hebrew_word_nikud
                "‫כַּף‬‬"
            ),
            (
                # translation_word
                "нож",
                # pronunciation_word
                "sakin",
                # hebrew_word_nikud
                "‫סַכִּין‬‬"
            ),
            (
                # translation_word
                "вилка",
                # pronunciation_word
                "mazleg",
                # hebrew_word_nikud
                "‫מַזלֵג‬‬"
            ),
            (
                # translation_word
                "чашка",
                # pronunciation_word
                "'sefel",
                # hebrew_word_nikud
                "‫סֵפֶל‬‬"
            ),
            (
                # translation_word
                "тарелка",
                # pronunciation_word
                "ʦa'laχat",
                # hebrew_word_nikud
                "‫צַלַחַת‬‬"
            ),
            (
                # translation_word
                "блюдце",
                # pronunciation_word
                "taχtit",
                # hebrew_word_nikud
                "‫תַחתִית‬‬"
            ),
            (
                # translation_word
                "салфетка",
                # pronunciation_word
                "mapit",
                # hebrew_word_nikud
                "‬‫מַפִּית‬"
            ),
            (
                # translation_word
                "зубочистка",
                # pronunciation_word
                "keisam ʃi'nayim",
                # hebrew_word_nikud
                "קֵיסַם‬ ‬‬‫שִינַיִים‬‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "53. Ресторан",
        # words
        [
            (
                # translation_word
                "ресторан",
                # pronunciation_word
                "misʿada",
                # hebrew_word_nikud
                "‫מִסעָדָה‬‬"
            ),
            (
                # translation_word
                "кофейня",
                # pronunciation_word
                "beit kafe",
                # hebrew_word_nikud
                "בֵּית‬ ‬‬‫קָפֶה‬‬"
            ),
            (
                # translation_word
                "бар",
                # pronunciation_word
                "bar",
                # hebrew_word_nikud
                "‫בָּר‬‬"
            ),
            (
                # translation_word
                "чайный салон",
                # pronunciation_word
                "beit te",
                # hebrew_word_nikud
                "‬בֵּית‬‬‬ ‫תֵה‬"
            ),
            (
                # translation_word
                "официант",
                # pronunciation_word
                "melʦar",
                # hebrew_word_nikud
                "‬‫מֶלצָר‬"
            ),
            (
                # translation_word
                "официантка",
                # pronunciation_word
                "melʦarit",
                # hebrew_word_nikud
                "‬‫מֶלצָרִית‬"
            ),
            (
                # translation_word
                "бармен",
                # pronunciation_word
                "'barmen",
                # hebrew_word_nikud
                "‫בַּרמֶן‬‬"
            ),
            (
                # translation_word
                "меню",
                # pronunciation_word
                "tafrit",
                # hebrew_word_nikud
                "‬‫תַפרִיט‬"
            ),
            (
                # translation_word
                "забронировать столик",
                # pronunciation_word
                "lehazmin ʃulχan",
                # hebrew_word_nikud
                "לְהַזמִין‬‬‬ ‫שוּלחָן‬‬"
            ),
            (
                # translation_word
                "блюдо",
                # pronunciation_word
                "mana",
                # hebrew_word_nikud
                "‬‫מָנָה‬"
            ),
            (
                # translation_word
                "заказать",
                # pronunciation_word
                "lehazmin",
                # hebrew_word_nikud
                "‫לְהַזמִין‬‬"
            ),
            (
                # translation_word
                "закуска",
                # pronunciation_word
                "metaʾaven",
                # hebrew_word_nikud
                "‬‫מְתַאֲבֵן‬"
            ),
            (
                # translation_word
                "десерт",
                # pronunciation_word
                "ki'nuaχ",
                # hebrew_word_nikud
                "‫קִינוּח‬‬"
            ),
            (
                # translation_word
                "счёт",
                # pronunciation_word
                "χeʃbon",
                # hebrew_word_nikud
                "‫חֶשבּוֹן‬‬"
            ),
            (
                # translation_word
                "оплатить счёт",
                # pronunciation_word
                "leʃalem",
                # hebrew_word_nikud
                "‫לְשַלֵם‬‬"
            ),
            (
                # translation_word
                "дать сдачу",
                # pronunciation_word
                "latet 'odef",
                # hebrew_word_nikud
                "לָתֵת‬‬‬ ‫עוֹדֶף‬‬"
            ),
            (
                # translation_word
                "чаевые",
                # pronunciation_word
                "tip",
                # hebrew_word_nikud
                "‫טִיפ‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "54. Анкета. Анкетные данные",
        # words
        [
            (
                # translation_word
                "имя",
                # pronunciation_word
                "ʃem",
                # hebrew_word_nikud
                "‬‫שֵם‬"
            ),
            (
                # translation_word
                "фамилия",
                # pronunciation_word
                "ʃem miʃpaχa",
                # hebrew_word_nikud
                "‬שֵם‬‬‬ ‫מִשפָּחָה‬"
            ),
            (
                # translation_word
                "дата рождения",
                # pronunciation_word
                "taʾariχ leda",
                # hebrew_word_nikud
                "‬תַאֲרִיך‬‬‬ ‫לֵידָה‬"
            ),
            (
                # translation_word
                "место рождения",
                # pronunciation_word
                "mekom leda",
                # hebrew_word_nikud
                "מְקוֹם‬‬‬ ‫לֵידָה‬‬"
            ),
            (
                # translation_word
                "национальность",
                # pronunciation_word
                "leʾom",
                # hebrew_word_nikud
                "‫לְאוֹם‬‬"
            ),
            (
                # translation_word
                "место жительства",
                # pronunciation_word
                "mekom megurim",
                # hebrew_word_nikud
                "מְקוֹם‬‬‬ ‫מְגוּרִים‬‬"
            ),
            (
                # translation_word
                "страна",
                # pronunciation_word
                "medina",
                # hebrew_word_nikud
                "‬‫מְדִינָה‬"
            ),
            (
                # translation_word
                "профессия",
                # pronunciation_word
                "mik'ʦoʿa",
                # hebrew_word_nikud
                "‫מִקצוֹע‬‬"
            ),
            (
                # translation_word
                "пол",
                # pronunciation_word
                "min",
                # hebrew_word_nikud
                "‫מִין‬‬"
            ),
            (
                # translation_word
                "рост",
                # pronunciation_word
                "'gova",
                # hebrew_word_nikud
                "ַ‫גוֹב‬‫ה‬‬"
            ),
            (
                # translation_word
                "вес",
                # pronunciation_word
                "miʃkal",
                # hebrew_word_nikud
                "‫מִשקָל‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "55. Семья. Родственники",
        # words
        [
            (
                # translation_word
                "мать",
                # pronunciation_word
                "em",
                # hebrew_word_nikud
                "‫אֵם‬‬"
            ),
            (
                # translation_word
                "отец",
                # pronunciation_word
                "av",
                # hebrew_word_nikud
                "‬‫אָב‬"
            ),
            (
                # translation_word
                "сын",
                # pronunciation_word
                "ben",
                # hebrew_word_nikud
                "‫בֵּן‬‬"
            ),
            (
                # translation_word
                "дочь",
                # pronunciation_word
                "bat",
                # hebrew_word_nikud
                "‫בַּת‬‬"
            ),
            (
                # translation_word
                "брат",
                # pronunciation_word
                "aχ",
                # hebrew_word_nikud
                "‫אָח‬‬"
            ),
            (
                # translation_word
                "сестра",
                # pronunciation_word
                "aχot",
                # hebrew_word_nikud
                "‫אָחוֹת‬‬"
            ),
            (
                # translation_word
                "двоюродный брат",
                # pronunciation_word
                "ben dod",
                # hebrew_word_nikud
                "‬בֶּן‬‬‬ ‫דוֹד‬"
            ),
            (
                # translation_word
                "двоюродная сестра",
                # pronunciation_word
                "bat 'doda",
                # hebrew_word_nikud
                "בַּת‬‬‬ ‫דוֹדָה‬‬"
            ),
            (
                # translation_word
                "мама",
                # pronunciation_word
                "'ima",
                # hebrew_word_nikud
                "‬‫אִמָא‬"
            ),
            (
                # translation_word
                "папа",
                # pronunciation_word
                "'aba",
                # hebrew_word_nikud
                "‫אַבָּא‬‬"
            ),
            (
                # translation_word
                "родители",
                # pronunciation_word
                "horim",
                # hebrew_word_nikud
                "‫הוֹרִים‬‬"
            ),
            (
                # translation_word
                "ребёнок",
                # pronunciation_word
                "'yeled",
                # hebrew_word_nikud
                "‫יֶלֶד‬‬"
            ),
            (
                # translation_word
                "бабушка",
                # pronunciation_word
                "'savta",
                # hebrew_word_nikud
                "‫סַבתָא‬‬"
            ),
            (
                # translation_word
                "дедушка",
                # pronunciation_word
                "'saba",
                # hebrew_word_nikud
                "‬‫סַבָּא‬"
            ),
            (
                # translation_word
                "внук",
                # pronunciation_word
                "'neχed",
                # hebrew_word_nikud
                "‫נֶכֶד‬‬"
            ),
            (
                # translation_word
                "внучка",
                # pronunciation_word
                "neχda",
                # hebrew_word_nikud
                "‬‫נֶכדָה‬"
            ),
            (
                # translation_word
                "дядя",
                # pronunciation_word
                "dod",
                # hebrew_word_nikud
                "‬‫דוֹד‬"
            ),
            (
                # translation_word
                "тётя",
                # pronunciation_word
                "'doda",
                # hebrew_word_nikud
                "‫דוֹדָה‬‬"
            ),
            (
                # translation_word
                "племянник",
                # pronunciation_word
                "aχyan",
                # hebrew_word_nikud
                "‫אַחייָן‬‬"
            ),
            (
                # translation_word
                "племянница",
                # pronunciation_word
                "aχyanit",
                # hebrew_word_nikud
                "‫אַחייָנִית‬‬"
            ),
            (
                # translation_word
                "младенец",
                # pronunciation_word
                "tinok",
                # hebrew_word_nikud
                "‫תִינוֹק‬‬"
            ),
            (
                # translation_word
                "малыш",
                # pronunciation_word
                "paʿot",
                # hebrew_word_nikud
                "‫פָּעוֹט‬‬"
            ),
            (
                # translation_word
                "жена",
                # pronunciation_word
                "iʃa",
                # hebrew_word_nikud
                "‫אִשָה‬‬"
            ),
            (
                # translation_word
                "муж",
                # pronunciation_word
                "'baʿal",
                # hebrew_word_nikud
                "‫בַּעַל‬‬"
            ),
            (
                # translation_word
                "женатый",
                # pronunciation_word
                "nasui",
                # hebrew_word_nikud
                "‫נָשׂוּי‬‬"
            ),
            (
                # translation_word
                "замужняя",
                # pronunciation_word
                "nesuʾa",
                # hebrew_word_nikud
                "‫נְשׂוּאָה‬‬"
            ),
            (
                # translation_word
                "холостяк",
                # pronunciation_word
                "ravak",
                # hebrew_word_nikud
                "‬‫רַווָק‬"
            ),
            (
                # translation_word
                "разведённый",
                # pronunciation_word
                "garuʃ",
                # hebrew_word_nikud
                "‫גָרוּש‬‬"
            ),
            (
                # translation_word
                "вдова",
                # pronunciation_word
                "almana",
                # hebrew_word_nikud
                "‫אַלמָנָה‬‬"
            ),
            (
                # translation_word
                "вдовец",
                # pronunciation_word
                "alman",
                # hebrew_word_nikud
                "‫אַלמָן‬‬"
            ),
            (
                # translation_word
                "родственник",
                # pronunciation_word
                "karov miʃpaχa",
                # hebrew_word_nikud
                "קָרוֹב‬‬‬ ‫מִשפָּחָה‬‬"
            ),
            (
                # translation_word
                "сирота",
                # pronunciation_word
                "yatom",
                # hebrew_word_nikud
                "‫יָתוֹם‬‬"
            ),
            (
                # translation_word
                "сирота",
                # pronunciation_word
                "yetoma",
                # hebrew_word_nikud
                "‫יְתוֹמָה‬‬"
            ),
            (
                # translation_word
                "усыновить, удочерить",
                # pronunciation_word
                "leʾameʦ",
                # hebrew_word_nikud
                "‫לְאַמֵץ‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "56. Друзья. Знакомые. Коллеги",
        # words
        [
            (
                # translation_word
                "друг",
                # pronunciation_word
                "χaver",
                # hebrew_word_nikud
                "‬‫חָבֵר‬"
            ),
            (
                # translation_word
                "подруга",
                # pronunciation_word
                "χavera",
                # hebrew_word_nikud
                "‫חֲבֵרָה‬‬"
            ),
            (
                # translation_word
                "дружба",
                # pronunciation_word
                "yedidut",
                # hebrew_word_nikud
                "‫יְדִידוּת‬‬"
            ),
            (
                # translation_word
                "дружить",
                # pronunciation_word
                "lihyot yadidim",
                # hebrew_word_nikud
                "לִהיוֹת‬‬‬ ‫יָדִידִים‬‬"
            ),
            (
                # translation_word
                "партнёр",
                # pronunciation_word
                "ʃutaf",
                # hebrew_word_nikud
                "‫שוּתָף‬‬"
            ),
            (
                # translation_word
                "шеф",
                # pronunciation_word
                "menahel",
                # hebrew_word_nikud
                "‬‫מְנַהֵל‬"
            ),
            (
                # translation_word
                "начальник",
                # pronunciation_word
                "memune",
                # hebrew_word_nikud
                "‫מְמוּנֶה‬‬"
            ),
            (
                # translation_word
                "владелец",
                # pronunciation_word
                "beʿalim",
                # hebrew_word_nikud
                "‬‫בְּעָלִים‬"
            ),
            (
                # translation_word
                "подчинённый",
                # pronunciation_word
                "kafuf le",
                # hebrew_word_nikud
                "כָּפוּף‬‬‬ ‫ל‬‬"
            ),
            (
                # translation_word
                "коллега",
                # pronunciation_word
                "amit",
                # hebrew_word_nikud
                "‫עָמִית‬‬"
            ),
            (
                # translation_word
                "знакомый",
                # pronunciation_word
                "makar",
                # hebrew_word_nikud
                "‫מַכָּר‬‬"
            ),
            (
                # translation_word
                "попутчик",
                # pronunciation_word
                "ben levaya",
                # hebrew_word_nikud
                "בֶּן‬ ‬‬‫לְווָיָה‬‬"
            ),
            (
                # translation_word
                "одноклассник",
                # pronunciation_word
                "χaver lekita",
                # hebrew_word_nikud
                "חָבֵר‬‬‬ ‫לְכִּיתָה‬‬"
            ),
            (
                # translation_word
                "сосед",
                # pronunciation_word
                "ʃaχen",
                # hebrew_word_nikud
                "‬‫שָכֵן‬"
            ),
            (
                # translation_word
                "соседка",
                # pronunciation_word
                "ʃχena",
                # hebrew_word_nikud
                "‫שכֵנָה‬‬"
            ),
            (
                # translation_word
                "соседи",
                # pronunciation_word
                "ʃχenim",
                # hebrew_word_nikud
                "‫שכֵנִים‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "57. Женщина. Мужчина",
        # words
        [
            (
                # translation_word
                "женщина",
                # pronunciation_word
                "iʃa",
                # hebrew_word_nikud
                "‫אִשָה‬‬"
            ),
            (
                # translation_word
                "девушка",
                # pronunciation_word
                "baχura",
                # hebrew_word_nikud
                "‫בַּחוּרָה‬‬"
            ),
            (
                # translation_word
                "невеста",
                # pronunciation_word
                "kala",
                # hebrew_word_nikud
                "‫כַּלָה‬‬"
            ),
            (
                # translation_word
                "красивая",
                # pronunciation_word
                "yafa",
                # hebrew_word_nikud
                "‬‫יָפָה‬"
            ),
            (
                # translation_word
                "высокая",
                # pronunciation_word
                "gvoha",
                # hebrew_word_nikud
                "‫גבוֹהַה‬‬"
            ),
            (
                # translation_word
                "стройная",
                # pronunciation_word
                "tmira",
                # hebrew_word_nikud
                "‫תמִירָה‬‬"
            ),
            (
                # translation_word
                "невысокого роста",
                # pronunciation_word
                "namuχ",
                # hebrew_word_nikud
                "‫נָמוּך‬‬"
            ),
            (
                # translation_word
                "блондинка",
                # pronunciation_word
                "blon'dinit",
                # hebrew_word_nikud
                "‬‫בּלוֹנדִינִית‬"
            ),
            (
                # translation_word
                "брюнетка",
                # pronunciation_word
                "bru'netit",
                # hebrew_word_nikud
                "‫בּרוּנֶטִית‬‬"
            ),
            (
                # translation_word
                "девственница",
                # pronunciation_word
                "betula",
                # hebrew_word_nikud
                "‬‫בְּתוּלָה‬"
            ),
            (
                # translation_word
                "беременная",
                # pronunciation_word
                "hara",
                # hebrew_word_nikud
                "‫הָרָה‬‬"
            ),
            (
                # translation_word
                "мужчина",
                # pronunciation_word
                "'gever",
                # hebrew_word_nikud
                "‫גֶבֶר‬‬"
            ),
            (
                # translation_word
                "блондин",
                # pronunciation_word
                "blon'dini",
                # hebrew_word_nikud
                "‬‫בּלוֹנדִינִי‬"
            ),
            (
                # translation_word
                "брюнет",
                # pronunciation_word
                "ʃχarχar",
                # hebrew_word_nikud
                "‫שחַרחַר‬‬"
            ),
            (
                # translation_word
                "высокий",
                # pronunciation_word
                "ga'voha",
                # hebrew_word_nikud
                "‫גָבוֹה‬‬"
            ),
            (
                # translation_word
                "невысокого роста",
                # pronunciation_word
                "namuχ",
                # hebrew_word_nikud
                "‫נָמוּך‬‬"
            ),
            (
                # translation_word
                "грубый",
                # pronunciation_word
                "gas",
                # hebrew_word_nikud
                "‫גַס‬‬"
            ),
            (
                # translation_word
                "крепкий",
                # pronunciation_word
                "χason",
                # hebrew_word_nikud
                "‫חָסוֹן‬‬"
            ),
            (
                # translation_word
                "сильный",
                # pronunciation_word
                "χazak",
                # hebrew_word_nikud
                "‫חָזָק‬‬"
            ),
            (
                # translation_word
                "полный (толстый)",
                # pronunciation_word
                "ʃamen",
                # hebrew_word_nikud
                "‫שָמֵן‬‬"
            ),
            (
                # translation_word
                "смуглый",
                # pronunciation_word
                "ʃaχum",
                # hebrew_word_nikud
                "‬‫שָחוּם‬"
            ),
            (
                # translation_word
                "стройный",
                # pronunciation_word
                "tamir",
                # hebrew_word_nikud
                "‫תָמִיר‬‬"
            ),
            (
                # translation_word
                "элегантный",
                # pronunciation_word
                "ele'ganti",
                # hebrew_word_nikud
                "‫אֶלֶגַנטִי‬‬"
            ),
        ]
    ),  
    
    (
        # group_name_ru
        "59. Ребёнок",
        # words
        [
            (
                # translation_word
                "ребёнок",
                # pronunciation_word
                "'yeled",
                # hebrew_word_nikud
                "‫יֶלֶד‬‬"
            ),
            (
                # translation_word
                "близнецы",
                # pronunciation_word
                "teʾomim",
                # hebrew_word_nikud
                "‫תְאוֹמִים‬‬"
            ),
            (
                # translation_word
                "люлька, колыбель",
                # pronunciation_word
                "arisa",
                # hebrew_word_nikud
                "‫עֲרִיסָה‬‬"
            ),
            (
                # translation_word
                "подгузник",
                # pronunciation_word
                "χitul",
                # hebrew_word_nikud
                "‬‫חִיתוּל‬"
            ),
            (
                # translation_word
                "соска",
                # pronunciation_word
                "moʦeʦ",
                # hebrew_word_nikud
                "‫מוֹצֵץ‬‬"
            ),
            (
                # translation_word
                "коляска (детская)",
                # pronunciation_word
                "agala",
                # hebrew_word_nikud
                "‫עֲגָלָה‬‬"
            ),
            (
                # translation_word
                "детский сад",
                # pronunciation_word
                "gan yeladim",
                # hebrew_word_nikud
                "‫יְלָדִים‬ ‫גַן‬‬"
            ),
            (
                # translation_word
                "няня",
                # pronunciation_word
                "beibi'siter",
                # hebrew_word_nikud
                "‫בֵּיבִּיסִיטֶר‬‬"
            ),
            (
                # translation_word
                "детство",
                # pronunciation_word
                "yaldut",
                # hebrew_word_nikud
                "‬‫יַלדוּת‬"
            ),
            (
                # translation_word
                "кукла",
                # pronunciation_word
                "buba",
                # hebrew_word_nikud
                "‫בּוּבָּה‬‬"
            ),
            (
                # translation_word
                "игрушка",
                # pronunciation_word
                "ʦaʿa'ʦuʿa",
                # hebrew_word_nikud
                "‫צַעֲצוּע‬‬"
            ),
            (
                # translation_word
                "воспитанный",
                # pronunciation_word
                "meχunaχ",
                # hebrew_word_nikud
                "‫מְחוּנָך‬‬"
            ),
            (
                # translation_word
                "невоспитанный",
                # pronunciation_word
                "lo meχunaχ",
                # hebrew_word_nikud
                "לֹא‬‬‬ ‫מְחוּנָך‬‬"
            ),
            (
                # translation_word
                "избалованный",
                # pronunciation_word
                "mefunak",
                # hebrew_word_nikud
                "‬‫מְפוּנָק‬"
            ),
            (
                # translation_word
                "послушный",
                # pronunciation_word
                "ʦaytan",
                # hebrew_word_nikud
                "‫צַייְתָן‬‬"
            ),
            (
                # translation_word
                "вундеркинд",
                # pronunciation_word
                "'yeled 'pele",
                # hebrew_word_nikud
                "‬יֶלֶד‬‬‬ ‫פֶּלֶא‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "60. Супруги. Супружеская жизнь",
        # words
        [
            (
                # translation_word
                "целовать",
                # pronunciation_word
                "lenaʃek",
                # hebrew_word_nikud
                "‫לְנַשֵק‬‬"
            ),
            (
                # translation_word
                "целоваться",
                # pronunciation_word
                "lehitnaʃek",
                # hebrew_word_nikud
                "‫לְהִתנַשֵק‬‬"
            ),
            (
                # translation_word
                "семья",
                # pronunciation_word
                "miʃpaχa",
                # hebrew_word_nikud
                "‬‫מִשפָּחָה‬"
            ),
            (
                # translation_word
                "семейный",
                # pronunciation_word
                "miʃpaχti",
                # hebrew_word_nikud
                "‫מִשפַּחתִי‬‬"
            ),
            (
                # translation_word
                "пара,",
                # pronunciation_word
                "zug",
                # hebrew_word_nikud
                "‫זוּג‬‬"
            ),
            (
                # translation_word
                "брак (семейная жизнь)",
                # pronunciation_word
                "nisuʾim",
                # hebrew_word_nikud
                "‫נִישׂוּאִים‬‬"
            ),
            (
                # translation_word
                "свидание",
                # pronunciation_word
                "deit",
                # hebrew_word_nikud
                "‫דֵייט‬‬"
            ),
            (
                # translation_word
                "поцелуй",
                # pronunciation_word
                "neʃika",
                # hebrew_word_nikud
                "‫נְשִיקָה‬‬"
            ),
            (
                # translation_word
                "любовь",
                # pronunciation_word
                "ahava",
                # hebrew_word_nikud
                "‫אַהֲבָה‬‬"
            ),
            (
                # translation_word
                "любить (кого-л.)",
                # pronunciation_word
                "leʾehov",
                # hebrew_word_nikud
                "‫לֶאֱהוֹב‬‬"
            ),
            (
                # translation_word
                "любимый (человек)",
                # pronunciation_word
                "ahuv",
                # hebrew_word_nikud
                "‫אָהוּב‬‬"
            ),
            (
                # translation_word
                "нежность",
                # pronunciation_word
                "roχ",
                # hebrew_word_nikud
                "‫רוֹך‬‬"
            ),
            (
                # translation_word
                "верность",
                # pronunciation_word
                "neʾemanut",
                # hebrew_word_nikud
                "‫נֶאֱמָנוּת‬‬"
            ),
            (
                # translation_word
                "верный",
                # pronunciation_word
                "masur",
                # hebrew_word_nikud
                "‫מָסוּר‬‬"
            ),
            (
                # translation_word
                "заботливый",
                # pronunciation_word
                "doʾeg",
                # hebrew_word_nikud
                "‫דָוֹאֵג‬‬"
            ),
            (
                # translation_word
                "молодожёны",
                # pronunciation_word
                "zug ʦaʿir",
                # hebrew_word_nikud
                "זוּג‬‬‬ ‫צָעִיר‬‬"
            ),
            (
                # translation_word
                "выйти замуж, жениться",
                # pronunciation_word
                "lehitχaten",
                # hebrew_word_nikud
                "‫לְהִתחַתֵן‬‬"
            ),
            (
                # translation_word
                "свадьба",
                # pronunciation_word
                "χatuna",
                # hebrew_word_nikud
                "‫חֲתוּנָה‬‬"
            ),
            (
                # translation_word
                "годовщина",
                # pronunciation_word
                "yom nisuʾin",
                # hebrew_word_nikud
                "‫נִישׂוּאִין‬ ‫יוֹם‬‬"
            ),
            (
                # translation_word
                "любовник",
                # pronunciation_word
                "meʾahev",
                # hebrew_word_nikud
                "‫מְאַהֵב‬‬"
            ),
            (
                # translation_word
                "любовница",
                # pronunciation_word
                "mea'hevet",
                # hebrew_word_nikud
                "‫מְאַהֶבֶת‬‬"
            ),
            (
                # translation_word
                "измена",
                # pronunciation_word
                "bgida",
                # hebrew_word_nikud
                "‬‫בּגִידָה‬"
            ),
            (
                # translation_word
                "изменить",
                # pronunciation_word
                "livgod be...",
                # hebrew_word_nikud
                "‬לִבגוֹד‬‬‬ ְּ‫ב‬"
            ),
            (
                # translation_word
                "ревнивый",
                # pronunciation_word
                "kanai",
                # hebrew_word_nikud
                "‫קַנַאי‬‬"
            ),
            (
                # translation_word
                "ревновать",
                # pronunciation_word
                "lekane",
                # hebrew_word_nikud
                "‬‫לְקַנֵא‬"
            ),
            (
                # translation_word
                "развод",
                # pronunciation_word
                "geruʃin",
                # hebrew_word_nikud
                "‫גֵרוּשִין‬‬"
            ),
            (
                # translation_word
                "ссориться",
                # pronunciation_word
                "lariv",
                # hebrew_word_nikud
                "‫לָרִיב‬‬"
            ),
            (
                # translation_word
                "мириться",
                # pronunciation_word
                "lehitpayes",
                # hebrew_word_nikud
                "‫לְהִתפַּייֵס‬‬"
            ),
            (
                # translation_word
                "вместе",
                # pronunciation_word
                "be'yaχad",
                # hebrew_word_nikud
                "‫בְּיַחַד‬‬"
            ),
            (
                # translation_word
                "секс",
                # pronunciation_word
                "min",
                # hebrew_word_nikud
                "‫מִין‬‬"
            ),
            (
                # translation_word
                "счастье",
                # pronunciation_word
                "'oʃer",
                # hebrew_word_nikud
                "‫אוֹשֶר‬‬"
            ),
            (
                # translation_word
                "счастливый",
                # pronunciation_word
                "meʾuʃar",
                # hebrew_word_nikud
                "‫מְאוּשָר‬‬"
            ),
            (
                # translation_word
                "несчастье",
                # pronunciation_word
                "ason",
                # hebrew_word_nikud
                "‫אָסוֹן‬‬"
            ),
            (
                # translation_word
                "несчастный",
                # pronunciation_word
                "umlal",
                # hebrew_word_nikud
                "‫אוּמלָל‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "61. Чувства. Состояние человека",
        # words
        [
            (
                # translation_word
                "чувство",
                # pronunciation_word
                "'regeʃ",
                # hebrew_word_nikud
                "‫רֶגֶש‬‬"
            ),
            (
                # translation_word
                "чувствовать",
                # pronunciation_word
                "lehargiʃ",
                # hebrew_word_nikud
                "‬‫לְהַרגִיש‬"
            ),
            (
                # translation_word
                "голод",
                # pronunciation_word
                "'raʿav",
                # hebrew_word_nikud
                "‬‫רָעָב‬"
            ),
            (
                # translation_word
                "хотеть есть",
                # pronunciation_word
                "lihyot raʿev",
                # hebrew_word_nikud
                "לִהיוֹת‬‬‬ ‫רָעֵב‬‬"
            ),
            (
                # translation_word
                "жажда",
                # pronunciation_word
                "ʦimaʾon",
                # hebrew_word_nikud
                "‫צִמָאוֹן‬‬"
            ),
            (
                # translation_word
                "хотеть пить",
                # pronunciation_word
                "lihyot ʦame",
                # hebrew_word_nikud
                "לִהיוֹת‬‬‬ ‫צָמֵא‬‬"
            ),
            (
                # translation_word
                "сонливость",
                # pronunciation_word
                "yaʃ'nuniyut",
                # hebrew_word_nikud
                "‬‫יַשְׁנוּנִיוּת‬"
            ),
            (
                # translation_word
                "хотеть спать",
                # pronunciation_word
                "lirʦot liʃon",
                # hebrew_word_nikud
                "לִרצוֹת‬‬‬ ‫לִישוֹן‬‬"
            ),
            (
                # translation_word
                "усталость",
                # pronunciation_word
                "ayefut",
                # hebrew_word_nikud
                "‫עֲייֵפוּת‬‬"
            ),
            (
                # translation_word
                "усталый",
                # pronunciation_word
                "ayef",
                # hebrew_word_nikud
                "‫עָייֵף‬‬"
            ),
            (
                # translation_word
                "настроение",
                # pronunciation_word
                "maʦav 'ruaχ",
                # hebrew_word_nikud
                "מַצַב‬‬‬ ‫רוּח‬‬"
            ),
            (
                # translation_word
                "уединение",
                # pronunciation_word
                "hitbodedut",
                # hebrew_word_nikud
                "‬‫הִתבּוֹדְדוּת‬"
            ),
            (
                # translation_word
                "беспокоиться",
                # pronunciation_word
                "lidʾog",
                # hebrew_word_nikud
                "‬‫לִדאוֹג‬"
            ),
            (
                # translation_word
                "беспокойство",
                # pronunciation_word
                "deʾaga",
                # hebrew_word_nikud
                "‫דְאָגָה‬‬"
            ),
            (
                # translation_word
                "тревога",
                # pronunciation_word
                "χarada",
                # hebrew_word_nikud
                "‬‫חֲרָדָה‬"
            ),
            (
                # translation_word
                "озабоченный",
                # pronunciation_word
                "mutrad",
                # hebrew_word_nikud
                "‫מוּטרָד‬‬"
            ),
            (
                # translation_word
                "нервничать",
                # pronunciation_word
                "lihyot aʦbani",
                # hebrew_word_nikud
                "לִהיוֹת‬‬‬ ‫עַצבָּנִי‬‬"
            ),
            (
                # translation_word
                "надежда",
                # pronunciation_word
                "tikva",
                # hebrew_word_nikud
                "‬‫תִקווָה‬"
            ),
            (
                # translation_word
                "надеяться",
                # pronunciation_word
                "lekavot",
                # hebrew_word_nikud
                "‫לְקַווֹת‬‬"
            ),
            (
                # translation_word
                "уверенность",
                # pronunciation_word
                "vadaʾut",
                # hebrew_word_nikud
                "‬‫וַדָּאוּת‬"
            ),
            (
                # translation_word
                "уверенный",
                # pronunciation_word
                "vadaʾi",
                # hebrew_word_nikud
                "‫וַדָאִי‬‬"
            ),
            (
                # translation_word
                "неуверенность",
                # pronunciation_word
                "i vadaʾut",
                # hebrew_word_nikud
                "אִי‬‬‬ ‫וַדָּאוּת‬‬"
            ),
            (
                # translation_word
                "неуверенный",
                # pronunciation_word
                "lo ba'tuaχ",
                # hebrew_word_nikud
                "לֹא‬‬‬ ‫בָּטוּח‬‬"
            ),
            (
                # translation_word
                "пьяный",
                # pronunciation_word
                "ʃikor",
                # hebrew_word_nikud
                "‬‫שִיכּוֹר‬"
            ),
            (
                # translation_word
                "трезвый",
                # pronunciation_word
                "pi'keaχ",
                # hebrew_word_nikud
                "‫פִּיכֵּח‬‬"
            ),
            (
                # translation_word
                "слабый",
                # pronunciation_word
                "χalaʃ",
                # hebrew_word_nikud
                "‫חַלָש‬‬"
            ),
            (
                # translation_word
                "счастливый",
                # pronunciation_word
                "meʾuʃar",
                # hebrew_word_nikud
                "‫מְאוּשָר‬‬"
            ),
            (
                # translation_word
                "испугать",
                # pronunciation_word
                "lehafχid",
                # hebrew_word_nikud
                "‬‫לְהַפחִיד‬"
            ),
            (
                # translation_word
                "бешенство",
                # pronunciation_word
                "teruf",
                # hebrew_word_nikud
                "‫טֵירוּף‬‬"
            ),
            (
                # translation_word
                "ярость",
                # pronunciation_word
                "'zaʿam",
                # hebrew_word_nikud
                "‫זַעַם‬‬"
            ),
            (
                # translation_word
                "депрессия",
                # pronunciation_word
                "dikaʾon",
                # hebrew_word_nikud
                "‫דִּיכָּאוֹן‬‬"
            ),
            (
                # translation_word
                "дискомфорт",
                # pronunciation_word
                "i noχut",
                # hebrew_word_nikud
                "אִי‬‬‬ ‫נוֹחוּת‬‬"
            ),
            (
                # translation_word
                "комфорт",
                # pronunciation_word
                "noχut",
                # hebrew_word_nikud
                "‬‫נוֹחוּת‬"
            ),
            (
                # translation_word
                "сожалеть",
                # pronunciation_word
                "lehiʦtaʿer",
                # hebrew_word_nikud
                "‫לְהִצטַעֵר‬‬"
            ),
            (
                # translation_word
                "сожаление",
                # pronunciation_word
                "χarata",
                # hebrew_word_nikud
                "‫חֲרָטָה‬‬"
            ),
            (
                # translation_word
                "невезение",
                # pronunciation_word
                "'χoser mazal",
                # hebrew_word_nikud
                "חוֹסֶר‬‬‬ ‫מַזָל‬‬"
            ),
            (
                # translation_word
                "огорчение",
                # pronunciation_word
                "'eʦev",
                # hebrew_word_nikud
                "‬‫עֶצֶב‬"
            ),
            (
                # translation_word
                "стыд",
                # pronunciation_word
                "buʃa",
                # hebrew_word_nikud
                "‫בּוּשָה‬‬"
            ),
            (
                # translation_word
                "веселье (радость)",
                # pronunciation_word
                "simχa",
                # hebrew_word_nikud
                "‫שִׂמחָה‬‬"
            ),
            (
                # translation_word
                "энтузиазм",
                # pronunciation_word
                "hitlahavut",
                # hebrew_word_nikud
                "‫הִתלַהֲבוּת‬‬"
            ),
        ]
    ),           
    (
        # group_name_ru
        "62. Черты характера. Личность",
        # words
        [
            (
                # translation_word
                "характер",
                # pronunciation_word
                "'ofi",
                # hebrew_word_nikud
                "‬‫אוֹפִי‬"
            ),
            (
                # translation_word
                "недостаток (характера)",
                # pronunciation_word
                "pgam be'ʾofi",
                # hebrew_word_nikud
                "‬פּגָם‬‬‬ ‫בְּאוֹפִי‬"
            ),
            (
                # translation_word
                "ум",
                # pronunciation_word
                "'seχel",
                # hebrew_word_nikud
                "‫שֵׂכֶל‬‬"
            ),
            (
                # translation_word
                "разум",
                # pronunciation_word
                "bina",
                # hebrew_word_nikud
                "‫בִּינָה‬‬"
            ),
            (
                # translation_word
                "совесть",
                # pronunciation_word
                "maʦpun",
                # hebrew_word_nikud
                "‫מַצפּוּן‬‬"
            ),
            (
                # translation_word
                "привычка",
                # pronunciation_word
                "hergel",
                # hebrew_word_nikud
                "‫הֶרגֵל‬‬"
            ),
            (
                # translation_word
                "способность (к чему-л.)",
                # pronunciation_word
                "ye'χolet",
                # hebrew_word_nikud
                "‫יְכוֹלֶת‬‬"
            ),
            (
                # translation_word
                "уметь",
                # pronunciation_word
                "la'daʿat",
                # hebrew_word_nikud
                "‫לָדַעַת‬‬"
            ),
            (
                # translation_word
                "терпеливый",
                # pronunciation_word
                "savlan",
                # hebrew_word_nikud
                "‫סַבלָן‬‬"
            ),
            (
                # translation_word
                "нетерпеливый",
                # pronunciation_word
                "χasar savlanut",
                # hebrew_word_nikud
                "חֲסַר‬‬‬ ‫סַבלָנוּת‬‬"
            ),
            (
                # translation_word
                "любопытный",
                # pronunciation_word
                "sakran",
                # hebrew_word_nikud
                "‫סַקרָן‬‬"
            ),
            (
                # translation_word
                "скромный",
                # pronunciation_word
                "ʦa'nuʿa",
                # hebrew_word_nikud
                "‫צָנוּע‬‬"
            ),
            (
                # translation_word
                "нескромный",
                # pronunciation_word
                "lo ʦa'nuʿa",
                # hebrew_word_nikud
                "לֹא‬‬‬ ‫צָנוּע‬‬"
            ),
            (
                # translation_word
                "лень",
                # pronunciation_word
                "aʦlut",
                # hebrew_word_nikud
                "‫עַצְלוּת‬‬"
            ),
            (
                # translation_word
                "ленивый",
                # pronunciation_word
                "aʦel",
                # hebrew_word_nikud
                "‫עָצֵל‬‬"
            ),
            (
                # translation_word
                "хитрый",
                # pronunciation_word
                "armumi",
                # hebrew_word_nikud
                "‫עַרמוּמִי‬‬"
            ),
            (
                # translation_word
                "недоверчивый",
                # pronunciation_word
                "χadʃani",
                # hebrew_word_nikud
                "‫חַדשָנִי‬‬"
            ),
            (
                # translation_word
                "щедрый",
                # pronunciation_word
                "nadiv",
                # hebrew_word_nikud
                "‬‫נָדִיב‬"
            ),
            (
                # translation_word
                "талантливый",
                # pronunciation_word
                "muχʃar",
                # hebrew_word_nikud
                "‫מוּכשָר‬‬"
            ),
            (
                # translation_word
                "смелый",
                # pronunciation_word
                "amiʦ",
                # hebrew_word_nikud
                "‫אַמִיץ‬‬"
            ),
            (
                # translation_word
                "честный",
                # pronunciation_word
                "yaʃar",
                # hebrew_word_nikud
                "‫יָשָר‬‬"
            ),
            (
                # translation_word
                "осторожный",
                # pronunciation_word
                "zahir",
                # hebrew_word_nikud
                "‫זָהִיר‬‬"
            ),
            (
                # translation_word
                "серьёзный",
                # pronunciation_word
                "reʦini",
                # hebrew_word_nikud
                "‫רְצִינִי‬‬"
            ),
            (
                # translation_word
                "строгий",
                # pronunciation_word
                "χamur",
                # hebrew_word_nikud
                "‬‫חָמוּר‬"
            ),
            (
                # translation_word
                "решительный",
                # pronunciation_word
                "neχraʦ",
                # hebrew_word_nikud
                "‫נֶחרַץ‬‬"
            ),
            (
                # translation_word
                "нерешительный",
                # pronunciation_word
                "hasesan",
                # hebrew_word_nikud
                "‫הַסְסָן‬‬"
            ),
            (
                # translation_word
                "робкий",
                # pronunciation_word
                "baiʃan",
                # hebrew_word_nikud
                "‫בַּיישָן‬‬"
            ),
            (
                # translation_word
                "доверие",
                # pronunciation_word
                "emun",
                # hebrew_word_nikud
                "‫אֵמוּן‬‬"
            ),
            (
                # translation_word
                "доверчивый",
                # pronunciation_word
                "tam",
                # hebrew_word_nikud
                "‫תָם‬‬"
            ),
            (
                # translation_word
                "искренний",
                # pronunciation_word
                "ken",
                # hebrew_word_nikud
                "‫כֵּן‬‬"
            ),
            (
                # translation_word
                "тихий (спокойный)",
                # pronunciation_word
                "ʃalev",
                # hebrew_word_nikud
                "‫שָלֵו‬‬"
            ),
            (
                # translation_word
                "откровенный",
                # pronunciation_word
                "glui lev",
                # hebrew_word_nikud
                "‬גלוּי‬‬‬ ‫לֵב‬"
            ),
            (
                # translation_word
                "открытый",
                # pronunciation_word
                "pa'tuaχ",
                # hebrew_word_nikud
                "‫פָּתוּח‬‬"
            ),
            (
                # translation_word
                "наивный",
                # pronunciation_word
                "na'ʾivi",
                # hebrew_word_nikud
                "‫נָאִיבִי‬‬"
            ),
            (
                # translation_word
                "рассеянный",
                # pronunciation_word
                "mefuzar",
                # hebrew_word_nikud
                "‫מְפוּזָר‬‬"
            ),
            (
                # translation_word
                "смешной (забавный)",
                # pronunciation_word
                "maʦχik",
                # hebrew_word_nikud
                "‫מַצחִיק‬‬"
            ),
            (
                # translation_word
                "жадный (скупой)",
                # pronunciation_word
                "rodef 'beʦa",
                # hebrew_word_nikud
                "רוֹדֵף‬‬‬ ‫בֶּצַע‬‬"
            ),
            (
                # translation_word
                "скупой",
                # pronunciation_word
                "kamʦan",
                # hebrew_word_nikud
                "‫קַמצָן‬‬"
            ),
            (
                # translation_word
                "злой",
                # pronunciation_word
                "raʃa",
                # hebrew_word_nikud
                "‫רָשָע‬‬"
            ),
            (
                # translation_word
                "упрямый",
                # pronunciation_word
                "akʃan",
                # hebrew_word_nikud
                "‫עַקשָן‬‬"
            ),
            (
                # translation_word
                "неприятный",
                # pronunciation_word
                "lo naʿim",
                # hebrew_word_nikud
                "‬לֹא‬‬‬ ‫נָעִים‬"
            ),
            (
                # translation_word
                "эгоистичный",
                # pronunciation_word
                "anoχi",
                # hebrew_word_nikud
                "‫אָנוֹכִי‬‬"
            ),
            (
                # translation_word
                "трусливый",
                # pronunciation_word
                "paχdani",
                # hebrew_word_nikud
                "‫פַּחדָנִי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "63. Сон. Состояние сна",
        # words
        [
            (
                # translation_word
                "спать",
                # pronunciation_word
                "liʃon",
                # hebrew_word_nikud
                "‫לִישוֹן‬‬"
            ),
            (
                # translation_word
                "сон (состояние)",
                # pronunciation_word
                "ʃena",
                # hebrew_word_nikud
                "‫שֵינָה‬‬"
            ),
            (
                # translation_word
                "сон (сновидения)",
                # pronunciation_word
                "χalom",
                # hebrew_word_nikud
                "‫חֲלוֹם‬‬"
            ),
            (
                # translation_word
                "видеть сны",
                # pronunciation_word
                "laχalom",
                # hebrew_word_nikud
                "‫לַחֲלוֹם‬‬"
            ),
            (
                # translation_word
                "сонный",
                # pronunciation_word
                "radum",
                # hebrew_word_nikud
                "‫רָדוּם‬‬"
            ),
            (
                # translation_word
                "кровать",
                # pronunciation_word
                "mita",
                # hebrew_word_nikud
                "‫מִיטָה‬‬"
            ),
            (
                # translation_word
                "матрас",
                # pronunciation_word
                "mizran",
                # hebrew_word_nikud
                "‫מִזרָן‬‬"
            ),
            (
                # translation_word
                "одеяло",
                # pronunciation_word
                "smiχa",
                # hebrew_word_nikud
                "‬‫שׂמִיכָה‬"
            ),
            (
                # translation_word
                "подушка",
                # pronunciation_word
                "karit",
                # hebrew_word_nikud
                "‫כָּרִית‬‬"
            ),
            (
                # translation_word
                "простыня",
                # pronunciation_word
                "sadin",
                # hebrew_word_nikud
                "‫סָדִין‬‬"
            ),
            (
                # translation_word
                "бессонница",
                # pronunciation_word
                "nedudei ʃena",
                # hebrew_word_nikud
                "נְדוּדֵי‬ ‫שֵינָה‬‬"
            ),
            (
                # translation_word
                "снотворное",
                # pronunciation_word
                "kadur ʃena",
                # hebrew_word_nikud
                "כַּדוּר‬ ‫שֵינָה‬‬"
            ),
            (
                # translation_word
                "хотеть спать",
                # pronunciation_word
                "lirʦot liʃon",
                # hebrew_word_nikud
                "לִרצוֹת‬ ‫לִישוֹן‬‬"
            ),
            (
                # translation_word
                "зевать",
                # pronunciation_word
                "lefahek",
                # hebrew_word_nikud
                "‬‫לְפַהֵק‬"
            ),
            (
                # translation_word
                "заснуть",
                # pronunciation_word
                "leheradem",
                # hebrew_word_nikud
                "‫לְהֵירָדֵם‬‬"
            ),
            (
                # translation_word
                "кошмар",
                # pronunciation_word
                "siyut",
                # hebrew_word_nikud
                "‬‫סִיוּט‬"
            ),
            (
                # translation_word
                "будильник",
                # pronunciation_word
                "ʃaʿon meʿorer",
                # hebrew_word_nikud
                "שָעוֹן‬ ‫מְעוֹרֵר‬‬"
            ),
            (
                # translation_word
                "просыпаться",
                # pronunciation_word
                "lehitʿorer",
                # hebrew_word_nikud
                "‫לְהִתעוֹרֵר‬‬"
            ),
            (
                # translation_word
                "вставать (утром)",
                # pronunciation_word
                "lakum",
                # hebrew_word_nikud
                "‫לָקוּם‬‬"
            ),
            (
                # translation_word
                "умываться",
                # pronunciation_word
                "lehitraχeʦ",
                # hebrew_word_nikud
                "‫לְהִתרַחֵץ‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "64. Юмор. Смех. Радость",
        # words
        [
            (
                # translation_word
                "юмор",
                # pronunciation_word
                "humor",
                # hebrew_word_nikud
                "‫הוּמוֹר‬‬"
            ),
            (
                # translation_word
                "чувство юмора",
                # pronunciation_word
                "χuʃ humor",
                # hebrew_word_nikud
                "חוּש‬ ‫הוּמוֹר‬‬"
            ),
            (
                # translation_word
                "веселиться",
                # pronunciation_word
                "lehanot",
                # hebrew_word_nikud
                "‫לֵיהָנוֹת‬‬"
            ),
            (
                # translation_word
                "весёлый",
                # pronunciation_word
                "sa'meaχ",
                # hebrew_word_nikud
                "‬‫שָׂמֵח‬"
            ),
            (
                # translation_word
                "улыбка",
                # pronunciation_word
                "χiyuχ",
                # hebrew_word_nikud
                "‫חִיוּך‬‬"
            ),
            (
                # translation_word
                "смеяться",
                # pronunciation_word
                "liʦχok",
                # hebrew_word_nikud
                "‫לִצחוֹק‬‬"
            ),
            (
                # translation_word
                "смех",
                # pronunciation_word
                "ʦχok",
                # hebrew_word_nikud
                "‫צחוֹק‬‬"
            ),
            (
                # translation_word
                "анекдот",
                # pronunciation_word
                "anek'dota",
                # hebrew_word_nikud
                "‫אָנֶקדוֹטָה‬‬"
            ),
            (
                # translation_word
                "смешной (анекдот)",
                # pronunciation_word
                "maʦχik",
                # hebrew_word_nikud
                "‫מַצחִיק‬‬"
            ),
            (
                # translation_word
                "шутка",
                # pronunciation_word
                "bdiχa",
                # hebrew_word_nikud
                "‫בּדִיחָה‬‬"
            ),
            (
                # translation_word
                "радоваться",
                # pronunciation_word
                "lis'moaχ",
                # hebrew_word_nikud
                "‫לִשׂמוֹח‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "65. Общение. Диалог. Разговор - 1",
        # words
        [
            (
                # translation_word
                "общение",
                # pronunciation_word
                "'keʃer",
                # hebrew_word_nikud
                "‬‫קֶשֶר‬"
            ),
            (
                # translation_word
                "общаться",
                # pronunciation_word
                "letakʃer",
                # hebrew_word_nikud
                "‫לְתַקשֵר‬‬"
            ),
            (
                # translation_word
                "разговор",
                # pronunciation_word
                "siχa",
                # hebrew_word_nikud
                "‫שִׂיחָה‬‬"
            ),
            (
                # translation_word
                "диалог",
                # pronunciation_word
                "du 'siaχ",
                # hebrew_word_nikud
                "‫דוּ־שִׂיח‬‬"
            ),
            (
                # translation_word
                "дискуссия",
                # pronunciation_word
                "diyun",
                # hebrew_word_nikud
                "‫דִיוּן‬‬"
            ),
            (
                # translation_word
                "спор (дебаты)",
                # pronunciation_word
                "vi'kuaχ",
                # hebrew_word_nikud
                "‫וִיכּוּח‬‬"
            ),
            (
                # translation_word
                "спорить",
                # pronunciation_word
                "lehitva'keaχ",
                # hebrew_word_nikud
                "‫לְהִתווַכֵּח‬‬"
            ),
            (
                # translation_word
                "собеседник",
                # pronunciation_word
                "ben 'siaχ",
                # hebrew_word_nikud
                "בֶּן‬ ‫שִׂיח‬‬"
            ),
            (
                # translation_word
                "тема",
                # pronunciation_word
                "nose",
                # hebrew_word_nikud
                "‫נוֹשֵׂא‬‬"
            ),
            (
                # translation_word
                "мнение",
                # pronunciation_word
                "deʿa",
                # hebrew_word_nikud
                "‫דֵעָה‬‬"
            ),
            (
                # translation_word
                "речь (выступление)",
                # pronunciation_word
                "neʾum",
                # hebrew_word_nikud
                "‫נְאוּם‬‬"
            ),
            (
                # translation_word
                "обсуждать",
                # pronunciation_word
                "ladun",
                # hebrew_word_nikud
                "‫לָדוּן‬‬"
            ),
            (
                # translation_word
                "беседовать",
                # pronunciation_word
                "leso'χeaχ",
                # hebrew_word_nikud
                "‫לְשׂוֹחֵח‬"
            ),
            (
                # translation_word
                "встреча",
                # pronunciation_word
                "pgiʃa",
                # hebrew_word_nikud
                "‫פּגִישָה‬‬"
            ),
            (
                # translation_word
                "пароль",
                # pronunciation_word
                "sisma",
                # hebrew_word_nikud
                "‫סִיסמָה‬‬"
            ),
            (
                # translation_word
                "секрет",
                # pronunciation_word
                "sod",
                # hebrew_word_nikud
                "‫סוֹד‬‬"
            ),
            (
                # translation_word
                "обещание",
                # pronunciation_word
                "havtaχa",
                # hebrew_word_nikud
                "‫הַבטָחָה‬‬"
            ),
            (
                # translation_word
                "обещать",
                # pronunciation_word
                "lehav'tiaχ",
                # hebrew_word_nikud
                "‫לְהַבטִיח‬‬"
            ),
            (
                # translation_word
                "совет",
                # pronunciation_word
                "eʦa",
                # hebrew_word_nikud
                "‬‫עֵצָה‬"
            ),
            (
                # translation_word
                "советовать",
                # pronunciation_word
                "leyaʿeʦ",
                # hebrew_word_nikud
                "‫לְייַעֵץ‬‬"
            ),
            (
                # translation_word
                "новость",
                # pronunciation_word
                "χadaʃot",
                # hebrew_word_nikud
                "‫חֲדָשוֹת‬‬"
            ),
            (
                # translation_word
                "вывод (заключение)",
                # pronunciation_word
                "maskana",
                # hebrew_word_nikud
                "‫מַסקָנָה‬‬"
            ),
            (
                # translation_word
                "голос",
                # pronunciation_word
                "kol",
                # hebrew_word_nikud
                "‫קוֹל‬‬"
            ),
            (
                # translation_word
                "комплимент",
                # pronunciation_word
                "maχmaʾa",
                # hebrew_word_nikud
                "‫מַחמָאָה‬‬"
            ),
            (
                # translation_word
                "слово",
                # pronunciation_word
                "mila",
                # hebrew_word_nikud
                "‫מִילָה‬‬"
            ),
            (
                # translation_word
                "ответ (на вопрос)",
                # pronunciation_word
                "tʃuva",
                # hebrew_word_nikud
                "‫תשוּבָה‬‬"
            ),
            (
                # translation_word
                "правда",
                # pronunciation_word
                "emet",
                # hebrew_word_nikud
                "‫אֱמֶת‬‬"
            ),
            (
                # translation_word
                "ложь",
                # pronunciation_word
                "'ʃeker",
                # hebrew_word_nikud
                "‫שֶקֶר‬‬"
            ),
            (
                # translation_word
                "мысль",
                # pronunciation_word
                "maχʃava",
                # hebrew_word_nikud
                "‫מַחשָבָה‬‬"
            ),
            (
                # translation_word
                "мысль (идея)",
                # pronunciation_word
                "raʿayon",
                # hebrew_word_nikud
                "‬‫רַעֲיוֹן‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "66. Общение. Диалог. Разговор - 2",
        # words
        [
            (
                # translation_word
                "уважаемый",
                # pronunciation_word
                "meχubad",
                # hebrew_word_nikud
                "‬‫מְכוּבָּד‬"
            ),
            (
                # translation_word
                "Уважаемый ... (в письме)",
                # pronunciation_word
                "hayakar ...",
                # hebrew_word_nikud
                "‬‫הַיָקָר‬"
            ),
            (
                # translation_word
                "познакомиться (с кем-л.)",
                # pronunciation_word
                "lehakir",
                # hebrew_word_nikud
                "‬‫לְהַכִּיר‬"
            ),
            (
                # translation_word
                "пожелать",
                # pronunciation_word
                "leʾaχel",
                # hebrew_word_nikud
                "‫לְאַחֵל‬‬"
            ),
            (
                # translation_word
                "удивление",
                # pronunciation_word
                "haftaʿa",
                # hebrew_word_nikud
                "‫הַפתָעָה‬‬"
            ),
            (
                # translation_word
                "удивлять",
                # pronunciation_word
                "lehaf'tiʿa",
                # hebrew_word_nikud
                "‫לְהַפתִי‬‫ע‬‬"
            ),
            (
                # translation_word
                "дать",
                # pronunciation_word
                "latet",
                # hebrew_word_nikud
                "‫לָתֵת‬‬"
            ),
            (
                # translation_word
                "взять",
                # pronunciation_word
                "la'kaχat",
                # hebrew_word_nikud
                "‫לָקַחַת‬‬"
            ),
            (
                # translation_word
                "вернуть",
                # pronunciation_word
                "lehaχzir",
                # hebrew_word_nikud
                "‫לְהַחזִיר‬‬"
            ),
            (
                # translation_word
                "извиняться",
                # pronunciation_word
                "lehitnaʦel",
                # hebrew_word_nikud
                "‫לְהִתנַצֵל‬‬"
            ),
            (
                # translation_word
                "извинение",
                # pronunciation_word
                "hitnaʦlut",
                # hebrew_word_nikud
                "‬‫הִתנַצלוּת‬"
            ),
            (
                # translation_word
                "прощать",
                # pronunciation_word
                "lis'loaχ",
                # hebrew_word_nikud
                "‫לִסלוֹח‬‬"
            ),
            (
                # translation_word
                "разговаривать",
                # pronunciation_word
                "ledaber",
                # hebrew_word_nikud
                "‬‫לְדַבֵּר‬"
            ),
            (
                # translation_word
                "слушать",
                # pronunciation_word
                "lehakʃiv",
                # hebrew_word_nikud
                "‬‫לְהַקשִיב‬"
            ),
            (
                # translation_word
                "понять",
                # pronunciation_word
                "lehavin",
                # hebrew_word_nikud
                "‫לְהָבִין‬‬"
            ),
            (
                # translation_word
                "показать",
                # pronunciation_word
                "leharʾot",
                # hebrew_word_nikud
                "‬‫לְהַראוֹת‬"
            ),
            (
                # translation_word
                "глядеть на",
                # pronunciation_word
                "lehistakel",
                # hebrew_word_nikud
                "‫לְהִסתַכֵּל‬‬"
            ),
            (
                # translation_word
                "позвать",
                # pronunciation_word
                "likro le",
                # hebrew_word_nikud
                "‬לִקרוֹא‬ ְ‫ל‬"
            ),
            (
                # translation_word
                "беспокоить (отвлечь от дел)",
                # pronunciation_word
                "lehaf'riʿa",
                # hebrew_word_nikud
                "‫לְהַפרִיע‬‬"
            ),
            (
                # translation_word
                "просьба",
                # pronunciation_word
                "bakaʃa",
                # hebrew_word_nikud
                "‫בַּקָשָה‬‬"
            ),
            (
                # translation_word
                "просить",
                # pronunciation_word
                "levakeʃ",
                # hebrew_word_nikud
                "‫לְבַקֵש‬‬"
            ),
            (
                # translation_word
                "требование",
                # pronunciation_word
                "driʃa",
                # hebrew_word_nikud
                "‫דרִישָה‬‬"
            ),
            (
                # translation_word
                "требовать",
                # pronunciation_word
                "lidroʃ",
                # hebrew_word_nikud
                "‫לִדרוֹש‬‬"
            ),
            (
                # translation_word
                "насмехаться",
                # pronunciation_word
                "lilʿog",
                # hebrew_word_nikud
                "‫לִלעוֹג‬‬"
            ),
            (
                # translation_word
                "намекать",
                # pronunciation_word
                "lirmoz",
                # hebrew_word_nikud
                "‬‫לִרמוֹז‬"
            ),
            (
                # translation_word
                "описание",
                # pronunciation_word
                "teʾur",
                # hebrew_word_nikud
                "‫תֵיאוּר‬‬"
            ),
            (
                # translation_word
                "похвалить",
                # pronunciation_word
                "leʃa'beaχ",
                # hebrew_word_nikud
                "‫לְשַבֵּח‬‬"
            ),
            (
                # translation_word
                "разочарование",
                # pronunciation_word
                "aχzava",
                # hebrew_word_nikud
                "‫אַכזָבָה‬‬"
            ),
            (
                # translation_word
                "разочаровать",
                # pronunciation_word
                "leʾaχzev",
                # hebrew_word_nikud
                "‫לְאַכזֵב‬‬"
            ),
            (
                # translation_word
                "разочароваться",
                # pronunciation_word
                "lehitʾaχzev",
                # hebrew_word_nikud
                "‬‫לְהִתאַכזֵב‬"
            ),
            (
                # translation_word
                "предположение",
                # pronunciation_word
                "hanaχa",
                # hebrew_word_nikud
                "‬‫הַנָחָה‬"
            ),
            (
                # translation_word
                "предполагать",
                # pronunciation_word
                "leʃaʿer",
                # hebrew_word_nikud
                "‫לְשַעֵר‬‬"
            ),
            (
                # translation_word
                "предостережение",
                # pronunciation_word
                "azhara",
                # hebrew_word_nikud
                "‫אַזהָרָה‬‬"
            ),
            (
                # translation_word
                "предостеречь",
                # pronunciation_word
                "lehazhir",
                # hebrew_word_nikud
                "‫לְהַזהִיר‬‬"
            ),
        ]
    ),  
    
    (
        # group_name_ru
        "68. Согласие. Несогласие. Одобрение",
        # words
        [
            (
                # translation_word
                "согласие",
                # pronunciation_word
                "haskama",
                # hebrew_word_nikud
                "‫הַסכָּמָה‬‬"
            ),
            (
                # translation_word
                "соглашаться",
                # pronunciation_word
                "lehaskim",
                # hebrew_word_nikud
                "‫לְהַסכִּים‬‬"
            ),
            (
                # translation_word
                "одобрение",
                # pronunciation_word
                "iʃur",
                # hebrew_word_nikud
                "‫אִישוּר‬‬"
            ),
            (
                # translation_word
                "одобрить",
                # pronunciation_word
                "leʾaʃer",
                # hebrew_word_nikud
                "‫לְאַשֵר‬‬"
            ),
            (
                # translation_word
                "отказ",
                # pronunciation_word
                "siruv",
                # hebrew_word_nikud
                "‬‫סִירוּב‬"
            ),
            (
                # translation_word
                "отказываться",
                # pronunciation_word
                "lesarev",
                # hebrew_word_nikud
                "‫לְסָרֵב‬‬"
            ),
            (
                # translation_word
                "Отлично!",
                # pronunciation_word
                "meʦuyan!",
                # hebrew_word_nikud
                "!‫מְצוּיָן‬‬"
            ),
            (
                # translation_word
                "Хорошо! (согласен)",
                # pronunciation_word
                "tov!",
                # hebrew_word_nikud
                "!‫טוֹב‬‬"
            ),
            (
                # translation_word
                "Ладно! (согласен)",
                # pronunciation_word
                "be'seder!",
                # hebrew_word_nikud
                "!‫בְּסֵדֶר‬‬"
            ),
            (
                # translation_word
                "запрещённый, нельзя (запрещено)",
                # pronunciation_word
                "asur",
                # hebrew_word_nikud
                "‫אָסוּר‬‬"
            ),
            (
                # translation_word
                "невозможно",
                # pronunciation_word
                "'bilti efʃari",
                # hebrew_word_nikud
                "בִּלתִי‬ ‫אֶפשָרִי‬‬"
            ),
            (
                # translation_word
                "неправильный (ошибочный)",
                # pronunciation_word
                "ʃagui",
                # hebrew_word_nikud
                "‫שָגוּי‬‬"
            ),
            (
                # translation_word
                "отклонить (просьбу)",
                # pronunciation_word
                "lidχot",
                # hebrew_word_nikud
                "‫לִדחוֹת‬‬"
            ),
            (
                # translation_word
                "поддержать (предложение)",
                # pronunciation_word
                "litmoχ be",
                # hebrew_word_nikud
                "‬לִתמוֹך‬ ‫ב‬"
            ),
            (
                # translation_word
                "принять (согласиться)",
                # pronunciation_word
                "lekabel",
                # hebrew_word_nikud
                "‫לְקַבֵּל‬‬"
            ),
            (
                # translation_word
                "подтвердить",
                # pronunciation_word
                "leʾaʃer",
                # hebrew_word_nikud
                "‬‫לְאַשֵר‬"
            ),
            (
                # translation_word
                "разрешить",
                # pronunciation_word
                "leharʃot",
                # hebrew_word_nikud
                "‬‫לְהַרשוֹת‬"
            ),
            (
                # translation_word
                "решение",
                # pronunciation_word
                "haχlata",
                # hebrew_word_nikud
                "‬‫הַחלָטָה‬"
            ),
            (
                # translation_word
                "условие",
                # pronunciation_word
                "tnai",
                # hebrew_word_nikud
                "‬‫תנַאי‬"
            ),
            (
                # translation_word
                "похвалить",
                # pronunciation_word
                "leʃa'beaχ",
                # hebrew_word_nikud
                "‫לְשַבֵּח‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "69. Успех. Удача. Поражение",
        # words
        [
            (
                # translation_word
                "успех",
                # pronunciation_word
                "haʦala",
                # hebrew_word_nikud
                "‫הַצלָחָה‬‬"
            ),
            (
                # translation_word
                "успешно",
                # pronunciation_word
                "behaʦlaχa",
                # hebrew_word_nikud
                "‫בְּהַצלָחָה‬‬"
            ),
            (
                # translation_word
                "успешный",
                # pronunciation_word
                "muʦlaχ",
                # hebrew_word_nikud
                "‫מוּצלָח‬‬"
            ),
            (
                # translation_word
                "удача (везение)",
                # pronunciation_word
                "mazal",
                # hebrew_word_nikud
                "‬‫מַזָל‬"
            ),
            (
                # translation_word
                "Удачи!",
                # pronunciation_word
                "behaʦlaχa!",
                # hebrew_word_nikud
                "!‫בְּהַצלָחָה‬‬"
            ),
            (
                # translation_word
                "неудача",
                # pronunciation_word
                "kiʃalon",
                # hebrew_word_nikud
                "‫כִּישָלוֹן‬‬"
            ),
            (
                # translation_word
                "невезение",
                # pronunciation_word
                "'χoser mazal",
                # hebrew_word_nikud
                "חוֹסֶר‬ ‫מַזָל‬‬"
            ),
            (
                # translation_word
                "катастрофа",
                # pronunciation_word
                "ason",
                # hebrew_word_nikud
                "‫אָסוֹן‬‬"
            ),
            (
                # translation_word
                "гордость",
                # pronunciation_word
                "gaʾava",
                # hebrew_word_nikud
                "‫גַאֲווָה‬‬"
            ),
            (
                # translation_word
                "гордый",
                # pronunciation_word
                "geʾe",
                # hebrew_word_nikud
                "‫גֵאֶה‬‬"
            ),
            (
                # translation_word
                "гордиться",
                # pronunciation_word
                "lehitgaʾot",
                # hebrew_word_nikud
                "‫לְהִתגָאוֹת‬‬"
            ),
            (
                # translation_word
                "победитель",
                # pronunciation_word
                "zoχe",
                # hebrew_word_nikud
                "‬‫זוֹכֶה‬"
            ),
            (
                # translation_word
                "победить",
                # pronunciation_word
                "lena'ʦeaχ",
                # hebrew_word_nikud
                "‫לְנַצ‬‫ָח‬‬"
            ),
            (
                # translation_word
                "проиграть (в спорте)",
                # pronunciation_word
                "lehafsid",
                # hebrew_word_nikud
                "‫לְהַפסִיד‬‬"
            ),
            (
                # translation_word
                "попытка",
                # pronunciation_word
                "nisayon",
                # hebrew_word_nikud
                "‫נִיסָיוֹן‬‬"
            ),
            (
                # translation_word
                "пытаться",
                # pronunciation_word
                "lenasot",
                # hebrew_word_nikud
                "‫לְנַסוֹת‬‬"
            ),
            (
                # translation_word
                "шанс",
                # pronunciation_word
                "hizdamnut",
                # hebrew_word_nikud
                "‫הִזדַמנוּת‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "70. Обиды. Ссора. Негативные эмоции",
        # words
        [
            (
                # translation_word
                "крик",
                # pronunciation_word
                "ʦeʿaka",
                # hebrew_word_nikud
                "‬‫צְעָקָה‬"
            ),
            (
                # translation_word
                "кричать",
                # pronunciation_word
                "liʦʿok",
                # hebrew_word_nikud
                "‫לִצעוֹק‬‬"
            ),
            (
                # translation_word
                "ссора (перебранка)",
                # pronunciation_word
                "riv",
                # hebrew_word_nikud
                "‫רִיב‬‬"
            ),
            (
                # translation_word
                "ссориться",
                # pronunciation_word
                "lariv",
                # hebrew_word_nikud
                "‫לָרִיב‬‬"
            ),
            (
                # translation_word
                "конфликт",
                # pronunciation_word
                "siχsuχ",
                # hebrew_word_nikud
                "‫סִכסוּך‬‬"
            ),
            (
                # translation_word
                "недоразумение",
                # pronunciation_word
                "i havana",
                # hebrew_word_nikud
                "אִי‬ ‫הֲבָנָה‬‬"
            ),
            (
                # translation_word
                "оскорбление",
                # pronunciation_word
                "elbon",
                # hebrew_word_nikud
                "‫עֶלבּוֹן‬‬"
            ),
            (
                # translation_word
                "оскорблять",
                # pronunciation_word
                "lehaʿaliv",
                # hebrew_word_nikud
                "‫לְהַעֲלִיב‬‬"
            ),
            (
                # translation_word
                "обида",
                # pronunciation_word
                "tina",
                # hebrew_word_nikud
                "‫טִינָה‬‬"
            ),
            (
                # translation_word
                "обидеть",
                # pronunciation_word
                "lif'goʿa",
                # hebrew_word_nikud
                "‫לִפגוֹע‬‬"
            ),
            (
                # translation_word
                "обидеться",
                # pronunciation_word
                "lehipaga",
                # hebrew_word_nikud
                "‫לְהִיפָּגַע‬‬"
            ),
            (
                # translation_word
                "жалоба",
                # pronunciation_word
                "tluna",
                # hebrew_word_nikud
                "‫תלוּנָה‬‬"
            ),
            (
                # translation_word
                "жаловаться",
                # pronunciation_word
                "lehitlonen",
                # hebrew_word_nikud
                "‫לְהִתלוֹנֵן‬‬"
            ),
            (
                # translation_word
                "извинение",
                # pronunciation_word
                "hitnaʦlut",
                # hebrew_word_nikud
                "‫הִתנַצלוּת‬‬"
            ),
            (
                # translation_word
                "извиняться",
                # pronunciation_word
                "lehitnaʦel",
                # hebrew_word_nikud
                "‫לְהִתנַצֵל‬‬"
            ),
            (
                # translation_word
                "просить прощения",
                # pronunciation_word
                "levakeʃ sliχa",
                # hebrew_word_nikud
                "לְבַקֵש‬ ‫סלִיחָה‬‬"
            ),
            (
                # translation_word
                "критика",
                # pronunciation_word
                "bi'koret",
                # hebrew_word_nikud
                "‫בִּיקוֹרֶת‬‬"
            ),
            (
                # translation_word
                "критиковать",
                # pronunciation_word
                "levaker",
                # hebrew_word_nikud
                "‫לְבַקֵר‬‬"
            ),
            (
                # translation_word
                "обвинение",
                # pronunciation_word
                "haʾaʃama",
                # hebrew_word_nikud
                "‫הַאֲשָמָה‬‬"
            ),
            (
                # translation_word
                "обвинять",
                # pronunciation_word
                "lehaʾaʃim",
                # hebrew_word_nikud
                "‫לְהַאֲשִים‬‬"
            ),
            (
                # translation_word
                "месть",
                # pronunciation_word
                "nekama",
                # hebrew_word_nikud
                "‫נְקָמָה‬‬"
            ),
            (
                # translation_word
                "мстить",
                # pronunciation_word
                "linkom",
                # hebrew_word_nikud
                "‬‫לִנקוֹם‬"
            ),
            (
                # translation_word
                "презирать",
                # pronunciation_word
                "lezalzel be",
                # hebrew_word_nikud
                "לְזַלזֵל‬ ‫ב‬‬"
            ),
            (
                # translation_word
                "ненависть",
                # pronunciation_word
                "sinʾa",
                # hebrew_word_nikud
                "‬‫שִׂנאָה‬"
            ),
            (
                # translation_word
                "ненавидеть",
                # pronunciation_word
                "lisno",
                # hebrew_word_nikud
                "‫לִשׂנוֹא‬‬"
            ),
            (
                # translation_word
                "нервный",
                # pronunciation_word
                "aʦbani",
                # hebrew_word_nikud
                "‫עַצבָּנִי‬‬"
            ),
            (
                # translation_word
                "нервничать",
                # pronunciation_word
                "lihyot aʦbani",
                # hebrew_word_nikud
                "לִהיוֹת‬ ‫עַצבָּנִי‬‬"
            ),
            (
                # translation_word
                "рассердить",
                # pronunciation_word
                "lehargiz",
                # hebrew_word_nikud
                "‫לְהַרגִיז‬‬"
            ),
            (
                # translation_word
                "унижать",
                # pronunciation_word
                "lehaʃpil",
                # hebrew_word_nikud
                "‫לְהַשפִּיל‬‬"
            ),
            (
                # translation_word
                "шок",
                # pronunciation_word
                "'helem",
                # hebrew_word_nikud
                "‫הֶלֶם‬‬"
            ),
            (
                # translation_word
                "шокировать",
                # pronunciation_word
                "lezaʿa'zeʿa",
                # hebrew_word_nikud
                "‬‫לְזַעֲזֵע‬"
            ),
            (
                # translation_word
                "неприятный",
                # pronunciation_word
                "lo naʿim",
                # hebrew_word_nikud
                "‬לֹא‬ ‫נָעִים‬"
            ),
            (
                # translation_word
                "страх",
                # pronunciation_word
                "'paχad",
                # hebrew_word_nikud
                "‫פַּחַד‬‬"
            ),
            (
                # translation_word
                "страшный (рассказ)",
                # pronunciation_word
                "mafχid",
                # hebrew_word_nikud
                "‫מַפחִיד‬‬"
            ),
            (
                # translation_word
                "ужасный",
                # pronunciation_word
                "ayom",
                # hebrew_word_nikud
                "‬‫אָיוֹם‬"
            ),
            (
                # translation_word
                "плакать",
                # pronunciation_word
                "livkot",
                # hebrew_word_nikud
                "‫לִבכּוֹת‬‬"
            ),
            (
                # translation_word
                "слеза",
                # pronunciation_word
                "dimʿa",
                # hebrew_word_nikud
                "‬‫דִמעָה‬"
            ),
            (
                # translation_word
                "вина (чувство вины)",
                # pronunciation_word
                "rigʃei aʃam",
                # hebrew_word_nikud
                "רִגשֵי‬ ‫אָשָם‬‬"
            ),
            (
                # translation_word
                "стресс",
                # pronunciation_word
                "'laχaʦ",
                # hebrew_word_nikud
                "‫לַחַץ‬‬"
            ),
            (
                # translation_word
                "злиться",
                # pronunciation_word
                "liχʿos",
                # hebrew_word_nikud
                "‫לִכעוֹס‬‬"
            ),
            (
                # translation_word
                "злой (сердитый)",
                # pronunciation_word
                "zoʿem",
                # hebrew_word_nikud
                "‫זוֹעֵם‬‬"
            ),
            (
                # translation_word
                "ударить",
                # pronunciation_word
                "lehakot",
                # hebrew_word_nikud
                "‫לְהַכּוֹת‬‬"
            ),
            (
                # translation_word
                "драться (в драке)",
                # pronunciation_word
                "lehitkotet",
                # hebrew_word_nikud
                "‫לְהִתקוֹטֵט‬‬"
            ),
            (
                # translation_word
                "урегулировать (конфликт)",
                # pronunciation_word
                "lehasdir",
                # hebrew_word_nikud
                "‬‫לְהַסדִיר‬"
            ),
            (
                # translation_word
                "недовольный",
                # pronunciation_word
                "lo meruʦe",
                # hebrew_word_nikud
                "לֹא‬ ‫מְרוּצֶה‬‬"
            ),
            (
                # translation_word
                "Это нехорошо!",
                # pronunciation_word
                "ze lo tov!",
                # hebrew_word_nikud
                "!‬זֶה‬ ‫לֹא‬ ‫טוֹב‬"
            ),
            (
                # translation_word
                "Это плохо!",
                # pronunciation_word
                "ze ra!",
                # hebrew_word_nikud
                "!זֶה‬ ‫רַע‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "71. Болезни",
        # words
        [
            (
                # translation_word
                "болезнь",
                # pronunciation_word
                "maχala",
                # hebrew_word_nikud
                "‫מַחֲלָה‬‬"
            ),
            (
                # translation_word
                "болеть",
                # pronunciation_word
                "lihyot χole",
                # hebrew_word_nikud
                "‬לִהיוֹת‬ ‫חוֹלֶה‬"
            ),
            (
                # translation_word
                "здоровье",
                # pronunciation_word
                "briʾut",
                # hebrew_word_nikud
                "‫בּרִיאוּת‬‬"
            ),
            (
                # translation_word
                "простуда",
                # pronunciation_word
                "hiʦtanenut",
                # hebrew_word_nikud
                "‫הִצטַנְנוּת‬‬"
            ),
            (
                # translation_word
                "простудиться",
                # pronunciation_word
                "lehiʦtanen",
                # hebrew_word_nikud
                "‫לְהִצטַנֵן‬‬"
            ),
            (
                # translation_word
                "отравление (пищевое)",
                # pronunciation_word
                "harʿalat mazon",
                # hebrew_word_nikud
                "‬הַרעָלַת‬ ‫מָזוֹן‬"
            ),
            (
                # translation_word
                "гастрит",
                # pronunciation_word
                "da'leket keiva",
                # hebrew_word_nikud
                "‬דַלֶקֶת‬ ‫קֵיבָה‬"
            ),
            (
                # translation_word
                "аппендицит",
                # pronunciation_word
                "da'leket toseftan",
                # hebrew_word_nikud
                "דַלֶקֶת‬ ‫תוֹסֶפתָן‬‬"
            ),
            (
                # translation_word
                "гепатит",
                # pronunciation_word
                "da'leket kaved",
                # hebrew_word_nikud
                "דַלֶקֶת‬ ‫כָּבֵד‬‬"
            ),
            (
                # translation_word
                "зубная боль",
                # pronunciation_word
                "keʾev ʃi'nayim",
                # hebrew_word_nikud
                "‬כְּאֵב‬ ‫שִינַיִים‬"
            ),
            (
                # translation_word
                "кариес",
                # pronunciation_word
                "a'ʃeʃet",
                # hebrew_word_nikud
                "‬‫עַשֶשֶת‬"
            ),
            (
                # translation_word
                "диарея",
                # pronunciation_word
                "ʃilʃul",
                # hebrew_word_nikud
                "‬‫שִלשוּל‬"
            ),
            (
                # translation_word
                "насморк",
                # pronunciation_word
                "na'zelet",
                # hebrew_word_nikud
                "‫נַזֶלֶת‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "72. Симптомы болезней. Лечение - 1",
        # words
        [
            (
                # translation_word
                "симптом",
                # pronunciation_word
                "simptom",
                # hebrew_word_nikud
                "‫סִימפּטוֹם‬‬"
            ),
            (
                # translation_word
                "температура",
                # pronunciation_word
                "χom",
                # hebrew_word_nikud
                "‬‫חוֹם‬"
            ),
            (
                # translation_word
                "пульс",
                # pronunciation_word
                "'dofek",
                # hebrew_word_nikud
                "‫דוֹפֶק‬‬"
            ),
            (
                # translation_word
                "головокружение",
                # pronunciation_word
                "sχar'χoret",
                # hebrew_word_nikud
                "‫סחַרחוֹרֶת‬‬"
            ),
            (
                # translation_word
                "озноб",
                # pronunciation_word
                "ʦmar'moret",
                # hebrew_word_nikud
                "‬‫צמַרמוֹרֶת‬"
            ),
            (
                # translation_word
                "кашель",
                # pronunciation_word
                "ʃiʿul",
                # hebrew_word_nikud
                "‫שִיעוּל‬‬"
            ),
            (
                # translation_word
                "кашлять",
                # pronunciation_word
                "lehiʃtaʿel",
                # hebrew_word_nikud
                "‬‫לְהִשתַעֵל‬"
            ),
            (
                # translation_word
                "упасть в обморок",
                # pronunciation_word
                "lehitʿalef",
                # hebrew_word_nikud
                "‫לְהִתעַלֵף‬‬"
            ),
            (
                # translation_word
                "ушиб",
                # pronunciation_word
                "maka",
                # hebrew_word_nikud
                "‬‫מַכָּה‬"
            ),
            (
                # translation_word
                "удариться",
                # pronunciation_word
                "lekabel maka",
                # hebrew_word_nikud
                "‬לְקַבֵּל‬ ‫מַכָּה‬"
            ),
            (
                # translation_word
                "вывих",
                # pronunciation_word
                "'neka",
                # hebrew_word_nikud
                "‫נֶקַע‬‬"
            ),
            (
                # translation_word
                "получить перелом",
                # pronunciation_word
                "liʃbor",
                # hebrew_word_nikud
                "‫לִשבּוֹר‬‬"
            ),
            (
                # translation_word
                "перелом",
                # pronunciation_word
                "'ʃever",
                # hebrew_word_nikud
                "‫שֶבֶר‬‬"
            ),
            (
                # translation_word
                "порез",
                # pronunciation_word
                "χataχ",
                # hebrew_word_nikud
                "‬‫חֲתָך‬"
            ),
            (
                # translation_word
                "порезаться",
                # pronunciation_word
                "lehiχateχ",
                # hebrew_word_nikud
                "‫לְהֵיחָתֵך‬‬"
            ),
            (
                # translation_word
                "кровотечение",
                # pronunciation_word
                "dimum",
                # hebrew_word_nikud
                "‫דִימוּם‬‬"
            ),
            (
                # translation_word
                "ожог",
                # pronunciation_word
                "kviya",
                # hebrew_word_nikud
                "‬‫כּווִייָה‬"
            ),
            (
                # translation_word
                "обжечься",
                # pronunciation_word
                "laχatof kviya",
                # hebrew_word_nikud
                "לַחֲטוֹף‬ ‫כּווִייָה‬‬"
            ),
            (
                # translation_word
                "травма",
                # pronunciation_word
                "'traʾuma",
                # hebrew_word_nikud
                "‫טרָאוּמָה‬‬"
            ),
            (
                # translation_word
                "солнечный удар",
                # pronunciation_word
                "makat 'ʃemeʃ",
                # hebrew_word_nikud
                "‬מַכַּת‬ ‫שֶמֶש‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "73. Симптомы болезней. Лечение - 2",
        # words
        [
            (
                # translation_word
                "боль",
                # pronunciation_word
                "keʾev",
                # hebrew_word_nikud
                "‬‫כְּאֵב‬"
            ),
            (
                # translation_word
                "заноза",
                # pronunciation_word
                "koʦ",
                # hebrew_word_nikud
                "‫קוֹץ‬‬"
            ),
            (
                # translation_word
                "пот",
                # pronunciation_word
                "zeʿa",
                # hebrew_word_nikud
                "‫זֵיעָה‬‬"
            ),
            (
                # translation_word
                "потеть",
                # pronunciation_word
                "leha'ziʿa",
                # hebrew_word_nikud
                "‫לְהַזִיע‬‬"
            ),
            (
                # translation_word
                "рвота",
                # pronunciation_word
                "hakaʾa",
                # hebrew_word_nikud
                "‫הֲקָאָה‬‬"
            ),
            (
                # translation_word
                "судороги",
                # pronunciation_word
                "pirkusim",
                # hebrew_word_nikud
                "‫פִּירכּוּסִים‬‬"
            ),
            (
                # translation_word
                "беременная",
                # pronunciation_word
                "hara",
                # hebrew_word_nikud
                "‫הָרָה‬‬"
            ),
            (
                # translation_word
                "родиться",
                # pronunciation_word
                "lehivaled",
                # hebrew_word_nikud
                "‫לְהִיווָלֵד‬"
            ),
            (
                # translation_word
                "роды",
                # pronunciation_word
                "leda",
                # hebrew_word_nikud
                "‫לֵידָה‬‬"
            ),
            (
                # translation_word
                "рожать",
                # pronunciation_word
                "la'ledet",
                # hebrew_word_nikud
                "‫לָלֶדֶת‬‬"
            ),
            (
                # translation_word
                "аборт",
                # pronunciation_word
                "hapala",
                # hebrew_word_nikud
                "‬‫הַפָּלָה‬"
            ),
            (
                # translation_word
                "дыхание",
                # pronunciation_word
                "neʃima",
                # hebrew_word_nikud
                "‫נְשִימָה‬‬"
            ),
            (
                # translation_word
                "выдохнуть",
                # pronunciation_word
                "linʃof",
                # hebrew_word_nikud
                "‬‫לִנשוֹף‬"
            ),
            (
                # translation_word
                "вдыхать",
                # pronunciation_word
                "liʃʾof",
                # hebrew_word_nikud
                "‬‫לִשאוֹף‬"
            ),
            (
                # translation_word
                "инвалид",
                # pronunciation_word
                "naχe",
                # hebrew_word_nikud
                "‫נָכֶה‬‬"
            ),
            (
                # translation_word
                "наркоман",
                # pronunciation_word
                "narkoman",
                # hebrew_word_nikud
                "‬‫נַרקוֹמָן‬"
            ),
            (
                # translation_word
                "глухонемой",
                # pronunciation_word
                "χereʃ-ilem",
                # hebrew_word_nikud
                "‬‫חֵירֵש־אִילֵם‬"
            ),
            (
                # translation_word
                "сумасшедший",
                # pronunciation_word
                "meʃuga",
                # hebrew_word_nikud
                "‫מְשוּגָע‬‬"
            ),
            (
                # translation_word
                "ген",
                # pronunciation_word
                "gen",
                # hebrew_word_nikud
                "‫גֶן‬‬"
            ),
            (
                # translation_word
                "иммунитет",
                # pronunciation_word
                "χasinut",
                # hebrew_word_nikud
                "‫חֲסִינוּת‬‬"
            ),
            (
                # translation_word
                "наследственный",
                # pronunciation_word
                "toraʃti",
                # hebrew_word_nikud
                "‫תוֹרַשתִי‬‬"
            ),
            (
                # translation_word
                "вирус",
                # pronunciation_word
                "'virus",
                # hebrew_word_nikud
                "‫וִירוּס‬‬"
            ),
            (
                # translation_word
                "микроб",
                # pronunciation_word
                "χaidak",
                # hebrew_word_nikud
                "‬‫חַיידַק‬"
            ),
            (
                # translation_word
                "бактерия",
                # pronunciation_word
                "bak'terya",
                # hebrew_word_nikud
                "‫בַּקטֶריָה‬‬"
            ),
            (
                # translation_word
                "инфекция",
                # pronunciation_word
                "zihum",
                # hebrew_word_nikud
                "‫זִיהוּם‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "74. Симптомы болезней. Лечение - 3",
        # words
        [
            (
                # translation_word
                "больница",
                # pronunciation_word
                "beit χolim",
                # hebrew_word_nikud
                "בֵּית‬ ‫חוֹלִים‬‬"
            ),
            (
                # translation_word
                "пациент",
                # pronunciation_word
                "metupal",
                # hebrew_word_nikud
                "‬‫מְטוּפָּל‬"
            ),
            (
                # translation_word
                "диагноз",
                # pronunciation_word
                "avχana",
                # hebrew_word_nikud
                "‫אַבחָנָה‬‬"
            ),
            (
                # translation_word
                "лечение",
                # pronunciation_word
                "ripui",
                # hebrew_word_nikud
                "‫רִיפּוּי‬‬"
            ),
            (
                # translation_word
                "лечиться",
                # pronunciation_word
                "lekabel tipul",
                # hebrew_word_nikud
                "לְקַבֵּל‬ ‫טִיפּוּל‬‬"
            ),
            (
                # translation_word
                "операция (мед.)",
                # pronunciation_word
                "ni'tuaχ",
                # hebrew_word_nikud
                "‬‫נִיתוּח‬"
            ),
            (
                # translation_word
                "перевязать",
                # pronunciation_word
                "laχboʃ",
                # hebrew_word_nikud
                "‫לַחבּוֹש‬‬"
            ),
            (
                # translation_word
                "прививка",
                # pronunciation_word
                "χisun",
                # hebrew_word_nikud
                "‫חִיסוּן‬‬"
            ),
            (
                # translation_word
                "делать прививку",
                # pronunciation_word
                "leχasen",
                # hebrew_word_nikud
                "‬‫לְחַסֵן‬"
            ),
            (
                # translation_word
                "делать укол (кому-л.)",
                # pronunciation_word
                "lehazrik",
                # hebrew_word_nikud
                "‫לְהַזרִיק‬‬"
            ),
            (
                # translation_word
                "ампутация",
                # pronunciation_word
                "ktiʿa",
                # hebrew_word_nikud
                "‫קטִיעָה‬‬"
            ),
            (
                # translation_word
                "быть в коме",
                # pronunciation_word
                "lihyot betar'demet",
                # hebrew_word_nikud
                "לִהיוֹת‬ ‫בְּתַרדֶמֶת‬‬"
            ),
            (
                # translation_word
                "реанимация",
                # pronunciation_word
                "tipul nimraʦ",
                # hebrew_word_nikud
                "טִיפּוּל‬ ‫נִמרָץ‬‬"
            ),
            (
                # translation_word
                "выздоравливать",
                # pronunciation_word
                "lehaχlim",
                # hebrew_word_nikud
                "‬‫לְהַחלִים‬"
            ),
            (
                # translation_word
                "память",
                # pronunciation_word
                "zikaron",
                # hebrew_word_nikud
                "‬‫זִיכָּרוֹן‬"
            ),
            (
                # translation_word
                "удалять (зуб)",
                # pronunciation_word
                "laʿakor",
                # hebrew_word_nikud
                "‫לַעֲקוֹר‬"
            ),
            (
                # translation_word
                "пломбировать (зубы)",
                # pronunciation_word
                "laʿasot stima",
                # hebrew_word_nikud
                "לַעֲשׂוֹת‬ ‫סתִימָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "75. Врачи",
        # words
        [
            (
                # translation_word
                "врач",
                # pronunciation_word
                "rofe",
                # hebrew_word_nikud
                "‫רוֹפֵא‬‬"
            ),
            (
                # translation_word
                "медсестра",
                # pronunciation_word
                "aχot",
                # hebrew_word_nikud
                "‫אָחוֹת‬‬"
            ),
            (
                # translation_word
                "личный врач",
                # pronunciation_word
                "rofe iʃi",
                # hebrew_word_nikud
                "רוֹפֵא‬ ‫אִישִי‬‬"
            ),
            (
                # translation_word
                "стоматолог",
                # pronunciation_word
                "rofe ʃi'nayim",
                # hebrew_word_nikud
                "רוֹפֵא‬ ‫שִינַיִים‬‬"
            ),
            (
                # translation_word
                "окулист",
                # pronunciation_word
                "rofe ei'nayim",
                # hebrew_word_nikud
                "‬רוֹפֵא‬ ‫עֵינַיִים‬"
            ),
            (
                # translation_word
                "терапевт",
                # pronunciation_word
                "rofe pnimi",
                # hebrew_word_nikud
                "‬רוֹפֵא‬ ‫פּנִימִי‬"
            ),
            (
                # translation_word
                "хирург",
                # pronunciation_word
                "kirurg",
                # hebrew_word_nikud
                "‫כִּירוּרג‬‬"
            ),
            (
                # translation_word
                "психиатр",
                # pronunciation_word
                "psiχi'ʾater",
                # hebrew_word_nikud
                "‫פּסִיכִיאָטֶר‬‬"
            ),
            (
                # translation_word
                "педиатр",
                # pronunciation_word
                "rofe yeladim",
                # hebrew_word_nikud
                "‬רוֹפֵא‬ ‫יְלָדִים‬"
            ),
            (
                # translation_word
                "психолог",
                # pronunciation_word
                "psiχolog",
                # hebrew_word_nikud
                "‬‫פּסִיכוֹלוֹג‬"
            ),
            (
                # translation_word
                "гинеколог",
                # pronunciation_word
                "rofe naʃim",
                # hebrew_word_nikud
                "רוֹפֵא‬ ‫נָשִים‬‬"
            ),
            (
                # translation_word
                "кардиолог",
                # pronunciation_word
                "kardyolog",
                # hebrew_word_nikud
                "‫קַרדיוֹלוֹג‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "76. Лекарства. Принадлежности",
        # words
        [
            (
                # translation_word
                "лекарство",
                # pronunciation_word
                "trufa",
                # hebrew_word_nikud
                "‫תרוּפָה‬‬"
            ),
            (
                # translation_word
                "прописать (лекарство)",
                # pronunciation_word
                "lirʃom",
                # hebrew_word_nikud
                "‫לִרשוֹם‬‬"
            ),
            (
                # translation_word
                "рецепт",
                # pronunciation_word
                "mirʃam",
                # hebrew_word_nikud
                "‫מִרשָם‬‬"
            ),
            (
                # translation_word
                "таблетка",
                # pronunciation_word
                "kadur",
                # hebrew_word_nikud
                "‬‫כַּדוּר‬"
            ),
            (
                # translation_word
                "мазь",
                # pronunciation_word
                "miʃχa",
                # hebrew_word_nikud
                "‫מִשחָה‬‬"
            ),
            (
                # translation_word
                "ампула",
                # pronunciation_word
                "'ampula",
                # hebrew_word_nikud
                "‬‫אַמפּוּלָה‬"
            ),
            (
                # translation_word
                "порошок",
                # pronunciation_word
                "avka",
                # hebrew_word_nikud
                "‬‫אַבקָה‬"
            ),
            (
                # translation_word
                "бинт",
                # pronunciation_word
                "taχ'boʃet 'gaza",
                # hebrew_word_nikud
                "‬תַחבּוֹשֶת‬ ‫גָאזָה‬"
            ),
            (
                # translation_word
                "вата",
                # pronunciation_word
                "'gefen 'ʦemer",
                # hebrew_word_nikud
                "צֶמֶר‬ ‫גֶפֶן‬‬"
            ),
            (
                # translation_word
                "йод",
                # pronunciation_word
                "yod",
                # hebrew_word_nikud
                "‫יוֹד‬‬"
            ),
            (
                # translation_word
                "лейкопластырь",
                # pronunciation_word
                "'plaster",
                # hebrew_word_nikud
                "‫פּלַסטֶר‬‬"
            ),
            (
                # translation_word
                "градусник",
                # pronunciation_word
                "madχom",
                # hebrew_word_nikud
                "‬‫מַדחוֹם‬"
            ),
            (
                # translation_word
                "шприц",
                # pronunciation_word
                "mazrek",
                # hebrew_word_nikud
                "‫מַזרֵק‬‬"
            ),
            (
                # translation_word
                "инвалидная коляска",
                # pronunciation_word
                "kise galgalim",
                # hebrew_word_nikud
                "כִּיסֵא‬ ‫גַלגַלִים‬‬"
            ),
            (
                # translation_word
                "обезболивающее",
                # pronunciation_word
                "meʃakeχ keʾevim",
                # hebrew_word_nikud
                "מְשַכֵּך‬ ‫כְּאֵבִים‬‬"
            ),
            (
                # translation_word
                "слабительное",
                # pronunciation_word
                "trufa meʃal'ʃelet",
                # hebrew_word_nikud
                "תרוּפָה‬ ‫מְשַלשֶלֶת‬‬"
            ),
            (
                # translation_word
                "спирт",
                # pronunciation_word
                "'kohal",
                # hebrew_word_nikud
                "‬‫כּוֹהַל‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "77. Курение. Табачные изделия",
        # words
        [
            (
                # translation_word
                "табак",
                # pronunciation_word
                "'tabak",
                # hebrew_word_nikud
                "‬‫טַבָּק‬"
            ),
            (
                # translation_word
                "сигарета",
                # pronunciation_word
                "si'garya",
                # hebrew_word_nikud
                "‫סִיגַריָה‬‬"
            ),
            (
                # translation_word
                "сигара",
                # pronunciation_word
                "sigar",
                # hebrew_word_nikud
                "‬‫סִיגָר‬"
            ),
            (
                # translation_word
                "трубка",
                # pronunciation_word
                "mik'teret",
                # hebrew_word_nikud
                "‫מִקטֶרֶת‬‬"
            ),
            (
                # translation_word
                "спички",
                # pronunciation_word
                "gafrurim",
                # hebrew_word_nikud
                "‬‫גַפרוּרים‬"
            ),
            (
                # translation_word
                "зажигалка",
                # pronunciation_word
                "maʦit",
                # hebrew_word_nikud
                "‫מַצִית‬‬"
            ),
            (
                # translation_word
                "курить",
                # pronunciation_word
                "leʿaʃen",
                # hebrew_word_nikud
                "‫לְעַשֵן‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "78. Город. Жизнь в городе",
        # words
        [
            (
                # translation_word
                "город",
                # pronunciation_word
                "ir",
                # hebrew_word_nikud
                "‬‫עִיר‬"
            ),
            (
                # translation_word
                "столица",
                # pronunciation_word
                "ir bira",
                # hebrew_word_nikud
                "עִיר‬‬ ‫בִּירָה‬‬"
            ),
            (
                # translation_word
                "деревня",
                # pronunciation_word
                "kfar",
                # hebrew_word_nikud
                "‬‫כּפָר‬"
            ),
            (
                # translation_word
                "центр города",
                # pronunciation_word
                "merkaz haʿir",
                # hebrew_word_nikud
                "מֶרכַּז‬‬ ‫הָעִיר‬‬"
            ),
            (
                # translation_word
                "пригород",
                # pronunciation_word
                "parvar",
                # hebrew_word_nikud
                "‬‫פַּרווָר‬"
            ),
            (
                # translation_word
                "квартал",
                # pronunciation_word
                "ʃχuna",
                # hebrew_word_nikud
                "‬‫שכוּנָה‬"
            ),
            (
                # translation_word
                "уличное движение",
                # pronunciation_word
                "tnuʿa",
                # hebrew_word_nikud
                "‬‫תנוּעָה‬"
            ),
            (
                # translation_word
                "светофор",
                # pronunciation_word
                "ramzor",
                # hebrew_word_nikud
                "‬‫רַמזוֹר‬"
            ),
            (
                # translation_word
                "городской транспорт",
                # pronunciation_word
                "taχbura ʦiburit",
                # hebrew_word_nikud
                "‬תַחבּוּרָה‬‬ ‫צִיבּוּרִית‬"
            ),
            (
                # translation_word
                "перекрёсток",
                # pronunciation_word
                "'ʦomet",
                # hebrew_word_nikud
                "‬‫צוֹמֶת‬"
            ),
            (
                # translation_word
                "пешеходный переход",
                # pronunciation_word
                "maʿavar χaʦaya",
                # hebrew_word_nikud
                "מַעֲבַר‬‬ ‫חֲצָיָה‬‬"
            ),
            (
                # translation_word
                "переходить (улицу)",
                # pronunciation_word
                "laχaʦot",
                # hebrew_word_nikud
                "‫לַחֲצוֹת‬‬"
            ),
            (
                # translation_word
                "пешеход",
                # pronunciation_word
                "holeχ 'regel",
                # hebrew_word_nikud
                "‬הוֹלֵך‬‬ ‫רֶגֶל‬"
            ),
            (
                # translation_word
                "тротуар",
                # pronunciation_word
                "midraχa",
                # hebrew_word_nikud
                "‫מִדרָכָה‬‬"
            ),
            (
                # translation_word
                "мост",
                # pronunciation_word
                "'geʃer",
                # hebrew_word_nikud
                "‫גֶשֶר‬‬"
            ),
            (
                # translation_word
                "фонтан",
                # pronunciation_word
                "mizraka",
                # hebrew_word_nikud
                "‫מִזרָקָה‬‬"
            ),
            (
                # translation_word
                "аллея",
                # pronunciation_word
                "sdera",
                # hebrew_word_nikud
                "‫שׂדֵרָה‬‬"
            ),
            (
                # translation_word
                "парк",
                # pronunciation_word
                "park",
                # hebrew_word_nikud
                "‫פַּארק‬‬"
            ),
            (
                # translation_word
                "площадь",
                # pronunciation_word
                "kikar",
                # hebrew_word_nikud
                "‫כִּיכָּר‬‬"
            ),
            (
                # translation_word
                "проспект",
                # pronunciation_word
                "reχov raʃi",
                # hebrew_word_nikud
                "רְחוֹב‬‬ ‫רָאשִי‬‬"
            ),
            (
                # translation_word
                "улица",
                # pronunciation_word
                "reχov",
                # hebrew_word_nikud
                "‫רְחוֹב‬‬"
            ),
            (
                # translation_word
                "дом",
                # pronunciation_word
                "'bayit",
                # hebrew_word_nikud
                "‬‫בַּיִת‬"
            ),
            (
                # translation_word
                "здание",
                # pronunciation_word
                "binyan",
                # hebrew_word_nikud
                "‬‫בִּנייָן‬"
            ),
            (
                # translation_word
                "небоскрёб",
                # pronunciation_word
                "gored ʃχakim",
                # hebrew_word_nikud
                "גוֹרֵד‬‬ ‫שחָקִים‬‬"
            ),
            (
                # translation_word
                "крыша",
                # pronunciation_word
                "gag",
                # hebrew_word_nikud
                "‬‫גַג‬"
            ),
            (
                # translation_word
                "витрина",
                # pronunciation_word
                "χalon raʾava",
                # hebrew_word_nikud
                "חַלוֹן‬ ‬‫רַאֲווָה‬‬"
            ),
            (
                # translation_word
                "афиша",
                # pronunciation_word
                "kraza",
                # hebrew_word_nikud
                "‬‫כּרָזָה‬"
            ),
            (
                # translation_word
                "рекламный плакат",
                # pronunciation_word
                "'poster",
                # hebrew_word_nikud
                "‫פּוֹסטֶר‬‬"
            ),
            (
                # translation_word
                "мусор",
                # pronunciation_word
                "'zevel",
                # hebrew_word_nikud
                "‫זֶבֶל‬‬"
            ),
            (
                # translation_word
                "урна (для мусора)",
                # pronunciation_word
                "paχ aʃpa",
                # hebrew_word_nikud
                "‬פַּח‬ ‬‫אַשפָּה‬"
            ),
            (
                # translation_word
                "скамейка",
                # pronunciation_word
                "safsal",
                # hebrew_word_nikud
                "‫סַפסָל‬‬"
            ),
            (
                # translation_word
                "полиция",
                # pronunciation_word
                "miʃtara",
                # hebrew_word_nikud
                "‫מִשטָרָה‬‬"
            ),
            (
                # translation_word
                "полицейский",
                # pronunciation_word
                "ʃoter",
                # hebrew_word_nikud
                "‫שוֹטֵר‬‬"
            ),
            (
                # translation_word
                "нищий (бродяга)",
                # pronunciation_word
                "kabʦan",
                # hebrew_word_nikud
                "‫קַבּצָן‬‬"
            ),
            (
                # translation_word
                "бездомный",
                # pronunciation_word
                "χasar 'bayit",
                # hebrew_word_nikud
                "‬חֲסַר‬ ‬‫בַּיִת‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "79. Городские учреждения",
        # words
        [
            (
                # translation_word
                "магазин",
                # pronunciation_word
                "χanut",
                # hebrew_word_nikud
                "‫חֲנוּת‬‬"
            ),
            (
                # translation_word
                "аптека",
                # pronunciation_word
                "beit mir'kaχat",
                # hebrew_word_nikud
                "‬בֵּית‬ ‬‫מִרקַחַת‬"
            ),
            (
                # translation_word
                "торговый центр",
                # pronunciation_word
                "kanyon",
                # hebrew_word_nikud
                "‬‫קַניוֹן‬"
            ),
            (
                # translation_word
                "супермаркет",
                # pronunciation_word
                "super'market",
                # hebrew_word_nikud
                "‫סוּפֶּרמַרקֶט‬‬"
            ),
            (
                # translation_word
                "булочная",
                # pronunciation_word
                "maʾafiya",
                # hebrew_word_nikud
                "‫מַאֲפִייָה‬‬"
            ),
            (
                # translation_word
                "кондитерская",
                # pronunciation_word
                "χanut mamtakim",
                # hebrew_word_nikud
                "חֲנוּת‬ ‬‫מַמתָקִים‬‬"
            ),
            (
                # translation_word
                "продуктовый магазин",
                # pronunciation_word
                "ma'kolet",
                # hebrew_word_nikud
                "‫מַכּוֹלֶת‬‬"
            ),
            (
                # translation_word
                "мясная лавка",
                # pronunciation_word
                "itliz",
                # hebrew_word_nikud
                "‫אִטלִיז‬‬"
            ),
            (
                # translation_word
                "рынок",
                # pronunciation_word
                "ʃuk",
                # hebrew_word_nikud
                "‫שוּק‬‬"
            ),
            (
                # translation_word
                "кофейня",
                # pronunciation_word
                "beit kafe",
                # hebrew_word_nikud
                "בֵּית‬ ‬‫קָפֶה‬‬"
            ),
            (
                # translation_word
                "ресторан",
                # pronunciation_word
                "misʿada",
                # hebrew_word_nikud
                "‫מִסעָדָה‬‬"
            ),
            (
                # translation_word
                "пивная",
                # pronunciation_word
                "pab",
                # hebrew_word_nikud
                "‬‫פָּאב‬"
            ),
            (
                # translation_word
                "пиццерия",
                # pronunciation_word
                "pi'ʦeriya",
                # hebrew_word_nikud
                "‫פִּיצֶרִייָה‬‬"
            ),
            (
                # translation_word
                "парикмахерская",
                # pronunciation_word
                "mispara",
                # hebrew_word_nikud
                "‬‫מִספָּרָה‬"
            ),
            (
                # translation_word
                "почта",
                # pronunciation_word
                "'doʾar",
                # hebrew_word_nikud
                "‫דוֹאַר‬‬"
            ),
            (
                # translation_word
                "химчистка",
                # pronunciation_word
                "nikui yaveʃ",
                # hebrew_word_nikud
                "נִיקוּי‬‬ ‫יָבֵש‬‬"
            ),
            (
                # translation_word
                "обувной магазин",
                # pronunciation_word
                "χanut naʿa'layim",
                # hebrew_word_nikud
                "חֲנוּת‬‬ ‫נַעֲלַיִים‬‬"
            ),
            (
                # translation_word
                "книжный магазин",
                # pronunciation_word
                "χanut sfarim",
                # hebrew_word_nikud
                "חֲנוּת‬‬ ‫ספָרִים‬‬"
            ),
            (
                # translation_word
                "ремонт одежды",
                # pronunciation_word
                "χanut tikun bgadim",
                # hebrew_word_nikud
                "חֲנוּת‬‬ ‫תִיקוּן‬ ‫בּגָדִים‬‬"
            ),
            (
                # translation_word
                "цирк",
                # pronunciation_word
                "kirkas",
                # hebrew_word_nikud
                "‫קִרקָס‬‬"
            ),
               (
                # translation_word
                "зоопарк",
                # pronunciation_word
                "gan hayot",
                # hebrew_word_nikud
                "‬גַן‬ ‬‫חַיוֹת‬"
            ),
            (
                # translation_word
                "кинотеатр",
                # pronunciation_word
                "kol'noʿa",
                # hebrew_word_nikud
                "‬ַ‫קוֹלנוֹע‬"
            ),
               (
                # translation_word
                "музей",
                # pronunciation_word
                "muzeʾon",
                # hebrew_word_nikud
                "‫מוּזֵיאוֹן‬‬"
            ),
            (
                # translation_word
                "библиотека",
                # pronunciation_word
                "sifriya",
                # hebrew_word_nikud
                "‬‫סִפרִייָה‬"
            ),
               (
                # translation_word
                "театр",
                # pronunciation_word
                "teʾatron",
                # hebrew_word_nikud
                "‫תֵיאַטרוֹן‬‬"
            ),
            (
                # translation_word
                "опера",
                # pronunciation_word
                "beit 'opera",
                # hebrew_word_nikud
                "בֵּית‬‬ ‫אוֹפֶּרָה‬‬"
            ),
               (
                # translation_word
                "ночной клуб",
                # pronunciation_word
                "moʿadon 'laila",
                # hebrew_word_nikud
                "מוֹעֲדוֹן‬‬ ‫לַילָה‬‬"
            ),
            (
                # translation_word
                "мечеть",
                # pronunciation_word
                "misgad",
                # hebrew_word_nikud
                "‬‫מִסגָד‬"
            ),
               (
                # translation_word
                "синагога",
                # pronunciation_word
                "beit 'kneset",
                # hebrew_word_nikud
                "בֵּית‬‬ ‫כּנֶסֶת‬‬"
            ),
            (
                # translation_word
                "собор",
                # pronunciation_word
                "kated'rala",
                # hebrew_word_nikud
                "‫קָתֶדרָלָה‬‬"
            ),
               (
                # translation_word
                "церковь",
                # pronunciation_word
                "knesiya",
                # hebrew_word_nikud
                "‬‫כּנֵסִייָה‬"
            ),
            (
                # translation_word
                "институт",
                # pronunciation_word
                "miχlala",
                # hebrew_word_nikud
                "‫מִכלָלָה‬‬"
            ),
               (
                # translation_word
                "университет",
                # pronunciation_word
                "uni'versita",
                # hebrew_word_nikud
                "‬‫אוּנִיבֶרסִיטָה‬"
            ),
            (
                # translation_word
                "школа",
                # pronunciation_word
                "beit 'sefer",
                # hebrew_word_nikud
                "בֵּית‬‬ ‫סֵפֶר‬‬"
            ),
               (
                # translation_word
                "мэрия",
                # pronunciation_word
                "iriya",
                # hebrew_word_nikud
                "‫עִירִייָה‬‬"
            ),
            (
                # translation_word
                "гостиница",
                # pronunciation_word
                "beit malon",
                # hebrew_word_nikud
                "‬בֵּית‬‬ ‫מָלוֹן‬"
            ),
               (
                # translation_word
                "банк",
                # pronunciation_word
                "bank",
                # hebrew_word_nikud
                "‫בַּנק‬‬"
            ),
            (
                # translation_word
                "посольство",
                # pronunciation_word
                "ʃagrirut",
                # hebrew_word_nikud
                "‫שַגרִירוּת‬‬"
            ),
               (
                # translation_word
                "турагентство",
                # pronunciation_word
                "soχnut nesiʿot",
                # hebrew_word_nikud
                "סוֹכנוּת‬‬ ‫נְסִיעוֹת‬‬"
            ),
            (
                # translation_word
                "справочное бюро",
                # pronunciation_word
                "modiʿin",
                # hebrew_word_nikud
                "‫מוֹדִיעִין‬‬"
            ),
               (
                # translation_word
                "обменный пункт",
                # pronunciation_word
                "misrad hamarat mat'beʿa",
                # hebrew_word_nikud
                "מִשׂרַד‬‬ ‫הֲמָרַת‬ ַ‫מַטבֵּע‬‬"
            ),
            (
                # translation_word
                "метро",
                # pronunciation_word
                "ra'kevet taχtit",
                # hebrew_word_nikud
                "רַכֶּבֶת‬‬ ‫תַחתִית‬‬"
            ),
               (
                # translation_word
                "больница",
                # pronunciation_word
                "beit χolim",
                # hebrew_word_nikud
                "בֵּית‬‬ ‫חוֹלִים‬"
            ),
            (
                # translation_word
                "автозаправка",
                # pronunciation_word
                "taχanat 'delek",
                # hebrew_word_nikud
                "תַחֲנַת‬ ‬‫דֶלֶק‬‬"
            ),
            (
                # translation_word
                "автостоянка",
                # pronunciation_word
                "migraʃ χanaya",
                # hebrew_word_nikud
                "מִגרַש‬ ‬‫חֲנָיָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "80. Вывески. Указатели",
        # words
        [
            (
                # translation_word
                "вывеска",
                # pronunciation_word
                "'ʃelet",
                # hebrew_word_nikud
                "‫שֶלֶט‬‬"
            ),
            (
                # translation_word
                "надпись",
                # pronunciation_word
                "modaʿa",
                # hebrew_word_nikud
                "‫מוֹדָעָה‬‬"
            ),
            (
                # translation_word
                "указатель",
                # pronunciation_word
                "tamrur",
                # hebrew_word_nikud
                "‫תַמרוּר‬‬"
            ),
            (
                # translation_word
                "предупреждение",
                # pronunciation_word
                "'ʃelet azhara",
                # hebrew_word_nikud
                "שֶלֶט‬‬‬ ‫אַזהָרָה‬‬"
            ),
            (
                # translation_word
                "выходной день",
                # pronunciation_word
                "yom 'χofeʃ",
                # hebrew_word_nikud
                "‬יוֹם‬‬‬ ‫חוֹפֶש‬"
            ),
            (
                # translation_word
                "расписание",
                # pronunciation_word
                "'luaχ zmanim",
                # hebrew_word_nikud
                "‬לוּח‬‬‬ ‫זמַנִים‬"
            ),
            (
                # translation_word
                "часы работы",
                # pronunciation_word
                "ʃaʿot avoda",
                # hebrew_word_nikud
                "שָעוֹת‬‬‬ ‫עֲבוֹדָה‬‬"
            ),
            (
                # translation_word
                "ДОБРО ПОЖАЛОВАТЬ!",
                # pronunciation_word
                "bruχim habaʾim!",
                # hebrew_word_nikud
                "‬בּרוּכִים‬‬‬ ‫הַבָּאִים‬"
            ),
            (
                # translation_word
                "ВХОД",
                # pronunciation_word
                "knisa",
                # hebrew_word_nikud
                "‫כּנִיסָה‬‬"
            ),
            (
                # translation_word
                "ВЫХОД",
                # pronunciation_word
                "yeʦiʾa",
                # hebrew_word_nikud
                "‬‫יְצִיאָה‬"
            ),
            (
                # translation_word
                "ОТКРЫТО",
                # pronunciation_word
                "pa'tuaχ",
                # hebrew_word_nikud
                "‬‫פָּתוּח‬"
            ),
            (
                # translation_word
                "ЗАКРЫТО",
                # pronunciation_word
                "sagur",
                # hebrew_word_nikud
                "‫סָגוּר‬‬"
            ),
            (
                # translation_word
                "ДЛЯ ЖЕНЩИН",
                # pronunciation_word
                "lenaʃim",
                # hebrew_word_nikud
                "‫לְנָשִים‬‬"
            ),
            (
                # translation_word
                "ДЛЯ МУЖЧИН",
                # pronunciation_word
                "legvarim",
                # hebrew_word_nikud
                "‫לְגבָרִים‬‬"
            ),
            (
                # translation_word
                "СКИДКИ",
                # pronunciation_word
                "hanaχot",
                # hebrew_word_nikud
                "‬‫הֲנָחוֹת‬"
            ),
            (
                # translation_word
                "РАСПРОДАЖА",
                # pronunciation_word
                "mivʦa",
                # hebrew_word_nikud
                "‬‫מִבצָע‬"
            ),
            (
                # translation_word
                "БЕСПЛАТНО",
                # pronunciation_word
                "χinam",
                # hebrew_word_nikud
                "‫חִינָם‬‬"
            ),
            (
                # translation_word
                "ВНИМАНИЕ!",
                # pronunciation_word
                "sim lev!",
                # hebrew_word_nikud
                "שִׂים‬‬‬ ‫לֵב‬‬"
            ),
            (
                # translation_word
                "ЗАРЕЗЕРВИРОВАНО",
                # pronunciation_word
                "ʃamur",
                # hebrew_word_nikud
                "‬‫שָמוּר‬"
            ),
            (
                # translation_word
                "АДМИНИСТРАЦИЯ",
                # pronunciation_word
                "hanhala",
                # hebrew_word_nikud
                "‬‫הַנהָלָה‬"
            ),
            (
                # translation_word
                "ОПАСНО",
                # pronunciation_word
                "mesukan",
                # hebrew_word_nikud
                "‫מְסוּכָּן‬‬"
            ),
            (
                # translation_word
                "КУПАТЬСЯ ЗАПРЕЩЕНО",
                # pronunciation_word
                "haraχaʦa asura!",
                # hebrew_word_nikud
                "הָרַחֲצָה‬‬‬ ‫אָסוּרָה‬‬"
            ),
            (
                # translation_word
                "ОГНЕОПАСНО",
                # pronunciation_word
                "dalik",
                # hebrew_word_nikud
                "‫דָלִיק‬‬"
            ),
            (
                # translation_word
                "ЗАПРЕЩЕНО",
                # pronunciation_word
                "asur",
                # hebrew_word_nikud
                "‫אָסוּר‬‬"
            ),
            (
                # translation_word
                "ОКРАШЕНО",
                # pronunciation_word
                "'ʦeva laχ",
                # hebrew_word_nikud
                "‬צֶבַע‬‬‬ ‫לַח‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "81. Городской транспорт",
        # words
        [
            (
                # translation_word
                "автобус",
                # pronunciation_word
                "'otobus",
                # hebrew_word_nikud
                "‬‫אוֹטוֹבּוּס‬"
            ),
            (
                # translation_word
                "трамвай",
                # pronunciation_word
                "ra'kevet kala",
                # hebrew_word_nikud
                "‬רַכֶּבֶת‬‬‬ ‫קַלָה‬"
            ),
            (
                # translation_word
                "троллейбус",
                # pronunciation_word
                "tro'leibus",
                # hebrew_word_nikud
                "‬‫טרוֹלֵיבּוּס‬"
            ),
            (
                # translation_word
                "маршрут",
                # pronunciation_word
                "maslul",
                # hebrew_word_nikud
                "‫מַסלוּל‬‬"
            ),
            (
                # translation_word
                "номер (напр. автобуса)",
                # pronunciation_word
                "mispar",
                # hebrew_word_nikud
                "‫מִספָּר‬‬"
            ),
            (
                # translation_word
                "ехать на",
                # pronunciation_word
                "lin'soʿa be",
                # hebrew_word_nikud
                "לִנסוֹע‬‬‬ ְּ‫ב‬‬"
            ),
            (
                # translation_word
                "сесть (в автобус и т.п.)",
                # pronunciation_word
                "laʿalot",
                # hebrew_word_nikud
                "‫לַעֲלוֹת‬‬"
            ),
            (
                # translation_word
                "сойти (с автобуса и т.п.)",
                # pronunciation_word
                "la'redet mi",
                # hebrew_word_nikud
                "לָרֶדֶת‬‬‬ ‫מ‬‬"
            ),
            (
                # translation_word
                "остановка",
                # pronunciation_word
                "taχana",
                # hebrew_word_nikud
                "‫תַחֲנָה‬‬"
            ),
            (
                # translation_word
                "следующая остановка",
                # pronunciation_word
                "hataχana habaʾa",
                # hebrew_word_nikud
                "‬הַתַחֲנָה‬‬‬ ‫הַבָּאָה‬"
            ),
            (
                # translation_word
                "конечная остановка",
                # pronunciation_word
                "hataχana haʾaχrona",
                # hebrew_word_nikud
                "הַתַחֲנָה‬‬‬ ‫הָאַחרוֹנָה‬‬"
            ),
            (
                # translation_word
                "ждать",
                # pronunciation_word
                "lehamtin",
                # hebrew_word_nikud
                "‬‫לְהַמתִין‬"
            ),
            (
                # translation_word
                "билет",
                # pronunciation_word
                "kartis",
                # hebrew_word_nikud
                "‫כַּרטִיס‬‬"
            ),
            (
                # translation_word
                "стоимость билета",
                # pronunciation_word
                "meχir hanesiya",
                # hebrew_word_nikud
                "מְחִיר‬‬‬ ‫הַנְסִיעָה‬‬"
            ),
            (
                # translation_word
                "кассир",
                # pronunciation_word
                "kupai",
                # hebrew_word_nikud
                "‫קוּפַּאי‬‬"
            ),
            (
                # translation_word
                "контроль (в транспорте)",
                # pronunciation_word
                "bi'koret kartisim",
                # hebrew_word_nikud
                "‬בִּיקוֹרֶת‬‬‬ ‫כַּרטִיסִים‬"
            ),
            (
                # translation_word
                "опаздывать",
                # pronunciation_word
                "leʾaχer",
                # hebrew_word_nikud
                "‬‫לְאַחֵר‬"
            ),
            (
                # translation_word
                "спешить (торопиться)",
                # pronunciation_word
                "lemaher",
                # hebrew_word_nikud
                "‬‫לְמַהֵר‬"
            ),
            (
                # translation_word
                "такси",
                # pronunciation_word
                "monit",
                # hebrew_word_nikud
                "‬‫מוֹנִית‬"
            ),
            (
                # translation_word
                "таксист",
                # pronunciation_word
                "nahag monit",
                # hebrew_word_nikud
                "נַהַג‬‬‬ ‫מוֹנִית‬‬"
            ),
            (
                # translation_word
                "вызвать такси",
                # pronunciation_word
                "lehazmin monit",
                # hebrew_word_nikud
                "‬לְהַזמִין‬‬‬ ‫מוֹנִית‬"
            ),
            (
                # translation_word
                "пробка (на дороге)",
                # pronunciation_word
                "pkak",
                # hebrew_word_nikud
                "‬‫פּקָק‬"
            ),
            (
                # translation_word
                "часы пик",
                # pronunciation_word
                "ʃaʿot 'omes",
                # hebrew_word_nikud
                "שָעוֹת‬‬‬ ‫עוֹמֶס‬‬"
            ),
            (
                # translation_word
                "парковаться",
                # pronunciation_word
                "laχanot",
                # hebrew_word_nikud
                "‫לַחֲנוֹת‬‬"
            ),
            (
                # translation_word
                "стоянка (авто)",
                # pronunciation_word
                "χanaya",
                # hebrew_word_nikud
                "‬‫חֲנָיָה‬"
            ),
            (
                # translation_word
                "метро",
                # pronunciation_word
                "ra'kevet taχtit",
                # hebrew_word_nikud
                "‬רַכֶּבֶת‬ ‬‬‫תַחתִית‬"
            ),
            (
                # translation_word
                "ехать на метро",
                # pronunciation_word
                "lin'soʿa betaχtit",
                # hebrew_word_nikud
                "לִנסוֹע‬ ‬‬‫בְּתַחתִית‬‬"
            ),
            (
                # translation_word
                "вокзал",
                # pronunciation_word
                "taχanat ra'kevet",
                # hebrew_word_nikud
                "תַחֲנַת‬ ‬‬‫רַכֶּבֶת‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "82. Достопримечательности",
        # words
        [
            (
                # translation_word
                "памятник",
                # pronunciation_word
                "an'darta",
                # hebrew_word_nikud
                "‫אַנדַרטָה‬‬"
            ),
            (
                # translation_word
                "крепость",
                # pronunciation_word
                "mivʦar",
                # hebrew_word_nikud
                "‫מִבצָר‬‬"
            ),
            (
                # translation_word
                "зáмок",
                # pronunciation_word
                "tira",
                # hebrew_word_nikud
                "‫טִירָה‬‬"
            ),
            (
                # translation_word
                "архитектура",
                # pronunciation_word
                "adriχalut",
                # hebrew_word_nikud
                "‬‫אַדרִיכָלוּת‬"
            ),
            (
                # translation_word
                "старинный",
                # pronunciation_word
                "atik",
                # hebrew_word_nikud
                "‬‫עַתִיק‬"
            ),
            (
                # translation_word
                "национальный",
                # pronunciation_word
                "leʾumi",
                # hebrew_word_nikud
                "‬‫לְאוּמִי‬"
            ),
            (
                # translation_word
                "известный",
                # pronunciation_word
                "mefursam",
                # hebrew_word_nikud
                "‫מְפוּרסָם‬‬"
            ),
            (
                # translation_word
                "турист",
                # pronunciation_word
                "tayar",
                # hebrew_word_nikud
                "‫תַייָר‬‬"
            ),
            (
                # translation_word
                "гид (экскурсовод)",
                # pronunciation_word
                "madriχ tiyulim",
                # hebrew_word_nikud
                "‬מַדרִיך‬ ‬‬‫טִיוּלִים‬"
            ),
            (
                # translation_word
                "экскурсия",
                # pronunciation_word
                "tiyul",
                # hebrew_word_nikud
                "‫טִיוּל‬‬"
            ),
            (
                # translation_word
                "рассказывать",
                # pronunciation_word
                "lesaper",
                # hebrew_word_nikud
                "‬‫לְסַפֵּר‬"
            ),
            (
                # translation_word
                "найти",
                # pronunciation_word
                "limʦo",
                # hebrew_word_nikud
                "‫לִמצוֹא‬‬"
            ),
            (
                # translation_word
                "потеряться",
                # pronunciation_word
                "la'leχet leʾibud",
                # hebrew_word_nikud
                "לָלֶכֶת‬‬‬ ‫לְאִיבּוּד‬‬"
            ),
            (
                # translation_word
                "фотографировать",
                # pronunciation_word
                "leʦalem",
                # hebrew_word_nikud
                "‫לְצַלֵם‬"
            ),
        ]
    ),     
    (
        # group_name_ru
        "83. Покупки",
        # words
        [
            (
                # translation_word
                "покупать",
                # pronunciation_word
                "liknot",
                # hebrew_word_nikud
                "‫לִקנוֹת‬‬"
            ),
            (
                # translation_word
                "покупка (предмет)",
                # pronunciation_word
                "kniya",
                # hebrew_word_nikud
                "‫קנִייָה‬‬"
            ),
            (
                # translation_word
                "делать покупки",
                # pronunciation_word
                "la'leχet lekniyot",
                # hebrew_word_nikud
                "‬לָלֶכֶת‬‬‬ ‫לְקנִיוֹת‬"
            ),
            (
                # translation_word
                "работать (о магазине)",
                # pronunciation_word
                "pa'tuaχ",
                # hebrew_word_nikud
                "‫פָּתוּח‬‬"
            ),
            (
                # translation_word
                "быть закрытым",
                # pronunciation_word
                "sagur",
                # hebrew_word_nikud
                "‫סָגוּר‬‬"
            ),
            (
                # translation_word
                "обувь",
                # pronunciation_word
                "naʿa'layim",
                # hebrew_word_nikud
                "‬‫נַעֲלַיִים‬"
            ),
            (
                # translation_word
                "одежда",
                # pronunciation_word
                "bgadim",
                # hebrew_word_nikud
                "‫בּגָדִים‬"
            ),
            (
                # translation_word
                "косметика",
                # pronunciation_word
                "tamrukim",
                # hebrew_word_nikud
                "‬‫תַמרוּקִים‬"
            ),
            (
                # translation_word
                "продукты",
                # pronunciation_word
                "muʦrei mazon",
                # hebrew_word_nikud
                "‬מוּצרֵי‬ ‬‬‫מָזוֹן‬"
            ),
            (
                # translation_word
                "продавец",
                # pronunciation_word
                "moχer",
                # hebrew_word_nikud
                "‫מוֹכֵר‬‬"
            ),
            (
                # translation_word
                "продавщица",
                # pronunciation_word
                "mo'χeret",
                # hebrew_word_nikud
                "‫מוֹכֵרֶת‬‬"
            ),
            (
                # translation_word
                "зеркало",
                # pronunciation_word
                "marʾa",
                # hebrew_word_nikud
                "‫מַראָה‬‬"
            ),
            (
                # translation_word
                "прилавок",
                # pronunciation_word
                "duχan",
                # hebrew_word_nikud
                "‫דוּכָן‬‬"
            ),
            (
                # translation_word
                "примерочная",
                # pronunciation_word
                "'χeder halbaʃa",
                # hebrew_word_nikud
                "חֶדֶר‬ ‬‬‫הַלבָּשָה‬‬"
            ),
            (
                # translation_word
                "примерить",
                # pronunciation_word
                "limdod",
                # hebrew_word_nikud
                "‫לִמדוֹד‬‬"
            ),
            (
                # translation_word
                "подходить (быть впору)",
                # pronunciation_word
                "lehatʾim",
                # hebrew_word_nikud
                "‬‫לְהַתאִים‬"
            ),
            (
                # translation_word
                "цена",
                # pronunciation_word
                "meχir",
                # hebrew_word_nikud
                "‫מְחִיר‬‬"
            ),
            (
                # translation_word
                "стоить",
                # pronunciation_word
                "laʿalot",
                # hebrew_word_nikud
                "‬‫לַעֲלוֹת‬"
            ),
            (
                # translation_word
                "Сколько? (о цене)",
                # pronunciation_word
                "'kama?",
                # hebrew_word_nikud
                "‫כַּמָה‬‬"
            ),
            (
                # translation_word
                "скидка",
                # pronunciation_word
                "hanaχa",
                # hebrew_word_nikud
                "‬‫הֲנָחָה‬"
            ),
            (
                # translation_word
                "недорогой",
                # pronunciation_word
                "lo yakar",
                # hebrew_word_nikud
                "‬לֹא‬‬‬ ‫יָקַר‬"
            ),
            (
                # translation_word
                "дешёвый",
                # pronunciation_word
                "zol",
                # hebrew_word_nikud
                "‫זוֹל‬‬"
            ),
            (
                # translation_word
                "дорогой",
                # pronunciation_word
                "yakar",
                # hebrew_word_nikud
                "‫יָקָר‬‬"
            ),
            (
                # translation_word
                "прокат",
                # pronunciation_word
                "haskara",
                # hebrew_word_nikud
                "‫הַשׂכָּרָה‬‬"
            ),
            (
                # translation_word
                "взять напрокат",
                # pronunciation_word
                "liskor",
                # hebrew_word_nikud
                "‫לִשׂכּוֹר‬‬"
            ),
            (
                # translation_word
                "кредит",
                # pronunciation_word
                "aʃrai",
                # hebrew_word_nikud
                "‫אַשרַאי‬‬"
            ),
            (
                # translation_word
                "в кредит",
                # pronunciation_word
                "beʾaʃrai",
                # hebrew_word_nikud
                "‫בְּאַשרַאי‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "84. Деньги",
        # words
        [
            (
                # translation_word
                "деньги",
                # pronunciation_word
                "'kesef",
                # hebrew_word_nikud
                "‫כֶּסֶף‬‬"
            ),
            (
                # translation_word
                "обмен",
                # pronunciation_word
                "hamara",
                # hebrew_word_nikud
                "‫הֲמָרָה‬‬"
            ),
            (
                # translation_word
                "курс (валют)",
                # pronunciation_word
                "'ʃaʿar χalifin",
                # hebrew_word_nikud
                "‬שַעַר‬‬‬ ‫חֲלִיפִין‬"
            ),
            (
                # translation_word
                "банкомат",
                # pronunciation_word
                "kaspomat",
                # hebrew_word_nikud
                "‬‫כַּספּוֹמָט‬"
            ),
            (
                # translation_word
                "долг",
                # pronunciation_word
                "χov",
                # hebrew_word_nikud
                "‫חוֹב‬‬"
            ),
            (
                # translation_word
                "должник",
                # pronunciation_word
                "'baʿal χov",
                # hebrew_word_nikud
                "בַּעַל‬‬‬ ‫חוֹב‬‬"
            ),
            (
                # translation_word
                "дать в долг",
                # pronunciation_word
                "lehalvot",
                # hebrew_word_nikud
                "‫לְהַלווֹת‬‬"
            ),
            (
                # translation_word
                "взять в долг",
                # pronunciation_word
                "lilvot",
                # hebrew_word_nikud
                "‬‫לִלווֹת‬"
            ),
            (
                # translation_word
                "банк",
                # pronunciation_word
                "bank",
                # hebrew_word_nikud
                "‫בַּנק‬‬"
            ),
            (
                # translation_word
                "счёт (в банке)",
                # pronunciation_word
                "χeʃbon",
                # hebrew_word_nikud
                "‫חֶשבּוֹן‬‬"
            ),
            (
                # translation_word
                "положить (на счёт)",
                # pronunciation_word
                "lehafkid",
                # hebrew_word_nikud
                "‬‫לְהַפקִיד‬"
            ),
            (
                # translation_word
                "положить на счёт",
                # pronunciation_word
                "lehafkid leχeʃbon",
                # hebrew_word_nikud
                "לְהַפקִיד‬‬‬ ‫לְחֶשבּוֹן‬‬"
            ),
            (
                # translation_word
                "снять со счёта",
                # pronunciation_word
                "limʃoχ meχeʃbon",
                # hebrew_word_nikud
                "לִמשוֹך‬‬‬ ‫מֵחֶשבּוֹן‬"
            ),
            (
                # translation_word
                "кредитная карта",
                # pronunciation_word
                "kartis aʃrai",
                # hebrew_word_nikud
                "‬כַּרטִיס‬‬‬ ‫אַשרַאי‬"
            ),
            (
                # translation_word
                "наличные деньги",
                # pronunciation_word
                "mezuman",
                # hebrew_word_nikud
                "‫מְזוּמָן‬‬"
            ),
            (
                # translation_word
                "чек",
                # pronunciation_word
                "ʧek",
                # hebrew_word_nikud
                "‬‫צֶ׳ק‬"
            ),
            (
                # translation_word
                "выписать чек",
                # pronunciation_word
                "liχtov ʧek",
                # hebrew_word_nikud
                "לִכתוֹב‬‬‬ ‫צֶ׳ק‬‬"
            ),
            (
                # translation_word
                "чековая книжка",
                # pronunciation_word
                "pinkas 'ʧekim",
                # hebrew_word_nikud
                "‬פִּנקַס‬‬‬ ‫צֶ׳קִים‬"
            ),
            (
                # translation_word
                "кошелёк",
                # pronunciation_word
                "arnak lematbe'ʿot",
                # hebrew_word_nikud
                "‬אַרנָק‬‬‬ ‫לֵמַטבְּעוֹת‬"
            ),
            (
                # translation_word
                "сейф",
                # pronunciation_word
                "ka'sefet",
                # hebrew_word_nikud
                "‫כַּסֶפֶת‬‬"
            ),
            (
                # translation_word
                "наследник",
                # pronunciation_word
                "yoreʃ",
                # hebrew_word_nikud
                "‫יוֹרֵש‬‬"
            ),
            (
                # translation_word
                "аренда",
                # pronunciation_word
                "χoze sχirut",
                # hebrew_word_nikud
                "‬חוֹזֶה‬‬‬ ‫שׂכִירוּת‬"
            ),
            (
                # translation_word
                "квартирная плата",
                # pronunciation_word
                "sχar dira",
                # hebrew_word_nikud
                "שכַר‬‬‬ ‫דִירָה‬‬"
            ),
            (
                # translation_word
                "снимать (~ квартиру)",
                # pronunciation_word
                "sχar dira",
                # hebrew_word_nikud
                "‬שכַר‬‬‬ ‫דִירָה‬"
            ),
            (
                # translation_word
                "сумма",
                # pronunciation_word
                "sχum",
                # hebrew_word_nikud
                "‬‫סכוּם‬"
            ),
            (
                # translation_word
                "тратить, расходовать",
                # pronunciation_word
                "lehoʦi",
                # hebrew_word_nikud
                "‫לְהוֹצִיא‬‬"
            ),
            (
                # translation_word
                "расходы",
                # pronunciation_word
                "hoʦaʾot",
                # hebrew_word_nikud
                "‬‫הוֹצָאוֹת‬"
            ),
            (
                # translation_word
                "экономить",
                # pronunciation_word
                "laχasoχ",
                # hebrew_word_nikud
                "‫לַחֲסוֹך‬‬"
            ),
            (
                # translation_word
                "экономный",
                # pronunciation_word
                "χesχoni",
                # hebrew_word_nikud
                "‫חֶסכוֹנִי‬‬"
            ),
            (
                # translation_word
                "платить",
                # pronunciation_word
                "leʃalem",
                # hebrew_word_nikud
                "‫לְשַלֵם‬‬"
            ),
            (
                # translation_word
                "оплата",
                # pronunciation_word
                "taʃlum",
                # hebrew_word_nikud
                "‫תַשלוּם‬‬"
            ),
            (
                # translation_word
                "сдача (деньги)",
                # pronunciation_word
                "'odef",
                # hebrew_word_nikud
                "‬‫עוֹדֶף‬"
            ),
            (
                # translation_word
                "налог",
                # pronunciation_word
                "mas",
                # hebrew_word_nikud
                "‫מַס‬‬"
            ),
            (
                # translation_word
                "штраф",
                # pronunciation_word
                "knas",
                # hebrew_word_nikud
                "‫קנָס‬‬"
            ),
            (
                # translation_word
                "штрафовать",
                # pronunciation_word
                "liknos",
                # hebrew_word_nikud
                "‬‫לִקנוֹס‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "85. Почта",
        # words
        [
            (
                # translation_word
                "почта",
                # pronunciation_word
                "'doʾar",
                # hebrew_word_nikud
                "‫דוֹאַר‬‬"
            ),
            (
                # translation_word
                "почтальон",
                # pronunciation_word
                "davar",
                # hebrew_word_nikud
                "‬‫דַווָר‬"
            ),
            (
                # translation_word
                "письмо",
                # pronunciation_word
                "miχtav",
                # hebrew_word_nikud
                "‬‫מִכתָב‬"
            ),
            (
                # translation_word
                "заказное письмо",
                # pronunciation_word
                "miχtav raʃum",
                # hebrew_word_nikud
                "מִכתָב‬‬‬‬ ‫רָשוּם‬‬"
            ),
            (
                # translation_word
                "посылка",
                # pronunciation_word
                "χavila",
                # hebrew_word_nikud
                "‫חֲבִילָה‬‬"
            ),
            (
                # translation_word
                "денежный перевод",
                # pronunciation_word
                "haʿavarat ksafim",
                # hebrew_word_nikud
                "‬הַעֲבָרַת‬ ‬‬‬‬‬‬‫כּסָפִים‬"
            ),
            (
                # translation_word
                "получить",
                # pronunciation_word
                "lekabel",
                # hebrew_word_nikud
                "‫לְקַבֵּל‬‬"
            ),
            (
                # translation_word
                "отправить",
                # pronunciation_word
                "liʃ'loaχ",
                # hebrew_word_nikud
                "‫לִשלוֹח‬‬"
            ),
            (
                # translation_word
                "адрес",
                # pronunciation_word
                "'ktovet",
                # hebrew_word_nikud
                "‬‫כּתוֹבֶת‬"
            ),
            (
                # translation_word
                "индекс",
                # pronunciation_word
                "mikud",
                # hebrew_word_nikud
                "‬‫מִיקוּד‬"
            ),
            (
                # translation_word
                "отправитель",
                # pronunciation_word
                "ʃo'leaχ",
                # hebrew_word_nikud
                "‬‫שוֹלֵח‬"
            ),
            (
                # translation_word
                "получатель",
                # pronunciation_word
                "nimʿan",
                # hebrew_word_nikud
                "‫נִמעָן‬‬"
            ),
            (
                # translation_word
                "имя",
                # pronunciation_word
                "ʃem prati",
                # hebrew_word_nikud
                "‬שֵם‬‬‬‬‬‬‬ ‫פּרָטִי‬"
            ),
            (
                # translation_word
                "фамилия",
                # pronunciation_word
                "ʃem miʃpaχa",
                # hebrew_word_nikud
                "שֵם‬‬‬‬‬‬‬ ‫מִשפָּחָה‬‬"
            ),
            (
                # translation_word
                "тариф",
                # pronunciation_word
                "taʿarif",
                # hebrew_word_nikud
                "‫תַעֲרִיף‬‬"
            ),
            (
                # translation_word
                "обычный",
                # pronunciation_word
                "ragil",
                # hebrew_word_nikud
                "‫רָגִיל‬‬"
            ),
            (
                # translation_word
                "вес",
                # pronunciation_word
                "miʃkal",
                # hebrew_word_nikud
                "‬‫מִשקָל‬"
            ),
            (
                # translation_word
                "конверт",
                # pronunciation_word
                "maʿatafa",
                # hebrew_word_nikud
                "‫מַעֲטָפָה‬‬"
            ),
            (
                # translation_word
                "марка",
                # pronunciation_word
                "bul 'doʾar",
                # hebrew_word_nikud
                "בּוּל‬ ‬‬‬‬‬‬‫דוֹאַר‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "86. Дом. Жилище",
        # words
        [
            (
                # translation_word
                "дом",
                # pronunciation_word
                "'bayit",
                # hebrew_word_nikud
                "‫בַּיִת‬‬"
            ),
            (
                # translation_word
                "двор",
                # pronunciation_word
                "χaʦer",
                # hebrew_word_nikud
                "‫חָצֵר‬‬"
            ),
            (
                # translation_word
                "кирпичный",
                # pronunciation_word
                "milevenim",
                # hebrew_word_nikud
                "‬‫מִלְבֵנִים‬"
            ),
            (
                # translation_word
                "каменный",
                # pronunciation_word
                "me'ʾeven",
                # hebrew_word_nikud
                "‬‫מֵאֶבֶן‬"
            ),
            (
                # translation_word
                "бетонный",
                # pronunciation_word
                "mibeton",
                # hebrew_word_nikud
                "‫מִבֶּטוֹן‬‬"
            ),
            (
                # translation_word
                "новый",
                # pronunciation_word
                "χadaʃ",
                # hebrew_word_nikud
                "‬‫חָדָש‬"
            ),
            (
                # translation_word
                "старый",
                # pronunciation_word
                "yaʃan",
                # hebrew_word_nikud
                "‬‫יָשָן‬"
            ),
            (
                # translation_word
                "современный",
                # pronunciation_word
                "mo'derni",
                # hebrew_word_nikud
                "‫מוֹדֶרנִי‬‬"
            ),
            (
                # translation_word
                "многоэтажный",
                # pronunciation_word
                "rav komot",
                # hebrew_word_nikud
                "‫רַב־קוֹמוֹת‬‬"
            ),
            (
                # translation_word
                "высокий",
                # pronunciation_word
                "ga'voha",
                # hebrew_word_nikud
                "‬‫גָבוֹה‬"
            ),
            (
                # translation_word
                "этаж",
                # pronunciation_word
                "'koma",
                # hebrew_word_nikud
                "‫קוֹמָה‬‬"
            ),
            (
                # translation_word
                "крыша",
                # pronunciation_word
                "gag",
                # hebrew_word_nikud
                "‬‫גַג‬"
            ),
            (
                # translation_word
                "окно",
                # pronunciation_word
                "χalon",
                # hebrew_word_nikud
                "‫חַלוֹן‬‬"
            ),
            (
                # translation_word
                "стекло",
                # pronunciation_word
                "zχuχit",
                # hebrew_word_nikud
                "‬‫זכוּכִית‬"
            ),
            (
                # translation_word
                "ставни",
                # pronunciation_word
                "trisim",
                # hebrew_word_nikud
                "‬‫תרִיסִים‬"
            ),
            (
                # translation_word
                "стена",
                # pronunciation_word
                "kir",
                # hebrew_word_nikud
                "‫קִיר‬‬"
            ),
            (
                # translation_word
                "балкон",
                # pronunciation_word
                "mir'peset",
                # hebrew_word_nikud
                "‬‫מִרפֶּסֶת‬"
            ),
            (
                # translation_word
                "водосточная труба",
                # pronunciation_word
                "marzev",
                # hebrew_word_nikud
                "‫מַרזֵב‬‬"
            ),
            (
                # translation_word
                "подниматься",
                # pronunciation_word
                "laʿalot bemadregot",
                # hebrew_word_nikud
                "לַעֲלוֹת‬ ‬‬‬‬‬‬‫בְּמַדרֵגוֹת‬‬"
            ),
            (
                # translation_word
                "спускаться",
                # pronunciation_word
                "a'redet bemadregot",
                # hebrew_word_nikud
                "לָרֶדֶת‬ ‬‬‬‬‬‬‫בְּמַדרֵגוֹת‬‬"
            ),
             (
                # translation_word
                "переезжать",
                # pronunciation_word
                "laʿavor",
                # hebrew_word_nikud
                "‫לַעֲבוֹר‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "87. Дом. Подъезд. Лифт",
        # words
        [
            (
                # translation_word
                "подъезд",
                # pronunciation_word
                "knisa",
                # hebrew_word_nikud
                "‬‫כּנִיסָה‬"
            ),
            (
                # translation_word
                "лестница",
                # pronunciation_word
                "madregot",
                # hebrew_word_nikud
                "‬‫מַדרֵגוֹת‬"
            ),
            (
                # translation_word
                "почтовый ящик",
                # pronunciation_word
                "teivat 'doʾar",
                # hebrew_word_nikud
                "תֵיבַת‬ ‬‬‬‬‬‬‫דוֹאַר‬‬"
            ),
            (
                # translation_word
                "холл",
                # pronunciation_word
                "'lobi",
                # hebrew_word_nikud
                "‫לוֹבִּי‬‬"
            ),
            (
                # translation_word
                "мусорный бак",
                # pronunciation_word
                "paχ 'zevel",
                # hebrew_word_nikud
                "פַּח‬ ‬‬‬‬‬‬‫זֶבֶל‬"
            ),
            (
                # translation_word
                "мусоропровод",
                # pronunciation_word
                "merik aʃpa",
                # hebrew_word_nikud
                "‬מֵרִיק‬ ‬‬‬‬‬‬‫אַשפָּה‬"
            ),
            (
                # translation_word
                "лифт",
                # pronunciation_word
                "maʿalit",
                # hebrew_word_nikud
                "‫מַעֲלִית‬‬"
            ),
            (
                # translation_word
                "грузовой лифт",
                # pronunciation_word
                "maʿalit masa",
                # hebrew_word_nikud
                "מַעֲלִית‬‬‬‬‬‬‬ ‫מַשָׂא‬‬"
            ),
            (
                # translation_word
                "кабина (лифта)",
                # pronunciation_word
                "ta maʿalit",
                # hebrew_word_nikud
                "תָא‬‬‬‬‬‬‬ ‫מַעֲלִית‬‬"
            ),
            (
                # translation_word
                "ехать на лифте",
                # pronunciation_word
                "lin'soʿa bemaʿalit",
                # hebrew_word_nikud
                "‬לִנסוֹע‬‬‬‬‬‬‬ ‫בְּמַעֲלִית‬"
            ),
            (
                # translation_word
                "квартира",
                # pronunciation_word
                "dira",
                # hebrew_word_nikud
                "‫דִירָה‬‬"
            ),
            (
                # translation_word
                "жильцы",
                # pronunciation_word
                "dayarim",
                # hebrew_word_nikud
                "‬‫דַייָרִים‬"
            ),
            (
                # translation_word
                "сосед",
                # pronunciation_word
                "ʃaχen",
                # hebrew_word_nikud
                "‫שָכֵן‬‬"
            ),
            (
                # translation_word
                "соседка",
                # pronunciation_word
                "ʃχena",
                # hebrew_word_nikud
                "‫שכֵנָה‬‬"
            ),
            (
                # translation_word
                "соседи",
                # pronunciation_word
                "ʃχenim",
                # hebrew_word_nikud
                "‫שכֵנִים‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "88. Дом. Электричество",
        # words
        [
            (
                # translation_word
                "электричество",
                # pronunciation_word
                "χaʃmal",
                # hebrew_word_nikud
                "‫חַשמַל‬‬"
            ),
            (
                # translation_word
                "лампочка",
                # pronunciation_word
                "nura",
                # hebrew_word_nikud
                "‫נוּרָה‬‬"
            ),
            (
                # translation_word
                "выключатель",
                # pronunciation_word
                "'meteg",
                # hebrew_word_nikud
                "‬‫מֶתֶג‬"
            ),
            (
                # translation_word
                "пробка (электр.)",
                # pronunciation_word
                "natiχ",
                # hebrew_word_nikud
                "‫נָתִיך‬‬"
            ),
            (
                # translation_word
                "провод",
                # pronunciation_word
                "χut",
                # hebrew_word_nikud
                "‬‫חוּט‬"
            ),
            (
                # translation_word
                "проводка",
                # pronunciation_word
                "χivut",
                # hebrew_word_nikud
                "‬‫חִיווּט‬"
            ),
            (
                # translation_word
                "электросчётчик",
                # pronunciation_word
                "mone χaʃmal",
                # hebrew_word_nikud
                "מוֹנֵה‬‬‬‬‬‬‬ ‫חַשמַל‬‬"
            ),
            (
                # translation_word
                "показание (счётчика)",
                # pronunciation_word
                "kriʾa",
                # hebrew_word_nikud
                "‬‫קרִיאָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "89. Дом. Дверь. Замок",
        # words
        [
            (
                # translation_word
                "дверь",
                # pronunciation_word
                "'delet",
                # hebrew_word_nikud
                "‫דֶלֶת‬‬"
            ),
            (
                # translation_word
                "ворота",
                # pronunciation_word
                "'ʃaʿar",
                # hebrew_word_nikud
                "‫שַעַר‬‬"
            ),
            (
                # translation_word
                "ручка (дверная)",
                # pronunciation_word
                "yadit",
                # hebrew_word_nikud
                "‬‫יָדִית‬"
            ),
            (
                # translation_word
                "отпереть",
                # pronunciation_word
                "lif'toaχ",
                # hebrew_word_nikud
                "‫לִפתוֹח‬‬"
            ),
            (
                # translation_word
                "закрывать",
                # pronunciation_word
                "lisgor",
                # hebrew_word_nikud
                "‫לִסגוֹר‬‬"
            ),
            (
                # translation_word
                "ключ",
                # pronunciation_word
                "maf'teaχ",
                # hebrew_word_nikud
                "‬‫מַפתֵח‬"
            ),
            (
                # translation_word
                "петля (дверная)",
                # pronunciation_word
                "ʦir",
                # hebrew_word_nikud
                "‫צִיר‬‬"
            ),
            (
                # translation_word
                "коврик",
                # pronunciation_word
                "ʃtiχon",
                # hebrew_word_nikud
                "‫שטִיחוֹן‬‬"
            ),
            (
                # translation_word
                "замок (дверной ~)",
                # pronunciation_word
                "manʿul",
                # hebrew_word_nikud
                "‫מַנעוּל‬‬"
            ),
            (
                # translation_word
                "стук (в дверь)",
                # pronunciation_word
                "hakaʃa",
                # hebrew_word_nikud
                "‫הַקָשָה‬‬"
            ),
            (
                # translation_word
                "стучать",
                # pronunciation_word
                "lehakiʃ",
                # hebrew_word_nikud
                "‫לְהַקִיש‬‬"
            ),
            (
                # translation_word
                "кодовый замок",
                # pronunciation_word
                "manʿul kod",
                # hebrew_word_nikud
                "‬מַנעוּל‬‬‬‬‬‬‬ ‫קוֹד‬"
            ),
            (
                # translation_word
                "код",
                # pronunciation_word
                "kod",
                # hebrew_word_nikud
                "‬‫קוֹד‬"
            ),
            (
                # translation_word
                "домофон",
                # pronunciation_word
                "'interkom",
                # hebrew_word_nikud
                "‬‫אִינטֶרקוֹם‬"
            ),
            (
                # translation_word
                "номер",
                # pronunciation_word
                "mispar",
                # hebrew_word_nikud
                "‫מִספָּר‬‬"
            ),
            (
                # translation_word
                "глазок",
                # pronunciation_word
                "einit",
                # hebrew_word_nikud
                "‬‫עֵינִית‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "90. Загородный дом. Дом в деревне",
        # words
        [
            (
                # translation_word
                "деревня",
                # pronunciation_word
                "kfar",
                # hebrew_word_nikud
                "‫כּפָר‬‬"
            ),
            (
                # translation_word
                "забор",
                # pronunciation_word
                "gader",
                # hebrew_word_nikud
                "‬‫גָדֵר‬"
            ),
            (
                # translation_word
                "калитка",
                # pronunciation_word
                "piʃpaʃ",
                # hebrew_word_nikud
                "‫פִּשפָּש‬‬"
            ),
            (
                # translation_word
                "амбар",
                # pronunciation_word
                "asam",
                # hebrew_word_nikud
                "‬‫אָסָם‬"
            ),
            (
                # translation_word
                "сарай",
                # pronunciation_word
                "maχsan",
                # hebrew_word_nikud
                "‫מַחסָן‬‬"
            ),
            (
                # translation_word
                "печь (предмет)",
                # pronunciation_word
                "aχ",
                # hebrew_word_nikud
                "‬‫אָח‬"
            ),
            (
                # translation_word
                "топить печь",
                # pronunciation_word
                "lehasik et haʾaχ",
                # hebrew_word_nikud
                "‬לְהַסִיק‬‬‬‬‬‬‬ ‫אֶת‬ ‫הָאָ‬"
            ),
            (
                # translation_word
                "дрова",
                # pronunciation_word
                "aʦei hasaka",
                # hebrew_word_nikud
                "עֲצֵי‬‬‬‬‬‬‬ ‫הַסָקָה‬‬"
            ),
            (
                # translation_word
                "веранда",
                # pronunciation_word
                "mir'peset mekora",
                # hebrew_word_nikud
                "‬מִרפֶּסֶת‬‬‬‬‬‬‬ ‫מְקוֹרָה‬"
            ),
            (
                # translation_word
                "крыльцо",
                # pronunciation_word
                "madregot ba'petaχ 'bayit",
                # hebrew_word_nikud
                "‬מַדרֵגוֹת‬‬‬‬‬‬‬ ‫בַּפֶּתַח‬ ‫בַּיִת‬"
            ),
            (
                # translation_word
                "качели",
                # pronunciation_word
                "nadneda",
                # hebrew_word_nikud
                "‫נַדנֵדָה‬‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "91. Особняк. Вилла",
        # words
        [
            (
                # translation_word
                "загородный дом",
                # pronunciation_word
                "'bayit bakfar",
                # hebrew_word_nikud
                "‬בַּיִת‬‬‬‬‬‬‬ ‫בַּכּפָר‬"
            ),
            (
                # translation_word
                "вилла",
                # pronunciation_word
                "'vila",
                # hebrew_word_nikud
                "‫וִילָה‬‬"
            ),
            (
                # translation_word
                "сад",
                # pronunciation_word
                "gan",
                # hebrew_word_nikud
                "‫גַן‬‬"
            ),
            (
                # translation_word
                "парк",
                # pronunciation_word
                "park",
                # hebrew_word_nikud
                "‫פַּארק‬‬"
            ),
            (
                # translation_word
                "бассейн",
                # pronunciation_word
                "breχat sχiya",
                # hebrew_word_nikud
                "בּרֵיכַת‬‬‬‬‬‬‬ ‫שׂחִייָה‬‬"
            ),
            (
                # translation_word
                "тренажёрный зал",
                # pronunciation_word
                "'χeder 'koʃer",
                # hebrew_word_nikud
                "חֶדֶר‬‬‬‬‬‬‬ ‫כּוֹשֶר‬‬"
            ),
            (
                # translation_word
                "гараж",
                # pronunciation_word
                "musaχ",
                # hebrew_word_nikud
                "‫מוּסָך‬‬"
            ),
            (
                # translation_word
                "частная собственность",
                # pronunciation_word
                "reχuʃ prati",
                # hebrew_word_nikud
                "רְכוּש‬‬‬‬‬‬‬ ‫פּרָטִי‬‬"
            ),
            (
                # translation_word
                "предупреждение",
                # pronunciation_word
                "azhara",
                # hebrew_word_nikud
                "‫אַזהָרָה‬‬"
            ),
            (
                # translation_word
                "охрана",
                # pronunciation_word
                "avtaχa",
                # hebrew_word_nikud
                "‫אַבטָחָה‬‬"
            ),
            (
                # translation_word
                "охранник",
                # pronunciation_word
                "ʃomer",
                # hebrew_word_nikud
                "‬‫שוֹמֵר‬"
            ),
            (
                # translation_word
                "сигнализация",
                # pronunciation_word
                "maʿa'reχet azʿaka",
                # hebrew_word_nikud
                "מַעֲרֶכֶת‬‬‬‬‬‬‬ ‫אַזעָקָה‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "92. Замок. Дворец",
        # words
        [
            (
                # translation_word
                "зáмок",
                # pronunciation_word
                "tira",
                # hebrew_word_nikud
                "‫טִירָה‬‬"
            ),
            (
                # translation_word
                "дворец",
                # pronunciation_word
                "armon",
                # hebrew_word_nikud
                "‬‫אַרמוֹן‬"
            ),
            (
                # translation_word
                "великолепный",
                # pronunciation_word
                "mefoʾar",
                # hebrew_word_nikud
                "‬‫מְפוֹאָר‬"
            ),
            (
                # translation_word
                "средневековый",
                # pronunciation_word
                "benaimi",
                # hebrew_word_nikud
                "‬‫בֵּינַיימִי‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "93. Квартира",
        # words
        [
            (
                # translation_word
                "квартира",
                # pronunciation_word
                "dira",
                # hebrew_word_nikud
                "‬‫דִירָה‬"
            ),
            (
                # translation_word
                "комната",
                # pronunciation_word
                "'χeder",
                # hebrew_word_nikud
                "‬‫חֶדֶר‬"
            ),
            (
                # translation_word
                "спальня",
                # pronunciation_word
                "χadar ʃena",
                # hebrew_word_nikud
                "‬חֲדַר‬‬‬‬‬‬‬ ‫שֵינָה‬"
            ),
            (
                # translation_word
                "столовая (комната)",
                # pronunciation_word
                "pinat 'oχel",
                # hebrew_word_nikud
                "פִּינַת‬‬‬‬‬‬‬ ‫אוֹכֶל‬‬"
            ),
            (
                # translation_word
                "гостиная",
                # pronunciation_word
                "salon",
                # hebrew_word_nikud
                "‬‫סָלוֹן‬"
            ),
            (
                # translation_word
                "кабинет",
                # pronunciation_word
                "χadar avoda",
                # hebrew_word_nikud
                "חֲדַר‬‬‬‬‬‬‬ ‫עֲבוֹדָה‬‬"
            ),
            (
                # translation_word
                "прихожая",
                # pronunciation_word
                "prozdor",
                # hebrew_word_nikud
                "‬‫פּרוֹזדוֹר‬"
            ),
            (
                # translation_word
                "ванная комната",
                # pronunciation_word
                "χadar am'batya",
                # hebrew_word_nikud
                "‬חֲדַר‬‬‬‬‬‬‬ ‫אַמבַּטיָה‬"
            ),
            (
                # translation_word
                "туалет",
                # pronunciation_word
                "ʃerutim",
                # hebrew_word_nikud
                "‫שֵירוּתִים‬‬"
            ),
            (
                # translation_word
                "потолок",
                # pronunciation_word
                "tikra",
                # hebrew_word_nikud
                "‫תִקרָה‬‬"
            ),
            (
                # translation_word
                "пол",
                # pronunciation_word
                "riʦpa",
                # hebrew_word_nikud
                "‬‫רִצפָּה‬"
            ),
            (
                # translation_word
                "угол (комнаты)",
                # pronunciation_word
                "pina",
                # hebrew_word_nikud
                "‫פִּינָה‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "94. Квартира. Уборка",
        # words
        [
            (
                # translation_word
                "убирать (~ квартиру)",
                # pronunciation_word
                "lenakot",
                # hebrew_word_nikud
                "‬‫לְנַקוֹת‬"
            ),
            (
                # translation_word
                "убирать (в шкаф и т.п.)",
                # pronunciation_word
                "lefanot",
                # hebrew_word_nikud
                "‫לְפַנוֹת‬‬"
            ),
            (
                # translation_word
                "пыль",
                # pronunciation_word
                "avak",
                # hebrew_word_nikud
                "‬‫אָבָק‬"
            ),
            (
                # translation_word
                "пыльный",
                # pronunciation_word
                "meʾubak",
                # hebrew_word_nikud
                "‫מְאוּבָּק‬‬"
            ),
            (
                # translation_word
                "вытирать пыль",
                # pronunciation_word
                "lenakot avak",
                # hebrew_word_nikud
                "לְנַקוֹת‬‬‬‬‬‬‬ ‫אָבָק‬‬"
            ),
            (
                # translation_word
                "пылесос",
                # pronunciation_word
                "ʃoʾev avak",
                # hebrew_word_nikud
                "שוֹאֵב‬‬‬‬‬‬‬ ‫אָבָק‬‬"
            ),
            (
                # translation_word
                "пылесосить",
                # pronunciation_word
                "liʃʾov avak",
                # hebrew_word_nikud
                "לִשאוֹב‬‬‬‬‬‬‬ ‫אָבָק‬‬"
            ),
            (
                # translation_word
                "подметать",
                # pronunciation_word
                "letate",
                # hebrew_word_nikud
                "‫לְטַאטֵא‬‬"
            ),
            (
                # translation_word
                "мусор (сор)",
                # pronunciation_word
                "'psolet tiʾtu",
                # hebrew_word_nikud
                "פּסוֹלֶת‬ ‬‬‬‬‬‬‫טִאטוּא‬‬"
            ),
            (
                # translation_word
                "порядок (в комнате)",
                # pronunciation_word
                "'seder",
                # hebrew_word_nikud
                "‬‫סֶדֶר‬"
            ),
            (
                # translation_word
                "беспорядок",
                # pronunciation_word
                "i 'seder",
                # hebrew_word_nikud
                "אִי‬‬‬‬‬‬‬ ‫סֶדֶר‬‬"
            ),
            (
                # translation_word
                "швабра",
                # pronunciation_word
                "magev im smartut",
                # hebrew_word_nikud
                "מַגֵב‬ ‫עִם‬ ‬‬‬‬‬‬‫סמַרטוּט‬‬"
            ),
            (
                # translation_word
                "тряпка",
                # pronunciation_word
                "smartut avak",
                # hebrew_word_nikud
                "סמַרטוּט‬ ‬‬‬‬‬‬‫אָבָק‬‬"
            ),
            (
                # translation_word
                "веник",
                # pronunciation_word
                "matʾate katan",
                # hebrew_word_nikud
                "מַטאֲטֵא‬ ‬‬‬‬‬‬‫קָטַן‬‬"
            ),
            (
                # translation_word
                "совок для мусора",
                # pronunciation_word
                "yaʿe",
                # hebrew_word_nikud
                "‫יָעֶה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "95. Мебель. Интерьер",
        # words
        [
            (
                # translation_word
                "мебель",
                # pronunciation_word
                "rehitim",
                # hebrew_word_nikud
                "‫רָהִיטִים‬"
            ),
            (
                # translation_word
                "стол",
                # pronunciation_word
                "ʃulχan",
                # hebrew_word_nikud
                "‬‫שוּלחָן‬"
            ),
            (
                # translation_word
                "стул",
                # pronunciation_word
                "kise",
                # hebrew_word_nikud
                "‫כִּסֵא‬‬"
            ),
            (
                # translation_word
                "кровать",
                # pronunciation_word
                "mita",
                # hebrew_word_nikud
                "‬‫מִיטָה‬"
            ),
            (
                # translation_word
                "диван",
                # pronunciation_word
                "sapa",
                # hebrew_word_nikud
                "‫סַפָּה‬‬"
            ),
            (
                # translation_word
                "кресло",
                # pronunciation_word
                "kursa",
                # hebrew_word_nikud
                "‫כּוּרסָה‬‬"
            ),
            (
                # translation_word
                "шкаф (книжный)",
                # pronunciation_word
                "aron sfarim",
                # hebrew_word_nikud
                "אֲרוֹן‬ ‬‬‬‬‬‬‫ספָרִים‬‬"
            ),
            (
                # translation_word
                "полка (для книг)",
                # pronunciation_word
                "madaf",
                # hebrew_word_nikud
                "‫מַדָף‬‬"
            ),
            (
                # translation_word
                "шкаф (для одежды)",
                # pronunciation_word
                "aron bgadim",
                # hebrew_word_nikud
                "‬אֲרוֹן‬ ‬‬‬‬‬‬‫בּגָדִים‬"
            ),
            (
                # translation_word
                "вешалка",
                # pronunciation_word
                "mitle",
                # hebrew_word_nikud
                "‬‫מִתלֶה‬"
            ),
            (
                # translation_word
                "комод",
                # pronunciation_word
                "ʃida",
                # hebrew_word_nikud
                "‫שִידָה‬‬"
            ),
            (
                # translation_word
                "зеркало",
                # pronunciation_word
                "marʾa",
                # hebrew_word_nikud
                "‬‫מַראָה‬"
            ),
            (
                # translation_word
                "ковёр",
                # pronunciation_word
                "ʃa'tiaχ",
                # hebrew_word_nikud
                "‫שָטִיח‬‬"
            ),
            (
                # translation_word
                "шторы",
                # pronunciation_word
                "vilonot",
                # hebrew_word_nikud
                "‬‫וִילוֹנוֹת‬"
            ),
            (
                # translation_word
                "обои",
                # pronunciation_word
                "tapet",
                # hebrew_word_nikud
                "‫טַפֶּט‬‬"
            ),
            (
                # translation_word
                "жалюзи",
                # pronunciation_word
                "trisim",
                # hebrew_word_nikud
                "‫תרִיסִים‬‬"
            ),
            (
                # translation_word
                "настольная лампа",
                # pronunciation_word
                "menorat ʃulχan",
                # hebrew_word_nikud
                "מְנוֹרַת‬‬‬‬‬‬‬ ‫שוּלחָן‬‬"
            ),
            (
                # translation_word
                "светильник (на стене)",
                # pronunciation_word
                "menorat kir",
                # hebrew_word_nikud
                "‬מְנוֹרַת‬‬‬‬‬‬‬ ‫קִיר‬"
            ),
            (
                # translation_word
                "ящик (стола)",
                # pronunciation_word
                "megera",
                # hebrew_word_nikud
                "‫מְגֵירָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "96. Постельные принадлежности",
        # words
        [
            (
                # translation_word
                "постельное бельё",
                # pronunciation_word
                "maʦaʿim",
                # hebrew_word_nikud
                "‫מַצָעִים‬‬"
            ),
            (
                # translation_word
                "подушка",
                # pronunciation_word
                "karit",
                # hebrew_word_nikud
                "‬‫כָּרִית‬"
            ),
            (
                # translation_word
                "наволочка",
                # pronunciation_word
                "ʦipit",
                # hebrew_word_nikud
                "‬‫צִיפִּית‬"
            ),
            (
                # translation_word
                "одеяло",
                # pronunciation_word
                "smiχa",
                # hebrew_word_nikud
                "‬‫שׂמִיכָה‬"
            ),
            (
                # translation_word
                "простыня",
                # pronunciation_word
                "sadin",
                # hebrew_word_nikud
                "‫סָדִין‬‬"
            ),
            (
                # translation_word
                "покрывало",
                # pronunciation_word
                "kisui mita",
                # hebrew_word_nikud
                "‬כִּיסוּי‬‬‬‬‬‬‬ ‫מִיטָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "97. Кухня",
        # words
        [
            (
                # translation_word
                "кухня (помещение)",
                # pronunciation_word
                "mitbaχ",
                # hebrew_word_nikud
                "‫מִטבָּח‬‬"
            ),
            (
                # translation_word
                "газ",
                # pronunciation_word
                "gaz",
                # hebrew_word_nikud
                "‬‫גָז‬"
            ),
            (
                # translation_word
                "плита газовая",
                # pronunciation_word
                "tanur gaz",
                # hebrew_word_nikud
                "תַנוּר‬ ‬‬‬‬‬‬‫גָז‬‬"
            ),
            (
                # translation_word
                "плита электрическая",
                # pronunciation_word
                "tanur χaʃmali",
                # hebrew_word_nikud
                "‬תַנוּר‬ ‬‬‬‬‬‬‫חַשמַלִי‬"
            ),
            (
                # translation_word
                "духовка",
                # pronunciation_word
                "tanur afiya",
                # hebrew_word_nikud
                "תַנוּר‬ ‬‬‬‬‬‬‫אֲפִייָה‬‬"
            ),
            (
                # translation_word
                "микроволновая печь",
                # pronunciation_word
                "mikrogal",
                # hebrew_word_nikud
                "‫מִיקרוֹגַל‬‬"
            ),
            (
                # translation_word
                "холодильник",
                # pronunciation_word
                "mekarer",
                # hebrew_word_nikud
                "‬‫מְקָרֵר‬"
            ),
            (
                # translation_word
                "морозильник",
                # pronunciation_word
                "makpi",
                # hebrew_word_nikud
                "‬‫מַקפִּיא‬"
            ),
            (
                # translation_word
                "посудомоечная машина",
                # pronunciation_word
                "me'diaχ kelim",
                # hebrew_word_nikud
                "מֵדִיח‬ ‬‬‬‬‬‬‫כֵּלִים‬‬"
            ),
            (
                # translation_word
                "мясорубка",
                # pronunciation_word
                "matχenat basar",
                # hebrew_word_nikud
                "מַטחֵנַת‬ ‬‬‬‬‬‬‫בָּשָׂר‬‬"
            ),
            (
                # translation_word
                "соковыжималка",
                # pronunciation_word
                "masχeta",
                # hebrew_word_nikud
                "‬‫מַסחֵטָה‬"
            ),
            (
                # translation_word
                "тостер",
                # pronunciation_word
                "'toster",
                # hebrew_word_nikud
                "‫טוֹסטֶר‬‬"
            ),
            (
                # translation_word
                "миксер",
                # pronunciation_word
                "'mikser",
                # hebrew_word_nikud
                "‫מִיקסֶר‬"
            ),
            (
                # translation_word
                "кофеварка",
                # pronunciation_word
                "meχonat kafe",
                # hebrew_word_nikud
                "‬מְכוֹנַת‬ ‬‬‬‬‬‬‫קָפֶה‬"
            ),
            (
                # translation_word
                "кофейник",
                # pronunciation_word
                "finʤan",
                # hebrew_word_nikud
                "‫פִינגָ׳אן‬‬"
            ),
            (
                # translation_word
                "кофемолка",
                # pronunciation_word
                "matχenat kafe",
                # hebrew_word_nikud
                "מַטחֵנַת‬ ‬‬‬‬‬‬‫קָפֶה‬‬"
            ),
            (
                # translation_word
                "чайник",
                # pronunciation_word
                "kumkum",
                # hebrew_word_nikud
                "‬‫קוּמקוּם‬"
            ),
            (
                # translation_word
                "столовая ложка",
                # pronunciation_word
                "kaf",
                # hebrew_word_nikud
                "‫כַּף‬‬"
            ),
            (
                # translation_word
                "чайная ложка",
                # pronunciation_word
                "kapit",
                # hebrew_word_nikud
                "‬‫כַּפִּית‬"
            ),
            (
                # translation_word
                "вилка",
                # pronunciation_word
                "mazleg",
                # hebrew_word_nikud
                "‫מַזלֵג‬‬"
            ),
            (
                # translation_word
                "нож",
                # pronunciation_word
                "sakin",
                # hebrew_word_nikud
                "‬‫סַכִּין‬"
            ),
            (
                # translation_word
                "посуда",
                # pronunciation_word
                "kelim",
                # hebrew_word_nikud
                "‫כֵּלִים‬‬"
            ),
            (
                # translation_word
                "тарелка",
                # pronunciation_word
                "ʦa'laχat",
                # hebrew_word_nikud
                "‫צַלַחַת‬‬"
            ),
            (
                # translation_word
                "блюдце",
                # pronunciation_word
                "taχtit",
                # hebrew_word_nikud
                "‬‫תַחתִית‬"
            ),
            (
                # translation_word
                "стакан",
                # pronunciation_word
                "kos",
                # hebrew_word_nikud
                "‫כּוֹס‬‬"
            ),
            (
                # translation_word
                "чашка",
                # pronunciation_word
                "'sefel",
                # hebrew_word_nikud
                "‬‫סֵפֶל‬"
            ),
            (
                # translation_word
                "сахарница",
                # pronunciation_word
                "mis'keret",
                # hebrew_word_nikud
                "‬‫מִסכֶּרֶת‬"
            ),
            (
                # translation_word
                "солонка",
                # pronunciation_word
                "milχiya",
                # hebrew_word_nikud
                "‬‫מִלחִייָה‬"
            ),
            (
                # translation_word
                "кастрюля",
                # pronunciation_word
                "sir",
                # hebrew_word_nikud
                "‫סִיר‬‬"
            ),
            (
                # translation_word
                "сковородка",
                # pronunciation_word
                "maχvat",
                # hebrew_word_nikud
                "‬‫מַחבַת‬"
            ),
            (
                # translation_word
                "дуршлаг",
                # pronunciation_word
                "mis'nenet",
                # hebrew_word_nikud
                "‬‫מִסנֶנֶת‬"
            ),
            (
                # translation_word
                "поднос",
                # pronunciation_word
                "magaʃ",
                # hebrew_word_nikud
                "‫מַגָש‬‬"
            ),
            (
                # translation_word
                "бутылка",
                # pronunciation_word
                "bakbuk",
                # hebrew_word_nikud
                "‬‫בַּקבּוּק‬"
            ),
            (
                # translation_word
                "штопор",
                # pronunciation_word
                "maχleʦ",
                # hebrew_word_nikud
                "‫מַחלֵץ‬‬"
            ),
            (
                # translation_word
                "мусор (отходы)",
                # pronunciation_word
                "'zevel",
                # hebrew_word_nikud
                "‫זֶבֶל‬‬"
            ),
            (
                # translation_word
                "мусорное ведро",
                # pronunciation_word
                "paχ 'zevel",
                # hebrew_word_nikud
                "פַּח‬‬‬‬‬‬‬ ‫זֶבֶל‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "98. Ванная комната",
        # words
        [
            (
                # translation_word
                "ванная комната",
                # pronunciation_word
                "χadar am'batya",
                # hebrew_word_nikud
                "‬חֲדַר‬‬‬‬‬‬‬ ‫אַמבַּטיָה‬"
            ),
            (
                # translation_word
                "вода",
                # pronunciation_word
                "'mayim",
                # hebrew_word_nikud
                "‬‫מַיִם‬"
            ),
            (
                # translation_word
                "кран",
                # pronunciation_word
                "'berez",
                # hebrew_word_nikud
                "‬‫בֶּרֶז‬"
            ),
            (
                # translation_word
                "горячая вода",
                # pronunciation_word
                "'mayim χamim",
                # hebrew_word_nikud
                "מַיִם‬‬‬‬‬‬‬ ‫חָמִים‬‬"
            ),
            (
                # translation_word
                "холодная вода",
                # pronunciation_word
                "'mayim karim",
                # hebrew_word_nikud
                "‬מַיִם‬‬‬‬‬‬‬ ‫קַרִים‬"
            ),
            (
                # translation_word
                "зубная паста",
                # pronunciation_word
                "miʃχat ʃi'nayim",
                # hebrew_word_nikud
                "מִשחַת‬‬‬‬‬‬‬ ‫שִינַיִים‬‬"
            ),
            (
                # translation_word
                "чистить зубы",
                # pronunciation_word
                "leʦaχ'ʦeaχ ʃi'nayim",
                # hebrew_word_nikud
                "לְצַחצֵח‬‬‬‬‬‬‬ ‫שִינַיִים‬‬"
            ),
            (
                # translation_word
                "зубная щётка",
                # pronunciation_word
                "miv'reʃet ʃi'nayim",
                # hebrew_word_nikud
                "מִברֶשֶת‬‬‬‬‬‬‬ ‫שִינַיִים‬‬"
            ),
            (
                # translation_word
                "бриться",
                # pronunciation_word
                "lehitga'leaχ",
                # hebrew_word_nikud
                "‫לְהִתגַלֵח‬‬"
            ),
            (
                # translation_word
                "пена для бритья",
                # pronunciation_word
                "'keʦef gi'luaχ",
                # hebrew_word_nikud
                "‬קֶצֵף‬‬‬‬‬‬‬ ‫גִילוּח‬"
            ),
            (
                # translation_word
                "бритва",
                # pronunciation_word
                "'taʿar",
                # hebrew_word_nikud
                "‫תַעַר‬‬"
            ),
            (
                # translation_word
                "мыть",
                # pronunciation_word
                "liʃtof",
                # hebrew_word_nikud
                "‬‫לִשטוֹף‬"
            ),
            (
                # translation_word
                "мыться",
                # pronunciation_word
                "lehitraχeʦ",
                # hebrew_word_nikud
                "‫לְהִתרַחֵץ‬‬"
            ),
            (
                # translation_word
                "душ",
                # pronunciation_word
                "mik'laχat",
                # hebrew_word_nikud
                "‬‫מִקלַחַת‬"
            ),
            (
                # translation_word
                "принимать душ",
                # pronunciation_word
                "lehitka'leaχ",
                # hebrew_word_nikud
                "‫לְהִתקַלֵח‬‬"
            ),
            (
                # translation_word
                "ванна",
                # pronunciation_word
                "am'batya",
                # hebrew_word_nikud
                "‫אַמבַּטיָה‬‬"
            ),
            (
                # translation_word
                "унитаз",
                # pronunciation_word
                "asla",
                # hebrew_word_nikud
                "‫אַסלָה‬‬"
            ),
            (
                # translation_word
                "раковина",
                # pronunciation_word
                "kiyor",
                # hebrew_word_nikud
                "‫כִּיוֹר‬‬"
            ),
            (
                # translation_word
                "мыло",
                # pronunciation_word
                "sabon",
                # hebrew_word_nikud
                "‫סַבּוֹן‬‬"
            ),
            (
                # translation_word
                "мыльница",
                # pronunciation_word
                "saboniya",
                # hebrew_word_nikud
                "‫סַבּוֹנִייָה‬‬"
            ),
            (
                # translation_word
                "губка",
                # pronunciation_word
                "sfog 'lifa",
                # hebrew_word_nikud
                "‬ספוֹג‬‬‬‬‬‬‬ ‫לִיפָה‬"
            ),
            (
                # translation_word
                "шампунь",
                # pronunciation_word
                "ʃampu",
                # hebrew_word_nikud
                "‫שַמפּו‬"
            ),
            (
                # translation_word
                "полотенце",
                # pronunciation_word
                "ma'gevet",
                # hebrew_word_nikud
                "‫מַגֶבֶת‬"
            ),
            (
                # translation_word
                "халат (махровый)",
                # pronunciation_word
                "χaluk raχaʦa",
                # hebrew_word_nikud
                "חֲלוּק‬‬‬‬‬‬‬ ‫רַחְצָה‬‬"
            ),
            (
                # translation_word
                "стирка",
                # pronunciation_word
                "kvisa",
                # hebrew_word_nikud
                "‬‫כּבִיסָה‬"
            ),
            (
                # translation_word
                "стиральная машина",
                # pronunciation_word
                "meχonat kvisa",
                # hebrew_word_nikud
                "‬מְכוֹנַת‬‬‬‬‬‬‬ ‫כּבִיסָה‬"
            ),
            (
                # translation_word
                "стирать бельё",
                # pronunciation_word
                "leχabes",
                # hebrew_word_nikud
                "‫לְכַבֵּס‬‬"
            ),
            (
                # translation_word
                "стиральный порошок",
                # pronunciation_word
                "avkat kvisa",
                # hebrew_word_nikud
                "‬אַבקַת‬‬‬‬‬‬‬ ‫כּבִיסָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "99. Бытовая техника",
        # words
        [
            (
                # translation_word
                "телевизор",
                # pronunciation_word
                "tele'vizya",
                # hebrew_word_nikud
                "‫טֶלֶווִיזיָה‬‬"
            ),
            (
                # translation_word
                "видеокамера",
                # pronunciation_word
                "maʦlemat 'videʾo",
                # hebrew_word_nikud
                "‬מַצלֵמַת‬‬‬‬‬‬‬ ‫וִידֶאו‬"
            ),
            (
                # translation_word
                "цифровой фотоаппарат",
                # pronunciation_word
                "maʦlema digi'talit",
                # hebrew_word_nikud
                "מַצלֵמָה‬‬‬‬‬‬‬ ‫דִיגִיטָלִית‬‬"
            ),
            (
                # translation_word
                "пылесос",
                # pronunciation_word
                "ʃoʾev avak",
                # hebrew_word_nikud
                "‬שוֹאֵב‬‬‬‬‬‬‬ ‫אָבָק‬"
            ),
            (
                # translation_word
                "утюг",
                # pronunciation_word
                "magheʦ",
                # hebrew_word_nikud
                "‬‫מַגהֵץ‬"
            ),
            (
                # translation_word
                "гладильная доска",
                # pronunciation_word
                "'kereʃ gihuʦ",
                # hebrew_word_nikud
                "‬קֶרֶש‬‬‬‬‬‬‬ ‫גִיהוּץ‬"
            ),
            (
                # translation_word
                "мобильный телефон",
                # pronunciation_word
                "'telefon nayad",
                # hebrew_word_nikud
                "‬טֶלֶפוֹן‬ ‬‬‬‬‬‬‫נַייָד‬"
            ),
            (
                # translation_word
                "микрофон",
                # pronunciation_word
                "mikrofon",
                # hebrew_word_nikud
                "‫מִיקרוֹפוֹן‬‬"
            ),
            (
                # translation_word
                "наушники",
                # pronunciation_word
                "ozniyot",
                # hebrew_word_nikud
                "‬‫אוֹזנִיוֹת‬"
            ),
            (
                # translation_word
                "пульт",
                # pronunciation_word
                "'ʃelet",
                # hebrew_word_nikud
                "‫שֶלֶט‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "100. Ремонт",
        # words
        [
            (
                # translation_word
                "ремонт",
                # pronunciation_word
                "ʃipuʦ",
                # hebrew_word_nikud
                "‫שִיפּוּץ‬‬"
            ),
            (
                # translation_word
                "делать ремонт",
                # pronunciation_word
                "leʃapeʦ",
                # hebrew_word_nikud
                "‫לְשַפֵּץ‬‬"
            ),
            (
                # translation_word
                "ремонтировать",
                # pronunciation_word
                "letaken",
                # hebrew_word_nikud
                "‫לְתַקֵן‬‬"
            ),
            (
                # translation_word
                "приводить в порядок",
                # pronunciation_word
                "lesader",
                # hebrew_word_nikud
                "‫לְסַדֵר‬‬"
            ),
            (
                # translation_word
                "переделывать",
                # pronunciation_word
                "laʿasot meχadaʃ",
                # hebrew_word_nikud
                "לַעֲשׂוֹת‬ ‬‬‬‬‬‬‫מֵחָדָש‬‬"
            ),
            (
                # translation_word
                "краска",
                # pronunciation_word
                "'ʦeva",
                # hebrew_word_nikud
                "‫צֶבַע‬‬"
            ),
            (
                # translation_word
                "красить",
                # pronunciation_word
                "liʦ'boʿa",
                # hebrew_word_nikud
                "‬‫לִצבּוֹע‬"
            ),
            (
                # translation_word
                "оклеить обоями",
                # pronunciation_word
                "lehadbik ta'petim",
                # hebrew_word_nikud
                "לְהַדבִּיק‬ ‬‬‬‬‬‬‫טַפֶּטִים‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "101. Водопровод",
        # words
        [
            (
                # translation_word
                "вода",
                # pronunciation_word
                "'mayim",
                # hebrew_word_nikud
                "‬‫מַיִם‬"
            ),
            (
                # translation_word
                "кран, вентель",
                # pronunciation_word
                "'berez",
                # hebrew_word_nikud
                "‫בֶּרֶז‬‬"
            ),
            (
                # translation_word
                "капать",
                # pronunciation_word
                "letaftef",
                # hebrew_word_nikud
                "‬‫לְטַפטֵף‬"
            ),
            (
                # translation_word
                "течь (протекать)",
                # pronunciation_word
                "lidlof",
                # hebrew_word_nikud
                "‫לִדלוֹף‬‬"
            ),
            (
                # translation_word
                "лужа (на полу и т.п.)",
                # pronunciation_word
                "ʃlulit",
                # hebrew_word_nikud
                "‫שלוּלִית‬‬"
            ),
            (
                # translation_word
                "труба",
                # pronunciation_word
                "ʦinor",
                # hebrew_word_nikud
                "‫צִינוֹר‬‬"
            ),
            (
                # translation_word
                "засориться (о трубе)",
                # pronunciation_word
                "lehisatem",
                # hebrew_word_nikud
                "‫לְהִיסָתֵם‬‬"
            ),
            (
                # translation_word
                "инструменты",
                # pronunciation_word
                "klei avoda",
                # hebrew_word_nikud
                "‬כּלֵי‬ ‫עֲבוֹדָה‬"
            ),
            (
                # translation_word
                "разводной ключ",
                # pronunciation_word
                "maf'teaχ mitkavnen",
                # hebrew_word_nikud
                "‬מַפתֵח‬ ‫מִתכַּוונֵן‬"
            ),
            (
                # translation_word
                "открутить",
                # pronunciation_word
                "lif'toaχ",
                # hebrew_word_nikud
                "‫לִפתוֹח‬‬"
            ),
            (
                # translation_word
                "закрутить",
                # pronunciation_word
                "lehavrig",
                # hebrew_word_nikud
                "‬‫לְהַברִיג‬"
            ),
            (
                # translation_word
                "прочищать",
                # pronunciation_word
                "lif'toaχ et hastima",
                # hebrew_word_nikud
                "לִפתוֹח‬ ‫אֶת‬ ‫הַסתִימָה‬‬"
            ),
            (
                # translation_word
                "сантехник",
                # pronunciation_word
                "ʃravrav",
                # hebrew_word_nikud
                "‫שרַברָב‬‬"
            ),
            (
                # translation_word
                "подвал",
                # pronunciation_word
                "martef",
                # hebrew_word_nikud
                "‫מַרתֵף‬‬"
            ),
            (
                # translation_word
                "канализация",
                # pronunciation_word
                "biyuv",
                # hebrew_word_nikud
                "‫בִּיוּב‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "102. Пожар",
        # words
        [
            (
                # translation_word
                "пожар",
                # pronunciation_word
                "srefa",
                # hebrew_word_nikud
                "‬‫שׂרֵיפָה‬"
            ),
            (
                # translation_word
                "пламя",
                # pronunciation_word
                "lehava",
                # hebrew_word_nikud
                "‬‫לֶהָבָה‬"
            ),
            (
                # translation_word
                "дым",
                # pronunciation_word
                "aʃan",
                # hebrew_word_nikud
                "‫עָשָן‬‬"
            ),
            (
                # translation_word
                "костёр",
                # pronunciation_word
                "medura",
                # hebrew_word_nikud
                "‬‫מְדוּרָה‬"
            ),
            (
                # translation_word
                "бензин",
                # pronunciation_word
                "'delek",
                # hebrew_word_nikud
                "‫דֶלֶק‬‬"
            ),
            (
                # translation_word
                "керосин",
                # pronunciation_word
                "kerosin",
                # hebrew_word_nikud
                "‫קֶרוֹסִין‬‬"
            ),
            (
                # translation_word
                "горючий",
                # pronunciation_word
                "dalik",
                # hebrew_word_nikud
                "‬‫דָלִיק‬"
            ),
            (
                # translation_word
                "взрывоопасный",
                # pronunciation_word
                "nafiʦ",
                # hebrew_word_nikud
                "‫נָפִיץ‬‬"
            ),
            (
                # translation_word
                "безопасность",
                # pronunciation_word
                "betiχut",
                # hebrew_word_nikud
                "‬‫בְּטִיחוּת‬"
            ),
            (
                # translation_word
                "опасность",
                # pronunciation_word
                "sakana",
                # hebrew_word_nikud
                "‫סַכָּנָה‬‬"
            ),
            (
                # translation_word
                "опасный",
                # pronunciation_word
                "mesukan",
                # hebrew_word_nikud
                "‫מְסוּכָּן‬‬"
            ),
            (
                # translation_word
                "взрыв",
                # pronunciation_word
                "piʦuʦ",
                # hebrew_word_nikud
                "‫פִּיצוּץ‬‬"
            ),
            (
                # translation_word
                "гореть",
                # pronunciation_word
                "laʿalot beʾeʃ",
                # hebrew_word_nikud
                "לַעֲלוֹת‬ ‫בְּאֵש‬‬"
            ),
            (
                # translation_word
                "вызвать пожарных",
                # pronunciation_word
                "lehazmin meχabei eʃ",
                # hebrew_word_nikud
                "‬לְהַזמִין‬ ‫מְכַבֵּי‬ ‫אֵש‬"
            ),
            (
                # translation_word
                "пожарная машина",
                # pronunciation_word
                "'reχev kibui",
                # hebrew_word_nikud
                "‬רֶכֶב‬ ‫כִּיבּוּי‬"
            ),
            (
                # translation_word
                "шланг",
                # pronunciation_word
                "zarnuk",
                # hebrew_word_nikud
                "‬‫זַרנוּק‬"
            ),
            (
                # translation_word
                "огнетушитель",
                # pronunciation_word
                "mataf",
                # hebrew_word_nikud
                "‫מַטָף‬‬"
            ),
            (
                # translation_word
                "кричать",
                # pronunciation_word
                "liʦʿok",
                # hebrew_word_nikud
                "‫לִצעוֹק‬‬"
            ),
            (
                # translation_word
                "звать на помощь",
                # pronunciation_word
                "likro leʿezra",
                # hebrew_word_nikud
                "‬לִקרוֹא‬ ‫לְעֶזרָה‬"
            ),
            (
                # translation_word
                "спасатель",
                # pronunciation_word
                "maʦil",
                # hebrew_word_nikud
                "‬‫מַצִיל‬"
            ),
            (
                # translation_word
                "спасать",
                # pronunciation_word
                "lehaʦil",
                # hebrew_word_nikud
                "‫לְהַצִיל‬‬"
            ),
            (
                # translation_word
                "приехать",
                # pronunciation_word
                "leha'giʿa",
                # hebrew_word_nikud
                "‬‫לְהַגִיע‬"
            ),
            (
                # translation_word
                "рухнуть",
                # pronunciation_word
                "likros",
                # hebrew_word_nikud
                "‫לִקרוֹס‬‬"
            ),
            (
                # translation_word
                "пепел",
                # pronunciation_word
                "'efer",
                # hebrew_word_nikud
                "‬‫אֵפֶר‬"
            ),
            (
                # translation_word
                "задохнуться",
                # pronunciation_word
                "lehiχanek",
                # hebrew_word_nikud
                "‬‫לְהֵיחָנֵק‬"
            ),
            (
                # translation_word
                "погибнуть",
                # pronunciation_word
                "lehihareg",
                # hebrew_word_nikud
                "‫לְהֵיהָרֵג‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "103. Офис. Работа в офисе",
        # words
        [
            (
                # translation_word
                "офис",
                # pronunciation_word
                "misrad",
                # hebrew_word_nikud
                "‫מִשׂרָד‬‬"
            ),
            (
                # translation_word
                "ресепшн",
                # pronunciation_word
                "kabala",
                # hebrew_word_nikud
                "‬‫קַבָּלָה‬"
            ),
            (
                # translation_word
                "секретарь(женщина)",
                # pronunciation_word
                "mazkira",
                # hebrew_word_nikud
                "‬‫מַזכִּירָה‬"
            ),
            (
                # translation_word
                "директор, менеджер",
                # pronunciation_word
                "menahel",
                # hebrew_word_nikud
                "‫מְנַהֵל‬‬"
            ),
            (
                # translation_word
                "бухгалтер",
                # pronunciation_word
                "menahel χeʃbonot",
                # hebrew_word_nikud
                "‬מְנַהֵל‬ ‫חֶשבּוֹנוֹת‬"
            ),
            (
                # translation_word
                "сотрудник",
                # pronunciation_word
                "oved",
                # hebrew_word_nikud
                "‬‫עוֹבֵד‬"
            ),
            (
                # translation_word
                "мебель",
                # pronunciation_word
                "rehitim",
                # hebrew_word_nikud
                "‫רָהִיטִים‬‬"
            ),
            (
                # translation_word
                "компьютер",
                # pronunciation_word
                "maχʃev",
                # hebrew_word_nikud
                "‫מַחשֵב‬‬"
            ),
            (
                # translation_word
                "принтер",
                # pronunciation_word
                "mad'peset",
                # hebrew_word_nikud
                "‫מַדפֶּסֶת‬‬"
            ),
            (
                # translation_word
                "копировальный аппарат",
                # pronunciation_word
                "meχonat ʦilum",
                # hebrew_word_nikud
                "‬מְכוֹנַת‬ ‫צִילוּם‬"
            ),
            (
                # translation_word
                "бумага",
                # pronunciation_word
                "neyar",
                # hebrew_word_nikud
                "‫נְייָר‬‬"
            ),
            (
                # translation_word
                "канцтовары",
                # pronunciation_word
                "ʦiyud misradi",
                # hebrew_word_nikud
                "צִיוּד‬ ‫מִשׂרָדִי‬‬"
            ),
            (
                # translation_word
                "коврик для мыши",
                # pronunciation_word
                "ʃa'tiaχ leʿaχbar",
                # hebrew_word_nikud
                "שָטִיח‬ ‫לְעַכבָּר‬‬"
            ),
            (
                # translation_word
                "лист (бумаги и т.п.)",
                # pronunciation_word
                "daf",
                # hebrew_word_nikud
                "‫דַף‬‬"
            ),
            (
                # translation_word
                "папка",
                # pronunciation_word
                "klaser",
                # hebrew_word_nikud
                "‫קלָסֶר‬‬"
            ),
            (
                # translation_word
                "документация",
                # pronunciation_word
                "tiʿud",
                # hebrew_word_nikud
                "‫תִיעוּד‬‬"
            ),
            (
                # translation_word
                "образец",
                # pronunciation_word
                "dugma",
                # hebrew_word_nikud
                "‫דוּגמָה‬‬"
            ),
            (
                # translation_word
                "тренинг",
                # pronunciation_word
                "yeʃivat hadraχa",
                # hebrew_word_nikud
                "יְשִיבַת‬ ‫הַדרָכָה‬‬"
            ),
            (
                # translation_word
                "перерыв на обед",
                # pronunciation_word
                "hafsakat ʦaha'rayim",
                # hebrew_word_nikud
                "הַפסָקַת‬ ‫צָהֳרַיִים‬‬"
            ),
            (
                # translation_word
                "делать копию",
                # pronunciation_word
                "leʦalem mismaχ",
                # hebrew_word_nikud
                "לְצַלֵם‬ ‫מִסמָך‬‬"
            ),
             (
                # translation_word
                "позвонить",
                # pronunciation_word
                "lehitkaʃer",
                # hebrew_word_nikud
                "‫לְהִתקַשֵר‬‬"
            ),
            (
                # translation_word
                "ответить",
                # pronunciation_word
                "laʿanot",
                # hebrew_word_nikud
                "‬‫לְעַנוֹת‬"
            ),
             (
                # translation_word
                "соединить (по телефону)",
                # pronunciation_word
                "lekaʃer",
                # hebrew_word_nikud
                "‬‫לְקַשֵר‬"
            ),
            (
                # translation_word
                "назначать (встречу)",
                # pronunciation_word
                "lik'boʿa pgiʃa",
                # hebrew_word_nikud
                "‬‫פּגִישָה‬ ַ‫לִקבּוֹע‬"
            ),
             (
                # translation_word
                "демонстрировать",
                # pronunciation_word
                "lehadgim",
                # hebrew_word_nikud
                "‫לְהַדגִים‬‬"
            ),
            (
                # translation_word
                "отсутствовать",
                # pronunciation_word
                "leheʿader",
                # hebrew_word_nikud
                "‫לְהֵיעָדֵר‬‬"
            ),
            (
                # translation_word
                "пропуск (отсутствие)",
                # pronunciation_word
                "heʿadrut",
                # hebrew_word_nikud
                "‬‫הֵיעָדרוּת‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "104. Работа. Бизнес-процессы - 1",
        # words
        [
            (
                # translation_word
                "дело, бизнес",
                # pronunciation_word
                "'esek",
                # hebrew_word_nikud
                "‫עֵסֶק‬‬"
            ),
            (
                # translation_word
                "дело (занятие)",
                # pronunciation_word
                "isuk",
                # hebrew_word_nikud
                "‬‫עִיסוּק‬"
            ),
            (
                # translation_word
                "фирма",
                # pronunciation_word
                "χevra",
                # hebrew_word_nikud
                "‬‫חֶברָה‬"
            ),
            (
                # translation_word
                "корпорация",
                # pronunciation_word
                "taʾagid",
                # hebrew_word_nikud
                "‬‫תַאֲגִיד‬"
            ),
            (
                # translation_word
                "агентство",
                # pronunciation_word
                "soχnut",
                # hebrew_word_nikud
                "‬‫סוֹכנוּת‬"
            ),
            (
                # translation_word
                "договор",
                # pronunciation_word
                "heskem",
                # hebrew_word_nikud
                "‫הֶסכֵּם‬‬"
            ),
            (
                # translation_word
                "контракт",
                # pronunciation_word
                "χoze",
                # hebrew_word_nikud
                "‫חוִזֶה‬‬"
            ),
            (
                # translation_word
                "сделка",
                # pronunciation_word
                "iska",
                # hebrew_word_nikud
                "‫עִסקָה‬‬"
            ),
            (
                # translation_word
                "заказ",
                # pronunciation_word
                "hazmana",
                # hebrew_word_nikud
                "‫הַזמָנָה‬‬"
            ),
            (
                # translation_word
                "условие (договора)",
                # pronunciation_word
                "tnai",
                # hebrew_word_nikud
                "‬‫תנַאי‬"
            ),
            (
                # translation_word
                "оптом",
                # pronunciation_word
                "besitonut",
                # hebrew_word_nikud
                "‬‫בְּסִיטוֹנוּת‬"
            ),
            (
                # translation_word
                "оптовый",
                # pronunciation_word
                "sitonaʾi",
                # hebrew_word_nikud
                "‫סִיטוֹנָאִי‬‬"
            ),
            (
                # translation_word
                "розничный",
                # pronunciation_word
                "kimʿoni",
                # hebrew_word_nikud
                "‫קִמעוֹנִי‬‬"
            ),
            (
                # translation_word
                "конкурент",
                # pronunciation_word
                "mitχare",
                # hebrew_word_nikud
                "‬‫מִתחָרֶה‬"
            ),
            (
                # translation_word
                "конкуренция",
                # pronunciation_word
                "taχarut",
                # hebrew_word_nikud
                "‫תַחֲרוּת‬‬"
            ),
            (
                # translation_word
                "конкурировать",
                # pronunciation_word
                "lehitχarot",
                # hebrew_word_nikud
                "‫לְהִתחָרוֹת‬‬"
            ),
            (
                # translation_word
                "партнёр (соучредитель)",
                # pronunciation_word
                "ʃutaf",
                # hebrew_word_nikud
                "‬‫שוּתָף‬"
            ),
            (
                # translation_word
                "кризис",
                # pronunciation_word
                "maʃber",
                # hebrew_word_nikud
                "‬‫מַשבֵּר‬"
            ),
            (
                # translation_word
                "банкротство",
                # pronunciation_word
                "pʃitat 'regel",
                # hebrew_word_nikud
                "‬פּשִיטַת‬ ‫רֶגֶל‬"
            ),
            (
                # translation_word
                "обанкротиться",
                # pronunciation_word
                "lifʃot 'regel",
                # hebrew_word_nikud
                "לִפשוֹט‬ ‫רֶגֶל‬‬"
            ),
            (
                # translation_word
                "трудность",
                # pronunciation_word
                "'koʃi",
                # hebrew_word_nikud
                "‫קוֹשִי‬‬"
            ),
            (
                # translation_word
                "проблема",
                # pronunciation_word
                "beʿaya",
                # hebrew_word_nikud
                "‬‫בְּעָיָה‬"
            ),
            (
                # translation_word
                "катастрофа",
                # pronunciation_word
                "ason",
                # hebrew_word_nikud
                "‫אָסוֹן‬‬"
            ),
            (
                # translation_word
                "экономика",
                # pronunciation_word
                "kalkala",
                # hebrew_word_nikud
                "‫כַּלכָּלָה‬‬"
            ),
            (
                # translation_word
                "экономический",
                # pronunciation_word
                "kalkali",
                # hebrew_word_nikud
                "‫כַּלכָּלִי‬‬"
            ),
            (
                # translation_word
                "цель",
                # pronunciation_word
                "matara",
                # hebrew_word_nikud
                "‫מַטָרָה‬‬"
            ),
            (
                # translation_word
                "задача",
                # pronunciation_word
                "mesima",
                # hebrew_word_nikud
                "‬‫מְשִׂימָה‬"
            ),
            (
                # translation_word
                "торговать",
                # pronunciation_word
                "lisχor",
                # hebrew_word_nikud
                "‫לִסחוֹר‬‬"
            ),
            (
                # translation_word
                "сеть (дистрибьюторов)",
                # pronunciation_word
                "'reʃet",
                # hebrew_word_nikud
                "‫רֶשֶת‬‬"
            ),
            (
                # translation_word
                "лидер",
                # pronunciation_word
                "manhig",
                # hebrew_word_nikud
                "‫מַנהִיג‬‬"
            ),
            (
                # translation_word
                "монополия",
                # pronunciation_word
                "'monopol",
                # hebrew_word_nikud
                "‫מוֹנוֹפּוֹל‬‬"
            ),
            (
                # translation_word
                "теория",
                # pronunciation_word
                "te'ʾorya",
                # hebrew_word_nikud
                "‬‫תֵיאוֹריָה‬"
            ),
                (
                # translation_word
                "опыт (знания)",
                # pronunciation_word
                "nisayon",
                # hebrew_word_nikud
                "‫נִיסָיוֹן‬‬"
            ),
            (
                # translation_word
                "развитие",
                # pronunciation_word
                "pi'tuaχ",
                # hebrew_word_nikud
                "‫פִּיתוּח‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "105. Работа. Бизнес-процессы - 2",
        # words
        [
            (
                # translation_word
                "выгода",
                # pronunciation_word
                "'revaχ",
                # hebrew_word_nikud
                "‫רֶווַח‬‬"
            ),
            (
                # translation_word
                "заработная плата",
                # pronunciation_word
                "mas'koret",
                # hebrew_word_nikud
                "‫מַשׂכּוֹרֶת‬‬"
            ),
            (
                # translation_word
                "командировка",
                # pronunciation_word
                "nesiʿa batafkid",
                # hebrew_word_nikud
                "‬נְסִיעָה‬ ‫בַּתַפקִיד‬"
            ),
            (
                # translation_word
                "контролировать",
                # pronunciation_word
                "liʃlot",
                # hebrew_word_nikud
                "‫לִשלוֹט‬‬"
            ),
            (
                # translation_word
                "конференция",
                # pronunciation_word
                "kinus",
                # hebrew_word_nikud
                "‬‫כִּינוּס‬"
            ),
            (
                # translation_word
                "лицензия",
                # pronunciation_word
                "riʃayon",
                # hebrew_word_nikud
                "‫רִישָיוֹן‬‬"
            ),
            (
                # translation_word
                "обязанность",
                # pronunciation_word
                "χova",
                # hebrew_word_nikud
                "‬‫חוֹבָה‬"
            ),
            (
                # translation_word
                "отменить",
                # pronunciation_word
                "levatel",
                # hebrew_word_nikud
                "‬‫לְבַטֵל‬"
            ),
            (
                # translation_word
                "отчёт",
                # pronunciation_word
                "doχ",
                # hebrew_word_nikud
                "‫דוֹח‬‬"
            ),
            (
                # translation_word
                "патент",
                # pronunciation_word
                "patent",
                # hebrew_word_nikud
                "‫פָּטֶנט‬‬"
            ),
            (
                # translation_word
                "премия",
                # pronunciation_word
                "'bonus",
                # hebrew_word_nikud
                "‬‫בּוֹנוּס‬"
            ),
            (
                # translation_word
                "профессиональный",
                # pronunciation_word
                "mikʦoʿi",
                # hebrew_word_nikud
                "‬‫מִקצוֹעִי‬"
            ),
            (
                # translation_word
                "репутация",
                # pronunciation_word
                "monitin",
                # hebrew_word_nikud
                "‬‫מוֹנִיטִין‬"
            ),
            (
                # translation_word
                "риск",
                # pronunciation_word
                "sikun",
                # hebrew_word_nikud
                "‬‫סִיכּוּן‬"
            ),
            (
                # translation_word
                "руководить (чем-л.)",
                # pronunciation_word
                "lenahel",
                # hebrew_word_nikud
                "‫לְנַהֵל‬‬"
            ),
            (
                # translation_word
                "собственность",
                # pronunciation_word
                "baʿalut",
                # hebrew_word_nikud
                "‫בַּעֲלוּת‬‬"
            ),
            (
                # translation_word
                "страхование жизни",
                # pronunciation_word
                "bi'tuaχ χayim",
                # hebrew_word_nikud
                "בִּיטוּח‬ ‫חַיִים‬‬"
            ),
            (
                # translation_word
                "страховать",
                # pronunciation_word
                "leva'teaχ",
                # hebrew_word_nikud
                "‬‫לבַטֵח‬"
            ),
            (
                # translation_word
                "страховка",
                # pronunciation_word
                "bi'tuaχ",
                # hebrew_word_nikud
                "‫בִּיטוּח‬‬"
            ),
            (
                # translation_word
                "услуга",
                # pronunciation_word
                "ʃirut",
                # hebrew_word_nikud
                "‬‫שִירוּת‬"
            ),
            (
                # translation_word
                "этап (работы и т.п.)",
                # pronunciation_word
                "ʃalav",
                # hebrew_word_nikud
                "‫שָלָב‬‬"
            ),
            (
                # translation_word
                "юридический",
                # pronunciation_word
                "miʃpati",
                # hebrew_word_nikud
                "‫מִשפָּטִי‬‬"
            ),
            (
                # translation_word
                "юрист",
                # pronunciation_word
                "oreχ din",
                # hebrew_word_nikud
                "עוֹרֵך‬ ‫דִין‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "106. Производство",
        # words
        [
            (
                # translation_word
                "фабрика",
                # pronunciation_word
                "beit χa'roʃet",
                # hebrew_word_nikud
                "‬בֵּית‬ ‫חֲרוֹשֶת‬"
            ),
            (
                # translation_word
                "цех",
                # pronunciation_word
                "agaf",
                # hebrew_word_nikud
                "‫אֲגַף‬‬"
            ),
            (
                # translation_word
                "производство",
                # pronunciation_word
                "mifʿal",
                # hebrew_word_nikud
                "‫מִפעָל‬‬"
            ),
            (
                # translation_word
                "промышленность",
                # pronunciation_word
                "taʿasiya",
                # hebrew_word_nikud
                "‫תַעֲשִׂייָה‬‬"
            ),
            (
                # translation_word
                "продукция",
                # pronunciation_word
                "to'ʦeret",
                # hebrew_word_nikud
                "‬‫תוֹצֶרֶת‬"
            ),
            (
                # translation_word
                "сырьё",
                # pronunciation_word
                "'χomer 'gelem",
                # hebrew_word_nikud
                "חוֹמֶר‬ ‫גֶלֶם‬‬"
            ),
            (
                # translation_word
                "рабочий",
                # pronunciation_word
                "poʿel",
                # hebrew_word_nikud
                "‫פּוֹעֵל‬‬"
            ),
            (
                # translation_word
                "рабочий день",
                # pronunciation_word
                "yom avoda",
                # hebrew_word_nikud
                "‬יום‬ ‫עֲבוֹדָה‬"
            ),
            (
                # translation_word
                "остановка (перерыв)",
                # pronunciation_word
                "hafsaka",
                # hebrew_word_nikud
                "‫הַפסָקָה‬‬"
            ),
            (
                # translation_word
                "собрание",
                # pronunciation_word
                "yeʃiva",
                # hebrew_word_nikud
                "‫יְשִיבָה‬‬"
            ),
            (
                # translation_word
                "план",
                # pronunciation_word
                "toχnit",
                # hebrew_word_nikud
                "‫תוֹכנִית‬‬"
            ),
            (
                # translation_word
                "качество",
                # pronunciation_word
                "eiχut",
                # hebrew_word_nikud
                "‫אֵיכוּת‬‬"
            ),
            (
                # translation_word
                "безопасность труда",
                # pronunciation_word
                "betiχut beavoda",
                # hebrew_word_nikud
                "‬בְּטִיחוּת‬ ‫בְעֲבוֹדָה‬"
            ),
            (
                # translation_word
                "забастовка",
                # pronunciation_word
                "ʃvita",
                # hebrew_word_nikud
                "‫שבִיתָה‬‬"
            ),
            (
                # translation_word
                "изобретать",
                # pronunciation_word
                "lehamʦi",
                # hebrew_word_nikud
                "‫לְהַמצִיא‬‬"
            ),
            (
                # translation_word
                "транспорт",
                # pronunciation_word
                "hovala",
                # hebrew_word_nikud
                "‬‫הוֹבָלָה‬"
            ),
            (
                # translation_word
                "станок",
                # pronunciation_word
                "meχonat ibud",
                # hebrew_word_nikud
                "מְכוֹנַת‬ ‫עִיבּוּד‬‬"
            ),
            (
                # translation_word
                "отходы",
                # pronunciation_word
                "'psolet taʿasiyatit",
                # hebrew_word_nikud
                "פּסוֹלֶת‬ ‫תַעֲשִׂייָתִית‬‬"
            ),
            (
                # translation_word
                "упаковать",
                # pronunciation_word
                "leʾeroz",
                # hebrew_word_nikud
                "‬‫לֶאֱרוֹז‬"
            ),
            (
                # translation_word
                "разгружать",
                # pronunciation_word
                "lifrok mitʿan",
                # hebrew_word_nikud
                "לִפרוֹק‬ ‫מִטעָן‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "107. Контракт",
        # words
        [
            (
                # translation_word
                "контракт",
                # pronunciation_word
                "χoze",
                # hebrew_word_nikud
                "‫חוִזֶה‬‬"
            ),
            (
                # translation_word
                "соглашение",
                # pronunciation_word
                "heskem",
                # hebrew_word_nikud
                "‫הֶסכֵּם‬‬"
            ),
            (
                # translation_word
                "приложение",
                # pronunciation_word
                "'sefaχ",
                # hebrew_word_nikud
                "‫סֶפַח‬‬"
            ),
            (
                # translation_word
                "заключить контракт",
                # pronunciation_word
                "laʿaroχ heskem",
                # hebrew_word_nikud
                "לַעֲרוֹך‬ ‫הֶסכֵּם‬‬"
            ),
            (
                # translation_word
                "подпись",
                # pronunciation_word
                "χatima",
                # hebrew_word_nikud
                "‬‫חֲתִימָה‬"
            ),
            (
                # translation_word
                "подписать",
                # pronunciation_word
                "laχtom",
                # hebrew_word_nikud
                "‬‫לַחתוֹם‬"
            ),
            (
                # translation_word
                "печать (на документе)",
                # pronunciation_word
                "χo'temet",
                # hebrew_word_nikud
                "‫חוֹתֶמֶת‬‬"
            ),
            (
                # translation_word
                "предмет договора",
                # pronunciation_word
                "nose haχoze",
                # hebrew_word_nikud
                "נוֹשֵׂא‬ ‫הַחוֹזֶה‬‬"
            ),
            (
                # translation_word
                "пункт (договора)",
                # pronunciation_word
                "seʿif",
                # hebrew_word_nikud
                "‫סְעִיף‬‬"
            ),
            (
                # translation_word
                "стороны",
                # pronunciation_word
                "ʦdadim",
                # hebrew_word_nikud
                "‬‫צדָדִים‬"
            ),
            (
                # translation_word
                "юридический адрес",
                # pronunciation_word
                "'ktovet miʃpatit",
                # hebrew_word_nikud
                "כּתוֹבֶת‬ ‫מִשפָּטִית‬‬"
            ),
            (
                # translation_word
                "нарушить контракт",
                # pronunciation_word
                "lehafer χoze",
                # hebrew_word_nikud
                "‬לְהָפֵר‬ ‫חוֹזֶה‬"
            ),
            (
                # translation_word
                "обязательство",
                # pronunciation_word
                "hitχaivut",
                # hebrew_word_nikud
                "‫הִתחַייבוּת‬‬"
            ),
            (
                # translation_word
                "ответственность",
                # pronunciation_word
                "aχrayut",
                # hebrew_word_nikud
                "‬‫אַחרָיוּת‬"
            ),
            (
                # translation_word
                "форс-мажор",
                # pronunciation_word
                "'koaχ elyon",
                # hebrew_word_nikud
                "‬כּוֹח‬ ‫עֶליוֹן‬"
            ),
            (
                # translation_word
                "спор",
                # pronunciation_word
                "vi'kuaχ",
                # hebrew_word_nikud
                "‬‫וִיכּוּח‬"
            ),
            (
                # translation_word
                "штрафные санкции",
                # pronunciation_word
                "iʦumim",
                # hebrew_word_nikud
                "‬‫עִיצוּמִים‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "108. Импорт-Экспорт",
        # words
        [
            (
                # translation_word
                "импорт",
                # pronunciation_word
                "ye'vuʾa",
                # hebrew_word_nikud
                "‫יְבוּא‬‬"
            ),
            (
                # translation_word
                "импортировать",
                # pronunciation_word
                "leyabe",
                # hebrew_word_nikud
                "‫לְייַבֵּא‬‬"
            ),
            (
                # translation_word
                "импортный",
                # pronunciation_word
                "meyuba",
                # hebrew_word_nikud
                "‫מְיוּבָּא‬‬"
            ),
            (
                # translation_word
                "экспорт",
                # pronunciation_word
                "yitsu",
                # hebrew_word_nikud
                "‬‫יִיצוּא‬"
            ),
            (
                # translation_word
                "экспортировать",
                # pronunciation_word
                "leyaʦe",
                # hebrew_word_nikud
                "‫לְייַצֵא‬‬"
            ),
            (
                # translation_word
                "товар",
                # pronunciation_word
                "sχora",
                # hebrew_word_nikud
                "‬‫סחוֹרָה‬"
            ),
            (
                # translation_word
                "вес",
                # pronunciation_word
                "miʃkal",
                # hebrew_word_nikud
                "‫מִשקָל‬‬"
            ),
            (
                # translation_word
                "объём",
                # pronunciation_word
                "'nefaχ",
                # hebrew_word_nikud
                "‫נֶפַח‬‬"
            ),
            (
                # translation_word
                "производитель",
                # pronunciation_word
                "yaʦran",
                # hebrew_word_nikud
                "‬‫יַצרָן‬"
            ),
            (
                # translation_word
                "граница",
                # pronunciation_word
                "gvul",
                # hebrew_word_nikud
                "‬‫גבוּל‬"
            ),
            (
                # translation_word
                "таможня",
                # pronunciation_word
                "'meχes",
                # hebrew_word_nikud
                "‫מֶכֶס‬‬"
            ),
            (
                # translation_word
                "таможенная пошлина",
                # pronunciation_word
                "mas 'meχes",
                # hebrew_word_nikud
                "מַס‬ ‫מֶכֶס‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "109. Финансы",
        # words
        [
            (
                # translation_word
                "подешеветь",
                # pronunciation_word
                "la'redet bemeχir",
                # hebrew_word_nikud
                "‬לָרֶדֶת‬ ‫בְּמְחִיר‬"
            ),
            (
                # translation_word
                "подорожать",
                # pronunciation_word
                "lehityaker",
                # hebrew_word_nikud
                "‫לְהִתייַקֵר‬‬"
            ),
            (
                # translation_word
                "инвестиции",
                # pronunciation_word
                "haʃkaʿot",
                # hebrew_word_nikud
                "‬‫הַשקָעוֹת‬"
            ),
            (
                # translation_word
                "инвестировать",
                # pronunciation_word
                "lehaʃ'kiʿa",
                # hebrew_word_nikud
                "‫לְהַשקִיע‬‬"
            ),
            (
                # translation_word
                "процент",
                # pronunciation_word
                "aχuz",
                # hebrew_word_nikud
                "‬‫אָחוּז‬"
            ),
            (
                # translation_word
                "проценты (доход)",
                # pronunciation_word
                "ribit",
                # hebrew_word_nikud
                "‫רִיבִּית‬‬"
            ),
            (
                # translation_word
                "прибыль",
                # pronunciation_word
                "'revaχ",
                # hebrew_word_nikud
                "‫רֶווַח‬‬"
            ),
            (
                # translation_word
                "налог",
                # pronunciation_word
                "mas",
                # hebrew_word_nikud
                "‬‫מַס‬"
            ),
            (
                # translation_word
                "валюта",
                # pronunciation_word
                "mat'beʿa",
                # hebrew_word_nikud
                "‬‫מַטבֵּע‬"
            ),
            (
                # translation_word
                "национальный",
                # pronunciation_word
                "leʾumi",
                # hebrew_word_nikud
                "‫לְאוּמִי‬‬"
            ),
            (
                # translation_word
                "обмен",
                # pronunciation_word
                "hamara",
                # hebrew_word_nikud
                "‬‫הֲמָרָה‬"
            ),
            (
                # translation_word
                "инфляция",
                # pronunciation_word
                "inf'laʦya",
                # hebrew_word_nikud
                "‬‫אִינפלַציָה‬"
            ),
            (
                # translation_word
                "капитал",
                # pronunciation_word
                "hon",
                # hebrew_word_nikud
                "‫הוֹן‬‬"
            ),
            (
                # translation_word
                "доход",
                # pronunciation_word
                "haχnasa",
                # hebrew_word_nikud
                "‬‫הַכנָסָה‬"
            ),
            (
                # translation_word
                "ресурсы",
                # pronunciation_word
                "maʃʾabim",
                # hebrew_word_nikud
                "‬‫מַשאַבִּים‬"
            ),
            (
                # translation_word
                "денежные средства",
                # pronunciation_word
                "emʦaʿim kaspiyim",
                # hebrew_word_nikud
                "‬אֶמצָעִים‬ ‫כַּספִּייִם‬"
            ),
            (
                # translation_word
                "сократить (расходы)",
                # pronunciation_word
                "leʦamʦem",
                # hebrew_word_nikud
                "‫לְצַמצֵם‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "110. Маркетинг",
        # words
        [
            (
                # translation_word
                "маркетинг",
                # pronunciation_word
                "ʃivuk",
                # hebrew_word_nikud
                "‬‫שִיווּק‬"
            ),
            (
                # translation_word
                "рынок",
                # pronunciation_word
                "ʃuk",
                # hebrew_word_nikud
                "‫שוּק‬‬"
            ),
            (
                # translation_word
                "продукт",
                # pronunciation_word
                "muʦar",
                # hebrew_word_nikud
                "‬‫מוּצָר‬"
            ),
            (
                # translation_word
                "товар",
                # pronunciation_word
                "sχora",
                # hebrew_word_nikud
                "‫סחוֹרָה‬‬"
            ),
            (
                # translation_word
                "торговая марка",
                # pronunciation_word
                "'semel misχari",
                # hebrew_word_nikud
                "סֶמֶל‬ ‫מִסחָרִי‬‬"
            ),
            (
                # translation_word
                "логотип",
                # pronunciation_word
                "'logo",
                # hebrew_word_nikud
                "‬‫לוֹגו‬"
            ),
            (
                # translation_word
                "спрос",
                # pronunciation_word
                "bikuʃ",
                # hebrew_word_nikud
                "‫בִּיקוּש‬‬"
            ),
            (
                # translation_word
                "предложение",
                # pronunciation_word
                "he'ʦeʿa",
                # hebrew_word_nikud
                "‬‫הֶיצֵע‬"
            ),
            (
                # translation_word
                "потребность",
                # pronunciation_word
                "'ʦoreχ",
                # hebrew_word_nikud
                "‫צוֹרֶך‬‬"
            ),
            (
                # translation_word
                "потребитель",
                # pronunciation_word
                "ʦarχan",
                # hebrew_word_nikud
                "‫צַרכָן‬‬"
            ),
            (
                # translation_word
                "анализ",
                # pronunciation_word
                "ni'tuaχ",
                # hebrew_word_nikud
                "‫נִיתוּח‬‬"
            ),
            (
                # translation_word
                "позиционирование",
                # pronunciation_word
                "miʦuv",
                # hebrew_word_nikud
                "‫מִיצוּב‬‬"
            ),
            (
                # translation_word
                "цена",
                # pronunciation_word
                "meχir",
                # hebrew_word_nikud
                "‫מְחִיר‬‬"
            ),
            (
                # translation_word
                "ценообразование",
                # pronunciation_word
                "hamχara",
                # hebrew_word_nikud
                "‫הַמחָרָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "111. Реклама",
        # words
        [
            (
                # translation_word
                "реклама",
                # pronunciation_word
                "pirsum",
                # hebrew_word_nikud
                "‫פִּרסוּם‬‬"
            ),
            (
                # translation_word
                "рекламировать",
                # pronunciation_word
                "lefarsem",
                # hebrew_word_nikud
                "‫לְפַרסֵם‬‬"
            ),
            (
                # translation_word
                "бюджет",
                # pronunciation_word
                "takʦiv",
                # hebrew_word_nikud
                "‬‫תַקצִיב‬"
            ),
            (
                # translation_word
                "имидж",
                # pronunciation_word
                "tadmit",
                # hebrew_word_nikud
                "‬‫תַדמִית‬"
            ),
            (
                # translation_word
                "кампания (промоушн ~)",
                # pronunciation_word
                "masa",
                # hebrew_word_nikud
                "‫מַסָע‬‬"
            ),
            (
                # translation_word
                "целевая аудитория",
                # pronunciation_word
                "oχlusiyat 'yaʿad",
                # hebrew_word_nikud
                "אוֹכלוּסִייַת‬ ‫יַעַד‬‬"
            ),
            (
                # translation_word
                "визитная карточка",
                # pronunciation_word
                "kartis bikur",
                # hebrew_word_nikud
                "כַּרטִיס‬ ‫בִּיקוּר‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "113. Телефон. Общение по телефону",
        # words
        [
            (
                # translation_word
                "телефон",
                # pronunciation_word
                "'telefon",
                # hebrew_word_nikud
                "‬‫טֶלֶפוֹן‬"
            ),
            (
                # translation_word
                "мобильный телефон",
                # pronunciation_word
                "'telefon nayad",
                # hebrew_word_nikud
                "טֶלֶפוֹן‬ ‫נַייָד‬‬"
            ),
            (
                # translation_word
                "звонить (по телефону)",
                # pronunciation_word
                "leʦalʦel",
                # hebrew_word_nikud
                "‫לְצַלצֵל‬‬"
            ),
            (
                # translation_word
                "звонок (по телефону)",
                # pronunciation_word
                "siχat 'telefon",
                # hebrew_word_nikud
                "שִׂיחַת‬ ‫טֶלֶפוֹן‬‬"
            ),
            (
                # translation_word
                "набрать номер",
                # pronunciation_word
                "leχayeg mispar",
                # hebrew_word_nikud
                "‬לְחַייֵג‬ ‫מִספָּר‬"
            ),
            (
                # translation_word
                "Алло!",
                # pronunciation_word
                "'halo!",
                # hebrew_word_nikud
                "‬!ֹ‫הַלו‬"
            ),
            (
                # translation_word
                "спросить",
                # pronunciation_word
                "liʃʾol",
                # hebrew_word_nikud
                "‬‫לִשאוֹל‬"
            ),
            (
                # translation_word
                "ответить",
                # pronunciation_word
                "laʿanot",
                # hebrew_word_nikud
                "‫לְעַנוֹת‬‬"
            ),
            (
                # translation_word
                "слышать",
                # pronunciation_word
                "liʃ'moʿa",
                # hebrew_word_nikud
                "‬‫לִשמוֹע‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "115. Канцелярские принадлежности",
        # words
        [
            (
                # translation_word
                "ручка",
                # pronunciation_word
                "et",
                # hebrew_word_nikud
                "‫עֵט‬‬"
            ),
            (
                # translation_word
                "карандаш",
                # pronunciation_word
                "iparon",
                # hebrew_word_nikud
                "‫עִיפָּרוֹן‬‬"
            ),
            (
                # translation_word
                "фломастер",
                # pronunciation_word
                "tuʃ",
                # hebrew_word_nikud
                "‫טוּש‬‬"
            ),
            (
                # translation_word
                "блокнот",
                # pronunciation_word
                "pinkas",
                # hebrew_word_nikud
                "‬‫פִּנקָס‬"
            ),
            (
                # translation_word
                "ежедневник",
                # pronunciation_word
                "yoman",
                # hebrew_word_nikud
                "‫יוֹמָן‬‬"
            ),
            (
                # translation_word
                "линейка",
                # pronunciation_word
                "sargel",
                # hebrew_word_nikud
                "‫סַרגֵל‬‬"
            ),
            (
                # translation_word
                "калькулятор",
                # pronunciation_word
                "maχʃevon",
                # hebrew_word_nikud
                "‫מַחשְבוֹן‬‬"
            ),
            (
                # translation_word
                "скрепка",
                # pronunciation_word
                "mehadek",
                # hebrew_word_nikud
                "‬‫מְהַדֵק‬"
            ),
            (
                # translation_word
                "клей",
                # pronunciation_word
                "'devek",
                # hebrew_word_nikud
                "‫דֶבֶק‬‬"
            ),
            (
                # translation_word
                "дырокол",
                # pronunciation_word
                "menakev",
                # hebrew_word_nikud
                "‫מְנַקֵב‬‬"
            ),
            (
                # translation_word
                "степлер",
                # pronunciation_word
                "ʃadχan",
                # hebrew_word_nikud
                "‫שַדכָן‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "116. Документы. Названия документов",
        # words
        [
            (
                # translation_word
                "анкета",
                # pronunciation_word
                "'tofes",
                # hebrew_word_nikud
                "‬‫טוֹפֶס‬"
            ),
            (
                # translation_word
                "бюллетень",
                # pronunciation_word
                "alon meida",
                # hebrew_word_nikud
                "עָלוֹן‬ ‫מֵידָע‬‬"
            ),
            (
                # translation_word
                "визитная карточка",
                # pronunciation_word
                "kartis bikur",
                # hebrew_word_nikud
                "כַּרטִיס‬ ‫בִּיקוּר‬‬"
            ),
            (
                # translation_word
                "водительские права",
                # pronunciation_word
                "riʃyon nehiga",
                # hebrew_word_nikud
                "‬רִשיוֹן‬ ‫נְהִיגָה‬"
            ),
            (
                # translation_word
                "таможенная декларация",
                # pronunciation_word
                "haʦharat meχes",
                # hebrew_word_nikud
                "‬הַצהָרַת‬ ‫מֶכֶס‬"
            ),
            (
                # translation_word
                "договор",
                # pronunciation_word
                "χoze",
                # hebrew_word_nikud
                "‫חוִזֶה‬‬"
            ),
            (
                # translation_word
                "документ",
                # pronunciation_word
                "mismaχ",
                # hebrew_word_nikud
                "‬‫מִסמָך‬"
            ),
            (
                # translation_word
                "завещание (документ)",
                # pronunciation_word
                "ʦavaʾa",
                # hebrew_word_nikud
                "‫צַווָאָה‬‬"
            ),
            (
                # translation_word
                "закон",
                # pronunciation_word
                "χok",
                # hebrew_word_nikud
                "‬‫חוֹק‬"
            ),
            (
                # translation_word
                "квитанция",
                # pronunciation_word
                "kabala",
                # hebrew_word_nikud
                "‫קַבָּלָה‬‬"
            ),
            (
                # translation_word
                "копия",
                # pronunciation_word
                "'otek",
                # hebrew_word_nikud
                "‫עוֹתֶק‬‬"
            ),
            (
                # translation_word
                "накладная",
                # pronunciation_word
                "ʃtar mitʿan",
                # hebrew_word_nikud
                "שטַר‬ ‫מִטעָן‬‬"
            ),
            (
                # translation_word
                "отчёт",
                # pronunciation_word
                "doχ",
                # hebrew_word_nikud
                "‬‫דוֹח‬"
            ),
            (
                # translation_word
                "паспорт",
                # pronunciation_word
                "darkon",
                # hebrew_word_nikud
                "‫דַרכּוֹן‬‬"
            ),
            (
                # translation_word
                "печать (на документе)",
                # pronunciation_word
                "χo'temet",
                # hebrew_word_nikud
                "‬‫חוֹתֶמֶת‬"
            ),
            (
                # translation_word
                "подписать",
                # pronunciation_word
                "laχtom",
                # hebrew_word_nikud
                "‫לַחתוֹם‬‬"
            ),
            (
                # translation_word
                "подпись",
                # pronunciation_word
                "χatima",
                # hebrew_word_nikud
                "‫חֲתִימָה‬‬"
            ),
            (
                # translation_word
                "пропуск (документ)",
                # pronunciation_word
                "iʃur knisa",
                # hebrew_word_nikud
                "‬אִישוּר‬ ‫כּנִיסָה‬"
            ),
            (
                # translation_word
                "сертификат",
                # pronunciation_word
                "teʿuda",
                # hebrew_word_nikud
                "‫תְעוּדָה‬‬"
            ),
            (
                # translation_word
                "соглашение",
                # pronunciation_word
                "heskem",
                # hebrew_word_nikud
                "‬‫הֶסכֵּם‬"
            ),
             (
                # translation_word
                "разрешение (документ)",
                # pronunciation_word
                "riʃayon",
                # hebrew_word_nikud
                "‬‫רִישָיוֹן‬"
            ),
            (
                # translation_word
                "расписка",
                # pronunciation_word
                "ʃtar χov",
                # hebrew_word_nikud
                "שטַר‬ ‫חוֹב‬‬"
            ),
             (
                # translation_word
                "резюме",
                # pronunciation_word
                "korot χayim",
                # hebrew_word_nikud
                "‬קוֹרוֹת‬ ‫חַיִים‬"
            ),
            (
                # translation_word
                "счёт (в бизнесе)",
                # pronunciation_word
                "χeʃbonit",
                # hebrew_word_nikud
                "‫חֶשבּוֹנִית‬‬"
            ),
             (
                # translation_word
                "счёт (в ресторане)",
                # pronunciation_word
                "χeʃbon",
                # hebrew_word_nikud
                "‫חֶשבּוֹן‬‬"
            ),
            (
                # translation_word
                "удостоверение",
                # pronunciation_word
                "teʿuda mezaha",
                # hebrew_word_nikud
                "תְעוּדָה‬ ‫מְזַהָה‬‬"
            ),
             (
                # translation_word
                "экземпляр (документа)",
                # pronunciation_word
                "'otek",
                # hebrew_word_nikud
                "‫עוֹתֶק‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "117. Отрасли и виды бизнеса",
        # words
        [
            (
                # translation_word
                "авиакомпания",
                # pronunciation_word
                "χevrat teʿufa",
                # hebrew_word_nikud
                "‬חֶברַת‬ ‫תְעוּפָה‬"
            ),
            (
                # translation_word
                "аптека",
                # pronunciation_word
                "beit mir'kaχat",
                # hebrew_word_nikud
                "‬בֵּית‬ ‫מִרקַחַת‬"
            ),
            (
                # translation_word
                "аудиторские услуги",
                # pronunciation_word
                "ʃerutei bi'koret χeʃbonot",
                # hebrew_word_nikud
                "שֵירוּתֵי‬ ‫בִּיקוֹרֶת‬ ‫חֶשבּוֹנוֹת‬‬"
            ),
            (
                # translation_word
                "банковский бизнес",
                # pronunciation_word
                "bankaʾut",
                # hebrew_word_nikud
                "‫בַּנקָאוּת‬‬"
            ),
            (
                # translation_word
                "бассейн",
                # pronunciation_word
                "breχat sχiya",
                # hebrew_word_nikud
                "בּרֵיכַת‬ ‫שׂחִייָה‬‬"
            ),
            (
                # translation_word
                "бизнес-центр",
                # pronunciation_word
                "merkaz asakim",
                # hebrew_word_nikud
                "מֶרכַּז‬ ‫עֲסָקִים‬‬"
            ),
            (
                # translation_word
                "бухгалтерские услуги",
                # pronunciation_word
                "ʃerutei hanhalat χeʃbonot",
                # hebrew_word_nikud
                "‬שֵירוּתֵי‬ ‫הַנהָלַת‬ ‫חֶשבּוֹנוֹת‬"
            ),
            (
                # translation_word
                "ветеринар",
                # pronunciation_word
                "veterinar",
                # hebrew_word_nikud
                "‫וֶטֶרִינָר‬‬"
            ),
            (
                # translation_word
                "вывоз мусора",
                # pronunciation_word
                "isuf 'zevel",
                # hebrew_word_nikud
                "אִיסוּף‬ ‫זֶבֶל‬‬"
            ),
            (
                # translation_word
                "гостиница",
                # pronunciation_word
                "beit malon",
                # hebrew_word_nikud
                "בֵּית‬ ‫מָלוֹן‬‬"
            ),
            (
                # translation_word
                "дизайн",
                # pronunciation_word
                "iʦuv",
                # hebrew_word_nikud
                "‫עִיצוּב‬‬"
            ),
            (
                # translation_word
                "инвестиции",
                # pronunciation_word
                "haʃkaʿot",
                # hebrew_word_nikud
                "‫הַשקָעוֹת‬‬"
            ),
            (
                # translation_word
                "интернет",
                # pronunciation_word
                "'internet",
                # hebrew_word_nikud
                "‬‫אִינטֶרנֶט‬"
            ),
            (
                # translation_word
                "информационное агентство",
                # pronunciation_word
                "soχnut yediʿot",
                # hebrew_word_nikud
                "סוֹכנוּת‬ ‫יְדִיעוֹת‬‬"
            ),
            (
                # translation_word
                "кадровое агентство",
                # pronunciation_word
                "soχnut 'koaχ adam",
                # hebrew_word_nikud
                "‬סוֹכנוּת‬ ַ‫כּוֹח‬ ‫אָדָם‬"
            ),
            (
                # translation_word
                "книжный магазин",
                # pronunciation_word
                "χanut sfarim",
                # hebrew_word_nikud
                "‬חֲנוּת‬ ‫ספָרִים‬"
            ),
            (
                # translation_word
                "кондиционеры",
                # pronunciation_word
                "mazganim",
                # hebrew_word_nikud
                "‫מַזגָנִים‬‬"
            ),
            (
                # translation_word
                "консалтинг",
                # pronunciation_word
                "yiʿuʦ",
                # hebrew_word_nikud
                "‬‫יִיעוּץ‬"
            ),
            (
                # translation_word
                "курьерская служба",
                # pronunciation_word
                "ʃirut ʃliχim",
                # hebrew_word_nikud
                "שִירוּת‬ ‫שלִיחִים‬‬"
            ),
            (
                # translation_word
                "мебель",
                # pronunciation_word
                "rehitim",
                # hebrew_word_nikud
                "‫רָהִיטִים‬‬"
            ),
            (
                # translation_word
                "медицина",
                # pronunciation_word
                "refuʾa",
                # hebrew_word_nikud
                "‬‫רְפוּאָה‬"
            ),
            (
                # translation_word
                "недвижимость",
                # pronunciation_word
                "nadlan",
                # hebrew_word_nikud
                "‬‫נַדלָן‬"
            ),
            (
                # translation_word
                "полиграфия",
                # pronunciation_word
                "beit dfus",
                # hebrew_word_nikud
                "‬בֵּית‬ ‫דפוּס‬"
            ),
            (
                # translation_word
                "продукты питания",
                # pronunciation_word
                "muʦrei mazon",
                # hebrew_word_nikud
                "מוּצרֵי‬ ‫מָזוֹן‬‬"
            ),
            (
                # translation_word
                "реклама",
                # pronunciation_word
                "pirsum",
                # hebrew_word_nikud
                "‬‫פִּרסוּם‬"
            ),
            (
                # translation_word
                "салон красоты",
                # pronunciation_word
                "meχon 'yofi",
                # hebrew_word_nikud
                "‬מְכוֹן‬ ‫יוֹפִי‬"
            ),
            (
                # translation_word
                "стоматология",
                # pronunciation_word
                "mirpaʾat ʃi'nayim",
                # hebrew_word_nikud
                "מִרפְּאַת‬ ‫שִינַיִים‬‬"
            ),
            (
                # translation_word
                "страхование",
                # pronunciation_word
                "bi'tuaχ",
                # hebrew_word_nikud
                "‬‫בִּיטוּח‬"
            ),
            (
                # translation_word
                "строительство",
                # pronunciation_word
                "bniya",
                # hebrew_word_nikud
                "‬‫בּנִייָה‬"
            ),
            (
                # translation_word
                "торговля",
                # pronunciation_word
                "misχar",
                # hebrew_word_nikud
                "‫מִסחָר‬‬"
            ),
            (
                # translation_word
                "туризм",
                # pronunciation_word
                "tayarut",
                # hebrew_word_nikud
                "‫תַייָרוּת‬‬"
            ),
            (
                # translation_word
                "фармацевтика",
                # pronunciation_word
                "rokχut",
                # hebrew_word_nikud
                "‫רוֹקחוּת‬‬"
            ),
            (
                # translation_word
                "финансовые услуги",
                # pronunciation_word
                "ʃerutim fi'nansim",
                # hebrew_word_nikud
                "שֵירוּתִים‬ ‫פִינַנסִיים‬‬"
            ),
            (
                # translation_word
                "химчистка",
                # pronunciation_word
                "nikui yaveʃ",
                # hebrew_word_nikud
                "נִיקוּי‬ ‫יָבֵש‬‬"
            ),
            (
                # translation_word
                "ювелир",
                # pronunciation_word
                "ʦoref",
                # hebrew_word_nikud
                "‬‫צוֹרֵף‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "118. Выставка",
        # words
        [
            (
                # translation_word
                "выставка",
                # pronunciation_word
                "taʿaruχa",
                # hebrew_word_nikud
                "‫תַעֲרוּכָה‬‬"
            ),
            (
                # translation_word
                "участвовать",
                # pronunciation_word
                "lehiʃtatef",
                # hebrew_word_nikud
                "‫לְהִשתַתֵף‬‬"
            ),
            (
                # translation_word
                "участник",
                # pronunciation_word
                "miʃtatef",
                # hebrew_word_nikud
                "‫מִשתַתֵף‬‬"
            ),
            (
                # translation_word
                "информация",
                # pronunciation_word
                "meida",
                # hebrew_word_nikud
                "‬‫מֵידָע‬"
            ),
            (
                # translation_word
                "цена",
                # pronunciation_word
                "meχir",
                # hebrew_word_nikud
                "‫מְחִיר‬‬"
            ),
            (
                # translation_word
                "выставочный стенд",
                # pronunciation_word
                "duχan",
                # hebrew_word_nikud
                "‬‫דוּכָן‬"
            ),
            (
                # translation_word
                "располагаться",
                # pronunciation_word
                "lehimatse",
                # hebrew_word_nikud
                "‫לְהִימָצֵא‬‬"
            ),
            (
                # translation_word
                "иностранный",
                # pronunciation_word
                "meχul",
                # hebrew_word_nikud
                "‫מֵחוּייל‬‬"
            ),
            (
                # translation_word
                "продукт",
                # pronunciation_word
                "muʦar",
                # hebrew_word_nikud
                "‫מוּצָר‬‬"
            ),
            (
                # translation_word
                "ассоциация",
                # pronunciation_word
                "amuta",
                # hebrew_word_nikud
                "‫עֲמוּתָה‬‬"
            ),
            (
                # translation_word
                "конкурс",
                # pronunciation_word
                "taχarut",
                # hebrew_word_nikud
                "‬‫תַחֲרוּת‬"
            ),
            (
                # translation_word
                "посетитель",
                # pronunciation_word
                "mevaker",
                # hebrew_word_nikud
                "‫מְבַקֵר‬‬"
            ),
            (
                # translation_word
                "посещать",
                # pronunciation_word
                "levaker",
                # hebrew_word_nikud
                "‬‫לְבַקֵר‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "119. Средства массовой информации",
        # words
        [
            (
                # translation_word
                "журнал",
                # pronunciation_word
                "ʒurnal",
                # hebrew_word_nikud
                "‫ז׳וּרנָל‬‬"
            ),
            (
                # translation_word
                "пресса",
                # pronunciation_word
                "itonut",
                # hebrew_word_nikud
                "‬‫עִיתוֹנוּת‬"
            ),
            (
                # translation_word
                "телевидение",
                # pronunciation_word
                "tele'vizya",
                # hebrew_word_nikud
                "‫טֶלֶווִיזיָה‬‬"
            ),
            (
                # translation_word
                "диктор",
                # pronunciation_word
                "karyan",
                # hebrew_word_nikud
                "‫קַרייָן‬‬"
            ),
            (
                # translation_word
                "журналист",
                # pronunciation_word
                "itonai",
                # hebrew_word_nikud
                "‬‫עִיתוֹנַאי‬"
            ),
            (
                # translation_word
                "репортёр",
                # pronunciation_word
                "katav",
                # hebrew_word_nikud
                "‬‫כַּתָב‬"
            ),
            (
                # translation_word
                "подписка",
                # pronunciation_word
                "minui",
                # hebrew_word_nikud
                "‫מִנוּי‬‬"
            ),
            (
                # translation_word
                "подписчик",
                # pronunciation_word
                "manui",
                # hebrew_word_nikud
                "‫מָנוּי‬‬"
            ),
            (
                # translation_word
                "читатель",
                # pronunciation_word
                "kore",
                # hebrew_word_nikud
                "‫קוֹרֵא‬‬"
            ),
            (
                # translation_word
                "ежемесячный",
                # pronunciation_word
                "χodʃi",
                # hebrew_word_nikud
                "‫חוֹדשִי‬‬"
            ),
            (
                # translation_word
                "еженедельный",
                # pronunciation_word
                "ʃvuʿi",
                # hebrew_word_nikud
                "‫שבוּעִי‬‬"
            ),
            (
                # translation_word
                "статья",
                # pronunciation_word
                "maʾamar",
                # hebrew_word_nikud
                "‬‫מַאֲמָר‬"
            ),
            (
                # translation_word
                "страница",
                # pronunciation_word
                "amud",
                # hebrew_word_nikud
                "‬‫עַמוּד‬"
            ),
            (
                # translation_word
                "событие",
                # pronunciation_word
                "ei'ruʿa",
                # hebrew_word_nikud
                "‬‫אֵירוּע‬"
            ),
            (
                # translation_word
                "скандал",
                # pronunciation_word
                "ʃaʿaruriya",
                # hebrew_word_nikud
                "‬‫שַעֲרוּרִייָה‬"
            ),
            (
                # translation_word
                "интервью",
                # pronunciation_word
                "raʾayon",
                # hebrew_word_nikud
                "‫רַאֲיוֹן‬‬"
            ),
            (
                # translation_word
                "прямая трансляция",
                # pronunciation_word
                "ʃidur χai",
                # hebrew_word_nikud
                "שִידוּר‬ ‫חַי‬‬"
            ),
            (
                # translation_word
                "канал (вещания)",
                # pronunciation_word
                "aruʦ",
                # hebrew_word_nikud
                "‫עָרוּץ‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "120. Сельское хозяйство",
        # words
        [
            (
                # translation_word
                "сельское хозяйство",
                # pronunciation_word
                "χaklaʾut",
                # hebrew_word_nikud
                "‬‫חַקלָאוּת‬"
            ),
            (
                # translation_word
                "фермер",
                # pronunciation_word
                "χavai",
                # hebrew_word_nikud
                "‫חַווַאי‬‬"
            ),
            (
                # translation_word
                "поле",
                # pronunciation_word
                "sade",
                # hebrew_word_nikud
                "‫שָׂדֶה‬‬"
            ),
            (
                # translation_word
                "огород",
                # pronunciation_word
                "gan yarak",
                # hebrew_word_nikud
                "גַן‬ ‫יָרָק‬‬"
            ),
            (
                # translation_word
                "сад",
                # pronunciation_word
                "bustan",
                # hebrew_word_nikud
                "‫בּוּסתָן‬‬"
            ),
            (
                # translation_word
                "плантация",
                # pronunciation_word
                "mata",
                # hebrew_word_nikud
                "‫מַטָע‬‬"
            ),
            (
                # translation_word
                "мука",
                # pronunciation_word
                "'kemaχ",
                # hebrew_word_nikud
                "‫קֶמַח‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "121. Стройка. Строительные работы",
        # words
        [
            (
                # translation_word
                "стройка (место)",
                # pronunciation_word
                "atar bniya",
                # hebrew_word_nikud
                "‬אֲתַר‬ ‫בּנִייָה‬"
            ),
            (
                # translation_word
                "строить",
                # pronunciation_word
                "livnot",
                # hebrew_word_nikud
                "‫לִבנוֹת‬‬"
            ),
            (
                # translation_word
                "строитель",
                # pronunciation_word
                "banai",
                # hebrew_word_nikud
                "‫בַּנַאי‬‬"
            ),
            (
                # translation_word
                "архитектор",
                # pronunciation_word
                "adriχal",
                # hebrew_word_nikud
                "‬‫אַדרִיכָל‬"
            ),
            (
                # translation_word
                "штукатурить",
                # pronunciation_word
                "letaʿyeaχ",
                # hebrew_word_nikud
                "‫לְטַייֵח‬‬"
            ),
            (
                # translation_word
                "каска",
                # pronunciation_word
                "kasda",
                # hebrew_word_nikud
                "‫קַסדָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "122. Наука. Исследования. Учёные",
        # words
        [
            (
                # translation_word
                "наука",
                # pronunciation_word
                "mada",
                # hebrew_word_nikud
                "‫מַדָע‬‬"
            ),
            (
                # translation_word
                "учёный",
                # pronunciation_word
                "madʿan",
                # hebrew_word_nikud
                "‬‫מַדעָן‬"
            ),
            (
                # translation_word
                "анализ",
                # pronunciation_word
                "ni'tuaχ",
                # hebrew_word_nikud
                "‬‫נִיתוּח‬"
            ),
            (
                # translation_word
                "анализировать",
                # pronunciation_word
                "lena'teaχ",
                # hebrew_word_nikud
                "‬‫לְנַתֵח‬"
            ),
            (
                # translation_word
                "гипотеза",
                # pronunciation_word
                "hipo'teza",
                # hebrew_word_nikud
                "‬‫הִיפּוֹתֵזָה‬"
            ),
            (
                # translation_word
                "лаборатория",
                # pronunciation_word
                "maʿabada",
                # hebrew_word_nikud
                "‫מַעֲבָּדָה‬‬"
            ),
            (
                # translation_word
                "метод",
                # pronunciation_word
                "ʃita",
                # hebrew_word_nikud
                "‬‫שִיטָה‬"
            ),
            (
                # translation_word
                "открытие (в науке)",
                # pronunciation_word
                "gilui",
                # hebrew_word_nikud
                "‫גִילוּי‬‬"
            ),
            (
                # translation_word
                "принцип",
                # pronunciation_word
                "ikaron",
                # hebrew_word_nikud
                "‫עִיקָרוֹן‬‬"
            ),
            (
                # translation_word
                "теорема",
                # pronunciation_word
                "miʃpat",
                # hebrew_word_nikud
                "‫מִשפָּט‬‬"
            ),
            (
                # translation_word
                "учения",
                # pronunciation_word
                "tora",
                # hebrew_word_nikud
                "‬‫תוֹרָה‬"
            ),
            (
                # translation_word
                "факт",
                # pronunciation_word
                "uvda",
                # hebrew_word_nikud
                "‫עוּבדָה‬‬"
            ),
            (
                # translation_word
                "экспедиция",
                # pronunciation_word
                "miʃ'laχat",
                # hebrew_word_nikud
                "‬‫מִשלַחַת‬"
            ),
            (
                # translation_word
                "эксперимент",
                # pronunciation_word
                "nisui",
                # hebrew_word_nikud
                "‬‫נִיסוּי‬"
            ),
            (
                # translation_word
                "академик",
                # pronunciation_word
                "akademai",
                # hebrew_word_nikud
                "‬‫אֲקָדֵמַאי‬"
            ),
            (
                # translation_word
                "бакалавр",
                # pronunciation_word
                "'toʾar riʃon",
                # hebrew_word_nikud
                "תוֹאַר‬ ‫רִאשוֹן‬‬"
            ),
            (
                # translation_word
                "доктор",
                # pronunciation_word
                "'doktor",
                # hebrew_word_nikud
                "‫דוֹקטוֹר‬‬"
            ),
            (
                # translation_word
                "магистр",
                # pronunciation_word
                "musmaχ",
                # hebrew_word_nikud
                "‬‫מוּסמָך‬"
            ),
            (
                # translation_word
                "профессор",
                # pronunciation_word
                "pro'fesor",
                # hebrew_word_nikud
                "‫פּרוֹפֶסוֹר‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "124. Люди в среде бизнеса",
        # words
        [
            (
                # translation_word
                "директор",
                # pronunciation_word
                "menahel",
                # hebrew_word_nikud
                "‫מְנַהֵל‬"
            ),
            (
                # translation_word
                "президент",
                # pronunciation_word
                "nasi",
                # hebrew_word_nikud
                "‫נָשִׂיא‬‬"
            ),
            (
                # translation_word
                "заместитель",
                # pronunciation_word
                "sgan",
                # hebrew_word_nikud
                "‫סגָן‬‬"
            ),
            (
                # translation_word
                "помощник",
                # pronunciation_word
                "ozer",
                # hebrew_word_nikud
                "‫עוֹזֵר‬‬"
            ),
            (
                # translation_word
                "секретарь",
                # pronunciation_word
                "mazkir",
                # hebrew_word_nikud
                "‬‫מַזכִּיר‬"
            ),
            (
                # translation_word
                "бизнесмен",
                # pronunciation_word
                "iʃ asakim",
                # hebrew_word_nikud
                "אִיש‬ ‫עֲסָקִים‬‬"
            ),
            (
                # translation_word
                "предприниматель",
                # pronunciation_word
                "yazam",
                # hebrew_word_nikud
                "‬‫יַזָם‬"
            ),
            (
                # translation_word
                "партнёр",
                # pronunciation_word
                "ʃutaf",
                # hebrew_word_nikud
                "‬‫שוּתָף‬"
            ),
            (
                # translation_word
                "акционер",
                # pronunciation_word
                "'baʿal menayot",
                # hebrew_word_nikud
                "‬בַּעַל‬ ‫מְנָיוֹת‬"
            ),
            (
                # translation_word
                "владелец",
                # pronunciation_word
                "beʿalim",
                # hebrew_word_nikud
                "‫בְּעָלִים‬‬"
            ),
            (
                # translation_word
                "клиент",
                # pronunciation_word
                "la'koaχ",
                # hebrew_word_nikud
                "‫לָקוֹח‬‬"
            ),
            (
                # translation_word
                "покупатель",
                # pronunciation_word
                "kone",
                # hebrew_word_nikud
                "‫קוֹנֶה‬‬"
            ),
            (
                # translation_word
                "посетитель",
                # pronunciation_word
                "mevaker",
                # hebrew_word_nikud
                "‬‫מְבַקֵר‬"
            ),
            (
                # translation_word
                "профессионал",
                # pronunciation_word
                "mikʦoʿan",
                # hebrew_word_nikud
                "‫מִקצוֹעָן‬‬"
            ),
            (
                # translation_word
                "эксперт",
                # pronunciation_word
                "mumχe",
                # hebrew_word_nikud
                "‬‫מוּמחֶה‬"
            ),
            (
                # translation_word
                "банкир",
                # pronunciation_word
                "bankai",
                # hebrew_word_nikud
                "‬‫בַּנקַאי‬"
            ),
            (
                # translation_word
                "кассир",
                # pronunciation_word
                "kupai",
                # hebrew_word_nikud
                "‫קוּפַּאי‬"
            ),
            (
                # translation_word
                "инвестор",
                # pronunciation_word
                "maʃ'kiʿa",
                # hebrew_word_nikud
                "‬‫מַשקִיע‬"
            ),
            (
                # translation_word
                "должник",
                # pronunciation_word
                "'baʿal χov",
                # hebrew_word_nikud
                "‬בַּעַל‬ ‫חוֹב‬"
            ),
            (
                # translation_word
                "производитель",
                # pronunciation_word
                "yaʦran",
                # hebrew_word_nikud
                "‬‫יַצרָן‬"
            ),
            (
                # translation_word
                "консультант",
                # pronunciation_word
                "yoʿeʦ",
                # hebrew_word_nikud
                "‬‫יוֹעֵץ‬"
            ),
            (
                # translation_word
                "страховой агент",
                # pronunciation_word
                "soχen bi'tuaχ",
                # hebrew_word_nikud
                "‬סוֹכֵן‬ ַ‫בִּיטוּח‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "125. Профессии в сфере услуг",
        # words
        [
            (
                # translation_word
                "повар",
                # pronunciation_word
                "tabaχ",
                # hebrew_word_nikud
                "‬‫טַבָּח‬"
            ),
            (
                # translation_word
                "шеф-повар",
                # pronunciation_word
                "ʃef",
                # hebrew_word_nikud
                "‬‫שֶף‬"
            ),
            (
                # translation_word
                "пекарь",
                # pronunciation_word
                "ofe",
                # hebrew_word_nikud
                "‬‫אוֹפֶה‬"
            ),
            (
                # translation_word
                "бармен",
                # pronunciation_word
                "'barmen",
                # hebrew_word_nikud
                "‫בַּרמֶן‬‬"
            ),
            (
                # translation_word
                "официант",
                # pronunciation_word
                "melʦar",
                # hebrew_word_nikud
                "‬‫מֶלצָר‬"
            ),
            (
                # translation_word
                "официантка",
                # pronunciation_word
                "melʦarit",
                # hebrew_word_nikud
                "‫מֶלצָרִית‬‬"
            ),
            (
                # translation_word
                "адвокат, юрист",
                # pronunciation_word
                "oreχ din",
                # hebrew_word_nikud
                "עוֹרֵך‬‬ ‫דִין‬‬"
            ),
            (
                # translation_word
                "нотариус",
                # pronunciation_word
                "notaryon",
                # hebrew_word_nikud
                "‫נוֹטַריוֹן‬‬"
            ),
            (
                # translation_word
                "электрик",
                # pronunciation_word
                "χaʃmalai",
                # hebrew_word_nikud
                "‬‫חַשמַלאַי‬"
            ),
            (
                # translation_word
                "сантехник",
                # pronunciation_word
                "ʃravrav",
                # hebrew_word_nikud
                "‫שרַברָב‬‬"
            ),
            (
                # translation_word
                "плотник",
                # pronunciation_word
                "nagar",
                # hebrew_word_nikud
                "‫נַגָר‬‬"
            ),
            (
                # translation_word
                "массажист",
                # pronunciation_word
                "maʿase",
                # hebrew_word_nikud
                "‬‫מְעַסֶה‬"
            ),
            (
                # translation_word
                "массажистка",
                # pronunciation_word
                "masa'ʒistit",
                # hebrew_word_nikud
                "‫מַסָזִ׳יסטִית‬‬"
            ),
            (
                # translation_word
                "врач",
                # pronunciation_word
                "rofe",
                # hebrew_word_nikud
                "‬‫רוֹפֵא‬"
            ),
            (
                # translation_word
                "таксист",
                # pronunciation_word
                "nahag monit",
                # hebrew_word_nikud
                "נַהַג‬‬‬ ‫מוֹנִית‬‬"
            ),
            (
                # translation_word
                "шофёр",
                # pronunciation_word
                "nahag",
                # hebrew_word_nikud
                "‬‫נַהָג‬"
            ),
            (
                # translation_word
                "курьер",
                # pronunciation_word
                "ʃa'liaχ",
                # hebrew_word_nikud
                "‫שָלִיח‬‬"
            ),
            (
                # translation_word
                "горничная",
                # pronunciation_word
                "χadranit",
                # hebrew_word_nikud
                "‫חַדרָנִית‬‬"
            ),
            (
                # translation_word
                "охранник",
                # pronunciation_word
                "ʃomer",
                # hebrew_word_nikud
                "‫שוֹמֵר‬‬‬"
            ),
            (
                # translation_word
                "стюардесса",
                # pronunciation_word
                "da'yelet",
                # hebrew_word_nikud
                "‫דַייֶלֶת‬‬"
            ),
            (
                # translation_word
                "учитель",
                # pronunciation_word
                "more",
                # hebrew_word_nikud
                "‫מוֹרֶה‬‬"
            ),
            (
                # translation_word
                "библиотекарь",
                # pronunciation_word
                "safran",
                # hebrew_word_nikud
                "‫סַפרָן‬‬‬"
            ),
            (
                # translation_word
                "переводчик",
                # pronunciation_word
                "metargem",
                # hebrew_word_nikud
                "‫מְתַרגֵם‬‬"
            ),
            (
                # translation_word
                "переводчик",
                # pronunciation_word
                "meturgeman",
                # hebrew_word_nikud
                "‫מְתוּרגְמָן‬‬‬"
            ),
            (
                # translation_word
                "гид (экскурсовод)",
                # pronunciation_word
                "madriχ tiyulim",
                # hebrew_word_nikud
                "מַדרִיך‬ ‫טִיוּלִים‬‬‬"
            ),
            (
                # translation_word
                "парикмахер",
                # pronunciation_word
                "sapar",
                # hebrew_word_nikud
                "‫סַפָּר‬‬‬"
            ),
            (
                # translation_word
                "почтальон",
                # pronunciation_word
                "davar",
                # hebrew_word_nikud
                "‫דַווָר‬‬‬"
            ),
            (
                # translation_word
                "продавец",
                # pronunciation_word
                "moχer",
                # hebrew_word_nikud
                "‫מוֹכֵר‬‬‬"
            ),
            (
                # translation_word
                "садовник",
                # pronunciation_word
                "ganan",
                # hebrew_word_nikud
                "‫גַנָן‬‬‬"
            ),
            (
                # translation_word
                "слуга",
                # pronunciation_word
                "meʃaret",
                # hebrew_word_nikud
                "‫מְשָרֵת‬‬‬"
            ),
            (
                # translation_word
                "служанка",
                # pronunciation_word
                "meʃa'retet",
                # hebrew_word_nikud
                "‬‬‫מְשָרֵתֶת‬"
            ),
            (
                # translation_word
                "уборщица",
                # pronunciation_word
                "menaka",
                # hebrew_word_nikud
                "‫מְנַקֶה‬‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "126. Военные профессии. Звания",
        # words
        [
            (
                # translation_word
                "рядовой",
                # pronunciation_word
                "turai",
                # hebrew_word_nikud
                "‫טוּרַאי‬‬"
            ),
            (
                # translation_word
                "сержант",
                # pronunciation_word
                "samal",
                # hebrew_word_nikud
                "‫סַמָל‬‬"
            ),
            (
                # translation_word
                "лейтенант",
                # pronunciation_word
                "'segen",
                # hebrew_word_nikud
                "‫סֶגֶן‬‬"
            ),
            (
                # translation_word
                "капитан",
                # pronunciation_word
                "'seren",
                # hebrew_word_nikud
                "‫סֶרֶן‬‬"
            ),
            (
                # translation_word
                "майор",
                # pronunciation_word
                "rav 'seren",
                # hebrew_word_nikud
                "‫רַב־סֶרֶן‬‬"
            ),
            (
                # translation_word
                "полковник",
                # pronunciation_word
                "aluf miʃne",
                # hebrew_word_nikud
                "אַלוּף‬ ‫מִשנֶה‬‬"
            ),
            (
                # translation_word
                "генерал",
                # pronunciation_word
                "aluf",
                # hebrew_word_nikud
                "‫אַלוּף‬‬"
            ),
            (
                # translation_word
                "маршал",
                # pronunciation_word
                "'marʃal",
                # hebrew_word_nikud
                "‫מַרשָל‬‬"
            ),
            (
                # translation_word
                "адмирал",
                # pronunciation_word
                "admiral",
                # hebrew_word_nikud
                "‫אַדמִירָל‬‬"
            ),
            (
                # translation_word
                "военный",
                # pronunciation_word
                "iʃ ʦava",
                # hebrew_word_nikud
                "‫צָבָא‬ ‫אִיש‬‬"
            ),
            (
                # translation_word
                "солдат",
                # pronunciation_word
                "χayal",
                # hebrew_word_nikud
                "‫חַייָל‬‬"
            ),
            (
                # translation_word
                "офицер",
                # pronunciation_word
                "kaʦin",
                # hebrew_word_nikud
                "‬‫קָצִין‬"
            ),
            (
                # translation_word
                "командир",
                # pronunciation_word
                "mefaked",
                # hebrew_word_nikud
                "‫מְפַקֵד‬‬"
            ),
            (
                # translation_word
                "пограничник",
                # pronunciation_word
                "ʃomer gvul",
                # hebrew_word_nikud
                "שוֹמֵר‬ ‫גבוּל‬‬"
            ),
            (
                # translation_word
                "радист",
                # pronunciation_word
                "alχutai",
                # hebrew_word_nikud
                "‬‫אַלחוּטַאי‬"
            ),
            (
                # translation_word
                "разведчик",
                # pronunciation_word
                "iʃ modiʿin kravi",
                # hebrew_word_nikud
                "אִיש‬ ‫מוֹדִיעִין‬ ‫קרָבִי‬‬"
            ),
            (
                # translation_word
                "сапёр",
                # pronunciation_word
                "χablan",
                # hebrew_word_nikud
                "‫חַבּלָן‬‬"
            ),
            (
                # translation_word
                "стрелок",
                # pronunciation_word
                "ʦalaf",
                # hebrew_word_nikud
                "‫צַלָף‬‬"
            ),
            (
                # translation_word
                "штурман",
                # pronunciation_word
                "navat",
                # hebrew_word_nikud
                "‫נַווָט‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "127. Государственные и религиозные служащие",
        # words
        [
            (
                # translation_word
                "президент",
                # pronunciation_word
                "nasi",
                # hebrew_word_nikud
                "‫נָשִׂיא‬‬"
            ),
            (
                # translation_word
                "министр",
                # pronunciation_word
                "sar",
                # hebrew_word_nikud
                "‫שַׂר‬‬"
            ),
            (
                # translation_word
                "премьер-министр",
                # pronunciation_word
                "roʃ memʃala",
                # hebrew_word_nikud
                "רֹאש‬ ‫מֶמשָלָה‬‬"
            ),
            (
                # translation_word
                "дипломат",
                # pronunciation_word
                "diplomat",
                # hebrew_word_nikud
                "‫דִיפּלוֹמָט‬‬"
            ),
            (
                # translation_word
                "консул",
                # pronunciation_word
                "'konsul",
                # hebrew_word_nikud
                "‫קוֹנסוּל‬‬"
            ),
            (
                # translation_word
                "чиновник",
                # pronunciation_word
                "pakid",
                # hebrew_word_nikud
                "‫פָּקִיד‬‬"
            ),
            (
                # translation_word
                "мэр",
                # pronunciation_word
                "roʃ haʿir",
                # hebrew_word_nikud
                "רֹאש‬ ‫הָעִיר‬‬"
            ),
            (
                # translation_word
                "судья",
                # pronunciation_word
                "ʃofet",
                # hebrew_word_nikud
                "‫שוֹפֵט‬‬"
            ),
            (
                # translation_word
                "прокурор",
                # pronunciation_word
                "to'veʿa",
                # hebrew_word_nikud
                "‫תוֹבֵע‬‬"
            ),
            (
                # translation_word
                "монах",
                # pronunciation_word
                "nazir",
                # hebrew_word_nikud
                "‫נָזִיר‬‬"
            ),
            (
                # translation_word
                "раввин",
                # pronunciation_word
                "rav",
                # hebrew_word_nikud
                "‫רַב‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "128. Профессии в сельском хозяйстве",
        # words
        [
            (
                # translation_word
                "пчеловод",
                # pronunciation_word
                "kavran",
                # hebrew_word_nikud
                "‬‫כַּוורָן‬"
            ),
            (
                # translation_word
                "ветеринар",
                # pronunciation_word
                "veterinar",
                # hebrew_word_nikud
                "‫וֶטֶרִינָר‬‬"
            ),
            (
                # translation_word
                "фермер",
                # pronunciation_word
                "χavai",
                # hebrew_word_nikud
                "‫חַווַאי‬‬"
            ),
            (
                # translation_word
                "винодел",
                # pronunciation_word
                "yeinan",
                # hebrew_word_nikud
                "‫יֵינָן‬‬"
            ),
            (
                # translation_word
                "зоолог",
                # pronunciation_word
                "zoʾolog",
                # hebrew_word_nikud
                "‬‫זוֹאוֹלוֹג‬"
            ),
            (
                # translation_word
                "ковбой",
                # pronunciation_word
                "'kaʾuboi",
                # hebrew_word_nikud
                "‫קָאוּבּוֹי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "129. Профессии в области искусства",
        # words
        [
            (
                # translation_word
                "актёр, артист",
                # pronunciation_word
                "saχkan",
                # hebrew_word_nikud
                "‫שַׂחקָן‬‬"
            ),
            (
                # translation_word
                "актриса, артистка",
                # pronunciation_word
                "saχkanit",
                # hebrew_word_nikud
                "‫שַׂחקָנִית‬‬"
            ),
            (
                # translation_word
                "певец",
                # pronunciation_word
                "zamar",
                # hebrew_word_nikud
                "‫זַמָר‬‬"
            ),
            (
                # translation_word
                "певица",
                # pronunciation_word
                "za'meret",
                # hebrew_word_nikud
                "‫זַמֶרֶת‬‬"
            ),
            (
                # translation_word
                "танцор",
                # pronunciation_word
                "rakdan",
                # hebrew_word_nikud
                "‫רַקדָן‬‬"
            ),
            (
                # translation_word
                "танцовщица",
                # pronunciation_word
                "rakdanit",
                # hebrew_word_nikud
                "‬‫רַקדָנִית‬"
            ),
            (
                # translation_word
                "музыкант",
                # pronunciation_word
                "muzikai",
                # hebrew_word_nikud
                "‬‫מוּזִיקַאי‬"
            ),
            (
                # translation_word
                "пианист",
                # pronunciation_word
                "psantran",
                # hebrew_word_nikud
                "‫פּסַנתרָן‬‬"
            ),
            (
                # translation_word
                "гитарист",
                # pronunciation_word
                "nagan gi'tara",
                # hebrew_word_nikud
                "נ‫ַגַן‬ ‫גִיטָרָה‬‬"
            ),
            (
                # translation_word
                "композитор",
                # pronunciation_word
                "malχin",
                # hebrew_word_nikud
                "‫מַלחִין‬‬"
            ),
            (
                # translation_word
                "режиссёр",
                # pronunciation_word
                "bamai",
                # hebrew_word_nikud
                "‬‫בַּמַאי‬"
            ),
            (
                # translation_word
                "критик",
                # pronunciation_word
                "mevaker",
                # hebrew_word_nikud
                "‫מְבַקֵר‬‬"
            ),
            (
                # translation_word
                "писатель",
                # pronunciation_word
                "sofer",
                # hebrew_word_nikud
                "‫סוֹפֵר‬‬"
            ),
            (
                # translation_word
                "поэт",
                # pronunciation_word
                "meʃorer",
                # hebrew_word_nikud
                "‫מְשוֹרֵר‬‬"
            ),
            (
                # translation_word
                "скульптор",
                # pronunciation_word
                "pasal",
                # hebrew_word_nikud
                "‫פַּסָל‬‬"
            ),
            (
                # translation_word
                "художник",
                # pronunciation_word
                "ʦayar",
                # hebrew_word_nikud
                "‫צַייָר‬‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "130. Профессии различные",
        # words
        [
            (
                # translation_word
                "врач",
                # pronunciation_word
                "rofe",
                # hebrew_word_nikud
                "‫רוֹפֵא‬‬"
            ),
            (
                # translation_word
                "медсестра",
                # pronunciation_word
                "aχot",
                # hebrew_word_nikud
                "‫אָחוֹת‬‬"
            ),
            (
                # translation_word
                "психиатр",
                # pronunciation_word
                "psiχi'ʾater",
                # hebrew_word_nikud
                "‫פּסִיכִיאָטֶר‬‬"
            ),
            (
                # translation_word
                "стоматолог",
                # pronunciation_word
                "rofe ʃi'nayim",
                # hebrew_word_nikud
                "‬רוֹפֵא‬ ‫שִינַיִים‬"
            ),
            (
                # translation_word
                "хирург",
                # pronunciation_word
                "kirurg",
                # hebrew_word_nikud
                "‫כִּירוּרג‬‬"
            ),
            (
                # translation_word
                "астронавт",
                # pronunciation_word
                "astro'naʾut",
                # hebrew_word_nikud
                "‫אַסטרוֹנָאוּט‬‬"
            ),
            (
                # translation_word
                "астроном",
                # pronunciation_word
                "astronom",
                # hebrew_word_nikud
                "‫אַסטרוֹנוֹם‬‬"
            ),
            (
                # translation_word
                "лётчик, пилот",
                # pronunciation_word
                "tayas",
                # hebrew_word_nikud
                "‫טַייָס‬‬"
            ),
            (
                # translation_word
                "водитель",
                # pronunciation_word
                "nahag",
                # hebrew_word_nikud
                "‬‫נַהָג‬"
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
                "механик",
                # pronunciation_word
                "meχonai",
                # hebrew_word_nikud
                "‫מְכוֹנַאי‬‬"
            ),
            (
                # translation_word
                "шахтёр",
                # pronunciation_word
                "kore",
                # hebrew_word_nikud
                "‫כּוֹרֶה‬‬"
            ),
            (
                # translation_word
                "рабочий",
                # pronunciation_word
                "poʿel",
                # hebrew_word_nikud
                "‫פּוֹעֵל‬‬"
            ),
            (
                # translation_word
                "слесарь",
                # pronunciation_word
                "misgad",
                # hebrew_word_nikud
                "‫מִסגָד‬‬"
            ),
            (
                # translation_word
                "столяр",
                # pronunciation_word
                "nagar",
                # hebrew_word_nikud
                "‫נַגָר‬‬"
            ),
            (
                # translation_word
                "строитель",
                # pronunciation_word
                "banai",
                # hebrew_word_nikud
                "‫בַּנַאי‬‬"
            ),
            (
                # translation_word
                "профессор",
                # pronunciation_word
                "pro'fesor",
                # hebrew_word_nikud
                "‫פּרוֹפֶסוֹר‬‬"
            ),
            (
                # translation_word
                "архитектор",
                # pronunciation_word
                "adriχal",
                # hebrew_word_nikud
                "‫אַדרִיכָל‬‬"
            ),
            (
                # translation_word
                "учёный",
                # pronunciation_word
                "madʿan",
                # hebrew_word_nikud
                "‬‫מַדעָן‬"
            ),
            (
                # translation_word
                "археолог",
                # pronunciation_word
                "arχeʾolog",
                # hebrew_word_nikud
                "‫אַרכֵיאוֹלוֹג‬‬"
            ),
            (
                # translation_word
                "геолог",
                # pronunciation_word
                "geʾolog",
                # hebrew_word_nikud
                "‫גֵיאוֹלוֹג‬‬"
            ),
            (
                # translation_word
                "няня",
                # pronunciation_word
                "ʃmartaf",
                # hebrew_word_nikud
                "‫שמַרטַף‬‬"
            ),
            (
                # translation_word
                "дизайнер",
                # pronunciation_word
                "meʿaʦev",
                # hebrew_word_nikud
                "‫מְעַצֵב‬‬"
            ),
            (
                # translation_word
                "компьютерщик",
                # pronunciation_word
                "mumχe maχʃevim",
                # hebrew_word_nikud
                "מוּמחֶה‬ ‫מַחשֵבִים‬‬"
            ),
            (
                # translation_word
                "программист",
                # pronunciation_word
                "metaχnet",
                # hebrew_word_nikud
                "‫מְתַכנֵת‬‬"
            ),
            (
                # translation_word
                "инженер",
                # pronunciation_word
                "mehandes",
                # hebrew_word_nikud
                "‫מְהַנדֵס‬‬"
            ),
            (
                # translation_word
                "моряк",
                # pronunciation_word
                "yamai",
                # hebrew_word_nikud
                "‫יַמַאי‬‬"
            ),
            (
                # translation_word
                "спасатель",
                # pronunciation_word
                "maʦil",
                # hebrew_word_nikud
                "‫מַצִיל‬‬"
            ),
            (
                # translation_word
                "пожарный",
                # pronunciation_word
                "kabai",
                # hebrew_word_nikud
                "‫כַּבַּאי‬‬"
            ),
            (
                # translation_word
                "полицейский",
                # pronunciation_word
                "ʃoter",
                # hebrew_word_nikud
                "‫שוֹטֵר‬‬"
            ),
            (
                # translation_word
                "сторож",
                # pronunciation_word
                "ʃomer",
                # hebrew_word_nikud
                "‫שוֹמֵר‬‬"
            ),
            (
                # translation_word
                "телохранитель",
                # pronunciation_word
                "ʃomer roʃ",
                # hebrew_word_nikud
                "שוֹמֵר‬ ‫רֹאש‬‬"
            ),
            (
                # translation_word
                "спортсмен",
                # pronunciation_word
                "sportai",
                # hebrew_word_nikud
                "‫ספּוֹרטַאי‬‬"
            ),
            (
                # translation_word
                "тренер",
                # pronunciation_word
                "meʾamen",
                # hebrew_word_nikud
                "‫מְאַמֵן‬‬"
            ),
            (
                # translation_word
                "сапожник",
                # pronunciation_word
                "sandlar",
                # hebrew_word_nikud
                "‫סַנדלָר‬‬"
            ),
            (
                # translation_word
                "модель",
                # pronunciation_word
                "dugmanit",
                # hebrew_word_nikud
                "‫דוּגמָנִית‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "131. Занятия. Социальное положение",
        # words
        [
            (
                # translation_word
                "школьник",
                # pronunciation_word
                "talmid",
                # hebrew_word_nikud
                "‫תַלמִיד‬‬"
            ),
            (
                # translation_word
                "студент",
                # pronunciation_word
                "student",
                # hebrew_word_nikud
                "‫סטוּדֶנט‬‬"
            ),
            (
                # translation_word
                "философ",
                # pronunciation_word
                "filosof",
                # hebrew_word_nikud
                "‫פִילוֹסוֹף‬‬"
            ),
            (
                # translation_word
                "экономист",
                # pronunciation_word
                "kalkelan",
                # hebrew_word_nikud
                "‫כַּלכְּלָן‬‬"
            ),
            (
                # translation_word
                "изобретатель",
                # pronunciation_word
                "mamʦi",
                # hebrew_word_nikud
                "‫מַמצִיא‬‬"
            ),
            (
                # translation_word
                "безработный",
                # pronunciation_word
                "muvtal",
                # hebrew_word_nikud
                "‫מוּבטָל‬‬"
            ),
            (
                # translation_word
                "пенсионер",
                # pronunciation_word
                "pensyoner",
                # hebrew_word_nikud
                "‫פֶּנסיוֹנֶר‬‬"
            ),
            (
                # translation_word
                "шпион",
                # pronunciation_word
                "meragel",
                # hebrew_word_nikud
                "‫מְרַגֵל‬‬"
            ),
            (
                # translation_word
                "заключённый",
                # pronunciation_word
                "asir",
                # hebrew_word_nikud
                "‫אָסִיר‬‬"
            ),
            (
                # translation_word
                "бюрократ",
                # pronunciation_word
                "birokrat",
                # hebrew_word_nikud
                "‫בִּירוֹקרָט‬‬"
            ),
            (
                # translation_word
                "путешественник",
                # pronunciation_word
                "metayel",
                # hebrew_word_nikud
                "‬‫מְטַייֵל‬"
            ),
            (
                # translation_word
                "гомосексуалист",
                # pronunciation_word
                "'lesbit, 'homo",
                # hebrew_word_nikud
                " ‫לֶסבִּית‬,‫הוֹמו‬‬"
            ),
            (
                # translation_word
                "наркоман",
                # pronunciation_word
                "narkoman",
                # hebrew_word_nikud
                "‫נַרקוֹמָן‬‬"
            ),
            (
                # translation_word
                "проститутка",
                # pronunciation_word
                "zona",
                # hebrew_word_nikud
                "‫זוֹנָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "132. Виды спорта. Спортсмены",
        # words
        [
            (
                # translation_word
                "спортсмен",
                # pronunciation_word
                "sportai",
                # hebrew_word_nikud
                "‫ספּוֹרטַאי‬‬"
            ),
            (
                # translation_word
                "вид спорта",
                # pronunciation_word
                "anaf sport",
                # hebrew_word_nikud
                "עָנַף‬ ‫ספּוֹרט‬‬"
            ),
            (
                # translation_word
                "баскетбол",
                # pronunciation_word
                "kadursal",
                # hebrew_word_nikud
                "‬‫כַּדוּרסַל‬"
            ),
            (
                # translation_word
                "футбол",
                # pronunciation_word
                "kadu'regel",
                # hebrew_word_nikud
                "‫כַּדוּרֶגֶל‬‬"
            ),
            (
                # translation_word
                "волейбол",
                # pronunciation_word
                "kadurʿaf",
                # hebrew_word_nikud
                "‫כַּדוּרעָף‬‬"
            ),
            (
                # translation_word
                "теннис",
                # pronunciation_word
                "'tenis",
                # hebrew_word_nikud
                "‫טֶניִס‬‬"
            ),
            (
                # translation_word
                "плавание",
                # pronunciation_word
                "sχiya",
                # hebrew_word_nikud
                "‫שׂחִייָה‬‬"
            ),
            (
                # translation_word
                "бег",
                # pronunciation_word
                "riʦa",
                # hebrew_word_nikud
                "‫רִיצָה‬‬"
            ),
            (
                # translation_word
                "велоспорт",
                # pronunciation_word
                "reχiva al ofa'nayim",
                # hebrew_word_nikud
                "רְכִיבָה‬ ‫עַל‬ ‫אוֹפַנַיִים‬‬"
            ),
            (
                # translation_word
                "велосипедист",
                # pronunciation_word
                "roχev ofa'nayim",
                # hebrew_word_nikud
                "רוֹכֵב‬ ‫אוֹפַנַיִים‬‬"
            ),
            
        ]
    ),
    (
        # group_name_ru
        "133. Виды спорта. Разное",
        # words
        [
            (
                # translation_word
                "бадминтон",
                # pronunciation_word
                "noʦit",
                # hebrew_word_nikud
                "‫נוֹצִית‬‬"
            ),
            (
                # translation_word
                "бильярд",
                # pronunciation_word
                "bilyard",
                # hebrew_word_nikud
                "‫בִּיליַארד‬‬"
            ),
            (
                # translation_word
                "дайвинг",
                # pronunciation_word
                "ʦlila",
                # hebrew_word_nikud
                "‫צלִילָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "134. Спортивный зал",
        # words
        [
            (
                # translation_word
                "штанга",
                # pronunciation_word
                "miʃ'kolet",
                # hebrew_word_nikud
                "‫מִשקוֹלֶת‬‬"
            ),
            (
                # translation_word
                "гантели",
                # pronunciation_word
                "miʃkolot",
                # hebrew_word_nikud
                "‫מִשקוֹלוֹת‬‬"
            ),
            (
                # translation_word
                "тренажёр",
                # pronunciation_word
                "maχʃir 'koʃer",
                # hebrew_word_nikud
                "מַכשִיר‬ ‫כּוֹשֶר‬‬"
            ),
            (
                # translation_word
                "велотренажёр",
                # pronunciation_word
                "ofanei 'koʃer",
                # hebrew_word_nikud
                "אוֹפַנֵי‬ ‫כּוֹשֶר‬‬"
            ),
            (
                # translation_word
                "беговая дорожка",
                # pronunciation_word
                "haliχon",
                # hebrew_word_nikud
                "‫הֲלִיכוֹן‬‬"
            ),
            (
                # translation_word
                "скакалка",
                # pronunciation_word
                "dalgit",
                # hebrew_word_nikud
                "‫דַלגִית‬‬"
            ),
            (
                # translation_word
                "аэробика",
                # pronunciation_word
                "ei'robika",
                # hebrew_word_nikud
                "‬‫אֵירוֹבִּיקָה‬"
            ),
            (
                # translation_word
                "йога",
                # pronunciation_word
                "yoga",
                # hebrew_word_nikud
                "‫יוֹגָה‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "135. Спорт. Разное",
        # words
        [
            (
                # translation_word
                "Олимпийские игры",
                # pronunciation_word
                "hamisχakim haʾo'limpiyim",
                # hebrew_word_nikud
                "‬הַמִשׂחָקִים‬ ‫הָאוֹלִימפִּייִם‬"
            ),
            (
                # translation_word
                "победитель",
                # pronunciation_word
                "mena'ʦeaχ",
                # hebrew_word_nikud
                "‫מְנַצֵח‬‬"
            ),
            (
                # translation_word
                "побеждать",
                # pronunciation_word
                "lena'ʦeaχ",
                # hebrew_word_nikud
                "‫לְנַצֵח‬‬"
            ),
            (
                # translation_word
                "лидер",
                # pronunciation_word
                "manhig",
                # hebrew_word_nikud
                "‫מַנהִיג‬‬"
            ),
            (
                # translation_word
                "чемпион",
                # pronunciation_word
                "aluf",
                # hebrew_word_nikud
                "‫אַלוּף‬‬"
            ),
            (
                # translation_word
                "чемпионат",
                # pronunciation_word
                "alifut",
                # hebrew_word_nikud
                "‫אַלִיפוּת‬‬"
            ),
            (
                # translation_word
                "стадион",
                # pronunciation_word
                "iʦtadyon",
                # hebrew_word_nikud
                "‫אִצטַדיוֹן‬‬"
            ),
            (
                # translation_word
                "противник",
                # pronunciation_word
                "yariv",
                # hebrew_word_nikud
                "‫יָרִיב‬‬"
            ),
            (
                # translation_word
                "проиграть",
                # pronunciation_word
                "lehafsid",
                # hebrew_word_nikud
                "‫לְהַפסִיד‬‬"
            ),
            (
                # translation_word
                "результат",
                # pronunciation_word
                "toʦaʾa",
                # hebrew_word_nikud
                "‫תוֹצָאָה‬‬"
            ),
            (
                # translation_word
                "перерыв",
                # pronunciation_word
                "hafsaka",
                # hebrew_word_nikud
                "‫הַפסָקָה‬‬"
            ),
            (
                # translation_word
                "упражнение",
                # pronunciation_word
                "imun",
                # hebrew_word_nikud
                "‫אִימוּן‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "136. Школа",
        # words
        [
            (
                # translation_word
                "школа",
                # pronunciation_word
                "beit 'sefer",
                # hebrew_word_nikud
                "‬בֵּית‬ ‫סֵפֶר‬"
            ),
            (
                # translation_word
                "ученик",
                # pronunciation_word
                "talmid",
                # hebrew_word_nikud
                "‫תַלמִיד‬‬"
            ),
            (
                # translation_word
                "ученица",
                # pronunciation_word
                "talmida",
                # hebrew_word_nikud
                "‫תַלמִידָה‬‬"
            ),
            (
                # translation_word
                "учить(об учителе)",
                # pronunciation_word
                "lelamed",
                # hebrew_word_nikud
                "‫לְלַמֵד‬‬"
            ),
            (
                # translation_word
                "учить наизусть",
                # pronunciation_word
                "lilmod beʿal pe",
                # hebrew_word_nikud
                "‫פֶּה‬ ‫בְּעַל‬ ‫לִלמוֹד‬‬"
            ),
            (
                # translation_word
                "учить (что-л.)",
                # pronunciation_word
                "lilmod",
                # hebrew_word_nikud
                "‫לִלמוֹד‬‬"
            ),
            (
                # translation_word
                "идти в школу",
                # pronunciation_word
                "la'leχet le'beit 'sefer",
                # hebrew_word_nikud
                "לָלֶכֶת‬ ‫לְבֵּית‬ ‫סֶפֶר‬‬"
            ),
            (
                # translation_word
                "предмет (дисциплина)",
                # pronunciation_word
                "mik'ʦoʿa",
                # hebrew_word_nikud
                "‫מִקצוֹע‬‬"
            ),
            (
                # translation_word
                "класс",
                # pronunciation_word
                "kita",
                # hebrew_word_nikud
                "‫כִּיתָה‬‬"
            ),
            (
                # translation_word
                "урок",
                # pronunciation_word
                "ʃiʿur",
                # hebrew_word_nikud
                "‫שִיעוּר‬‬"
            ),
            (
                # translation_word
                "парта",
                # pronunciation_word
                "ʃulχan limudim",
                # hebrew_word_nikud
                "שוּלחַן‬ ‫לִימוּדִים‬‬"
            ),
            (
                # translation_word
                "доска (школьная)",
                # pronunciation_word
                "'luaχ",
                # hebrew_word_nikud
                "‫לוּח‬‬"
            ),
            (
                # translation_word
                "отметка",
                # pronunciation_word
                "ʦiyun",
                # hebrew_word_nikud
                "‫צִיוּן‬‬"
            ),
            (
                # translation_word
                "ошибка",
                # pronunciation_word
                "taʿut",
                # hebrew_word_nikud
                "‫טָעוּת‬‬"
            ),
            (
                # translation_word
                "делать ошибки",
                # pronunciation_word
                "laʿasot taʿuyot",
                # hebrew_word_nikud
                "‬‫טָעוּיוֹת‬ ‫לַעֲשׂוֹת‬"
            ),
            (
                # translation_word
                "исправлять (ошибку)",
                # pronunciation_word
                "letaken",
                # hebrew_word_nikud
                "‫לְתַקֵן‬‬"
            ),
            (
                # translation_word
                "домашнее задание",
                # pronunciation_word
                "ʃiʿurei 'bayit",
                # hebrew_word_nikud
                "שִיעוּרֵי‬ ‫בַּיִת‬‬"
            ),
            (
                # translation_word
                "упражнение",
                # pronunciation_word
                "targil",
                # hebrew_word_nikud
                "‫תַרגִיל‬‬"
            ),
            (
                # translation_word
                "присутствовать",
                # pronunciation_word
                "lihyot no'χeaχ",
                # hebrew_word_nikud
                "לִהיוֹת‬ ‫נוֹכֵח‬‬"
            ),
            (
                # translation_word
                "отсутствовать",
                # pronunciation_word
                "leheʿader",
                # hebrew_word_nikud
                "‫לְהֵיעָדֵר‬‬"
            ),
            (
                # translation_word
                "карандаш",
                # pronunciation_word
                "iparon",
                # hebrew_word_nikud
                "‫עִיפָּרוֹן‬‬"
            ),
            (
                # translation_word
                "ручка",
                # pronunciation_word
                "et",
                # hebrew_word_nikud
                "‬‫עֵט‬"
            ),
            (
                # translation_word
                "тетрадь",
                # pronunciation_word
                "maχ'beret",
                # hebrew_word_nikud
                "‫מַחבֶּרֶת‬‬"
            ),
            (
                # translation_word
                "учебник",
                # pronunciation_word
                "'sefer limud",
                # hebrew_word_nikud
                "סֵפֶר‬ ‫לִימוּד‬‬"
            ),
            (
                # translation_word
                "каникулы",
                # pronunciation_word
                "χufʃa",
                # hebrew_word_nikud
                "‫חוּפשָה‬‬"
            ),
            (
                # translation_word
                "экзамен",
                # pronunciation_word
                "bχina",
                # hebrew_word_nikud
                "‫בּחִינָה‬‬"
            ),
            (
                # translation_word
                "сдавать экзамены",
                # pronunciation_word
                "lehibaχen",
                # hebrew_word_nikud
                "‫לְהִיבָּחֵן‬‬"
            ),
            (
                # translation_word
                "контрольная работа",
                # pronunciation_word
                "mivχan",
                # hebrew_word_nikud
                "‫מִבחָן‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "137. Высшее учебное заведение",
        # words
        [
            (
                # translation_word
                "академия",
                # pronunciation_word
                "aka'demya",
                # hebrew_word_nikud
                "‫אֲקָדֶמיָה‬‬"
            ),
            (
                # translation_word
                "университет",
                # pronunciation_word
                "uni'versita",
                # hebrew_word_nikud
                "‫אוּנִיבֶרסִיטָה‬‬"
            ),
            (
                # translation_word
                "факультет",
                # pronunciation_word
                "fa'kulta",
                # hebrew_word_nikud
                "‫פָקוּלטָה‬‬"
            ),
            (
                # translation_word
                "преподаватель",
                # pronunciation_word
                "marʦe",
                # hebrew_word_nikud
                "‫מַרצֶה‬‬"
            ),
            (
                # translation_word
                "студент",
                # pronunciation_word
                "student",
                # hebrew_word_nikud
                "‫סטוּדֶנט‬‬"
            ),
            (
                # translation_word
                "студентка",
                # pronunciation_word
                "stu'dentit",
                # hebrew_word_nikud
                "‬‫סטוּדֶנטִית‬"
            ),
            (
                # translation_word
                "аудитория (помещение)",
                # pronunciation_word
                "ulam harʦaʾot",
                # hebrew_word_nikud
                "אוּלַם‬ ‫הַרצָאוֹת‬‬"
            ),
            (
                # translation_word
                "диплом",
                # pronunciation_word
                "di'ploma",
                # hebrew_word_nikud
                "‫דִיפּלוֹמָה‬‬"
            ),
            (
                # translation_word
                "диссертация",
                # pronunciation_word
                "diser'taʦya",
                # hebrew_word_nikud
                "‫דִיסֶרטַציָה‬‬"
            ),
            (
                # translation_word
                "лекция",
                # pronunciation_word
                "harʦaʾa",
                # hebrew_word_nikud
                "‫הַרצָאָה‬‬"
            ),
            (
                # translation_word
                "однокурсник",
                # pronunciation_word
                "χaver lelimudim",
                # hebrew_word_nikud
                "חָבֵר‬ ‫לְלִימוּדִים‬‬"
            ),
            (
                # translation_word
                "стипендия",
                # pronunciation_word
                "milga",
                # hebrew_word_nikud
                "‫מִלגָה‬‬"
            ),
            (
                # translation_word
                "учёная степень",
                # pronunciation_word
                "'toʾar aka'demi",
                # hebrew_word_nikud
                "‫אָקָדֶמִי‬ ‫תוֹאַר‬‬"
            ),
        ]
    ),     
    (
        # group_name_ru
        "138. Названия наук и дисциплин",
        # words
        [
            (
                # translation_word
                "математика",
                # pronunciation_word
                "mate'matika",
                # hebrew_word_nikud
                "‫מָתֶמָטִיקָה‬‬"
            ),
            (
                # translation_word
                "астрономия",
                # pronunciation_word
                "astro'nomya",
                # hebrew_word_nikud
                "‫אַסטרוֹנוֹמיָה‬‬"
            ),
            (
                # translation_word
                "биология",
                # pronunciation_word
                "bio'logya",
                # hebrew_word_nikud
                "‫בִּיוֹלוֹגיָה‬‬"
            ),
            (
                # translation_word
                "география",
                # pronunciation_word
                "geʾo'grafya",
                # hebrew_word_nikud
                "‫גֵיאוֹגרַפיָה‬‬"
            ),
            (
                # translation_word
                "история",
                # pronunciation_word
                "his'torya",
                # hebrew_word_nikud
                "‫הִיסטוֹריָה‬‬"
            ),
            (
                # translation_word
                "медицина",
                # pronunciation_word
                "refuʾa",
                # hebrew_word_nikud
                "‫רְפוּאָה‬‬"
            ),
            (
                # translation_word
                "педагогика",
                # pronunciation_word
                "χinuχ",
                # hebrew_word_nikud
                "‫חִינוּך‬‬"
            ),
            (
                # translation_word
                "право",
                # pronunciation_word
                "miʃpatim",
                # hebrew_word_nikud
                "‫מִשפָּטִים‬‬"
            ),
            (
                # translation_word
                "физика",
                # pronunciation_word
                "'fizika",
                # hebrew_word_nikud
                "‫פִיזִיקָה‬‬"
            ),
            (
                # translation_word
                "химия",
                # pronunciation_word
                "'χimya",
                # hebrew_word_nikud
                "‫כִימיָה‬‬"
            ),
            (
                # translation_word
                "философия",
                # pronunciation_word
                "filo'sofya",
                # hebrew_word_nikud
                "‫פִילוֹסוֹפיָה‬‬"
            ),
            (
                # translation_word
                "психология",
                # pronunciation_word
                "psiχo'logya",
                # hebrew_word_nikud
                "‫פּסִיכוֹלוֹגיָה‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "139. Письмо. Части речи. Орфография",
        # words
        [
            (
                # translation_word
                "грамматика",
                # pronunciation_word
                "dikduk",
                # hebrew_word_nikud
                "‫דִקדוּק‬‬"
            ),
            (
                # translation_word
                "лексика",
                # pronunciation_word
                "oʦar milim",
                # hebrew_word_nikud
                "אוֹצַר‬ ‫מִילִים‬‬"
            ),
            (
                # translation_word
                "существительное",
                # pronunciation_word
                "ʃem 'eʦem",
                # hebrew_word_nikud
                "שֵם‬ ‫עֶצֶם‬‬‬"
            ),
            (
                # translation_word
                "прилагательное",
                # pronunciation_word
                "ʃem 'toʾar",
                # hebrew_word_nikud
                "שֵם‬ ‫תוֹאַר‬‬‬‬"
            ),
            (
                # translation_word
                "глагол",
                # pronunciation_word
                "poʿel",
                # hebrew_word_nikud
                "‫פּוֹעַל‬‬"
            ),
            (
                # translation_word
                "наречие",
                # pronunciation_word
                "'toʾar 'poʿal",
                # hebrew_word_nikud
                "‬תוֹאַר‬ ‫פּוֹעַל‬"
            ),
            (
                # translation_word
                "местоимение",
                # pronunciation_word
                "ʃem guf",
                # hebrew_word_nikud
                "שֵם‬ ‫גוּף‬‬"
            ),
            (
                # translation_word
                "предлог",
                # pronunciation_word
                "milat 'yaχas",
                # hebrew_word_nikud
                "מִילַת‬ ‫יַחַס‬‬"
            ),
            (
                # translation_word
                "ударение",
                # pronunciation_word
                "'taʿam",
                # hebrew_word_nikud
                "‫טַעַם‬‬"
            ),
            (
                # translation_word
                "точка",
                # pronunciation_word
                "nekuda",
                # hebrew_word_nikud
                "‬‫נְקוּדָה‬"
            ),
            (
                # translation_word
                "запятая",
                # pronunciation_word
                "psik",
                # hebrew_word_nikud
                "‫פּסִיק‬‬"
            ),
            (
                # translation_word
                "вопросительный знак",
                # pronunciation_word
                "siman ʃeʾela",
                # hebrew_word_nikud
                "‬סִימַן‬ ‫שְאֵלָה‬"
            ),
            (
                # translation_word
                "буква",
                # pronunciation_word
                "ot",
                # hebrew_word_nikud
                "‬‫אוֹת‬"
            ),
            (
                # translation_word
                "гласный звук",
                # pronunciation_word
                "tnuʿa",
                # hebrew_word_nikud
                "‫תנוּעָה‬‬"
            ),
            (
                # translation_word
                "согласный звук",
                # pronunciation_word
                "iʦur",
                # hebrew_word_nikud
                "‬‫עִיצוּר‬"
            ),
            (
                # translation_word
                "предложение",
                # pronunciation_word
                "miʃpat",
                # hebrew_word_nikud
                "‫מִשפָּט‬‬"
            ),
            (
                # translation_word
                "строка",
                # pronunciation_word
                "ʃura",
                # hebrew_word_nikud
                "‫שוּרָה‬‬"
            ),
            (
                # translation_word
                "слово",
                # pronunciation_word
                "mila",
                # hebrew_word_nikud
                "‬‫מִילָה‬"
            ),
            (
                # translation_word
                "словосочетание",
                # pronunciation_word
                "ʦiruf milim",
                # hebrew_word_nikud
                "צִירוּף‬ ‫מִילִים‬‬"
            ),
            (
                # translation_word
                "правило",
                # pronunciation_word
                "klal",
                # hebrew_word_nikud
                "‫כּלָל‬‬"
            ),
            (
                # translation_word
                "спряжение, склонение",
                # pronunciation_word
                "hataya",
                # hebrew_word_nikud
                "‫הַטָייָה‬‬"
            ),
            (
                # translation_word
                "вопрос",
                # pronunciation_word
                "ʃeʾela",
                # hebrew_word_nikud
                "‫שְאֵלָה‬‬"
            ),
            (
                # translation_word
                "подчеркнуть",
                # pronunciation_word
                "lehadgiʃ",
                # hebrew_word_nikud
                "‫לְהַדגִיש‬‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "140. Изучение иностранных языков",
        # words
        [
            (
                # translation_word
                "язык (напр. русский)",
                # pronunciation_word
                "safa",
                # hebrew_word_nikud
                "‫שָׂפָה‬‬"
            ),
            (
                # translation_word
                "иностранный",
                # pronunciation_word
                "zar",
                # hebrew_word_nikud
                "‬‫זָר‬"
            ),
            (
                # translation_word
                "иностранный язык",
                # pronunciation_word
                "safa zara",
                # hebrew_word_nikud
                "שָׂפָה‬ ‫זָרָה‬‬"
            ),
            (
                # translation_word
                "читать",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "говорить",
                # pronunciation_word
                "ledaber",
                # hebrew_word_nikud
                "‫לְדַבֵּר‬‬"
            ),
            (
                # translation_word
                "понимать",
                # pronunciation_word
                "lehavin",
                # hebrew_word_nikud
                "‫לְהָבִין‬‬"
            ),
            (
                # translation_word
                "писать",
                # pronunciation_word
                "liχtov",
                # hebrew_word_nikud
                "‫לִכתוֹב‬‬"
            ),
            (
                # translation_word
                "быстро",
                # pronunciation_word
                "maher",
                # hebrew_word_nikud
                "‫מַהֵר‬‬"
            ),
            (
                # translation_word
                "медленно",
                # pronunciation_word
                "leʾat",
                # hebrew_word_nikud
                "‫לְאַט‬‬"
            ),
            (
                # translation_word
                "свободно",
                # pronunciation_word
                "χofʃi",
                # hebrew_word_nikud
                "‫חוֹפשִי‬‬"
            ),
            (
                # translation_word
                "словарь",
                # pronunciation_word
                "milon",
                # hebrew_word_nikud
                "‫מִילוֹן‬‬"
            ),
            (
                # translation_word
                "самоучитель",
                # pronunciation_word
                "'sefer lelimud aʦmi",
                # hebrew_word_nikud
                "סֵפֶר‬ ‫לְלִימוּד‬ ‫עַצמִי‬‬"
            ),
            (
                # translation_word
                "разговорник",
                # pronunciation_word
                "siχon",
                # hebrew_word_nikud
                "‫שִׂיחוֹן‬‬"
            ),
            (
                # translation_word
                "говорить по буквам",
                # pronunciation_word
                "leʾayet",
                # hebrew_word_nikud
                "‫לְאַייֵת‬‬"
            ),
            (
                # translation_word
                "произношение",
                # pronunciation_word
                "hagiya",
                # hebrew_word_nikud
                "‬‫הֲגִייָה‬"
            ),
            (
                # translation_word
                "акцент",
                # pronunciation_word
                "mivta",
                # hebrew_word_nikud
                "‬‫מִבטָא‬"
            ),
            (
                # translation_word
                "курсы",
                # pronunciation_word
                "kurs",
                # hebrew_word_nikud
                "‫קוּרס‬‬"
            ),
            (
                # translation_word
                "перевод",
                # pronunciation_word
                "tirgum",
                # hebrew_word_nikud
                "‫תִרגוּם‬‬"
            ),
            (
                # translation_word
                "переводчик",
                # pronunciation_word
                "metargem",
                # hebrew_word_nikud
                "‫מְתַרגֵם‬"
            ),
            (
                # translation_word
                "память",
                # pronunciation_word
                "zikaron",
                # hebrew_word_nikud
                "‫זִיכָּרוֹן‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "141. Театр",
        # words
        [
            (
                # translation_word
                "театр",
                # pronunciation_word
                "teʾatron",
                # hebrew_word_nikud
                "‬‫תֵיאַטרוֹן‬"
            ),
            (
                # translation_word
                "опера",
                # pronunciation_word
                "'opera",
                # hebrew_word_nikud
                "‫אוֹפֶּרָה‬‬"
            ),
            (
                # translation_word
                "балет",
                # pronunciation_word
                "balet",
                # hebrew_word_nikud
                "‫בָּלֶט‬‬"
            ),
            (
                # translation_word
                "репетиция",
                # pronunciation_word
                "χazara",
                # hebrew_word_nikud
                "‫חֲזָרָה‬‬"
            ),
            (
                # translation_word
                "репетировать",
                # pronunciation_word
                "laʿaroχ χazara",
                # hebrew_word_nikud
                "לַעֲרוֹך‬ ‫חֲזָרָה‬‬"
            ),
            (
                # translation_word
                "спектакль",
                # pronunciation_word
                "haʦaga",
                # hebrew_word_nikud
                "‫הַצָגָה‬‬"
            ),
            (
                # translation_word
                "билет",
                # pronunciation_word
                "kartis",
                # hebrew_word_nikud
                "‬‫כַּרטִיס‬"
            ),
            (
                # translation_word
                "билетная касса",
                # pronunciation_word
                "kupa",
                # hebrew_word_nikud
                "‫קוּפָּה‬‬"
            ),
            (
                # translation_word
                "зритель",
                # pronunciation_word
                "ʦofe",
                # hebrew_word_nikud
                "‬‫צוֹפֶה‬"
            ),
            (
                # translation_word
                "хлопать (артистам)",
                # pronunciation_word
                "imχo ka'payim",
                # hebrew_word_nikud
                "לִמחוֹא‬ ‫כַּפַּיִים‬‬"
            ),
            (
                # translation_word
                "сцена",
                # pronunciation_word
                "bama",
                # hebrew_word_nikud
                "‫בָּמָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "142. Кино",
        # words
        [
            (
                # translation_word
                "актёр",
                # pronunciation_word
                "saχkan",
                # hebrew_word_nikud
                "‫שַׂחקָן‬‬"
            ),
            (
                # translation_word
                "актриса",
                # pronunciation_word
                "saχkanit",
                # hebrew_word_nikud
                "‫שַׂחקָנִית‬‬"
            ),
            (
                # translation_word
                "кино (вид искусства)",
                # pronunciation_word
                "kol'noʿa",
                # hebrew_word_nikud
                "‫קוֹלנוֹע‬‬"
            ),
            (
                # translation_word
                "кино, фильм",
                # pronunciation_word
                "'seret",
                # hebrew_word_nikud
                "‫סֶרֶט‬‬"
            ),
            (
                # translation_word
                "серия (часть фильма)",
                # pronunciation_word
                "epi'zoda",
                # hebrew_word_nikud
                "‫אֶפִּיזוֹדָה‬‬"
            ),
            (
                # translation_word
                "детектив",
                # pronunciation_word
                "'seret balaʃi",
                # hebrew_word_nikud
                "סֶרֶט‬ ‫בַּלָשִי‬‬"
            ),
            (
                # translation_word
                "боевик",
                # pronunciation_word
                "maʿarvon",
                # hebrew_word_nikud
                "‬‫מַעַרבוֹן‬"
            ),
            (
                # translation_word
                "фантастический фильм",
                # pronunciation_word
                "'seret mada bidyoni",
                # hebrew_word_nikud
                "סֶרֶט‬ ‫מַדָע‬ ‫בִּדיוֹנִי‬‬"
            ),
            (
                # translation_word
                "фильм ужасов",
                # pronunciation_word
                "'seret eima",
                # hebrew_word_nikud
                "‬‫אֵימָה‬ ‫סֶרֶט‬"
            ),
            (
                # translation_word
                "кинокомедия",
                # pronunciation_word
                "ko'medya",
                # hebrew_word_nikud
                "‬‫קוֹמֶדיָה‬"
            ),
            (
                # translation_word
                "мелодрама",
                # pronunciation_word
                "melo'drama",
                # hebrew_word_nikud
                "‫מֶלוֹדרָמָה‬‬"
            ),
            (
                # translation_word
                "драма",
                # pronunciation_word
                "'drama",
                # hebrew_word_nikud
                "‫דרָמָה‬‬"
            ),
            (
                # translation_word
                "мультфильм",
                # pronunciation_word
                "'seret ani'maʦya",
                # hebrew_word_nikud
                "סֶרֶט‬ ‫אֲנִימַציָה‬‬"
            ),
            (
                # translation_word
                "играть (роль)",
                # pronunciation_word
                "lesaχek",
                # hebrew_word_nikud
                "‫לְשַׂחֵק‬‬"
            ),
            (
                # translation_word
                "популярный",
                # pronunciation_word
                "popu'lari",
                # hebrew_word_nikud
                "‫פּוֹפּוּלָרִי‬‬"
            ),
            (
                # translation_word
                "снимать фильм",
                # pronunciation_word
                "leʦalem 'seret",
                # hebrew_word_nikud
                "לְצַלֵם‬ ‫סֶרֶט‬‬"
            ),
            (
                # translation_word
                "кинотеатр",
                # pronunciation_word
                "beit kol'noʿa",
                # hebrew_word_nikud
                "בֵּית‬ ‫קוֹלנוֹע‬‬"
            ),
            (
                # translation_word
                "субтитры",
                # pronunciation_word
                "ktuviyot",
                # hebrew_word_nikud
                "‫כּתוּבִיוֹת‬‬"
            ),
            (
                # translation_word
                "перевод (с другого языка)",
                # pronunciation_word
                "tirgum",
                # hebrew_word_nikud
                "‫תִרגוּם‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "143. Изобразительное искусство",
        # words
        [
            (
                # translation_word
                "искусство",
                # pronunciation_word
                "amanut",
                # hebrew_word_nikud
                "‫אָמָנוּת‬‬"
            ),
            (
                # translation_word
                "выставка картин",
                # pronunciation_word
                "taʿaruχat amanut",
                # hebrew_word_nikud
                "תַעֲרוּכַת‬ ‫אָמָנוּת‬‬"
            ),
            (
                # translation_word
                "живопись",
                # pronunciation_word
                "ʦiyur",
                # hebrew_word_nikud
                "‫צִיוּר‬‬"
            ),
            (
                # translation_word
                "картина",
                # pronunciation_word
                "tmuna",
                # hebrew_word_nikud
                "‫תמוּנָה‬‬"
            ),
            (
                # translation_word
                "скульптура, статуя",
                # pronunciation_word
                "pesel",
                # hebrew_word_nikud
                "‫פֶּסֶל‬‬"
            ),
            (
                # translation_word
                "краска",
                # pronunciation_word
                "'ʦeva",
                # hebrew_word_nikud
                "‫צֶבַע‬‬"
            ),
            (
                # translation_word
                "рисовать",
                # pronunciation_word
                "leʦayer",
                # hebrew_word_nikud
                "‬‫לְצַייֵר‬"
            ),
            (
                # translation_word
                "художник",
                # pronunciation_word
                "ʦayar",
                # hebrew_word_nikud
                "‫צַייָר‬‬"
            ),
            (
                # translation_word
                "реставрировать",
                # pronunciation_word
                "leʃaχzer",
                # hebrew_word_nikud
                "‬‫לְשַחזֵר‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "144. Литература. Поэзия",
        # words
        [
            (
                # translation_word
                "литература",
                # pronunciation_word
                "sifrut",
                # hebrew_word_nikud
                "‫סִפרוּת‬‬"
            ),
            (
                # translation_word
                "автор",
                # pronunciation_word
                "sofer",
                # hebrew_word_nikud
                "‬‫סוֹפֵר‬"
            ),
            (
                # translation_word
                "оглавление",
                # pronunciation_word
                "'toχen inyanim",
                # hebrew_word_nikud
                "‬תוֹכֶן‬ ‫עִנייָנִים‬"
            ),
            (
                # translation_word
                "страница",
                # pronunciation_word
                "amud",
                # hebrew_word_nikud
                "‬‫עַמוּד‬"
            ),
            (
                # translation_word
                "главный герой",
                # pronunciation_word
                "hagibor haraʃi",
                # hebrew_word_nikud
                "‬הַגִיבּוֹר‬ ‫הָרָאשִי‬"
            ),
            (
                # translation_word
                "рассказ",
                # pronunciation_word
                "sipur kaʦar",
                # hebrew_word_nikud
                "‬‫קָצַר‬ ‫סִיפּוּר‬"
            ),
            (
                # translation_word
                "повесть",
                # pronunciation_word
                "sipur",
                # hebrew_word_nikud
                "‫סִיפּוּר‬‬"
            ),
            (
                # translation_word
                "роман",
                # pronunciation_word
                "roman",
                # hebrew_word_nikud
                "‫רוֹמָן‬‬"
            ),
            (
                # translation_word
                "детектив",
                # pronunciation_word
                "roman balaʃi",
                # hebrew_word_nikud
                "רוֹמָן‬ ‫בַּלָשִי‬‬"
            ),
            (
                # translation_word
                "стихотворение",
                # pronunciation_word
                "ʃir",
                # hebrew_word_nikud
                "‫שִיר‬‬"
            ),
            (
                # translation_word
                "поэзия",
                # pronunciation_word
                "ʃira",
                # hebrew_word_nikud
                "‫שִירָה‬‬"
            ),
            (
                # translation_word
                "поэт",
                # pronunciation_word
                "meʃorer",
                # hebrew_word_nikud
                "‫מְשוֹרֵר‬‬"
            ),
            (
                # translation_word
                "учебная литература",
                # pronunciation_word
                "sifrut limudit",
                # hebrew_word_nikud
                "סִפרוּת‬ ‫לִימוּדִית‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "145. Музыка. Эстрада",
        # words
        [
            (
                # translation_word
                "музыка",
                # pronunciation_word
                "'muzika",
                # hebrew_word_nikud
                "‫מוּזִיקָה‬‬"
            ),
            (
                # translation_word
                "музыкант",
                # pronunciation_word
                "muzikai",
                # hebrew_word_nikud
                "‫מוּזִיקַאי‬‬"
            ),
            (
                # translation_word
                "играть на ...",
                # pronunciation_word
                "enagen be...",
                # hebrew_word_nikud
                "...לְנַגֵן ‫ב‬‬"
            ),
            (
                # translation_word
                "гитара",
                # pronunciation_word
                "gi'tara",
                # hebrew_word_nikud
                "‫גִיטָרָה‬‬"
            ),
            (
                # translation_word
                "скрипка",
                # pronunciation_word
                "kinor",
                # hebrew_word_nikud
                "‬‫כִּינוֹר‬"
            ),
            (
                # translation_word
                "пианино",
                # pronunciation_word
                "psanter",
                # hebrew_word_nikud
                "‫פּסַנתֵר‬‬"
            ),
            (
                # translation_word
                "барабан",
                # pronunciation_word
                "tof",
                # hebrew_word_nikud
                "‫תוֹף‬‬"
            ),
            (
                # translation_word
                "поп-музыка",
                # pronunciation_word
                "'muzikat pop",
                # hebrew_word_nikud
                "מוּזִיקַת‬ ‫פּוֹפ‬‬"
            ),
            (
                # translation_word
                "рок-музыка",
                # pronunciation_word
                "'muzikat rok",
                # hebrew_word_nikud
                "מוּזִיקַת‬ ‫רוֹק‬‬"
            ),
            (
                # translation_word
                "концерт",
                # pronunciation_word
                "konʦert",
                # hebrew_word_nikud
                "‫קוֹנצֶרט‬‬"
            ),
            (
                # translation_word
                "симфония",
                # pronunciation_word
                "si'fonya",
                # hebrew_word_nikud
                "‫סִימפוֹניָה‬‬"
            ),
            (
                # translation_word
                "песня",
                # pronunciation_word
                "ʃir",
                # hebrew_word_nikud
                "‫שִיר‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "146. Турпоездка",
        # words
        [
            (
                # translation_word
                "туризм",
                # pronunciation_word
                "tayarut",
                # hebrew_word_nikud
                "‬‫תַייָרוּת‬"
            ),
            (
                # translation_word
                "турист",
                # pronunciation_word
                "tayar",
                # hebrew_word_nikud
                "‬‫תַייָר‬"
            ),
            (
                # translation_word
                "путешествие",
                # pronunciation_word
                "tiyul",
                # hebrew_word_nikud
                "‫טִיוּל‬‬"
            ),
            (
                # translation_word
                "поездка",
                # pronunciation_word
                "nesiʿa",
                # hebrew_word_nikud
                "‬‫נְסִיעָה‬"
            ),
            (
                # translation_word
                "отпуск",
                # pronunciation_word
                "χufʃa",
                # hebrew_word_nikud
                "‫חוּפשָה‬‬"
            ),
            (
                # translation_word
                "отдых",
                # pronunciation_word
                "menuχa",
                # hebrew_word_nikud
                "‫מְנוּחָה‬‬"
            ),
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
                "самолёт",
                # pronunciation_word
                "matos",
                # hebrew_word_nikud
                "‫מָטוֹס‬‬"
            ),
            (
                # translation_word
                "багаж",
                # pronunciation_word
                "mitʿan",
                # hebrew_word_nikud
                "‫מִטעָן‬‬"
            ),
            (
                # translation_word
                "паспорт",
                # pronunciation_word
                "darkon",
                # hebrew_word_nikud
                "‫דַרכּוֹן‬‬"
            ),
            (
                # translation_word
                "виза",
                # pronunciation_word
                "viza",
                # hebrew_word_nikud
                "‫וִיזָה‬‬"
            ),
            (
                # translation_word
                "авиабилет",
                # pronunciation_word
                "kartis tisa",
                # hebrew_word_nikud
                "‫טִיסָה‬ ‫כַּרטִיס‬‬"
            ),
            (
                # translation_word
                "карта (географ.)",
                # pronunciation_word
                "mapa",
                # hebrew_word_nikud
                "‫מַפָּה‬‬"
            ),
            (
                # translation_word
                "экскурсия",
                # pronunciation_word
                "tiyul",
                # hebrew_word_nikud
                "‫טִיוּל‬‬"
            ),
            (
                # translation_word
                "экскурсовод",
                # pronunciation_word
                "madriχ tiyulim",
                # hebrew_word_nikud
                "מַדרִיך‬ ‫טִיוּלִים‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "147. Гостиница",
        # words
        [
            (
                # translation_word
                "гостиница",
                # pronunciation_word
                "beit malon",
                # hebrew_word_nikud
                "בֵּית‬ ‫מָלוֹן‬‬"
            ),
            (
                # translation_word
                "отель",
                # pronunciation_word
                "malon",
                # hebrew_word_nikud
                "‫מָלוֹן‬‬"
            ),
            (
                # translation_word
                "остановиться (в отеле)",
                # pronunciation_word
                "lehitʾaχsen",
                # hebrew_word_nikud
                "‫לְהִתאַכסֵן‬‬"
            ),
            (
                # translation_word
                "номер (в гостинице)",
                # pronunciation_word
                "'χeder",
                # hebrew_word_nikud
                "‫חֶדֶר‬‬"
            ),
            (
                # translation_word
                "одноместный номер",
                # pronunciation_word
                "'χeder yaχid",
                # hebrew_word_nikud
                "חֶדֶר‬ ‫יָחִיד‬‬"
            ),
            (
                # translation_word
                "двухместный номер",
                # pronunciation_word
                "'χeder zugi",
                # hebrew_word_nikud
                "חֶדֶר‬ ‫זוּגִי‬‬"
            ),
            (
                # translation_word
                "бронировать номер",
                # pronunciation_word
                "lehazmin 'χeder",
                # hebrew_word_nikud
                "‬לְהַזמִין‬ ‫חֶדֶר‬"
            ),
            (
                # translation_word
                "с ванной",
                # pronunciation_word
                "im am'batya",
                # hebrew_word_nikud
                "עִם‬ ‫אַמבַּטיָה‬‬"
            ),
            (
                # translation_word
                "с душем",
                # pronunciation_word
                "im mik'laχat",
                # hebrew_word_nikud
                "‬עִם‬ ‫מִקלַחַת‬"
            ),
            (
                # translation_word
                "кондиционер",
                # pronunciation_word
                "mazgan",
                # hebrew_word_nikud
                "‫מַזגָן‬‬"
            ),
            (
                # translation_word
                "полотенце",
                # pronunciation_word
                "ma'gevet",
                # hebrew_word_nikud
                "‫מַגֶבֶת‬‬"
            ),
            (
                # translation_word
                "ключ",
                # pronunciation_word
                "maf'teaχ",
                # hebrew_word_nikud
                "‬‫מַפתֵח‬"
            ),
            (
                # translation_word
                "администратор",
                # pronunciation_word
                "amarkal",
                # hebrew_word_nikud
                "‫אֲמַרכָּל‬‬"
            ),
            (
                # translation_word
                "горничная",
                # pronunciation_word
                "χadranit",
                # hebrew_word_nikud
                "‫חַדרָנִית‬‬"
            ),
            (
                # translation_word
                "носильщик",
                # pronunciation_word
                "sabal",
                # hebrew_word_nikud
                "‫סַבָּל‬‬"
            ),
            (
                # translation_word
                "ресторан",
                # pronunciation_word
                "misʿada",
                # hebrew_word_nikud
                "‬‫מִסעָדָה‬"
            ),
            (
                # translation_word
                "бар",
                # pronunciation_word
                "bar",
                # hebrew_word_nikud
                "‬‫בָּר‬"
            ),
            (
                # translation_word
                "завтрак",
                # pronunciation_word
                "aruχat 'boker",
                # hebrew_word_nikud
                "‬אֲרוּחַת‬ ‫בּוֹקֶר‬"
            ),
            (
                # translation_word
                "ужин",
                # pronunciation_word
                "aruχat 'erev",
                # hebrew_word_nikud
                "אֲרוּחַת‬ ‫עֶרֶב‬‬"
            ),
            (
                # translation_word
                "шведский стол",
                # pronunciation_word
                "miznon",
                # hebrew_word_nikud
                "‫מִזנוֹן‬‬"
            ),
            (
                # translation_word
                "вестибюль",
                # pronunciation_word
                "'lobi",
                # hebrew_word_nikud
                "‫לוֹבִּי‬‬"
            ),
            (
                # translation_word
                "лифт",
                # pronunciation_word
                "maʿalit",
                # hebrew_word_nikud
                "‫מַעֲלִית‬‬"
            ),
            (
                # translation_word
                "НЕ БЕСПОКОИТЬ",
                # pronunciation_word
                "lo lehaf'riʿa",
                # hebrew_word_nikud
                "לֹא‬ ‫לְהַפרִיע‬‬"
            ),
            (
                # translation_word
                "НЕ КУРИТЬ!",
                # pronunciation_word
                "asur leʿaʃen!",
                # hebrew_word_nikud
                "!אָסוּר‬ ‫לְעַשֵן‬‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "148. Книга. Чтение",
        # words
        [
            (
                # translation_word
                "книга",
                # pronunciation_word
                "'sefer",
                # hebrew_word_nikud
                "‬‫סֶפֶר‬"
            ),
            (
                # translation_word
                "автор",
                # pronunciation_word
                "sofer",
                # hebrew_word_nikud
                "‫סוֹפֵר‬‬"
            ),
            (
                # translation_word
                "написать (книгу)",
                # pronunciation_word
                "liχtov",
                # hebrew_word_nikud
                "‫לִכתוֹב‬‬"
            ),
            (
                # translation_word
                "читатель",
                # pronunciation_word
                "kore",
                # hebrew_word_nikud
                "‬‫קוֹרֵא‬"
            ),
            (
                # translation_word
                "читать",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "чтение",
                # pronunciation_word
                "kriʾa",
                # hebrew_word_nikud
                "‫קרִיאָה‬‬"
            ),
            (
                # translation_word
                "издатель",
                # pronunciation_word
                "moʦi leʾor",
                # hebrew_word_nikud
                "מוֹצִיא‬ ‫לְאוֹר‬‬"
            ),
            (
                # translation_word
                "издательство",
                # pronunciation_word
                "hoʦaʾa laʾor",
                # hebrew_word_nikud
                "‬הוֹצָאָה‬ ‫לָאוֹר‬"
            ),
            (
                # translation_word
                "книжный магазин",
                # pronunciation_word
                "χanut sfarim",
                # hebrew_word_nikud
                "חֲנוּת‬ ‫ספָרִים‬‬"
            ),
            (
                # translation_word
                "библиотека",
                # pronunciation_word
                "sifriya",
                # hebrew_word_nikud
                "‫סִפרִייָה‬‬"
            ),
            (
                # translation_word
                "сюжет",
                # pronunciation_word
                "alila",
                # hebrew_word_nikud
                "‫עֲלִילָה‬‬"
            ),
            (
                # translation_word
                "содержание (список)",
                # pronunciation_word
                "'toχen",
                # hebrew_word_nikud
                "‫תוֹכֶן‬‬"
            ),
            (
                # translation_word
                "страница",
                # pronunciation_word
                "amud",
                # hebrew_word_nikud
                "‬‫עַמוּד‬"
            ),
            (
                # translation_word
                "текст",
                # pronunciation_word
                "tekst",
                # hebrew_word_nikud
                "‫טֶקסט‬‬"
            ),
            (
                # translation_word
                "шрифт",
                # pronunciation_word
                "gufan",
                # hebrew_word_nikud
                "‫גוּפָן‬‬"
            ),
            (
                # translation_word
                "бестселлер",
                # pronunciation_word
                "rav 'meχer",
                # hebrew_word_nikud
                "‫רַב־מֶכֶר‬‬"
            ),
            (
                # translation_word
                "словарь",
                # pronunciation_word
                "milon",
                # hebrew_word_nikud
                "‫מִילוֹן‬‬"
            ),
            (
                # translation_word
                "учебник",
                # pronunciation_word
                "'sefer limud",
                # hebrew_word_nikud
                "סֵפֶר‬ ‫לִימוּד‬‬"
            ),
            (
                # translation_word
                "энциклопедия",
                # pronunciation_word
                "enʦiklo'pedya",
                # hebrew_word_nikud
                "‫אֶנצִיקלוֹפֶּדיָה‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "149. Активные виды отдыха.",
        # words
        [
            (
                # translation_word
                "охота",
                # pronunciation_word
                "'ʦayid",
                # hebrew_word_nikud
                "‫צַיִד‬‬"
            ),
            (
                # translation_word
                "рыбалка",
                # pronunciation_word
                "'dayig",
                # hebrew_word_nikud
                "‬‫דַיִג‬"
            ),
            (
                # translation_word
                "бильярд",
                # pronunciation_word
                "bilyard",
                # hebrew_word_nikud
                "‬‫בִּיליַארד‬"
            ),
            (
                # translation_word
                "карты",
                # pronunciation_word
                "klafim",
                # hebrew_word_nikud
                "‫קלָפִים‬‬"
            ),
            (
                # translation_word
                "казино",
                # pronunciation_word
                "ka'zino",
                # hebrew_word_nikud
                "‫קָזִינו‬‬"
            ),
            (
                # translation_word
                "гулять (прогуливаться)",
                # pronunciation_word
                "letayel ba'regel",
                # hebrew_word_nikud
                "‬לְטַייֵל‬ ‫בָּרֶגֶל‬"
            ),
            (
                # translation_word
                "пикник",
                # pronunciation_word
                "'piknik",
                # hebrew_word_nikud
                "‫פִּיקנִיק‬‬"
            ),
            (
                # translation_word
                "игра",
                # pronunciation_word
                "misχak",
                # hebrew_word_nikud
                "‫מִשׂחָק‬‬"
            ),
            (
                # translation_word
                "дискотека",
                # pronunciation_word
                "diskotek",
                # hebrew_word_nikud
                "‫דִיסקוֹטֶק‬‬"
            ),
            (
                # translation_word
                "сауна",
                # pronunciation_word
                "'saʾuna",
                # hebrew_word_nikud
                "‫סָאוּנָה‬‬"
            ),
            (
                # translation_word
                "поход",
                # pronunciation_word
                "tiyul maχanaʾut",
                # hebrew_word_nikud
                "טִיוּל‬ ‫מַחֲנָאוּת‬‬"
            ),
            (
                # translation_word
                "лагерь",
                # pronunciation_word
                "maχane",
                # hebrew_word_nikud
                "‫מַחֲנֶה‬‬"
            ),
            (
                # translation_word
                "смотреть (телевизор)",
                # pronunciation_word
                "lirʾot",
                # hebrew_word_nikud
                "‫לִראוֹת‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "150. Пляж",
        # words
        [
            (
                # translation_word
                "пляж",
                # pronunciation_word
                "χof yam",
                # hebrew_word_nikud
                "חוֹף‬ ‫יָם‬‬"
            ),
            (
                # translation_word
                "песок",
                # pronunciation_word
                "χol",
                # hebrew_word_nikud
                "‬‫חוֹל‬"
            ),
            (
                # translation_word
                "пустынный (пляж)",
                # pronunciation_word
                "ʃomem",
                # hebrew_word_nikud
                "‫שוֹמֵם‬‬"
            ),
            (
                # translation_word
                "загар",
                # pronunciation_word
                "ʃizuf",
                # hebrew_word_nikud
                "‫שִיזוּף‬‬"
            ),
            (
                # translation_word
                "загорать",
                # pronunciation_word
                "lehiʃtazef",
                # hebrew_word_nikud
                "‫לְהִשתַזֵף‬‬"
            ),
            (
                # translation_word
                "крем для загара",
                # pronunciation_word
                "krem hagana",
                # hebrew_word_nikud
                "‬קרֶם‬ ‫הֲגָנָה‬"
            ),
            (
                # translation_word
                "бикини",
                # pronunciation_word
                "bi'kini",
                # hebrew_word_nikud
                "‫בִּיקִינִי‬‬"
            ),
            (
                # translation_word
                "купальник, плавки",
                # pronunciation_word
                "beged yam",
                # hebrew_word_nikud
                "בֶּגֶד‬ ‫יָם‬‬"
            ),
            (
                # translation_word
                "бассейн",
                # pronunciation_word
                "breχa",
                # hebrew_word_nikud
                "‫בּרֵיכָה‬‬"
            ),
            (
                # translation_word
                "плавать",
                # pronunciation_word
                "lisχot",
                # hebrew_word_nikud
                "‫לִשׂחוֹת‬‬"
            ),
            (
                # translation_word
                "переодеваться",
                # pronunciation_word
                "lehaχlif bgadim",
                # hebrew_word_nikud
                "לְהַחלִיף‬ ‫בּגָדִים‬‬"
            ),
            (
                # translation_word
                "лодка",
                # pronunciation_word
                "sira",
                # hebrew_word_nikud
                "‫סִירָה‬‬"
            ),
            (
                # translation_word
                "нырять",
                # pronunciation_word
                "liʦlol",
                # hebrew_word_nikud
                "‬‫לִצלוֹל‬"
            ),
            (
                # translation_word
                "купаться",
                # pronunciation_word
                "lehitraχeʦ",
                # hebrew_word_nikud
                "‫לְהִתרַחֵץ‬‬"
            ),
            (
                # translation_word
                "волна",
                # pronunciation_word
                "gal",
                # hebrew_word_nikud
                "‫גַל‬‬"
            ),
            (
                # translation_word
                "спасать",
                # pronunciation_word
                "lehaʦil",
                # hebrew_word_nikud
                "‫לְהַצִיל‬‬"
            ),
            (
                # translation_word
                "спасатель",
                # pronunciation_word
                "maʦil",
                # hebrew_word_nikud
                "‫מַצִיל‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "151. Компьютер",
        # words
        [
            (
                # translation_word
                "компьютер",
                # pronunciation_word
                "maχʃev",
                # hebrew_word_nikud
                "‫מַחשֵב‬‬"
            ),
            (
                # translation_word
                "ноутбук",
                # pronunciation_word
                "maχʃev nayad",
                # hebrew_word_nikud
                "מַחשֵב‬ ‫נַייָד‬‬"
            ),
            (
                # translation_word
                "включить",
                # pronunciation_word
                "lehadlik",
                # hebrew_word_nikud
                "‬‫לְהַדלִיק‬"
            ),
            (
                # translation_word
                "выключить",
                # pronunciation_word
                "leχabot",
                # hebrew_word_nikud
                "‫לְכַבּוֹת‬‬"
            ),
            (
                # translation_word
                "клавиатура",
                # pronunciation_word
                "mik'ledet",
                # hebrew_word_nikud
                "‫מִקלֶדֶת‬‬"
            ),
            (
                # translation_word
                "мышь",
                # pronunciation_word
                "aχbar",
                # hebrew_word_nikud
                "‫עַכבָּר‬‬"
            ),
            (
                # translation_word
                "курсор",
                # pronunciation_word
                "saman",
                # hebrew_word_nikud
                "‫סַמָן‬‬"
            ),
            (
                # translation_word
                "кнопка",
                # pronunciation_word
                "kaftor",
                # hebrew_word_nikud
                "‫כַּפתוֹר‬‬"
            ),
            (
                # translation_word
                "монитор",
                # pronunciation_word
                "masaχ",
                # hebrew_word_nikud
                "‫מָסָך‬‬"
            ),
            (
                # translation_word
                "экран",
                # pronunciation_word
                "ʦag",
                # hebrew_word_nikud
                "‫צָג‬‬"
            ),
            (
                # translation_word
                "жёсткий диск",
                # pronunciation_word
                "disk ka'ʃiaχ",
                # hebrew_word_nikud
                "דִיסק‬ ַ‫קָשִיח‬‬"
            ),
            (
                # translation_word
                "оперативная память",
                # pronunciation_word
                "zikaron giʃa akraʾit",
                # hebrew_word_nikud
                "זִיכָּרוֹן‬ ‫גיִשָה‬ ‫אַקרַאִית‬‬"
            ),
            (
                # translation_word
                "файл",
                # pronunciation_word
                "'koveʦ",
                # hebrew_word_nikud
                "‫קוֹבֶץ‬‬"
            ),
            (
                # translation_word
                "папка (комп.)",
                # pronunciation_word
                "tikiya",
                # hebrew_word_nikud
                "‬‫תִיקִייָה‬"
            ),
            (
                # translation_word
                "открыть",
                # pronunciation_word
                "lif'toaχ",
                # hebrew_word_nikud
                "‫לִפתוֹח‬‬"
            ),
            (
                # translation_word
                "закрыть",
                # pronunciation_word
                "lisgor",
                # hebrew_word_nikud
                "‫לִסגוֹר‬‬"
            ),
            (
                # translation_word
                "сохранить",
                # pronunciation_word
                "liʃmor",
                # hebrew_word_nikud
                "‫לִשמוֹר‬‬"
            ),
            (
                # translation_word
                "удалить",
                # pronunciation_word
                "limχok",
                # hebrew_word_nikud
                "‫לִמחוֹק‬‬"
            ),
            (
                # translation_word
                "скопировать",
                # pronunciation_word
                "lehaʿatik",
                # hebrew_word_nikud
                "‫לְהַעֲתִיק‬‬"
            ),
            (
                # translation_word
                "программа, программное обеспечение",
                # pronunciation_word
                "toχna",
                # hebrew_word_nikud
                "‫תוֹכנָה‬‬"
            ),
            (
                # translation_word
                "программист",
                # pronunciation_word
                "metaχnet",
                # hebrew_word_nikud
                "‫מְתַכנֵת‬‬"
            ),
            (
                # translation_word
                "программировать",
                # pronunciation_word
                "letaχnet",
                # hebrew_word_nikud
                "‫לְתַכנֵת‬‬"
            ),
            (
                # translation_word
                "хакер",
                # pronunciation_word
                "'haker",
                # hebrew_word_nikud
                "‫הָאקֶר‬‬"
            ),
            (
                # translation_word
                "пароль",
                # pronunciation_word
                "sisma",
                # hebrew_word_nikud
                "‫סִיסמָה‬‬"
            ),
            (
                # translation_word
                "вирус",
                # pronunciation_word
                "'virus",
                # hebrew_word_nikud
                "‫וִירוּס‬‬"
            ),
            (
                # translation_word
                "байт",
                # pronunciation_word
                "bait",
                # hebrew_word_nikud
                "‫בַּייט‬‬"
            ),
            (
                # translation_word
                "данные",
                # pronunciation_word
                "netunim",
                # hebrew_word_nikud
                "‬‫נְתוּנִים‬"
            ),
            (
                # translation_word
                "база данных",
                # pronunciation_word
                "bsis netunim",
                # hebrew_word_nikud
                "בּסִיס‬ ‫נְתוּנִים‬‬‬"
            ),
            (
                # translation_word
                "кабель",
                # pronunciation_word
                "'kevel",
                # hebrew_word_nikud
                "‬‫כֶּבֶל‬"
            ),
            (
                # translation_word
                "отсоединить",
                # pronunciation_word
                "lenatek",
                # hebrew_word_nikud
                "‬‫לְנַתֵק‬"
            ),(
                # translation_word
                "подсоединить",
                # pronunciation_word
                "leχaber",
                # hebrew_word_nikud
                "‫לְחַבֵּר‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "152. Интернет. E-mail",
        # words
        [
            (
                # translation_word
                "интернет",
                # pronunciation_word
                "'internet",
                # hebrew_word_nikud
                "‫אִינטֶרנֶט‬‬"
            ),
            (
                # translation_word
                "браузер",
                # pronunciation_word
                "dafdefan",
                # hebrew_word_nikud
                "‫דַפדְפָן‬‬"
            ),
            (
                # translation_word
                "провайдер",
                # pronunciation_word
                "sapak",
                # hebrew_word_nikud
                "‫סַפָּק‬‬"
            ),
            (
                # translation_word
                "веб-сайт",
                # pronunciation_word
                "atar",
                # hebrew_word_nikud
                "‬‫אֲתַר‬"
            ),
            (
                # translation_word
                "адрес",
                # pronunciation_word
                "'ktovet",
                # hebrew_word_nikud
                "‫כּתוֹבֶת‬‬"
            ),
            (
                # translation_word
                "сообщение",
                # pronunciation_word
                "hodaʿa",
                # hebrew_word_nikud
                "‫הוֹדָעָה‬‬"
            ),
            (
                # translation_word
                "переписка",
                # pronunciation_word
                "hitkatvut",
                # hebrew_word_nikud
                "‫הִתכַּתבוּת‬‬"
            ),
            (
                # translation_word
                "связь",
                # pronunciation_word
                "χibur",
                # hebrew_word_nikud
                "‫חִיבּוּר‬‬"
            ),
            (
                # translation_word
                "скорость",
                # pronunciation_word
                "mehirut",
                # hebrew_word_nikud
                "‫מְהִירוּת‬‬"
            ),
            (
                # translation_word
                "модем",
                # pronunciation_word
                "'modem",
                # hebrew_word_nikud
                "‫מוֹדֶם‬‬"
            ),
            (
                # translation_word
                "доступ",
                # pronunciation_word
                "giʃa",
                # hebrew_word_nikud
                "‫גִישָה‬‬"
            ),
            (
                # translation_word
                "порт (комп.)",
                # pronunciation_word
                "port",
                # hebrew_word_nikud
                "‬‫פּוֹרט‬"
            ),
            (
                # translation_word
                "подключение",
                # pronunciation_word
                "χibur",
                # hebrew_word_nikud
                "‫חִיבּוּר‬‬"
            ),
            (
                # translation_word
                "подключиться",
                # pronunciation_word
                "lehitχaber",
                # hebrew_word_nikud
                "‫לְהִתחַבֵּר‬‬"
            ),
            (
                # translation_word
                "искать",
                # pronunciation_word
                "leχapes",
                # hebrew_word_nikud
                "‬‫לְחַפֵּש‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "153. Электричество",
        # words
        [
            (
                # translation_word
                "электричество",
                # pronunciation_word
                "χaʃmal",
                # hebrew_word_nikud
                "‫חַשמַל‬‬"
            ),
            (
                # translation_word
                "электрический",
                # pronunciation_word
                "χaʃmali",
                # hebrew_word_nikud
                "‫חַשמַלִי‬‬"
            ),
            (
                # translation_word
                "энергия",
                # pronunciation_word
                "e'nergya",
                # hebrew_word_nikud
                "‫אֶנֶרגיָה‬‬"
            ),
            (
                # translation_word
                "электроэнергия",
                # pronunciation_word
                "e'nergya χaʃmalit",
                # hebrew_word_nikud
                "‬אֶנֶרגיָה‬ ‫חַשמַלִית‬"
            ),
            (
                # translation_word
                "лампочка",
                # pronunciation_word
                "nura",
                # hebrew_word_nikud
                "‫נוּרָה‬‬"
            ),
            (
                # translation_word
                "свет (электричество)",
                # pronunciation_word
                "or",
                # hebrew_word_nikud
                "‫אוֹר‬‬"
            ),
            (
                # translation_word
                "выключатель",
                # pronunciation_word
                "'meteg",
                # hebrew_word_nikud
                "‫מֶתֶג‬‬"
            ),
            (
                # translation_word
                "розетка",
                # pronunciation_word
                "'ʃeka",
                # hebrew_word_nikud
                "‫שֶקַע‬‬"
            ),
            (
                # translation_word
                "вилка",
                # pronunciation_word
                "'teka",
                # hebrew_word_nikud
                "‬‫תֶקַע‬"
            ),
            (
                # translation_word
                "удлинитель",
                # pronunciation_word
                "'kabel maʾariχ",
                # hebrew_word_nikud
                "כַּבֶּל‬ ‫מַאֲרִיך‬‬"
            ),
            (
                # translation_word
                "предохранитель",
                # pronunciation_word
                "natiχ",
                # hebrew_word_nikud
                "‫נָתִיך‬‬"
            ),
            (
                # translation_word
                "электрик",
                # pronunciation_word
                "χaʃmalai",
                # hebrew_word_nikud
                "‫חַשמַלאַי‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "154. Самолёт",
        # words
        [
            (
                # translation_word
                "самолёт",
                # pronunciation_word
                "matos",
                # hebrew_word_nikud
                "‫מָטוֹס‬‬"
            ),
            (
                # translation_word
                "авиабилет",
                # pronunciation_word
                "kartis tisa",
                # hebrew_word_nikud
                "כַּרטִיס‬ ‫טִיסָה‬‬‬"
            ),
            (
                # translation_word
                "авиакомпания",
                # pronunciation_word
                "χevrat teʿufa",
                # hebrew_word_nikud
                "חֶברַת‬ ‫תְעוּפָה‬‬"
            ),
            (
                # translation_word
                "аэропорт",
                # pronunciation_word
                "nemal teʿufa",
                # hebrew_word_nikud
                "נְמַל‬ ‫תְעוּפָה‬‬"
            ),
            (
                # translation_word
                "пилот",
                # pronunciation_word
                "tayas",
                # hebrew_word_nikud
                "‫טַייָס‬‬"
            ),
            (
                # translation_word
                "стюардесса",
                # pronunciation_word
                "da'yelet",
                # hebrew_word_nikud
                "‫דַייֶלֶת‬‬"
            ),
            (
                # translation_word
                "парашют",
                # pronunciation_word
                "miʦnaχ",
                # hebrew_word_nikud
                "‫מִצנָח‬‬"
            ),
        ]
    ), 
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
    (
        # group_name_ru
        "156. Аэропорт",
        # words
        [
            (
                # translation_word
                "аэропорт",
                # pronunciation_word
                "nemal teʿufa",
                # hebrew_word_nikud
                "נְמַל‬‬ ‫תְעוּפָה‬‬"
            ),
            (
                # translation_word
                "самолёт",
                # pronunciation_word
                "matos",
                # hebrew_word_nikud
                "‫מָטוֹס‬‬"
            ),
            (
                # translation_word
                "авиакомпания",
                # pronunciation_word
                "χevrat teʿufa",
                # hebrew_word_nikud
                "חֶברַת‬‬ ‫תְעוּפָה‬‬"
            ),
            (
                # translation_word
                "вылет",
                # pronunciation_word
                "hamraʾa",
                # hebrew_word_nikud
                "‫הַמרָאָה‬‬"
            ),
            (
                # translation_word
                "прилёт",
                # pronunciation_word
                "neχita",
                # hebrew_word_nikud
                "‫נְחִיתָה‬‬"
            ),
            (
                # translation_word
                "прилететь",
                # pronunciation_word
                "leha'giʿa betisa",
                # hebrew_word_nikud
                "לְהַגִיע‬‬ ‫בְּטִיסָה‬‬"
            ),
            (
                # translation_word
                "задерживаться (о рейсе)",
                # pronunciation_word
                "lehitʿakev",
                # hebrew_word_nikud
                "‫לְהִתעַכֵּב‬‬"
            ),
            (
                # translation_word
                "информационное табло",
                # pronunciation_word
                "'luaχ meida",
                # hebrew_word_nikud
                "לוּח‬‬ ‫מֵידָע‬‬"
            ),
            (
                # translation_word
                "информация",
                # pronunciation_word
                "meida",
                # hebrew_word_nikud
                "‫מֵידָע‬‬"
            ),
            (
                # translation_word
                "объявлять",
                # pronunciation_word
                "leho'dia",
                # hebrew_word_nikud
                "‫לְהוֹדִיע‬‬"
            ),
            (
                # translation_word
                "рейс",
                # pronunciation_word
                "tisa",
                # hebrew_word_nikud
                "‫טִיסָה‬‬"
            ),
            (
                # translation_word
                "таможня",
                # pronunciation_word
                "'meχes",
                # hebrew_word_nikud
                "‫מֶכֶס‬‬"
            ),
            (
                # translation_word
                "таможенная декларация",
                # pronunciation_word
                "haʦharat meχes",
                # hebrew_word_nikud
                "הַצהָרַת‬‬ ‫מֶכֶס‬‬"
            ),
            (
                # translation_word
                "багаж",
                # pronunciation_word
                "kvuda",
                # hebrew_word_nikud
                "‫כּבוּדָה‬‬"
            ),
            (
                # translation_word
                "ручная кладь",
                # pronunciation_word
                "kvudat yad",
                # hebrew_word_nikud
                "כּבוּדַת‬‬ ‫יָד‬‬"
            ),
            (
                # translation_word
                "посадка",
                # pronunciation_word
                "neχita",
                # hebrew_word_nikud
                "‫נְחִיתָה‬‬"
            ),
            (
                # translation_word
                "трап (к самолету)",
                # pronunciation_word
                "'keveʃ",
                # hebrew_word_nikud
                "‫כֶּבֶש‬‬"
            ),
            (
                # translation_word
                "регистрация",
                # pronunciation_word
                "ʧek in",
                # hebrew_word_nikud
                "צֶ׳ק‬‬ ‫אִין‬‬"
            ),
            (
                # translation_word
                "посадочный талон",
                # pronunciation_word
                "kartis aliya lematos",
                # hebrew_word_nikud
                "‬כַּרטִיס‬‬ ‫עֲלִיָה‬ ‫לְמָטוֹס‬"
            ),
            (
                # translation_word
                "зал ожидания",
                # pronunciation_word
                "traklin tisa",
                # hebrew_word_nikud
                "טרַקלִין‬‬ ‫טיִסָה‬‬"
            ),
        ]
    ),     
    (
        # group_name_ru
        "157. Праздник. Событие",
        # words
        [
            (
                # translation_word
                "праздник (торжество)",
                # pronunciation_word
                "χagiga",
                # hebrew_word_nikud
                "‫חֲגִיגָה‬‬"
            ),
            (
                # translation_word
                "национальный праздник",
                # pronunciation_word
                "χag leʾumi",
                # hebrew_word_nikud
                "חַג‬‬ ‫לְאוּמִי‬‬"
            ),
            (
                # translation_word
                "праздничный день",
                # pronunciation_word
                "yom χag",
                # hebrew_word_nikud
                "‫יוֹם‬‬ ‫חַג‬‬"
            ),
            (
                # translation_word
                "праздновать",
                # pronunciation_word
                "laχgog",
                # hebrew_word_nikud
                "‫לַחגוֹג‬‬"
            ),
            (
                # translation_word
                "событие",
                # pronunciation_word
                "hitraχaʃut",
                # hebrew_word_nikud
                "‫הִתרַחֲשוּת‬‬"
            ),
            (
                # translation_word
                "мероприятие (событие)",
                # pronunciation_word
                "ei'ruʿa",
                # hebrew_word_nikud
                "‫אֵירוּע‬‬"
            ),
            (
                # translation_word
                "годовщина",
                # pronunciation_word
                "yom haʃana",
                # hebrew_word_nikud
                "יוֹם‬‬ ‫הַשָנָה‬‬"
            ),
            (
                # translation_word
                "юбилей",
                # pronunciation_word
                "χag hayovel",
                # hebrew_word_nikud
                "חַג‬‬ ‫הַיוֹבֵל‬‬"
            ),
            (
                # translation_word
                "Новый год",
                # pronunciation_word
                "ʃana χadaʃa",
                # hebrew_word_nikud
                "שָנָה‬‬ ‫חָדָשָה‬‬"
            ),
            (
                # translation_word
                "С Новым Годом!",
                # pronunciation_word
                "ʃana tova!",
                # hebrew_word_nikud
                "!שָנָה‬‬ ‫טוֹבָה‬‬"
            ),
            (
                # translation_word
                "Рождество",
                # pronunciation_word
                "χag hamolad",
                # hebrew_word_nikud
                "חַג‬‬ ‫הַמוֹלָד‬‬"
            ),
            (
                # translation_word
                "салют (фейерверк)",
                # pronunciation_word
                "zikukim",
                # hebrew_word_nikud
                "‫זִיקוּקִים‬‬"
            ),
            (
                # translation_word
                "свадьба",
                # pronunciation_word
                "χatuna",
                # hebrew_word_nikud
                "‫חֲתוּנָה‬‬"
            ),
            (
                # translation_word
                "жених",
                # pronunciation_word
                "χatan",
                # hebrew_word_nikud
                "‫חָתָן‬‬"
            ),
            (
                # translation_word
                "невеста",
                # pronunciation_word
                "kala",
                # hebrew_word_nikud
                "‫הַזמָנָה‬‬"
            ),
            (
                # translation_word
                "приглашать",
                # pronunciation_word
                "lehazmin",
                # hebrew_word_nikud
                "‬‫לְהַזמִין‬"
            ),
            (
                # translation_word
                "приглашение (документ)",
                # pronunciation_word
                "hazmana",
                # hebrew_word_nikud
                "‫הַזמָנָה‬‬"
            ),
            (
                # translation_word
                "гость",
                # pronunciation_word
                "o'reaχ",
                # hebrew_word_nikud
                "‫אוֹרֵח‬‬"
            ),
            (
                # translation_word
                "идти в гости",
                # pronunciation_word
                "levaker",
                # hebrew_word_nikud
                "‬‫לְבַקֵר‬"
            ),
            (
                # translation_word
                "встречать гостей",
                # pronunciation_word
                "lekabel orχim",
                # hebrew_word_nikud
                "לְקַבֵּל‬‬ ‫אוֹרחִים‬‬"
            ),
             (
                # translation_word
                "подарок",
                # pronunciation_word
                "matana",
                # hebrew_word_nikud
                "‫מַתָנָה‬‬"
            ),
            (
                # translation_word
                "дарить (подарок)",
                # pronunciation_word
                "latet matana",
                # hebrew_word_nikud
                "לָתֵת‬‬ ‫מַתָנָה‬‬"
            ),
             (
                # translation_word
                "получать подарки",
                # pronunciation_word
                "lekabel matanot",
                # hebrew_word_nikud
                "לְקַבֵּל‬‬ ‫מַתָנוֹת‬‬"
            ),
            (
                # translation_word
                "букет",
                # pronunciation_word
                "zer",
                # hebrew_word_nikud
                "‫זֵר‬‬"
            ),
             (
                # translation_word
                "поздравление",
                # pronunciation_word
                "braχa",
                # hebrew_word_nikud
                "‫בּרָכָה‬‬"
            ),
            (
                # translation_word
                "поздравлять",
                # pronunciation_word
                "levareχ",
                # hebrew_word_nikud
                "‫לְבָרֵך‬‬"
            ),
             (
                # translation_word
                "тост",
                # pronunciation_word
                "leharim kosit",
                # hebrew_word_nikud
                "לְהָרִים‬‬ ‫כוֹסִית‬‬"
            ),
            (
                # translation_word
                "угощать",
                # pronunciation_word
                "leχabed",
                # hebrew_word_nikud
                "‫לְכַבֵּד‬‬"
            ),
             (
                # translation_word
                "шампанское",
                # pronunciation_word
                "ʃam'panya",
                # hebrew_word_nikud
                "‫שַמפַּניָה‬‬"
            ),
            (
                # translation_word
                "веселье",
                # pronunciation_word
                "aliʦut",
                # hebrew_word_nikud
                "‬‫עֲלִיצוּת‬"
            ),
             (
                # translation_word
                "радость",
                # pronunciation_word
                "simχa",
                # hebrew_word_nikud
                "‫שִׂמחָה‬‬"
            ),
            (
                # translation_word
                "танец",
                # pronunciation_word
                "rikud",
                # hebrew_word_nikud
                "‫רִיקוּד‬‬"
            ),
             (
                # translation_word
                "танцевать",
                # pronunciation_word
                "lirkod",
                # hebrew_word_nikud
                "‫לִרקוֹד‬‬"
            ),
            (
                # translation_word
                "похороны",
                # pronunciation_word
                "levaya",
                # hebrew_word_nikud
                "‫לְווָיָה‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "158. Правитель. Шеф. Руководитель",
        # words
        [
            (
                # translation_word
                "король",
                # pronunciation_word
                "'meleχ",
                # hebrew_word_nikud
                "‫מֶלֶך‬‬"
            ),
            (
                # translation_word
                "королева",
                # pronunciation_word
                "malka",
                # hebrew_word_nikud
                "‫מַלכָּה‬‬"
            ),
            (
                # translation_word
                "президент",
                # pronunciation_word
                "nasi",
                # hebrew_word_nikud
                "‫נָשִׂיא‬‬"
            ),
            (
                # translation_word
                "сенатор",
                # pronunciation_word
                "se'nator",
                # hebrew_word_nikud
                "‫סֶנָאטוֹר‬‬"
            ),
            (
                # translation_word
                "монарх",
                # pronunciation_word
                "'meleχ",
                # hebrew_word_nikud
                "‫מֶלֶך‬‬"
            ),
            (
                # translation_word
                "правитель",
                # pronunciation_word
                "ʃalit",
                # hebrew_word_nikud
                "‫שַלִיט‬‬"
            ),
            (
                # translation_word
                "диктатор",
                # pronunciation_word
                "rodan",
                # hebrew_word_nikud
                "‫רוֹדָן‬‬"
            ),
            (
                # translation_word
                "тиран",
                # pronunciation_word
                "aruʦ",
                # hebrew_word_nikud
                "‫עָרוּץ‬‬"
            ),
            (
                # translation_word
                "директор",
                # pronunciation_word
                "menahel",
                # hebrew_word_nikud
                "‫מְנַהֵל‬‬"
            ),
            (
                # translation_word
                "босс",
                # pronunciation_word
                "bos",
                # hebrew_word_nikud
                "‫בּוֹס‬‬"
            ),
            (
                # translation_word
                "хозяин (владелец)",
                # pronunciation_word
                "'baʿal",
                # hebrew_word_nikud
                "‫בַּעַל‬‬"
            ),
            (
                # translation_word
                "глава (~ делегации)",
                # pronunciation_word
                "roʃ",
                # hebrew_word_nikud
                "‫רֹאש‬‬"
            ),
            (
                # translation_word
                "начальство",
                # pronunciation_word
                "memunim",
                # hebrew_word_nikud
                "‫מְמוּנִים‬‬"
            ),
            (
                # translation_word
                "губернатор",
                # pronunciation_word
                "moʃel",
                # hebrew_word_nikud
                "‫מוֹשֵל‬‬"
            ),
            (
                # translation_word
                "консул",
                # pronunciation_word
                "'konsul",
                # hebrew_word_nikud
                "‫קוֹנסוּל‬‬"
            ),
            (
                # translation_word
                "дипломат",
                # pronunciation_word
                "diplomat",
                # hebrew_word_nikud
                "‫דִיפּלוֹמָט‬‬"
            ),
            (
                # translation_word
                "мэр",
                # pronunciation_word
                "roʃ haʿir",
                # hebrew_word_nikud
                "רֹאש‬‬ ‫הָעִיר‬‬"
            ),
            (
                # translation_word
                "шериф",
                # pronunciation_word
                "ʃerif",
                # hebrew_word_nikud
                "‫שֶרִיף‬‬"
            ),
            (
                # translation_word
                "император",
                # pronunciation_word
                "keisar",
                # hebrew_word_nikud
                "‫קֵיסָר‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "159. Планета Земля",
        # words
        [
            (
                # translation_word
                "Земля, земной шар",
                # pronunciation_word
                "kadur ha'ʾareʦ",
                # hebrew_word_nikud
                "כַּדוּר‬‬ ‫הָאָרֶץ‬‬"
            ),
            (
                # translation_word
                "планета",
                # pronunciation_word
                "koχav 'leχet",
                # hebrew_word_nikud
                "‬כּוֹכַב‬‬ ‫לֶכֶת‬"
            ),
            (
                # translation_word
                "атмосфера",
                # pronunciation_word
                "atmos'fera",
                # hebrew_word_nikud
                "‫אַטמוֹספֶרָה‬‬"
            ),
            (
                # translation_word
                "география",
                # pronunciation_word
                "geʾo'grafya",
                # hebrew_word_nikud
                "‫גֵיאוֹגרַפיָה‬‬"
            ),
            (
                # translation_word
                "природа",
                # pronunciation_word
                "'teva",
                # hebrew_word_nikud
                "‫טֶבַע‬‬"
            ),
            (
                # translation_word
                "Европа",
                # pronunciation_word
                "ei'ropa",
                # hebrew_word_nikud
                "‫אֵירוֹפָּה‬‬"
            ),
            (
                # translation_word
                "Азия",
                # pronunciation_word
                "'asya",
                # hebrew_word_nikud
                "‫אַסיָה‬‬"
            ),
            (
                # translation_word
                "Африка",
                # pronunciation_word
                "'afrika",
                # hebrew_word_nikud
                "‫אַפרִיקָה‬‬"
            ),
            (
                # translation_word
                "Австралия",
                # pronunciation_word
                "ost'ralya",
                # hebrew_word_nikud
                "‫אוֹסטרַליָה‬‬"
            ),
            (
                # translation_word
                "Америка",
                # pronunciation_word
                "a'merika",
                # hebrew_word_nikud
                "‫אָמֶרִיקָה‬‬"
            ),
            (
                # translation_word
                "Северная Америка",
                # pronunciation_word
                "a'merika haʦfonit",
                # hebrew_word_nikud
                "‬אָמֶרִיקָה‬‬ ‬‫הַצפוֹנִית‬"
            ),
            (
                # translation_word
                "Южная Америка",
                # pronunciation_word
                "a'merika hadromit",
                # hebrew_word_nikud
                "אָמֶרִיקָה‬‬‬ ‫הַדרוֹמִית‬‬"
            ),
            (
                # translation_word
                "Антарктида",
                # pronunciation_word
                "ya'beʃet an'tarktika",
                # hebrew_word_nikud
                "‬יַבֶּשֶת‬‬‬ ‫אַנטַארקטִיקָה‬"
            ),
            (
                # translation_word
                "север",
                # pronunciation_word
                "ʦafon",
                # hebrew_word_nikud
                "‫צָפוֹן‬‬"
            ),
            (
                # translation_word
                "юг",
                # pronunciation_word
                "darom",
                # hebrew_word_nikud
                "‬‫דָרוֹם‬"
            ),
            (
                # translation_word
                "запад‬",
                # pronunciation_word
                "maʿarav",
                # hebrew_word_nikud
                "‫מַעֲרָב‬‬"
            ),
            (
                # translation_word
                "восток",
                # pronunciation_word
                "mizraχ",
                # hebrew_word_nikud
                "‬‫מִזרָח‬"
            ),
            (
                # translation_word
                "море",
                # pronunciation_word
                "yam",
                # hebrew_word_nikud
                "‫יָם‬‬"
            ),
            (
                # translation_word
                "океан",
                # pronunciation_word
                "ok'yanos",
                # hebrew_word_nikud
                "‬‫אוֹקיָאנוֹס‬"
            ),
            (
                # translation_word
                "остров",
                # pronunciation_word
                "i",
                # hebrew_word_nikud
                "‫אִי‬‬"
            ),
            (
                # translation_word
                "полуостров",
                # pronunciation_word
                "χaʦi i",
                # hebrew_word_nikud
                "חֲצִי‬‬‬ ‫אִי‬‬"
            ),
            (
                # translation_word
                "волна",
                # pronunciation_word
                "gal",
                # hebrew_word_nikud
                "‫גַל‬‬"
            ),
            (
                # translation_word
                "экватор",
                # pronunciation_word
                "kav hamaʃve",
                # hebrew_word_nikud
                "קַו‬‬‬ ‫הַמַשווֶה‬‬"
            ),
            (
                # translation_word
                "горизонт",
                # pronunciation_word
                "'ofek",
                # hebrew_word_nikud
                "‬‫אוֹפֶק‬"
            ),
            (
                # translation_word
                "небо",
                # pronunciation_word
                "ʃa'mayim",
                # hebrew_word_nikud
                "‫שָמַיִים‬‬"
            ),
            (
                # translation_word
                "воздух",
                # pronunciation_word
                "avir",
                # hebrew_word_nikud
                "‫אֲווִיר‬‬"
            ),
            (
                # translation_word
                "гора",
                # pronunciation_word
                "har",
                # hebrew_word_nikud
                "‫הַר‬‬"
            ),
            (
                # translation_word
                "река",
                # pronunciation_word
                "nahar",
                # hebrew_word_nikud
                "‫נָהָר‬‬"
            ),
            (
                # translation_word
                "лес",
                # pronunciation_word
                "'yaʿar",
                # hebrew_word_nikud
                "‫יַעַר‬‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "160. Погода",
        # words
        [
            (
                # translation_word
                "погода",
                # pronunciation_word
                "'mezeg avir",
                # hebrew_word_nikud
                "מֶזֶג‬‬‬ ‫אֲווִיר‬‬"
            ),
            (
                # translation_word
                "температура",
                # pronunciation_word
                "tempera'tura",
                # hebrew_word_nikud
                "‫טֶמפֶּרָטוּרָה‬‬"
            ),
            (
                # translation_word
                "влажный",
                # pronunciation_word
                "laχ",
                # hebrew_word_nikud
                "‫לַח‬‬"
            ),
            (
                # translation_word
                "жара",
                # pronunciation_word
                "χom",
                # hebrew_word_nikud
                "‫חוֹם‬‬"
            ),
            (
                # translation_word
                "жаркий",
                # pronunciation_word
                "χam",
                # hebrew_word_nikud
                "‫חַם‬‬"
            ),
            (
                # translation_word
                "тепло (о погоде)",
                # pronunciation_word
                "χamim",
                # hebrew_word_nikud
                "‫חָמִים‬‬"
            ),
            (
                # translation_word
                "холодно (о погоде)",
                # pronunciation_word
                "kar",
                # hebrew_word_nikud
                "‫קַר‬‬"
            ),
            (
                # translation_word
                "солнце",
                # pronunciation_word
                "'ʃemeʃ",
                # hebrew_word_nikud
                "‫שֶמֶש‬‬"
            ),
            (
                # translation_word
                "облако",
                # pronunciation_word
                "anan",
                # hebrew_word_nikud
                "‬‫עָנָן‬"
            ),
            (
                # translation_word
                "дождь",
                # pronunciation_word
                "'geʃem",
                # hebrew_word_nikud
                "‫גֶשֶם‬‬"
            ),
            (
                # translation_word
                "ливень",
                # pronunciation_word
                "mabul",
                # hebrew_word_nikud
                "‫מַבּוּל‬‬"
            ),
            (
                # translation_word
                "туман",
                # pronunciation_word
                "arafel",
                # hebrew_word_nikud
                "‫עֲרָפֶל‬‬"
            ),
            (
                # translation_word
                "снег",
                # pronunciation_word
                "'ʃeleg",
                # hebrew_word_nikud
                "‫שֶלֶג‬‬"
            ),
            (
                # translation_word
                "гроза",
                # pronunciation_word
                "sufat reʿamim",
                # hebrew_word_nikud
                "סוּפַת‬‬‬ ‫רְעָמִים‬‬"
            ),
            (
                # translation_word
                "молния",
                # pronunciation_word
                "barak",
                # hebrew_word_nikud
                "‫בָּרָק‬‬"
            ),
            (
                # translation_word
                "гром",
                # pronunciation_word
                "'raʿam",
                # hebrew_word_nikud
                "‬‫רַעַם‬"
            ),
            (
                # translation_word
                "град",
                # pronunciation_word
                "barad",
                # hebrew_word_nikud
                "‫בָּרָד‬‬"
            ),
            (
                # translation_word
                "ураган",
                # pronunciation_word
                "hurikan",
                # hebrew_word_nikud
                "‫הוּרִיקָן‬‬"
            ),
            (
                # translation_word
                "пожар",
                # pronunciation_word
                "srefa",
                # hebrew_word_nikud
                "‬‫שׂרֵיפָה‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "161. Дикие животные",
        # words
        [
            (
                # translation_word
                "животное",
                # pronunciation_word
                "'baʿal χayim",
                # hebrew_word_nikud
                "בַּעַל‬‬‬ ‫חַיִים‬‬"
            ),
            (
                # translation_word
                "хищник",
                # pronunciation_word
                "χayat 'teref",
                # hebrew_word_nikud
                "‬חַייַת‬‬‬ ‫טֶרֶף‬"
            ),
            (
                # translation_word
                "белка",
                # pronunciation_word
                "snaʾi",
                # hebrew_word_nikud
                "‫סנָאִי‬‬"
            ),
            (
                # translation_word
                "кролик",
                # pronunciation_word
                "ʃafan",
                # hebrew_word_nikud
                "‫שָפָן‬‬"
            ),
            (
                # translation_word
                "мышь",
                # pronunciation_word
                "aχbar",
                # hebrew_word_nikud
                "‫עַכבָּר‬‬"
            ),
            (
                # translation_word
                "лошадь",
                # pronunciation_word
                "sus",
                # hebrew_word_nikud
                "‫סוּס‬‬"
            ),
            (
                # translation_word
                "медведь",
                # pronunciation_word
                "dov",
                # hebrew_word_nikud
                "‫דוֹב‬‬"
            ),
            (
                # translation_word
                "панда",
                # pronunciation_word
                "'panda",
                # hebrew_word_nikud
                "‫פַּנדָה‬‬"
            ),
            (
                # translation_word
                "кот",
                # pronunciation_word
                "χatul",
                # hebrew_word_nikud
                "‫חָתוּל‬‬"
            ),
            (
                # translation_word
                "собака",
                # pronunciation_word
                "'kelev",
                # hebrew_word_nikud
                "‫כֶּלֶב‬‬"
            ),
            (
                # translation_word
                "домашние животные",
                # pronunciation_word
                "χayot 'bayit",
                # hebrew_word_nikud
                "חַיוֹת‬‬‬ ‫בַּיִת‬‬"
            ),
            (
                # translation_word
                "змея",
                # pronunciation_word
                "naχaʃ",
                # hebrew_word_nikud
                "‬‫נָחָש‬"
            ),
            (
                # translation_word
                "ящерица",
                # pronunciation_word
                "letaʾa",
                # hebrew_word_nikud
                "‫לְטָאָה‬‬"
            ),
            (
                # translation_word
                "скорпион",
                # pronunciation_word
                "akrav",
                # hebrew_word_nikud
                "‫עַקרָב‬‬"
            ),
            (
                # translation_word
                "насекомое",
                # pronunciation_word
                "χarak",
                # hebrew_word_nikud
                "‫חָרָק‬‬"
            ),
            (
                # translation_word
                "бабочка",
                # pronunciation_word
                "parpar",
                # hebrew_word_nikud
                "‫פַּרפַּר‬‬"
            ),
            (
                # translation_word
                "пчела",
                # pronunciation_word
                "dvora",
                # hebrew_word_nikud
                "‫דבוֹרָה‬‬"
            ),
            (
                # translation_word
                "паук",
                # pronunciation_word
                "akaviʃ",
                # hebrew_word_nikud
                "‫עַכָּבִיש‬‬"
            ),
            (
                # translation_word
                "таракан",
                # pronunciation_word
                "makak",
                # hebrew_word_nikud
                "‫מַקָק‬‬"
            ),
            (
                # translation_word
                "зоопарк",
                # pronunciation_word
                "gan hayot",
                # hebrew_word_nikud
                "גַן‬‬‬ ‫חַיוֹת‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "162. Растения",
        # words
        [
            (
                # translation_word
                "дерево",
                # pronunciation_word
                "eʦ",
                # hebrew_word_nikud
                "‫עֵץ‬‬"
            ),
            (
                # translation_word
                "кустарник",
                # pronunciation_word
                "'siaχ",
                # hebrew_word_nikud
                "‫שִׂיח‬‬"
            ),
            (
                # translation_word
                "гриб",
                # pronunciation_word
                "pitriya",
                # hebrew_word_nikud
                "‫פִּטרִייָה‬‬"
            ),
            (
                # translation_word
                "фрукт, плод",
                # pronunciation_word
                "pri",
                # hebrew_word_nikud
                "‫פּרִי‬‬"
            ),
            (
                # translation_word
                "яблоко",
                # pronunciation_word
                "ta'puaχ",
                # hebrew_word_nikud
                "‫תַפּוּח‬‬"
            ),
            (
                # translation_word
                "груша",
                # pronunciation_word
                "agas",
                # hebrew_word_nikud
                "‬‫אַגָס‬"
            ),
            (
                # translation_word
                "клубника",
                # pronunciation_word
                "tut",
                # hebrew_word_nikud
                "‫תוּת‬‬"
            ),
            (
                # translation_word
                "вишня",
                # pronunciation_word
                "duvdevan",
                # hebrew_word_nikud
                "‫דוּבדְבָן‬‬"
            ),
            (
                # translation_word
                "виноград",
                # pronunciation_word
                "anavim",
                # hebrew_word_nikud
                "‬‫עֲנָבִים‬"
            ),
            (
                # translation_word
                "малина",
                # pronunciation_word
                "'petel",
                # hebrew_word_nikud
                "‬‫פֶּטֶל‬"
            ),
            (
                # translation_word
                "апельсин",
                # pronunciation_word
                "tapuz",
                # hebrew_word_nikud
                "‫תַפּוּז‬‬"
            ),
            (
                # translation_word
                "мандарин",
                # pronunciation_word
                "klemen'tina",
                # hebrew_word_nikud
                "‬‫קלֶמֶנטִינָה‬"
            ),
            (
                # translation_word
                "ананас",
                # pronunciation_word
                "'ananas",
                # hebrew_word_nikud
                "‫אָנָנָס‬‬"
            ),
            (
                # translation_word
                "банан",
                # pronunciation_word
                "ba'nana",
                # hebrew_word_nikud
                "‫בַּנָנָה‬‬"
            ),
            (
                # translation_word
                "финик",
                # pronunciation_word
                "tamar",
                # hebrew_word_nikud
                "‫תָמָר‬‬"
            ),
            (
                # translation_word
                "лимон",
                # pronunciation_word
                "limon",
                # hebrew_word_nikud
                "‫לִימוֹן‬‬"
            ),
            (
                # translation_word
                "абрикос",
                # pronunciation_word
                "'miʃmeʃ",
                # hebrew_word_nikud
                "‫מִשמֵש‬‬"
            ),
            (
                # translation_word
                "персик",
                # pronunciation_word
                "afarsek",
                # hebrew_word_nikud
                "‫אֲפַרסֵק‬‬"
            ),
            (
                # translation_word
                "киви",
                # pronunciation_word
                "'kivi",
                # hebrew_word_nikud
                "‫קִיווִי‬‬"
            ),
            (
                # translation_word
                "грейпфрут",
                # pronunciation_word
                "eʃkolit",
                # hebrew_word_nikud
                "‫אֶשכּוֹלִית‬‬"
            ),
            (
                # translation_word
                "ягоды",
                # pronunciation_word
                "gargerim",
                # hebrew_word_nikud
                "‫גַרגֵרִים‬‬"
            ),
            (
                # translation_word
                "цветок",
                # pronunciation_word
                "'peraχ",
                # hebrew_word_nikud
                "‫פֶּרַח‬‬"
            ),
            (
                # translation_word
                "пшеница",
                # pronunciation_word
                "χita",
                # hebrew_word_nikud
                "‬‫חִיטָה‬"
            ),
            (
                # translation_word
                "рожь",
                # pronunciation_word
                "ʃifon",
                # hebrew_word_nikud
                "‫שִיפוֹן‬‬"
            ),
            (
                # translation_word
                "овёс",
                # pronunciation_word
                "ʃi'bolet ʃuʿal",
                # hebrew_word_nikud
                "שִיבּוֹלֶת‬‬‬ ‫שוּעָל‬‬"
            ),
            (
                # translation_word
                "ячмень",
                # pronunciation_word
                "seʿora",
                # hebrew_word_nikud
                "‫שְׂעוֹרָה‬‬"
            ),
            (
                # translation_word
                "кукуруза",
                # pronunciation_word
                "'tiras",
                # hebrew_word_nikud
                "‫תִירָס‬‬"
            ),
            (
                # translation_word
                "рис",
                # pronunciation_word
                "'orez",
                # hebrew_word_nikud
                "‫אוֹרֶז‬‬"
            ),
            (
                # translation_word
                "овощи",
                # pronunciation_word
                "yerakot",
                # hebrew_word_nikud
                "‬‫יְרָקוֹת‬"
            ),
            (
                # translation_word
                "зелень",
                # pronunciation_word
                "'yerek",
                # hebrew_word_nikud
                "‫יֶרֶק‬‬"
            ),
            (
                # translation_word
                "помидор",
                # pronunciation_word
                "agvaniya",
                # hebrew_word_nikud
                "‫עַגבָנִייָה‬‬"
            ),
            (
                # translation_word
                "огурец",
                # pronunciation_word
                "melafefon",
                # hebrew_word_nikud
                "‫מְלָפְפוֹן‬‬"
            ),
            (
                # translation_word
                "морковь",
                # pronunciation_word
                "'gezer",
                # hebrew_word_nikud
                "‫גֶזֶר‬‬"
            ),
            (
                # translation_word
                "картофель",
                # pronunciation_word
                "ta'puaχ adama",
                # hebrew_word_nikud
                "תַפּוּח‬‬‬ ‫אֲדָמָה‬‬"
            ),
            (
                # translation_word
                "лук",
                # pronunciation_word
                "baʦal",
                # hebrew_word_nikud
                "‫בָּצָל‬‬"
            ),
            (
                # translation_word
                "чеснок",
                # pronunciation_word
                "ʃum",
                # hebrew_word_nikud
                "‫שוּם‬‬"
            ),
            (
                # translation_word
                "капуста",
                # pronunciation_word
                "kruv",
                # hebrew_word_nikud
                "‫כּרוּב‬‬"
            ),
            (
                # translation_word
                "свёкла",
                # pronunciation_word
                "'selek",
                # hebrew_word_nikud
                "‫סֶלֶק‬‬"
            ),
            (
                # translation_word
                "баклажан",
                # pronunciation_word
                "χaʦil",
                # hebrew_word_nikud
                "‫חָצִיל‬‬"
            ),
            (
                # translation_word
                "тыква",
                # pronunciation_word
                "'dlaʿat",
                # hebrew_word_nikud
                "‬‫דלַעַת‬"
            ),
            (
                # translation_word
                "шпинат",
                # pronunciation_word
                "'tered",
                # hebrew_word_nikud
                "‫תֶרֶד‬‬"
            ),
            (
                # translation_word
                "перец",
                # pronunciation_word
                "'pilpel",
                # hebrew_word_nikud
                "‫פִּלפֵּל‬‬"
            ),
        ]
    ),   
    (
        # group_name_ru
        "163. Страны, национальности",
        # words
        [
            (
                # translation_word
                "Австрия",
                # pronunciation_word
                "'ostriya",
                # hebrew_word_nikud
                "‫אוֹסטרִיָה‬‬"
            ),
            (
                # translation_word
                "Соединённые Штаты Америки",
                # pronunciation_word
                "arʦot habrit",
                # hebrew_word_nikud
                "אַרצוֹת‬‬‬ ‫הַבּרִית‬‬‬"
            ),
            (
                # translation_word
                "Великобритания",
                # pronunciation_word
                "bri'tanya hagdola",
                # hebrew_word_nikud
                "בּרִיטַניָה‬‬‬ ָ‫הַגדוֹל‬‬"
            ),
            (
                # translation_word
                "Канада",
                # pronunciation_word
                "'kanada",
                # hebrew_word_nikud
                "‫קָנָדָה‬"
            ),
            (
                # translation_word
                "Бельгия",
                # pronunciation_word
                "'belgya",
                # hebrew_word_nikud
                "‫בֶּלגיָה‬‬"
            ),
            (
                # translation_word
                "Аргентина",
                # pronunciation_word
                "argen'tina",
                # hebrew_word_nikud
                "‫אַרגֶנטִינָה‬‬‬"
            ),
            (
                # translation_word
                "Германия",
                # pronunciation_word
                "ger'manya",
                # hebrew_word_nikud
                "‫גֶרמַניָה‬‬"
            ),
            (
                # translation_word
                "Бразилия",
                # pronunciation_word
                "brazil",
                # hebrew_word_nikud
                "‫בּרָזִיל‬"
            ),
            (
                # translation_word
                "Нидерланды",
                # pronunciation_word
                "'holand",
                # hebrew_word_nikud
                "‫הוֹלַנד‬‬"
            ),
            (
                # translation_word
                "Египет",
                # pronunciation_word
                "miʦ'rayim",
                # hebrew_word_nikud
                "‫מִצרַיִם‬"
            ),
            (
                # translation_word
                "Греция",
                # pronunciation_word
                "yavan",
                # hebrew_word_nikud
                "‫יָווָן‬‬"
            ),
            (
                # translation_word
                "Австралия",
                # pronunciation_word
                "ost'ralya",
                # hebrew_word_nikud
                "‫אוֹסטרַליָה‬"
            ),
            (
                # translation_word
                "Дания",
                # pronunciation_word
                "'denemark",
                # hebrew_word_nikud
                "‫דֶנֶמַרק‬‬"
            ),
            (
                # translation_word
                "Ирландия",
                # pronunciation_word
                "'irland",
                # hebrew_word_nikud
                "‬‫אִירלַנד‬"
            ),
            (
                # translation_word
                "Испания",
                # pronunciation_word
                "sfarad",
                # hebrew_word_nikud
                "‫ספָרַד‬‬"
            ),
            (
                # translation_word
                "Италия",
                # pronunciation_word
                "i'talya",
                # hebrew_word_nikud
                "‫אִיטַליָה‬‬"
            ),
            (
                # translation_word
                "Норвегия",
                # pronunciation_word
                "nor'vegya",
                # hebrew_word_nikud
                "‫נוֹרבֶגיָה‬‬"
            ),
            (
                # translation_word
                "Португалия",
                # pronunciation_word
                "portugal",
                # hebrew_word_nikud
                "‫פּוֹרטוּגָל‬‬"
            ),
            (
                # translation_word
                "Франция",
                # pronunciation_word
                "ʦarfat",
                # hebrew_word_nikud
                "‫צָרפַת‬‬"
            ),
            (
                # translation_word
                "Швеция",
                # pronunciation_word
                "'ʃvedya",
                # hebrew_word_nikud
                "‫שבֶדיָה‬‬"
            ),
            (
                # translation_word
                "Болгария",
                # pronunciation_word
                "bul'garya",
                # hebrew_word_nikud
                "‫בּוּלגַריָה‬‬"
            ),
            (
                # translation_word
                "Литва",
                # pronunciation_word
                "'lita",
                # hebrew_word_nikud
                "‫לִיטָא‬‬"
            ),
            (
                # translation_word
                "Польша",
                # pronunciation_word
                "polin",
                # hebrew_word_nikud
                "‫פּוֹלִין‬‬"
            ),
            (
                # translation_word
                "Чехия",
                # pronunciation_word
                "'ʧeχya",
                # hebrew_word_nikud
                "‫צֶ׳כיָה‬‬"
            ),
            (
                # translation_word
                "Беларусь",
                # pronunciation_word
                "'belarus",
                # hebrew_word_nikud
                "‫בֶּלָרוּס‬‬"
            ),
            (
                # translation_word
                "Россия",
                # pronunciation_word
                "'rusya",
                # hebrew_word_nikud
                "‫רוּסיָה‬‬"
            ),
            (
                # translation_word
                "Украина",
                # pronunciation_word
                "uk'rayna",
                # hebrew_word_nikud
                "‫אוּקרַאינָה‬‬"
            ),
            (
                # translation_word
                "Израиль",
                # pronunciation_word
                "yisraʾel",
                # hebrew_word_nikud
                "‬‫יִשׂרָאֵל‬"
            ),
            (
                # translation_word
                "еврей",
                # pronunciation_word
                "yehudi",
                # hebrew_word_nikud
                "‫יְהוּדִי‬‬"
            ),
            (
                # translation_word
                "еврейка",
                # pronunciation_word
                "yehudiya",
                # hebrew_word_nikud
                "‫יְהוּדִיָה‬‬"
            ),
            (
                # translation_word
                "Китай",
                # pronunciation_word
                "sin",
                # hebrew_word_nikud
                "‫סִין‬‬"
            ),
            (
                # translation_word
                "Турция",
                # pronunciation_word
                "'turkiya",
                # hebrew_word_nikud
                "‫טוּרקִיָה‬‬"
            ),
            (
                # translation_word
                "Япония",
                # pronunciation_word
                "yapan",
                # hebrew_word_nikud
                "‫יַפָּן‬‬"
            ),
            (
                # translation_word
                "Палестина",
                # pronunciation_word
                "falastin",
                # hebrew_word_nikud
                "‫פָלַסטִין‬‬"
            ),
            (
                # translation_word
                "израильтянин",
                # pronunciation_word
                "yisraʾeli",
                # hebrew_word_nikud
                "‫יִשׂרְאֵלִי‬‬"
            ),
            (
                # translation_word
                "израильтянка",
                # pronunciation_word
                "yisraʾelit",
                # hebrew_word_nikud
                "‫יִשׂרְאֵלִית‬‬"
            ),
            (
                # translation_word
                "израильский",
                # pronunciation_word
                "yisraʾeli",
                # hebrew_word_nikud
                "‫יִשׂרְאֵלִי‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "164. Страны. Разное",
        # words
        [
            (
                # translation_word
                "иностранец, иностранный",
                # pronunciation_word
                "zar",
                # hebrew_word_nikud
                "‬‫זָר‬"
            ),
            (
                # translation_word
                "за границей",
                # pronunciation_word
                "beχul",
                # hebrew_word_nikud
                "‫בְּחוּל‬‬"
            ),
            (
                # translation_word
                "эмигрант",
                # pronunciation_word
                "mehager",
                # hebrew_word_nikud
                "‬‫מְהַגֵר‬"
            ),
            (
                # translation_word
                "эмиграция",
                # pronunciation_word
                "hagira",
                # hebrew_word_nikud
                "‬‫הֲגִירָה‬"
            ),
            (
                # translation_word
                "эмигрировать",
                # pronunciation_word
                "lehager",
                # hebrew_word_nikud
                "‫לְהַגֵר‬‬"
            ),
            (
                # translation_word
                "мир (вся планета)",
                # pronunciation_word
                "olam",
                # hebrew_word_nikud
                "‫עוֹלָם‬‬"
            ),
            (
                # translation_word
                "человечество",
                # pronunciation_word
                "enoʃut",
                # hebrew_word_nikud
                "‬‫אֱנוֹשוּת‬"
            ),
            (
                # translation_word
                "родина",
                # pronunciation_word
                "mo'ledet",
                # hebrew_word_nikud
                "‬‫מוֹלֶדֶת‬"
            ),
            (
                # translation_word
                "население",
                # pronunciation_word
                "oχlusiya",
                # hebrew_word_nikud
                "‫אוֹכלוּסִיָה‬‬"
            ),
            (
                # translation_word
                "нация",
                # pronunciation_word
                "uma",
                # hebrew_word_nikud
                "‫אוּמָה‬‬"
            ),
            (
                # translation_word
                "поколение",
                # pronunciation_word
                "dor",
                # hebrew_word_nikud
                "‫דוֹר‬‬"
            ),
            (
                # translation_word
                "территория",
                # pronunciation_word
                "'ʃetaχ",
                # hebrew_word_nikud
                "‬‫שֶטַח‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "165. Мировые религии. Конфессии",
        # words
        [
            (
                # translation_word
                "религия",
                # pronunciation_word
                "dat",
                # hebrew_word_nikud
                "‫דָת‬‬"
            ),
            (
                # translation_word
                "религиозный",
                # pronunciation_word
                "dati",
                # hebrew_word_nikud
                "‫דָתִי‬‬"
            ),
            (
                # translation_word
                "верующий (сущ.)",
                # pronunciation_word
                "maʾamin",
                # hebrew_word_nikud
                "‫מַאֲמִין‬‬"
            ),
            (
                # translation_word
                "атеизм",
                # pronunciation_word
                "ateʾizm",
                # hebrew_word_nikud
                "‫אָתֵאִיזם‬‬"
            ),
            (
                # translation_word
                "атеист",
                # pronunciation_word
                "ateʾist",
                # hebrew_word_nikud
                "‫אָתֵאִיסט‬‬"
            ),
            (
                # translation_word
                "Христианство",
                # pronunciation_word
                "naʦrut",
                # hebrew_word_nikud
                "‫נַצרוּת‬‬"
            ),
            (
                # translation_word
                "христианин",
                # pronunciation_word
                "noʦri",
                # hebrew_word_nikud
                "‫נוֹצרִי‬‬"
            ),
            (
                # translation_word
                "Католицизм",
                # pronunciation_word
                "kaʿtoliyut",
                # hebrew_word_nikud
                "‫נוֹצרִי‬‬"
            ),
            (
                # translation_word
                "Протестантство",
                # pronunciation_word
                "protes'tantiyut",
                # hebrew_word_nikud
                "‫פּרוֹטֶסטַנטִיוּת‬‬"
            ),
            (
                # translation_word
                "Православие",
                # pronunciation_word
                "naʦrut orto'doksit",
                # hebrew_word_nikud
                "נַצרוּת‬‬‬ ‫אוֹרתוֹדוֹקסִית‬‬"
            ),
            (
                # translation_word
                "Иудаизм",
                # pronunciation_word
                "yahadut",
                # hebrew_word_nikud
                "‫יַהדוּת‬‬"
            ),
            (
                # translation_word
                "иудей",
                # pronunciation_word
                "yehudi, yehudiya",
                # hebrew_word_nikud
                " ‫יְהוּדִיָה‬, ‫יְהוּדִי‬‬"
            ),
            (
                # translation_word
                "Ислам",
                # pronunciation_word
                "islam",
                # hebrew_word_nikud
                "‫אִיסלָאם‬‬"
            ),
            (
                # translation_word
                "Бог",
                # pronunciation_word
                "elohim",
                # hebrew_word_nikud
                "‫אֱלוֹהִים‬‬"
            ),
            (
                # translation_word
                "грех",
                # pronunciation_word
                "χet",
                # hebrew_word_nikud
                "‫חֵטא‬‬"
            ),
            (
                # translation_word
                "ад",
                # pronunciation_word
                "gehinom",
                # hebrew_word_nikud
                "‫גֵיהִינוֹם‬‬"
            ),
            (
                # translation_word
                "рай",
                # pronunciation_word
                "gan 'eden",
                # hebrew_word_nikud
                "גַן‬‬‬ ‫עֵדֶן‬‬"
            ),
            (
                # translation_word
                "ангел",
                # pronunciation_word
                "malʾaχ",
                # hebrew_word_nikud
                "‫מַלאָך‬‬"
            ),
            (
                # translation_word
                "Церковь",
                # pronunciation_word
                "knesiya",
                # hebrew_word_nikud
                "‫כּנֵסִייָה‬‬"
            ),
            (
                # translation_word
                "библия",
                # pronunciation_word
                "tanaχ",
                # hebrew_word_nikud
                "‫תַנַך‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "166. Общие существительные",
        # words
        [
            (
                # translation_word
                "база (основа)",
                # pronunciation_word
                "basis",
                # hebrew_word_nikud
                "‫בָּסִיס‬‬"
            ),
            (
                # translation_word
                "баланс",
                # pronunciation_word
                "izun",
                # hebrew_word_nikud
                "‫אִיזוּן‬‬"
            ),
            (
                # translation_word
                "вещь",
                # pronunciation_word
                "'χefeʦ",
                # hebrew_word_nikud
                "‬‫חֶפֶץ‬"
            ),
            (
                # translation_word
                "выбор (ассортимент)",
                # pronunciation_word
                "bχina",
                # hebrew_word_nikud
                "‫בּחִינָה‬‬"
            ),
            (
                # translation_word
                "идеал",
                # pronunciation_word
                "ideʾal",
                # hebrew_word_nikud
                "‫אִידֵיאָל‬‬"
            ),
            (
                # translation_word
                "момент",
                # pronunciation_word
                "'rega",
                # hebrew_word_nikud
                "‬‫רֶגַע‬"
            ),
            (
                # translation_word
                "начало",
                # pronunciation_word
                "hatχala",
                # hebrew_word_nikud
                "‫הַתחָלָה‬‬"
            ),
            (
                # translation_word
                "объект (предмет)",
                # pronunciation_word
                "'eʦem",
                # hebrew_word_nikud
                "‬‫עֶצֶם‬"
            ),
            (
                # translation_word
                "окончание (конец)",
                # pronunciation_word
                "sof",
                # hebrew_word_nikud
                "‫סוֹף‬‬"
            ),
            (
                # translation_word
                "остановка (перерыв)",
                # pronunciation_word
                "hafsaka",
                # hebrew_word_nikud
                "‫הַפסָקָה‬‬"
            ),
            (
                # translation_word
                "очередь (сейчас моя ~)",
                # pronunciation_word
                "tor",
                # hebrew_word_nikud
                "‫תוֹר‬‬"
            ),
            (
                # translation_word
                "ошибка",
                # pronunciation_word
                "taʿut",
                # hebrew_word_nikud
                "‫טָעוּת‬‬"
            ),
            (
                # translation_word
                "пауза",
                # pronunciation_word
                "hafuga",
                # hebrew_word_nikud
                "‫הֲפוּגָה‬‬"
            ),
            (
                # translation_word
                "польза",
                # pronunciation_word
                "to'ʿelet",
                # hebrew_word_nikud
                "‬‫תוֹעֶלֶת‬"
            ),
            (
                # translation_word
                "помощь",
                # pronunciation_word
                "ezra",
                # hebrew_word_nikud
                "‫עֶזרָה‬‬"
            ),
            (
                # translation_word
                "препятствие",
                # pronunciation_word
                "maχsom",
                # hebrew_word_nikud
                "‫מַחסוֹם‬‬"
            ),
            (
                # translation_word
                "пример",
                # pronunciation_word
                "dugma",
                # hebrew_word_nikud
                "‫דוּגמָה‬‬"
            ),
            (
                # translation_word
                "принцип",
                # pronunciation_word
                "ikaron",
                # hebrew_word_nikud
                "‫עִיקָרוֹן‬‬"
            ),
            (
                # translation_word
                "причина",
                # pronunciation_word
                "siba",
                # hebrew_word_nikud
                "‫סִיבָּה‬‬"
            ),
            (
                # translation_word
                "проблема",
                # pronunciation_word
                "beʿaya",
                # hebrew_word_nikud
                "‫בְּעָיָה‬‬"
            ),
            (
                # translation_word
                "процесс",
                # pronunciation_word
                "tahaliχ",
                # hebrew_word_nikud
                "‫תַהֲלִיך‬‬"
            ),
            (
                # translation_word
                "развитие",
                # pronunciation_word
                "hitpatχut",
                # hebrew_word_nikud
                "‫הִתפַּתחוּת‬‬"
            ),
            (
                # translation_word
                "различие",
                # pronunciation_word
                "'ʃoni",
                # hebrew_word_nikud
                "‫שוֹנִי‬‬"
            ),
            (
                # translation_word
                "реакция",
                # pronunciation_word
                "tguva",
                # hebrew_word_nikud
                "‫תגוּבָה‬‬"
            ),
            (
                # translation_word
                "решение (задачи)",
                # pronunciation_word
                "pitaron",
                # hebrew_word_nikud
                "‫פִּיתָרוֹן‬‬"
            ),
            (
                # translation_word
                "риск",
                # pronunciation_word
                "sikun",
                # hebrew_word_nikud
                "‫סִיכּוּן‬‬"
            ),
            (
                # translation_word
                "рост (процесс)",
                # pronunciation_word
                "gidul",
                # hebrew_word_nikud
                "‬‫גִידוּל‬"
            ),
            (
                # translation_word
                "система",
                # pronunciation_word
                "ʃita",
                # hebrew_word_nikud
                "‫שִיטָה‬‬"
            ),
            (
                # translation_word
                "ситуация",
                # pronunciation_word
                "maʦav",
                # hebrew_word_nikud
                "‫מַצָב‬‬"
            ),
            (
                # translation_word
                "совпадение",
                # pronunciation_word
                "hatʾama",
                # hebrew_word_nikud
                "‫הַתאָמָה‬‬"
            ),
            (
                # translation_word
                "способ",
                # pronunciation_word
                "'ofen",
                # hebrew_word_nikud
                "‬‫אוֹפֵן‬"
            ),
            (
                # translation_word
                "сравнение",
                # pronunciation_word
                "haʃvaʾa",
                # hebrew_word_nikud
                "‬‫הַשווָאָה‬"
            ),
            (
                # translation_word
                "срочно",
                # pronunciation_word
                "bidχifut",
                # hebrew_word_nikud
                "‫בִּדחִיפוּת‬‬"
            ),
            (
                # translation_word
                "срочный",
                # pronunciation_word
                "daχuf",
                # hebrew_word_nikud
                "‫דָחוּף‬‬"
            ),
            (
                # translation_word
                "стандарт",
                # pronunciation_word
                "'teken",
                # hebrew_word_nikud
                "‬‫תֶקֶן‬"
            ),
            (
                # translation_word
                "степень",
                # pronunciation_word
                "darga",
                # hebrew_word_nikud
                "‫דַרגָה‬‬"
            ),
            (
                # translation_word
                "стиль",
                # pronunciation_word
                "signon",
                # hebrew_word_nikud
                "‫סִגנוֹן‬‬"
            ),
            (
                # translation_word
                "тайна, секрет",
                # pronunciation_word
                "sod",
                # hebrew_word_nikud
                "‫סוֹד‬‬"
            ),
            (
                # translation_word
                "усилие",
                # pronunciation_word
                "maʾamaʦ",
                # hebrew_word_nikud
                "‫מַאֲמָץ‬‬"
            ),
            (
                # translation_word
                "факт",
                # pronunciation_word
                "uvda",
                # hebrew_word_nikud
                "‬‫עוּבדָה‬"
            ),
            (
                # translation_word
                "часть (целого)",
                # pronunciation_word
                "'χelek",
                # hebrew_word_nikud
                "‫חֶלֶק‬‬"
            ),
            (
                # translation_word
                "элемент",
                # pronunciation_word
                "element",
                # hebrew_word_nikud
                "‫אֶלֶמֶנט‬‬"
            ),
            (
                # translation_word
                "эффект",
                # pronunciation_word
                "efekt",
                # hebrew_word_nikud
                "‫אֶפֶקט‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "167. Прилагательные 1",
        # words
        [
            (
                # translation_word
                "аккуратный",
                # pronunciation_word
                "kapdani",
                # hebrew_word_nikud
                "‫קַפּדָנִי‬‬"
            ),
            (
                # translation_word
                "бедный",
                # pronunciation_word
                "ani",
                # hebrew_word_nikud
                "‬‫עָנִי‬"
            ),
            (
                # translation_word
                "безопасный",
                # pronunciation_word
                "ba'tuaχ",
                # hebrew_word_nikud
                "‫בָּטוּח‬‬"
            ),
            (
                # translation_word
                "бесплатный",
                # pronunciation_word
                "χinam",
                # hebrew_word_nikud
                "‫חִינָם‬‬"
            ),
            (
                # translation_word
                "благодарный",
                # pronunciation_word
                "asir toda",
                # hebrew_word_nikud
                "אֲסִיר‬‬‬ ‫תוֹדָה‬‬"
            ),
            (
                # translation_word
                "близкий",
                # pronunciation_word
                "karov",
                # hebrew_word_nikud
                "‫קָרוֹב‬‬"
            ),
            (
                # translation_word
                "больной",
                # pronunciation_word
                "χole",
                # hebrew_word_nikud
                "‫חוֹלֶה‬‬"
            ),
            (
                # translation_word
                "большой",
                # pronunciation_word
                "gadol",
                # hebrew_word_nikud
                "‫גָדוֹל‬‬"
            ),
            (
                # translation_word
                "быстрый",
                # pronunciation_word
                "mahir",
                # hebrew_word_nikud
                "‫מָהִיר‬‬"
            ),
            (
                # translation_word
                "важный",
                # pronunciation_word
                "χaʃuv",
                # hebrew_word_nikud
                "‫חָשוּב‬‬"
            ),
            (
                # translation_word
                "вежливый",
                # pronunciation_word
                "menumas",
                # hebrew_word_nikud
                "‫מְנוּמָס‬‬"
            ),
            (
                # translation_word
                "весёлый",
                # pronunciation_word
                "sa'meaχ",
                # hebrew_word_nikud
                "‬‫שָׂמֵח‬"
            ),
            (
                # translation_word
                "вкусный",
                # pronunciation_word
                "taʿim",
                # hebrew_word_nikud
                "‫טָעִים‬‬"
            ),
            (
                # translation_word
                "влажный",
                # pronunciation_word
                "laχ",
                # hebrew_word_nikud
                "‫לַח‬‬"
            ),
            (
                # translation_word
                "возможный",
                # pronunciation_word
                "efʃari",
                # hebrew_word_nikud
                "‫אֶפשָרִי‬‬"
            ),
            (
                # translation_word
                "внешний",
                # pronunciation_word
                "χiʦoni",
                # hebrew_word_nikud
                "‫חִיצוֹנִי‬‬"
            ),
            (
                # translation_word
                "внутренний",
                # pronunciation_word
                "pnimi",
                # hebrew_word_nikud
                "‫פּנִימִי‬‬"
            ),
            (
                # translation_word
                "враждебный",
                # pronunciation_word
                "oyen",
                # hebrew_word_nikud
                "‫עוֹיֵן‬‬"
            ),
            (
                # translation_word
                "высший",
                # pronunciation_word
                "haga'voha beyoter",
                # hebrew_word_nikud
                "הַגָבוֹה‬‬‬ ‫בְּיוֹתֵר‬‬"
            ),
            (
                # translation_word
                "главный",
                # pronunciation_word
                "raʃi",
                # hebrew_word_nikud
                "‫רָאשִי‬‬"
            ),
            (
                # translation_word
                "гладкий",
                # pronunciation_word
                "χalak",
                # hebrew_word_nikud
                "‫חָלָק‬‬"
            ),
            (
                # translation_word
                "глупый",
                # pronunciation_word
                "tipeʃ",
                # hebrew_word_nikud
                "‬‫טִיפֵּש‬"
            ),
            (
                # translation_word
                "голодный",
                # pronunciation_word
                "raʿev",
                # hebrew_word_nikud
                "‫רָעֵב‬‬"
            ),
            (
                # translation_word
                "горький",
                # pronunciation_word
                "marir",
                # hebrew_word_nikud
                "‬‫מָרִיר‬"
            ),
            (
                # translation_word
                "горячий",
                # pronunciation_word
                "χam",
                # hebrew_word_nikud
                "‬‫חַם‬"
            ),
            (
                # translation_word
                "громкий",
                # pronunciation_word
                "ram",
                # hebrew_word_nikud
                "‫רָם‬‬"
            ),
            (
                # translation_word
                "грустный",
                # pronunciation_word
                "aʦuv",
                # hebrew_word_nikud
                "‫עָצוּב‬‬"
            ),
            (
                # translation_word
                "грязный",
                # pronunciation_word
                "meluχlaχ",
                # hebrew_word_nikud
                "‫מְלוּכלָך‬‬"
            ),
            (
                # translation_word
                "густой",
                # pronunciation_word
                "samuχ",
                # hebrew_word_nikud
                "‫סָמוּך‬‬"
            ),
            (
                # translation_word
                "дальний",
                # pronunciation_word
                "raχok",
                # hebrew_word_nikud
                "‫רָחוֹק‬‬"
            ),
            (
                # translation_word
                "детский",
                # pronunciation_word
                "yaldi",
                # hebrew_word_nikud
                "‫יַלדִי‬‬"
            ),
            (
                # translation_word
                "длинный",
                # pronunciation_word
                "aroχ",
                # hebrew_word_nikud
                "‫אָרוֹך‬‬"
            ),
            (
                # translation_word
                "добрый",
                # pronunciation_word
                "tov",
                # hebrew_word_nikud
                "‬‫טוֹב‬"
            ),
            (
                # translation_word
                "довольный",
                # pronunciation_word
                "meruʦe",
                # hebrew_word_nikud
                "‫מְרוּצָה‬‬"
            ),
            (
                # translation_word
                "дорогой",
                # pronunciation_word
                "yakar",
                # hebrew_word_nikud
                "‫יָקָר‬‬"
            ),
            (
                # translation_word
                "жидкий",
                # pronunciation_word
                "nozli",
                # hebrew_word_nikud
                "‫נוֹזלִי‬‬"
            ),
            (
                # translation_word
                "жирный (о пище)",
                # pronunciation_word
                "ʃamen",
                # hebrew_word_nikud
                "‫שָמֵן‬‬"
            ),
            (
                # translation_word
                "заботливый",
                # pronunciation_word
                "doʾeg",
                # hebrew_word_nikud
                "‫דָוֹאֵג‬‬"
            ),
            (
                # translation_word
                "загорелый",
                # pronunciation_word
                "ʃazuf",
                # hebrew_word_nikud
                "‫שָזוּף‬‬"
            ),
            (
                # translation_word
                "законный",
                # pronunciation_word
                "χuki",
                # hebrew_word_nikud
                "‫חוּקִי‬‬"
            ),
            (
                # translation_word
                "закрытый",
                # pronunciation_word
                "sagur",
                # hebrew_word_nikud
                "‫סָגוּר‬‬"
            ),
            (
                # translation_word
                "замороженный (продукт)",
                # pronunciation_word
                "kafu",
                # hebrew_word_nikud
                "‫קָפוּא‬‬"
            ),
            (
                # translation_word
                "искусственный",
                # pronunciation_word
                "melaχuti",
                # hebrew_word_nikud
                "‫מְלָאכוּתִי‬‬"
            ),
            (
                # translation_word
                "кислый",
                # pronunciation_word
                "χamuʦ",
                # hebrew_word_nikud
                "‫חָמוּץ‬‬"
            ),
            (
                # translation_word
                "короткий",
                # pronunciation_word
                "kaʦar",
                # hebrew_word_nikud
                "‫קָצַר‬‬"
            ),
            (
                # translation_word
                "красивый",
                # pronunciation_word
                "yafe",
                # hebrew_word_nikud
                "‫יָפֶה‬‬"
            ),
            (
                # translation_word
                "левый",
                # pronunciation_word
                "smali",
                # hebrew_word_nikud
                "‫שׂמָאלִי‬‬"
            ),
            (
                # translation_word
                "правый",
                # pronunciation_word
                "yemani",
                # hebrew_word_nikud
                "‫יְמָנִי‬‬"
            ),
            (
                # translation_word
                "лёгкий (и о грузе и простой)",
                # pronunciation_word
                "kal",
                # hebrew_word_nikud
                "‫קַל‬‬"
            ),
            (
                # translation_word
                "маленький,",
                # pronunciation_word
                "katan",
                # hebrew_word_nikud
                "‫קָטַן‬‬"
            ),
            (
                # translation_word
                "мёртвый",
                # pronunciation_word
                "met",
                # hebrew_word_nikud
                "‫מֵת‬‬"
            ),
            (
                # translation_word
                "милый (любезный)",
                # pronunciation_word
                "neχmad",
                # hebrew_word_nikud
                "‫נֶחמָד‬‬"
            ),
            (
                # translation_word
                "мокрый (промокший)",
                # pronunciation_word
                "ratuv",
                # hebrew_word_nikud
                "‬‫רָטוּב‬"
            ),
            (
                # translation_word
                "молодой",
                # pronunciation_word
                "ʦaʿir",
                # hebrew_word_nikud
                "‬‫צָעִיר‬"
            ),
            (
                # translation_word
                "мягкий",
                # pronunciation_word
                "raχ",
                # hebrew_word_nikud
                "‫רַך‬‬"
            ),
            (
                # translation_word
                "настоящий (момент)",
                # pronunciation_word
                "noχeχi",
                # hebrew_word_nikud
                "‫נוֹכְחִי‬‬"
            ),
            (
                # translation_word
                "невозможный",
                # pronunciation_word
                "'bilti efʃari",
                # hebrew_word_nikud
                "בִּלתִי‬‬‬ ‫אֶפשָרִי‬"
            ),
            (
                # translation_word
                "нежный (о человеке)",
                # pronunciation_word
                "raχ",
                # hebrew_word_nikud
                "‫רַך‬‬"
            ),
            (
                # translation_word
                "необходимый",
                # pronunciation_word
                "naχuʦ",
                # hebrew_word_nikud
                "‫נָחוּץ‬‬"
            ),
            (
                # translation_word
                "непонятный (~ текст)",
                # pronunciation_word
                "'bilti muvan",
                # hebrew_word_nikud
                "בִּלתִי‬‬‬ ‫מוּבָן‬‬"
            ),
            (
                # translation_word
                "нервный",
                # pronunciation_word
                "aʦbani",
                # hebrew_word_nikud
                "‫עַצבָּנִי‬‬"
            ),
            (
                # translation_word
                "новый",
                # pronunciation_word
                "χadaʃ",
                # hebrew_word_nikud
                "‫חָדָש‬‬"
            ),
            (
                # translation_word
                "нормальный",
                # pronunciation_word
                "nor'mali",
                # hebrew_word_nikud
                "‫נוֹרמָלִי‬‬"
            ),
            (
                # translation_word
                "нужный",
                # pronunciation_word
                "daruʃ",
                # hebrew_word_nikud
                "‫דָרוּש‬‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "168. Прилагательные 2",
        # words
        [
            (
                # translation_word
                "общественный",
                # pronunciation_word
                "ʦiburi",
                # hebrew_word_nikud
                "‫צִיבּוּרִי‬‬"
            ),
            (
                # translation_word
                "обыкновенный",
                # pronunciation_word
                "ragil",
                # hebrew_word_nikud
                "‫רָגִיל‬‬"
            ),
            (
                # translation_word
                "обязательный",
                # pronunciation_word
                "heχreχi",
                # hebrew_word_nikud
                "‫הֶכרֵחִי‬‬"
            ),
            (
                # translation_word
                "ограниченный",
                # pronunciation_word
                "mugbal",
                # hebrew_word_nikud
                "‫מוּגבָּל‬‬"
            ),
            (
                # translation_word
                "огромный",
                # pronunciation_word
                "anaki",
                # hebrew_word_nikud
                "‫עֲנָקִי‬‬"
            ),
            (
                # translation_word
                "одинаковый",
                # pronunciation_word
                "zehe",
                # hebrew_word_nikud
                "‫זֵהֶה‬‬"
            ),
            (
                # translation_word
                "опасный",
                # pronunciation_word
                "mesukan",
                # hebrew_word_nikud
                "‫מְסוּכָּן‬‬"
            ),
            (
                # translation_word
                "оригинальный",
                # pronunciation_word
                "mekori",
                # hebrew_word_nikud
                "‬‫מְקוֹרִי‬"
            ),
            (
                # translation_word
                "основной",
                # pronunciation_word
                "ikari",
                # hebrew_word_nikud
                "‫עִיקָרִי‬‬"
            ),
            (
                # translation_word
                "острый (нож и т.п.)",
                # pronunciation_word
                "χad",
                # hebrew_word_nikud
                "‫חַד‬‬"
            ),
            (
                # translation_word
                "открытый",
                # pronunciation_word
                "pa'tuaχ",
                # hebrew_word_nikud
                "‬ּפָּתו‬‫ח‬"
            ),
            (
                # translation_word
                "отличный (хороший)",
                # pronunciation_word
                "meʦuyan",
                # hebrew_word_nikud
                "‫מְצוּיָן‬‬"
            ),
            (
                # translation_word
                "отрицательный",
                # pronunciation_word
                "ʃlili",
                # hebrew_word_nikud
                "‫שלִילִי‬‬"
            ),
            (
                # translation_word
                "персональный",
                # pronunciation_word
                "prati",
                # hebrew_word_nikud
                "‫פּרָטִי‬‬"
            ),
            (
                # translation_word
                "плоский",
                # pronunciation_word
                "ʃa'tuaχ",
                # hebrew_word_nikud
                "‫שָטוּח‬‬"
            ),
            (
                # translation_word
                "плохой",
                # pronunciation_word
                "ra",
                # hebrew_word_nikud
                "‫רַע‬‬"
            ),
            (
                # translation_word
                "полный (наполненный)",
                # pronunciation_word
                "male",
                # hebrew_word_nikud
                "‫מָלֵא‬‬"
            ),
            (
                # translation_word
                "понятный (ясный)",
                # pronunciation_word
                "barur",
                # hebrew_word_nikud
                "‫בָּרוּר‬‬"
            ),
            (
                # translation_word
                "последний",
                # pronunciation_word
                "aχaron",
                # hebrew_word_nikud
                "‫אַחֲרוֹן‬‬"
            ),
            (
                # translation_word
                "постоянный (работа, адрес)",
                # pronunciation_word
                "ka'vuʿa",
                # hebrew_word_nikud
                "‫קָבוּע‬‬"
            ),
            (
                # translation_word
                "похожий",
                # pronunciation_word
                "dome",
                # hebrew_word_nikud
                "‬‫דוֹמֶה‬"
            ),
            (
                # translation_word
                "правильный (верный)",
                # pronunciation_word
                "naχon",
                # hebrew_word_nikud
                "‬‫נָכוֹן‬"
            ),
            (
                # translation_word
                "превосходный",
                # pronunciation_word
                "meʦuyan",
                # hebrew_word_nikud
                "‫מְצוּיָן‬‬"
            ),
            (
                # translation_word
                "приятный (голос)",
                # pronunciation_word
                "naʿim",
                # hebrew_word_nikud
                "‫נָעִים‬‬"
            ),
            (
                # translation_word
                "продолжительный",
                # pronunciation_word
                "memuʃaχ",
                # hebrew_word_nikud
                "‫מְמוּשָך‬‬"
            ),
            (
                # translation_word
                "прозрачный",
                # pronunciation_word
                "ʃakuf",
                # hebrew_word_nikud
                "‫שָקוּף‬‬"
            ),
            (
                # translation_word
                "простой",
                # pronunciation_word
                "paʃut",
                # hebrew_word_nikud
                "‫פָּשוּט‬‬"
            ),
            (
                # translation_word
                "просторный",
                # pronunciation_word
                "meruvaχ",
                # hebrew_word_nikud
                "‫מְרוּוָח‬‬"
            ),
            (
                # translation_word
                "противоположный",
                # pronunciation_word
                "negdi",
                # hebrew_word_nikud
                "‫נֶגדִי‬‬"
            ),
            (
                # translation_word
                "прохладный",
                # pronunciation_word
                "karir",
                # hebrew_word_nikud
                "‫קָרִיר‬‬"
            ),
            (
                # translation_word
                "прочный",
                # pronunciation_word
                "muʦak",
                # hebrew_word_nikud
                "‫מוּצָק‬‬"
            ),
            (
                # translation_word
                "прошлый",
                # pronunciation_word
                "ʃeʿavar",
                # hebrew_word_nikud
                "‫שֶעָבַר‬‬"
            ),
            (
                # translation_word
                "прямой",
                # pronunciation_word
                "yaʃar",
                # hebrew_word_nikud
                "‫יָשָר‬‬"
            ),
            (
                # translation_word
                "пунктуальный",
                # pronunciation_word
                "daikan",
                # hebrew_word_nikud
                "‫דַיקָן‬‬"
            ),
            (
                # translation_word
                "пустой (~ бокал)",
                # pronunciation_word
                "rek",
                # hebrew_word_nikud
                "‫רֵיק‬‬"
            ),
            (
                # translation_word
                "разный",
                # pronunciation_word
                "ʃone",
                # hebrew_word_nikud
                "‫שוֹנֶה‬‬"
            ),
            (
                # translation_word
                "редкий",
                # pronunciation_word
                "nadir",
                # hebrew_word_nikud
                "‫נָדִיר‬‬"
            ),
            (
                # translation_word
                "рискованный",
                # pronunciation_word
                "mesukan",
                # hebrew_word_nikud
                "‫מְסוּכָּן‬‬"
            ),
            (
                # translation_word
                "ровный (о поверхности)",
                # pronunciation_word
                "χalak",
                # hebrew_word_nikud
                "‫חָלָק‬‬"
            ),
            (
                # translation_word
                "свежий",
                # pronunciation_word
                "tari",
                # hebrew_word_nikud
                "‫טָרִי‬‬"
            ),
            (
                # translation_word
                "светлый (о цвете)",
                # pronunciation_word
                "bahir",
                # hebrew_word_nikud
                "‫בָּהִיר‬‬"
            ),
            (
                # translation_word
                "свободный",
                # pronunciation_word
                "χofʃi",
                # hebrew_word_nikud
                "‫חוֹפשִי‬‬"
            ),
            (
                # translation_word
                "сладкий",
                # pronunciation_word
                "matok",
                # hebrew_word_nikud
                "‫מָתוֹק‬‬"
            ),
            (
                # translation_word
                "следующий",
                # pronunciation_word
                "haba",
                # hebrew_word_nikud
                "‬‫הַבָּא‬"
            ),
            (
                # translation_word
                "слепой",
                # pronunciation_word
                "iver",
                # hebrew_word_nikud
                "‬‫עִיווֵר‬"
            ),
            (
                # translation_word
                "сложный (вопрос и т.п.)",
                # pronunciation_word
                "mesubaχ",
                # hebrew_word_nikud
                "‫מְסוּבָּך‬‬"
            ),
            (
                # translation_word
                "смуглый",
                # pronunciation_word
                "ʃaχum",
                # hebrew_word_nikud
                "‬‫שָחוּם‬"
            ),
            (
                # translation_word
                "совместимый",
                # pronunciation_word
                "toʾem",
                # hebrew_word_nikud
                "‬‫תוֹאֵם‬"
            ),
            (
                # translation_word
                "солёный",
                # pronunciation_word
                "ma'luaχ",
                # hebrew_word_nikud
                "‫מָלוּח‬"
            ),
            (
                # translation_word
                "солнечный",
                # pronunciation_word
                "ʃimʃi",
                # hebrew_word_nikud
                "‫שִמשִי‬‬"
            ),
            (
                # translation_word
                "соседний",
                # pronunciation_word
                "samuχ",
                # hebrew_word_nikud
                "‫סָמוּך‬‬"
            ),
            (
                # translation_word
                "специальный",
                # pronunciation_word
                "meyuχad",
                # hebrew_word_nikud
                "‫מְיוּחָד‬‬"
            ),
            (
                # translation_word
                "спокойный",
                # pronunciation_word
                "ʃaket",
                # hebrew_word_nikud
                "‫שָקֵט‬‬"
            ),
            (
                # translation_word
                "старый",
                # pronunciation_word
                "yaʃan",
                # hebrew_word_nikud
                "‫יָשָן‬‬"
            ),
            (
                # translation_word
                "сухой",
                # pronunciation_word
                "yaveʃ",
                # hebrew_word_nikud
                "‫יָבֵש‬‬"
            ),
            (
                # translation_word
                "счастливый",
                # pronunciation_word
                "meʾuʃar",
                # hebrew_word_nikud
                "‫מְאוּשָר‬‬"
            ),
            (
                # translation_word
                "твёрдый",
                # pronunciation_word
                "kaʃe",
                # hebrew_word_nikud
                "‫קָשֶה‬‬"
            ),
            (
                # translation_word
                "тёмный(о комнате)",
                # pronunciation_word
                "χaʃuχ",
                # hebrew_word_nikud
                "‫חָשוּך‬‬"
            ),
            (
                # translation_word
                "тёплый",
                # pronunciation_word
                "χamim",
                # hebrew_word_nikud
                "‫חָמִים‬‬"
            ),
            (
                # translation_word
                "тихий",
                # pronunciation_word
                "ʃaket",
                # hebrew_word_nikud
                "‫שָקֵט‬‬"
            ),
            (
                # translation_word
                "толстый",
                # pronunciation_word
                "ave",
                # hebrew_word_nikud
                "‫עָבֶה‬‬"
            ),
            (
                # translation_word
                "точный",
                # pronunciation_word
                "meduyak",
                # hebrew_word_nikud
                "‫מְדוּיָק‬‬"
            ),
            (
                # translation_word
                "тощий",
                # pronunciation_word
                "raze",
                # hebrew_word_nikud
                "‫רָזֶה‬‬"
            ),
            (
                # translation_word
                "трудный",
                # pronunciation_word
                "kaʃe",
                # hebrew_word_nikud
                "‫קָשֶה‬‬"
            ),
            (
                # translation_word
                "тяжёлый (напр. груз)",
                # pronunciation_word
                "kaved",
                # hebrew_word_nikud
                "‫כָּבֵד‬‬"
            ),
            (
                # translation_word
                "удовлетворённый",
                # pronunciation_word
                "mesupak",
                # hebrew_word_nikud
                "‫מְסוּפָּק‬‬"
            ),
            (
                # translation_word
                "узкий",
                # pronunciation_word
                "ʦar",
                # hebrew_word_nikud
                "‬‫צַר‬"
            ),
            (
                # translation_word
                "умный",
                # pronunciation_word
                "pi'keaχ",
                # hebrew_word_nikud
                "‬‫פִּיקֵח‬"
            ),
            (
                # translation_word
                "уникальный",
                # pronunciation_word
                "meyuχad bemino",
                # hebrew_word_nikud
                "‬מְיוּחָד‬ ‬‬‫בְּמִינו‬"
            ),
            (
                # translation_word
                "усталый",
                # pronunciation_word
                "ayef",
                # hebrew_word_nikud
                "‫עָייֵף‬‬"
            ),
            (
                # translation_word
                "холодный",
                # pronunciation_word
                "kar",
                # hebrew_word_nikud
                "‫קַר‬‬"
            ),
            (
                # translation_word
                "хрупкий",
                # pronunciation_word
                "ʃavir",
                # hebrew_word_nikud
                "‫שָבִיר‬‬"
            ),
            (
                # translation_word
                "центральный",
                # pronunciation_word
                "merkazi",
                # hebrew_word_nikud
                "‬‫מֶרכָּזִי‬"
            ),
            (
                # translation_word
                "частный (личный)",
                # pronunciation_word
                "iʃi",
                # hebrew_word_nikud
                "‬‫אִישִי‬"
            ),
            (
                # translation_word
                "чистый",
                # pronunciation_word
                "naki",
                # hebrew_word_nikud
                "‫נָקִי‬‬"
            ),
            (
                # translation_word
                "чрезмерный",
                # pronunciation_word
                "meyutar",
                # hebrew_word_nikud
                "‬‫מְיוּתָר‬"
            ),
            (
                # translation_word
                "широкий",
                # pronunciation_word
                "raχav",
                # hebrew_word_nikud
                "‫רָחָב‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "169. Глаголы 1",
        # words
        [
            (
                # translation_word
                "бежать",
                # pronunciation_word
                "laruʦ",
                # hebrew_word_nikud
                "‫לָרוּץ‬‬"
            ),
            (
                # translation_word
                "беспокоить (волновать)",
                # pronunciation_word
                "lehadʾig",
                # hebrew_word_nikud
                "‬‫לְהַדאִיג‬"
            ),
            (
                # translation_word
                "беспокоить (мешать)",
                # pronunciation_word
                "lehatrid",
                # hebrew_word_nikud
                "‫לְהַטרִיד‬‬"
            ),
            (
                # translation_word
                "беспокоиться",
                # pronunciation_word
                "lidʾog",
                # hebrew_word_nikud
                "‬‫לִדאוֹג‬"
            ),
            (
                # translation_word
                "бить (ударять)",
                # pronunciation_word
                "lehakot",
                # hebrew_word_nikud
                "‫לְהַכּוֹת‬‬"
            ),
            (
                # translation_word
                "благодарить",
                # pronunciation_word
                "lehodot",
                # hebrew_word_nikud
                "‬‫לְהוֹדוֹת‬"
            ),
            (
                # translation_word
                "бояться (чего-л.)",
                # pronunciation_word
                "lefaχed",
                # hebrew_word_nikud
                "‫לְפַחֵד‬‬"
            ),
            (
                # translation_word
                "брать",
                # pronunciation_word
                "la'kaχat",
                # hebrew_word_nikud
                "‫לָקַחַת‬‬"
            ),
            (
                # translation_word
                "бриться",
                # pronunciation_word
                "lehitga'leaχ",
                # hebrew_word_nikud
                "‫לְהִתגַלֵח‬‬"
            ),
            (
                # translation_word
                "бросать (напр. камень)",
                # pronunciation_word
                "lizrok",
                # hebrew_word_nikud
                "‫לִזרוֹק‬‬"
            ),
            (
                # translation_word
                "бросать (покидать)",
                # pronunciation_word
                "laʿazov",
                # hebrew_word_nikud
                "‬‫לַעֲזוֹב‬"
            ),
            (
                # translation_word
                "будить",
                # pronunciation_word
                "lehaʿir",
                # hebrew_word_nikud
                "‬‫לְהָעִיר‬"
            ),
            (
                # translation_word
                "быть",
                # pronunciation_word
                "lihyot",
                # hebrew_word_nikud
                "‫לִהיוֹת‬‬"
            ),
            (
                # translation_word
                "быть должным",
                # pronunciation_word
                "lihyot χayav",
                # hebrew_word_nikud
                "לִהיוֹת‬‬ ‫חַייָב‬‬"
            ),
            (
                # translation_word
                "быть похожим",
                # pronunciation_word
                "lihyot dome",
                # hebrew_word_nikud
                "‬לִהיוֹת‬‬ ‫דוֹמֶה‬"
            ),
            (
                # translation_word
                "верить (думать)",
                # pronunciation_word
                "lehaʾamin",
                # hebrew_word_nikud
                "‫לְהַאֲמִין‬‬"
            ),
            (
                # translation_word
                "веселиться",
                # pronunciation_word
                "lehanot",
                # hebrew_word_nikud
                "‫לֵיהָנוֹת‬‬"
            ),
            (
                # translation_word
                "весить (иметь вес)",
                # pronunciation_word
                "liʃkol",
                # hebrew_word_nikud
                "‫לִשקוֹל‬‬"
            ),
            (
                # translation_word
                "вести машину",
                # pronunciation_word
                "linhog",
                # hebrew_word_nikud
                "‬‫לִנהוֹג‬"
            ),
            (
                # translation_word
                "вести переговоры",
                # pronunciation_word
                "laset velatet",
                # hebrew_word_nikud
                "לָשֵׂאת‬‬ ‫וְלָתֵת‬‬"
            ),
            (
                # translation_word
                "вешать",
                # pronunciation_word
                "litlot",
                # hebrew_word_nikud
                "‫לִתלוֹת‬‬"
            ),
            (
                # translation_word
                "вздохнуть",
                # pronunciation_word
                "leheʾanaχ",
                # hebrew_word_nikud
                "‫לְהֵיאָנַח‬‬"
            ),
            (
                # translation_word
                "видеть сны",
                # pronunciation_word
                "laχalom",
                # hebrew_word_nikud
                "‫לַחֲלוֹם‬"
            ),
            (
                # translation_word
                "включать (напр. радио)",
                # pronunciation_word
                "lehadlik",
                # hebrew_word_nikud
                "‫לְהַדלִיק‬‬"
            ),
            (
                # translation_word
                "владеть",
                # pronunciation_word
                "lihyot 'baʿal ʃel",
                # hebrew_word_nikud
                "לִהיוֹת‬‬ ‫בַּעַל‬ ‫שֶל‬‬"
            ),
            (
                # translation_word
                "влиять",
                # pronunciation_word
                "lehaʃ'piʿa",
                # hebrew_word_nikud
                "‫לְהַשפִּיע‬‬"
            ),
            (
                # translation_word
                "влюбиться (в ...)",
                # pronunciation_word
                "lehitʾahev",
                # hebrew_word_nikud
                "‫לְהִתאַהֵב‬‬"
            ),
            (
                # translation_word
                "вмешиваться",
                # pronunciation_word
                "lehitʿarev",
                # hebrew_word_nikud
                "‫לְהִתעָרֵב‬‬"
            ),
            (
                # translation_word
                "возвращаться",
                # pronunciation_word
                "laʃuv",
                # hebrew_word_nikud
                "‫לָשוּב‬‬"
            ),
            (
                # translation_word
                "возмущаться",
                # pronunciation_word
                "lehitraʿem",
                # hebrew_word_nikud
                "‫לְהִתרַעֵם‬‬"
            ),
            (
                # translation_word
                "возражать",
                # pronunciation_word
                "lehitnaged",
                # hebrew_word_nikud
                "‬‫לְהִתנַגֵד‬"
            ),
            (
                # translation_word
                "войти (в комнату и т.п.)",
                # pronunciation_word
                "lehikanes",
                # hebrew_word_nikud
                "‫לְהִיכָּנֵס‬‬"
            ),
            (
                # translation_word
                "волноваться",
                # pronunciation_word
                "lidʾog",
                # hebrew_word_nikud
                "‫לִדאוֹג‬‬"
            ),
            (
                # translation_word
                "восхищаться",
                # pronunciation_word
                "lehitpaʿel",
                # hebrew_word_nikud
                "‫לְהִתפַּעֵל‬‬"
            ),
            (
                # translation_word
                "врать",
                # pronunciation_word
                "leʃaker",
                # hebrew_word_nikud
                "‫לְשַקֵר‬‬"
            ),
            (
                # translation_word
                "вспоминать",
                # pronunciation_word
                "lehizaχer",
                # hebrew_word_nikud
                "‫לְהִיזָכֵר‬‬"
            ),
            (
                # translation_word
                "выбирать",
                # pronunciation_word
                "livχor",
                # hebrew_word_nikud
                "‫לִבחוֹר‬‬"
            ),
            (
                # translation_word
                "выздоравливать",
                # pronunciation_word
                "lehaχlim",
                # hebrew_word_nikud
                "‫לְהַחלִים‬‬"
            ),
            (
                # translation_word
                "выйти (из дома и т.п.)",
                # pronunciation_word
                "laʦet",
                # hebrew_word_nikud
                "‫לָצֵאת‬‬"
            ),
            (
                # translation_word
                "гарантировать",
                # pronunciation_word
                "lehav'tiaχ",
                # hebrew_word_nikud
                "‫לְהַבטִיח‬‬"
            ),
            (
                # translation_word
                "говорить с ...",
                # pronunciation_word
                "ledaber",
                # hebrew_word_nikud
                "‫לְדַבֵּר‬‬"
            ),
            (
                # translation_word
                "голосовать",
                # pronunciation_word
                "lehaʦ'biʿa",
                # hebrew_word_nikud
                "‫לְהַצבִּיע‬‬"
            ),
            (
                # translation_word
                "готовить (обед)",
                # pronunciation_word
                "levaʃel",
                # hebrew_word_nikud
                "‫לְבַשֵל‬‬"
            ),
            (
                # translation_word
                "давать",
                # pronunciation_word
                "latet",
                # hebrew_word_nikud
                "‫לָתֵת‬‬"
            ),
            (
                # translation_word
                "делать",
                # pronunciation_word
                "laʿasot",
                # hebrew_word_nikud
                "‫לַעֲשׂוֹת‬‬"
            ),
            (
                # translation_word
                "делать прививки",
                # pronunciation_word
                "leχasen",
                # hebrew_word_nikud
                "‫לְחַסֵן‬‬"
            ),
            (
                # translation_word
                "добавлять",
                # pronunciation_word
                "lehosif",
                # hebrew_word_nikud
                "‫לְהוֹסִיף‬‬"
            ),
            (
                # translation_word
                "доверять",
                # pronunciation_word
                "liv'toaχ",
                # hebrew_word_nikud
                "‬‫לִבטוֹח‬"
            ),
            (
                # translation_word
                "доказывать",
                # pronunciation_word
                "leho'χiaχ",
                # hebrew_word_nikud
                "‫לְהוֹכִיח‬‬"
            ),
            (
                # translation_word
                "достигать (напр. ~ полюса)",
                # pronunciation_word
                "lehasig",
                # hebrew_word_nikud
                "‫לְהַשִׂיג‬‬"
            ),
            (
                # translation_word
                "достигать (результата)",
                # pronunciation_word
                "lehasig",
                # hebrew_word_nikud
                "‬‫לְהַשִׂיג‬"
            ),
            (
                # translation_word
                "драться (в драке)",
                # pronunciation_word
                "lehitkotet",
                # hebrew_word_nikud
                "‬‫לְהִתקוֹטֵט‬"
            ),
            (
                # translation_word
                "дрожать",
                # pronunciation_word
                "lirʿod",
                # hebrew_word_nikud
                "‫לִרעוֹד‬‬"
            ),
            (
                # translation_word
                "думать",
                # pronunciation_word
                "laχʃov",
                # hebrew_word_nikud
                "‬‫לַחשוֹב‬"
            ),
            (
                # translation_word
                "дышать",
                # pronunciation_word
                "linʃom",
                # hebrew_word_nikud
                "‫לִנשוֹם‬‬"
            ),
            (
                # translation_word
                "ехать",
                # pronunciation_word
                "lin'soʿa",
                # hebrew_word_nikud
                "‬‫לִנסוֹע‬"
            ),
        ]
    ),  
    (
        # group_name_ru
        "170. Глаголы 2",
        # words
        [
            (
                # translation_word
                "жаловаться",
                # pronunciation_word
                "lehitlonen",
                # hebrew_word_nikud
                "‬‫לְהִתלוֹנֵן‬"
            ),
            (
                # translation_word
                "ждать",
                # pronunciation_word
                "lehamtin",
                # hebrew_word_nikud
                "‫לְהַמתִין‬‬"
            ),
            (
                # translation_word
                "жениться",
                # pronunciation_word
                "lehitχaten",
                # hebrew_word_nikud
                "‫לְהִתחַתֵן‬‬"
            ),
            (
                # translation_word
                "жечь, сжигать",
                # pronunciation_word
                "lisrof",
                # hebrew_word_nikud
                "‬‫לִשׂרוֹף‬"
            ),
            (
                # translation_word
                "жить (проживать)",
                # pronunciation_word
                "lagur",
                # hebrew_word_nikud
                "‬‫לָגוּר‬"
            ),
            (
                # translation_word
                "жить (существовать)",
                # pronunciation_word
                "liχyot",
                # hebrew_word_nikud
                "‫לִחיוֹת‬‬"
            ),
            (
                # translation_word
                "забыть",
                # pronunciation_word
                "liʃ'koaχ",
                # hebrew_word_nikud
                "‫לִשכּוֹח‬‬"
            ),
            (
                # translation_word
                "завидовать",
                # pronunciation_word
                "lekane",
                # hebrew_word_nikud
                "‫לְקַנֵא‬‬"
            ),
            (
                # translation_word
                "зависеть (от ...)",
                # pronunciation_word
                "lihyot talui be...",
                # hebrew_word_nikud
                "לִהיוֹת‬‬ ‫תָלוּי‬ ‫ב‬‬"
            ),
            (
                # translation_word
                "завтракать",
                # pronunciation_word
                "leʾeχol aruχat 'boker",
                # hebrew_word_nikud
                "‬לֶאֱכוֹל‬‬ ‫אֲרוּחַת‬ ‫בּוֹקֶר‬"
            ),
            (
                # translation_word
                "заказывать (в ресторане)",
                # pronunciation_word
                "lehazmin",
                # hebrew_word_nikud
                "‬‫לְהַזמִין‬"
            ),
            (
                # translation_word
                "заканчивать",
                # pronunciation_word
                "lesayem",
                # hebrew_word_nikud
                "‫לְסַייֵם‬‬"
            ),
            (
                # translation_word
                "закрывать",
                # pronunciation_word
                "lisgor",
                # hebrew_word_nikud
                "‫לִסגוֹר‬‬"
            ),
            (
                # translation_word
                "замечать (увидеть)",
                # pronunciation_word
                "lasim lev",
                # hebrew_word_nikud
                "לָשִׂים‬‬ ‫לֵב‬‬"
            ),
            (
                # translation_word
                "замолчать",
                # pronunciation_word
                "lehiʃtatek",
                # hebrew_word_nikud
                "‫לְהִשתַתֵק‬‬"
            ),
            (
                # translation_word
                "занимать (деньги)",
                # pronunciation_word
                "lilvot",
                # hebrew_word_nikud
                "‫לִלווֹת‬‬"
            ),
            (
                # translation_word
                "записывать",
                # pronunciation_word
                "lirʃom",
                # hebrew_word_nikud
                "‬‫לִרשוֹם‬"
            ),
            (
                # translation_word
                "запомнить",
                # pronunciation_word
                "lizkor",
                # hebrew_word_nikud
                "‫לִזכּוֹר‬‬"
            ),
            (
                # translation_word
                "запрещать",
                # pronunciation_word
                "leʾesor",
                # hebrew_word_nikud
                "‫לֶאֱסוֹר‬‬"
            ),
            (
                # translation_word
                "заразиться чем-л.",
                # pronunciation_word
                "lehibadek",
                # hebrew_word_nikud
                "‫לְהִידָבֵק‬‬"
            ),
            (
                # translation_word
                "защищаться",
                # pronunciation_word
                "lehitgonen",
                # hebrew_word_nikud
                "‫לְהִתגוֹנֵן‬‬"
            ),
            (
                # translation_word
                "звать (на помощь и т.п.)",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "знакомить (кого-л. с кем-л.)",
                # pronunciation_word
                "lehaʦig",
                # hebrew_word_nikud
                "‬‫לְהַצִיג‬"
            ),
            (
                # translation_word
                "знакомиться (с кем-л.)",
                # pronunciation_word
                "lehakir",
                # hebrew_word_nikud
                "‫לְהַכִּיר‬‬"
            ),
            (
                # translation_word
                "знать (кого-л.)",
                # pronunciation_word
                "lehakir et",
                # hebrew_word_nikud
                "‬לְהַכִּיר‬‬ ‫אֶת‬"
            ),
            (
                # translation_word
                "знать (что-л.)",
                # pronunciation_word
                "la'daʿat",
                # hebrew_word_nikud
                "‬‫לָדַעַת‬"
            ),
            (
                # translation_word
                "значить",
                # pronunciation_word
                "lomar",
                # hebrew_word_nikud
                "‫לוֹמַר‬‬"
            ),
            (
                # translation_word
                "играть (в игру)",
                # pronunciation_word
                "lesaχek",
                # hebrew_word_nikud
                "‬‫לְשַׂחֵק‬"
            ),
            (
                # translation_word
                "идти",
                # pronunciation_word
                "la'leχet",
                # hebrew_word_nikud
                "‫לָלֶכֶת‬‬"
            ),
            (
                # translation_word
                "избегать",
                # pronunciation_word
                "lehimana",
                # hebrew_word_nikud
                "‫לְהִימָנַע‬‬"
            ),
            (
                # translation_word
                "извиняться",
                # pronunciation_word
                "lehitnaʦel",
                # hebrew_word_nikud
                "‬‫לְהִתנַצֵל‬"
            ),
            (
                # translation_word
                "изменить (поменять)",
                # pronunciation_word
                "leʃanot",
                # hebrew_word_nikud
                "‬‫לְשַנוֹת‬"
            ),
            (
                # translation_word
                "изучать",
                # pronunciation_word
                "lilmod",
                # hebrew_word_nikud
                "‬‫לִלמוֹד‬"
            ),
            (
                # translation_word
                "иметь",
                # pronunciation_word
                "lehaχzik",
                # hebrew_word_nikud
                "‫לְהַחזִיק‬‬"
            ),
            (
                # translation_word
                "имитировать",
                # pronunciation_word
                "leχakot",
                # hebrew_word_nikud
                "‫לְחַקוֹת‬‬"
            ),
            (
                # translation_word
                "импортировать",
                # pronunciation_word
                "leyabe",
                # hebrew_word_nikud
                "‫לְייַבֵּא‬‬"
            ),
            (
                # translation_word
                "интересоваться",
                # pronunciation_word
                "lehitʿanyen",
                # hebrew_word_nikud
                "‬‫לְהִתעַנייֵן‬"
            ),
            (
                # translation_word
                "информировать",
                # pronunciation_word
                "leho'dia",
                # hebrew_word_nikud
                "‫לְהוֹדִיע‬‬"
            ),
            (
                # translation_word
                "искать",
                # pronunciation_word
                "leχapes",
                # hebrew_word_nikud
                "‫לְחַפֵּש‬‬"
            ),
            (
                # translation_word
                "испачкаться",
                # pronunciation_word
                "lehitlaχleχ",
                # hebrew_word_nikud
                "‬‫לְהִתלַכלֵך‬"
            ),
            (
                # translation_word
                "исчезнуть",
                # pronunciation_word
                "leheʿalem",
                # hebrew_word_nikud
                "‫לְהֵיעָלֵם‬‬"
            ),
            (
                # translation_word
                "класть, положить",
                # pronunciation_word
                "lasim",
                # hebrew_word_nikud
                "‬‫לָשִׂים‬"
            ),
            (
                # translation_word
                "компенсировать",
                # pronunciation_word
                "lefaʦot",
                # hebrew_word_nikud
                "‫לְפַצוֹת‬‬"
            ),
            (
                # translation_word
                "компрометировать",
                # pronunciation_word
                "lehavʾiʃ et reχo",
                # hebrew_word_nikud
                "לְהַבאִיש‬ ‫אֶת‬ ‬‫רֵיחו‬‬"
            ),
            (
                # translation_word
                "конкурировать",
                # pronunciation_word
                "lehitχarot",
                # hebrew_word_nikud
                "‫לְהִתחָרוֹת‬‬"
            ),
            (
                # translation_word
                "консультироваться с ...",
                # pronunciation_word
                "lehityaʿeʦ im",
                # hebrew_word_nikud
                "לְהִתייַעֵץ‬ ‬‫עִם‬‬"
            ),
            (
                # translation_word
                "контролировать",
                # pronunciation_word
                "liʃlot",
                # hebrew_word_nikud
                "‬‫לִשלוֹט‬"
            ),
            (
                # translation_word
                "концентрироваться",
                # pronunciation_word
                "lehitrakez",
                # hebrew_word_nikud
                "‫לְהִתרַכֵּז‬‬"
            ),
            (
                # translation_word
                "кормить",
                # pronunciation_word
                "lehaʾaχil",
                # hebrew_word_nikud
                "‫לְהַאֲכִיל‬‬"
            ),
            (
                # translation_word
                "красть",
                # pronunciation_word
                "lignov",
                # hebrew_word_nikud
                "‫לִגנוֹב‬‬"
            ),
            (
                # translation_word
                "кричать",
                # pronunciation_word
                "liʦʿok",
                # hebrew_word_nikud
                "‫לִצעוֹק‬‬"
            ),
            (
                # translation_word
                "купать",
                # pronunciation_word
                "lirχoʦ",
                # hebrew_word_nikud
                "‫לִרחוֹץ‬‬"
            ),
            (
                # translation_word
                "купаться (в море и т.п.)",
                # pronunciation_word
                "lehitraχeʦ",
                # hebrew_word_nikud
                "‫לְהִתרַחֵץ‬‬"
            ),
            (
                # translation_word
                "кушать, есть",
                # pronunciation_word
                "leʾeχol",
                # hebrew_word_nikud
                "‫לֶאֱכוֹל‬‬"
            ),
            (
                # translation_word
                "лежать (о предмете)",
                # pronunciation_word
                "lihyot munaχ",
                # hebrew_word_nikud
                "לִהיוֹת‬‬ ‫מוּנָח‬‬"
            ),
            (
                # translation_word
                "лежать (о человеке)",
                # pronunciation_word
                "liʃkav",
                # hebrew_word_nikud
                "‫לִשכַּב‬‬"
            ),
            (
                # translation_word
                "летать",
                # pronunciation_word
                "laʿuf",
                # hebrew_word_nikud
                "‫לָעוּף‬‬"
            ),
            (
                # translation_word
                "лечить (болезнь)",
                # pronunciation_word
                "letapel be...",
                # hebrew_word_nikud
                "לְטַפֵּל‬ ‬ְּ‫ב‬‬"
            ),
            (
                # translation_word
                "ловить",
                # pronunciation_word
                "litfos",
                # hebrew_word_nikud
                "‫לִתפוֹס‬‬"
            ),
            (
                # translation_word
                "ложиться спать",
                # pronunciation_word
                "liʃkav liʃon",
                # hebrew_word_nikud
                "לִשכַּב‬ ‬‫לִישוֹן‬‬"
            ),
            (
                # translation_word
                "ломать",
                # pronunciation_word
                "liʃbor",
                # hebrew_word_nikud
                "‫לִשבּוֹר‬‬"
            ),
            (
                # translation_word
                "льстить",
                # pronunciation_word
                "lehaχnif",
                # hebrew_word_nikud
                "‫לְהַחנִיף‬‬"
            ),
            (
                # translation_word
                "любить",
                # pronunciation_word
                "leʾehov",
                # hebrew_word_nikud
                "‫לֶאֱהוֹב‬‬"
            ),
            (
                # translation_word
                "менять",
                # pronunciation_word
                "lehaχlif",
                # hebrew_word_nikud
                "‬‫לְהַחלִיף‬"
            ),
            (
                # translation_word
                "мечтать",
                # pronunciation_word
                "laχalom",
                # hebrew_word_nikud
                "‫לַחֲלוֹם‬‬"
            ),
            (
                # translation_word
                "молчать",
                # pronunciation_word
                "liʃtok",
                # hebrew_word_nikud
                "‫לִשתוֹק‬‬"
            ),
            (
                # translation_word
                "мочь",
                # pronunciation_word
                "yaχol",
                # hebrew_word_nikud
                "‫יָכוֹל‬‬"
            ),
            (
                # translation_word
                "мстить",
                # pronunciation_word
                "linkom",
                # hebrew_word_nikud
                "‬‫לִנקוֹם‬"
            ),
            (
                # translation_word
                "мыть",
                # pronunciation_word
                "liʃtof",
                # hebrew_word_nikud
                "‬‫לִשטוֹף‬"
            ),
            (
                # translation_word
                "мыться",
                # pronunciation_word
                "lehitraχeʦ",
                # hebrew_word_nikud
                "‬‫לְהִתרַחֵץ‬"
            ),
        ]
    ), 
    (
        # group_name_ru
        "171. Глаголы 3",
        # words
        [
            (
                # translation_word
                "наблюдать",
                # pronunciation_word
                "liʦpot,",
                # hebrew_word_nikud
                "‬‫לִצפּוֹת‬"
            ),
            (
                # translation_word
                "нагревать",
                # pronunciation_word
                "leχamem",
                # hebrew_word_nikud
                "‫לְחַמֵם‬‬"
            ),
            (
                # translation_word
                "называть",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "наказывать",
                # pronunciation_word
                "lehaʿaniʃ",
                # hebrew_word_nikud
                "‫לְהַעֲנִיש‬‬"
            ),
            (
                # translation_word
                "намекать",
                # pronunciation_word
                "lirmoz",
                # hebrew_word_nikud
                "‫לִרמוֹז‬‬"
            ),
            (
                # translation_word
                "нанимать (работника)",
                # pronunciation_word
                "lehaʿasik",
                # hebrew_word_nikud
                "‫לְהַעֲסִיק‬‬"
            ),
            (
                # translation_word
                "напоминать",
                # pronunciation_word
                "lehazkir",
                # hebrew_word_nikud
                "‬‫לְהַזכִּיר‬"
            ),
            (
                # translation_word
                "наследовать",
                # pronunciation_word
                "la'reʃet",
                # hebrew_word_nikud
                "‫לָרֶשֶת‬‬"
            ),
            (
                # translation_word
                "насмехаться",
                # pronunciation_word
                "lilʿog",
                # hebrew_word_nikud
                "‫לִלעוֹג‬‬"
            ),
            (
                # translation_word
                "находить",
                # pronunciation_word
                "limʦo",
                # hebrew_word_nikud
                "‬‫לִמצוֹא‬"
            ),
            (
                # translation_word
                "начинать",
                # pronunciation_word
                "lehatχil",
                # hebrew_word_nikud
                "‬‫לְהַתחִיל‬"
            ),
            (
                # translation_word
                "нравиться",
                # pronunciation_word
                "limʦo χen beʿei'nayim",
                # hebrew_word_nikud
                "‬לִמצוֹא‬ ‫חֵן‬ ‬‫בְּעֵינַיִים‬"
            ),
            (
                # translation_word
                "нюхать",
                # pronunciation_word
                "leha'riaχ",
                # hebrew_word_nikud
                "‫לְהָרִיח‬‬"
            ),
            (
                # translation_word
                "обвинять",
                # pronunciation_word
                "lehaʾaʃim",
                # hebrew_word_nikud
                "‫לְהַאֲשִים‬‬"
            ),
            (
                # translation_word
                "обедать",
                # pronunciation_word
                "leʾeχol aruχat ʦaha'rayim",
                # hebrew_word_nikud
                "לֶאֱכוֹל‬ ‫אֲרוּחַת‬ ‬‫צָהֳרַיִים‬‬"
            ),
            (
                # translation_word
                "обещать",
                # pronunciation_word
                "lehav'tiaχ",
                # hebrew_word_nikud
                "‫לְהַבטִיח‬‬"
            ),
            (
                # translation_word
                "обижать",
                # pronunciation_word
                "lif'goʿa",
                # hebrew_word_nikud
                "‬‫לִפגוֹע‬"
            ),
            (
                # translation_word
                "обманывать",
                # pronunciation_word
                "leramot",
                # hebrew_word_nikud
                "‫לְרַמוֹת‬‬"
            ),
            (
                # translation_word
                "обнимать",
                # pronunciation_word
                "leχabek",
                # hebrew_word_nikud
                "‫לְחַבֵּק‬‬"
            ),
            (
                # translation_word
                "обращаться (к кому-л.)",
                # pronunciation_word
                "lifnot el",
                # hebrew_word_nikud
                "לִפנוֹת‬‬ ‫אֶל‬‬"
            ),
            (
                # translation_word
                "обучать",
                # pronunciation_word
                "lelamed",
                # hebrew_word_nikud
                "‫לְלַמֵד‬‬"
            ),
            (
                # translation_word
                "объяснять",
                # pronunciation_word
                "lehasbir",
                # hebrew_word_nikud
                "‬‫לְהַסבִּיר‬"
            ),
            (
                # translation_word
                "ограничивать",
                # pronunciation_word
                "lehagbil",
                # hebrew_word_nikud
                "‬‫לְהַגבִּיל‬"
            ),
            (
                # translation_word
                "ожидать",
                # pronunciation_word
                "leʦapot",
                # hebrew_word_nikud
                "‫לְצַפּוֹת‬‬"
            ),
            (
                # translation_word
                "означать",
                # pronunciation_word
                "lomar",
                # hebrew_word_nikud
                "‫לוֹמַר‬‬"
            ),
            (
                # translation_word
                "оскорблять",
                # pronunciation_word
                "lehaʿaliv",
                # hebrew_word_nikud
                "‫לְהַעֲלִיב‬‬"
            ),
            (
                # translation_word
                "оставлять (забыть)",
                # pronunciation_word
                "lehaʃʾir",
                # hebrew_word_nikud
                "‫לְהַשאִיר‬‬"
            ),
            (
                # translation_word
                "останавливаться",
                # pronunciation_word
                "laʿaʦor",
                # hebrew_word_nikud
                "‬‫לַעֲצוֹר‬"
            ),
            (
                # translation_word
                "отвечать",
                # pronunciation_word
                "laʿanot",
                # hebrew_word_nikud
                "‫לְעַנוֹת‬‬"
            ),
            (
                # translation_word
                "отдыхать",
                # pronunciation_word
                "la'nuaχ",
                # hebrew_word_nikud
                "‬‫לָנוּח‬"
            ),
            (
                # translation_word
                "отказывать",
                # pronunciation_word
                "lesarev",
                # hebrew_word_nikud
                "‫לְסָרֵב‬‬"
            ),
            (
                # translation_word
                "отличаться",
                # pronunciation_word
                "lehibadel",
                # hebrew_word_nikud
                "‫לְהִיבָּדֵל‬‬"
            ),
            (
                # translation_word
                "отменить",
                # pronunciation_word
                "levatel",
                # hebrew_word_nikud
                "‫לְבַטֵל‬‬"
            ),
            (
                # translation_word
                "отрезать",
                # pronunciation_word
                "laχtoχ",
                # hebrew_word_nikud
                "‫לַחתוֹך‬‬"
            ),
            (
                # translation_word
                "отрицать",
                # pronunciation_word
                "liʃlol",
                # hebrew_word_nikud
                "‫לִשלוֹל‬‬"
            ),
            (
                # translation_word
                "охранять",
                # pronunciation_word
                "liʃmor",
                # hebrew_word_nikud
                "‬‫לִשמוֹר‬"
            ),
            (
                # translation_word
                "очаровывать",
                # pronunciation_word
                "lehaksim",
                # hebrew_word_nikud
                "‫לְהַקסִים‬‬"
            ),
            (
                # translation_word
                "очищать",
                # pronunciation_word
                "lenakot",
                # hebrew_word_nikud
                "‬‫לְנַקוֹת‬"
            ),
            (
                # translation_word
                "ошибаться",
                # pronunciation_word
                "litʿot",
                # hebrew_word_nikud
                "‫לִטעוֹת‬‬"
            ),
        ]
    ),
    (
        # group_name_ru
        "172. Глаголы 4",
        # words
        [
            (
                # translation_word
                "пахнуть",
                # pronunciation_word
                "leha'riaχ",
                # hebrew_word_nikud
                "‫לְהָרִיח‬‬"
            ),
            (
                # translation_word
                "переделывать",
                # pronunciation_word
                "laʿasot meχadaʃ",
                # hebrew_word_nikud
                "לַעֲשׂוֹת‬‬ ‫מֵחָדָש‬‬"
            ),
            (
                # translation_word
                "писать",
                # pronunciation_word
                "liχtov",
                # hebrew_word_nikud
                "‬‫לִכתוֹב‬"
            ),
            (
                # translation_word
                "пить",
                # pronunciation_word
                "liʃtot",
                # hebrew_word_nikud
                "‫לִשתוֹת‬‬"
            ),
            (
                # translation_word
                "плавать",
                # pronunciation_word
                "lisχot",
                # hebrew_word_nikud
                "‬‫לִשׂחוֹת‬"
            ),
            (
                # translation_word
                "плакать",
                # pronunciation_word
                "livkot",
                # hebrew_word_nikud
                "‫לִבכּוֹת‬‬"
            ),
            (
                # translation_word
                "планировать",
                # pronunciation_word
                "letaχnen",
                # hebrew_word_nikud
                "‬‫לְתַכנֵן‬"
            ),
            (
                # translation_word
                "платить",
                # pronunciation_word
                "leʃalem",
                # hebrew_word_nikud
                "‫לְשַלֵם‬‬"
            ),
            (
                # translation_word
                "плевать",
                # pronunciation_word
                "lirok",
                # hebrew_word_nikud
                "‫לִירוֹק‬‬"
            ),
            (
                # translation_word
                "поворачивать",
                # pronunciation_word
                "lifnot",
                # hebrew_word_nikud
                "‫לִפנוֹת‬‬"
            ),
            (
                # translation_word
                "повторять",
                # pronunciation_word
                "laχazor al",
                # hebrew_word_nikud
                "לַחֲזוֹר‬‬ ‫עַל‬‬"
            ),
            (
                # translation_word
                "подготовить",
                # pronunciation_word
                "lehaχin",
                # hebrew_word_nikud
                "‬‫לְהָכִין‬"
            ),
            (
                # translation_word
                "подозревать",
                # pronunciation_word
                "laχʃod",
                # hebrew_word_nikud
                "‬‫לַחשוֹד‬"
            ),
            (
                # translation_word
                "подписывать",
                # pronunciation_word
                "laχtom",
                # hebrew_word_nikud
                "‫לַחתוֹם‬‬"
            ),
            (
                # translation_word
                "подслушивать",
                # pronunciation_word
                "lehaʾazin be'seter",
                # hebrew_word_nikud
                "לְהַאֲזִין‬‬ ‫בְּסֵתֶר‬‬"
            ),
            (
                # translation_word
                "подсматривать",
                # pronunciation_word
                "lehaʦiʦ",
                # hebrew_word_nikud
                "‫לְהָצִיץ‬‬"
            ),
            (
                # translation_word
                "подчиняться",
                # pronunciation_word
                "leʦayet",
                # hebrew_word_nikud
                "‫לְצַייֵת‬‬"
            ),
            (
                # translation_word
                "поздравлять",
                # pronunciation_word
                "levareχ",
                # hebrew_word_nikud
                "‫לְבָרֵך‬‬"
            ),
            (
                # translation_word
                "показывать",
                # pronunciation_word
                "leharʾot",
                # hebrew_word_nikud
                "‬‫לְהַראוֹת‬"
            ),
            (
                # translation_word
                "покупать",
                # pronunciation_word
                "liknot",
                # hebrew_word_nikud
                "‬‫לִקנוֹת‬"
            ),
            (
                # translation_word
                "пользоваться (чем-л.)",
                # pronunciation_word
                "lehiʃtameʃ be...",
                # hebrew_word_nikud
                "‬לְהִשתַמֵש‬‬ ְּ‫ב‬"
            ),
            (
                # translation_word
                "помнить",
                # pronunciation_word
                "lizkor",
                # hebrew_word_nikud
                "‫לִזכּוֹר‬‬"
            ),
            (
                # translation_word
                "помогать",
                # pronunciation_word
                "laʿazor",
                # hebrew_word_nikud
                "‫לַעֲזוֹר‬‬"
            ),
            (
                # translation_word
                "понимать",
                # pronunciation_word
                "lehavin",
                # hebrew_word_nikud
                "‬‫לְהָבִין‬"
            ),
            (
                # translation_word
                "починить (машину, крышу)",
                # pronunciation_word
                "letaken",
                # hebrew_word_nikud
                "‬‫לְתַקֵן‬"
            ),
            (
                # translation_word
                "предлагать",
                # pronunciation_word
                "leha'ʦiʿa",
                # hebrew_word_nikud
                "‫לְהַצִיע‬‬"
            ),
            (
                # translation_word
                "предполагать",
                # pronunciation_word
                "leʃaʿer",
                # hebrew_word_nikud
                "‫לְשַעֵר‬‬"
            ),
            (
                # translation_word
                "предупреждать",
                # pronunciation_word
                "lehazhir",
                # hebrew_word_nikud
                "‬‫לְהַזהִיר‬"
            ),
            (
                # translation_word
                "презирать",
                # pronunciation_word
                "lezalzel be...",
                # hebrew_word_nikud
                "‬לְזַלזֵל‬‬ ‫ב‬"
            ),
            (
                # translation_word
                "прибывать",
                # pronunciation_word
                "leha'giʿa",
                # hebrew_word_nikud
                "‫לְהַגִיע‬‬"
            ),
            (
                # translation_word
                "приводить в порядок",
                # pronunciation_word
                "lesader",
                # hebrew_word_nikud
                "‫לְסַדֵר‬‬"
            ),
            (
                # translation_word
                "приглашать",
                # pronunciation_word
                "lehazmin",
                # hebrew_word_nikud
                "‫לְהַזמִין‬‬"
            ),
            (
                # translation_word
                "признавать (ошибку)",
                # pronunciation_word
                "lehakir be...",
                # hebrew_word_nikud
                "לְהַכִּיר‬‬ ְּ‫ב‬‬"
            ),
            (
                # translation_word
                "признаваться",
                # pronunciation_word
                "lehodot be...",
                # hebrew_word_nikud
                "‬לְהוֹדוֹת‬‬ ‫ב‬"
            ),
            (
                # translation_word
                "принуждать",
                # pronunciation_word
                "lehaχ'riaχ",
                # hebrew_word_nikud
                "‫לְהַכרִיח‬‬"
            ),
            (
                # translation_word
                "продавать",
                # pronunciation_word
                "limkor",
                # hebrew_word_nikud
                "‫לִמכּוֹר‬‬"
            ),
            (
                # translation_word
                "просить",
                # pronunciation_word
                "levakeʃ",
                # hebrew_word_nikud
                "‫לְבַקֵש‬‬"
            ),
            (
                # translation_word
                "протестовать",
                # pronunciation_word
                "limχot",
                # hebrew_word_nikud
                "‬‫לִמחוֹת‬"
            ),
            (
                # translation_word
                "прощать",
                # pronunciation_word
                "lis'loaχ",
                # hebrew_word_nikud
                "‫לִסלוֹח‬‬"
            ),
            (
                # translation_word
                "работать",
                # pronunciation_word
                "laʿavod",
                # hebrew_word_nikud
                "‬‫לַעֲבוֹד‬"
            ),
            (
                # translation_word
                "развлекать",
                # pronunciation_word
                "levader",
                # hebrew_word_nikud
                "‬‫לְבַדֵר‬"
            ),
            (
                # translation_word
                "раздражаться",
                # pronunciation_word
                "lehitragez",
                # hebrew_word_nikud
                "‬‫לְהִתרַגֵז‬"
            ),
            (
                # translation_word
                "разрешать (позволять)",
                # pronunciation_word
                "leharʃot",
                # hebrew_word_nikud
                "‫לְהַרשוֹת‬‬"
            ),
            (
                # translation_word
                "рассказывать",
                # pronunciation_word
                "lesaper",
                # hebrew_word_nikud
                "‬‫לְסַפֵּר‬"
            ),
            (
                # translation_word
                "рассчитывать на ...",
                # pronunciation_word
                "lismoχ al",
                # hebrew_word_nikud
                "‬לִסמוֹך‬‬ ‫עַל‬"
            ),
            (
                # translation_word
                "рвать",
                # pronunciation_word
                "liktof",
                # hebrew_word_nikud
                "‫לִקטוֹף‬‬"
            ),
            (
                # translation_word
                "рекламировать",
                # pronunciation_word
                "lefarsem",
                # hebrew_word_nikud
                "‫לְפַרסֵם‬‬"
            ),
            (
                # translation_word
                "решать (принимать решение)",
                # pronunciation_word
                "lehaχlit",
                # hebrew_word_nikud
                "‫לְהַחלִיט‬‬"
            ),
            (
                # translation_word
                "решить (задачу)",
                # pronunciation_word
                "liftor",
                # hebrew_word_nikud
                "‫לִפתוֹר‬‬"
            ),
            (
                # translation_word
                "рисковать",
                # pronunciation_word
                "la'kaχat sikun",
                # hebrew_word_nikud
                "לָקַחַת‬‬ ‫סִיכּוּן‬‬"
            ),
            (
                # translation_word
                "ругать",
                # pronunciation_word
                "linzof",
                # hebrew_word_nikud
                "‫לִנזוֹף‬‬"
            ),
            (
                # translation_word
                "руководить",
                # pronunciation_word
                "lenahel",
                # hebrew_word_nikud
                "‫לְנַהֵל‬‬"
            ),
        ]
    ),    
    (
        # group_name_ru
        "173. Глаголы 5",
        # words
        [
            (
                # translation_word
                "светиться (блестеть)",
                # pronunciation_word
                "lizhor",
                # hebrew_word_nikud
                "‫לִזהוֹר‬‬"
            ),
            (
                # translation_word
                "связывать",
                # pronunciation_word
                "likʃor",
                # hebrew_word_nikud
                "‫לִקשוֹר‬‬"
            ),
            (
                # translation_word
                "сердиться (на ...)",
                # pronunciation_word
                "lehitragez",
                # hebrew_word_nikud
                "‫לְהִתרַגֵז‬‬"
            ),
            (
                # translation_word
                "сесть",
                # pronunciation_word
                "lehityaʃev",
                # hebrew_word_nikud
                "‫לְהִתייַשֵב‬‬"
            ),
            (
                # translation_word
                "сидеть",
                # pronunciation_word
                "la'ʃevet",
                # hebrew_word_nikud
                "‬‫לָשֶבֶת‬"
            ),
            (
                # translation_word
                "сказать",
                # pronunciation_word
                "lomar",
                # hebrew_word_nikud
                "‬‫לוֹמַר‬"
            ),
            (
                # translation_word
                "скучать",
                # pronunciation_word
                "lehiʃtaʿamem",
                # hebrew_word_nikud
                "‫לְהִשתַעֲמֵם‬‬"
            ),
            (
                # translation_word
                "слушать",
                # pronunciation_word
                "lehakʃiv",
                # hebrew_word_nikud
                "‫לְהַקשִיב‬‬"
            ),
            (
                # translation_word
                "слышать",
                # pronunciation_word
                "liʃ'moʿa",
                # hebrew_word_nikud
                "‫לִשמוֹע‬‬"
            ),
            (
                # translation_word
                "смеяться",
                # pronunciation_word
                "liʦχok",
                # hebrew_word_nikud
                "‬‫לִצחוֹק‬"
            ),
            (
                # translation_word
                "смотреть",
                # pronunciation_word
                "lehistakel",
                # hebrew_word_nikud
                "‫לְהִסתַכֵּל‬‬"
            ),
            (
                # translation_word
                "снимать (~ квартиру)",
                # pronunciation_word
                "liskor",
                # hebrew_word_nikud
                "‫לִשׂכּוֹר‬‬"
            ),
            (
                # translation_word
                "советовать",
                # pronunciation_word
                "leyaʿeʦ",
                # hebrew_word_nikud
                "‫לְייַעֵץ‬‬"
            ),
            (
                # translation_word
                "соглашаться",
                # pronunciation_word
                "lehaskim",
                # hebrew_word_nikud
                "‫לְהַסכִּים‬‬"
            ),
            (
                # translation_word
                "создать",
                # pronunciation_word
                "liʦor",
                # hebrew_word_nikud
                "‫לִיצוֹר‬‬"
            ),
            (
                # translation_word
                "сомневаться",
                # pronunciation_word
                "lefakpek",
                # hebrew_word_nikud
                "‫לְפַקפֵּק‬‬"
            ),
            (
                # translation_word
                "сотрудничать",
                # pronunciation_word
                "leʃatef peʿula",
                # hebrew_word_nikud
                "לְשַתֵף‬ ‬‫פְּעוּלָה‬‬"
            ),
            (
                # translation_word
                "сохранять",
                # pronunciation_word
                "leʃamer",
                # hebrew_word_nikud
                "‫לְשַמֵר‬‬"
            ),
            (
                # translation_word
                "спасать",
                # pronunciation_word
                "lehaʦil",
                # hebrew_word_nikud
                "‫לְהַצִיל‬‬"
            ),
            (
                # translation_word
                "сравнивать",
                # pronunciation_word
                "lehaʃvot",
                # hebrew_word_nikud
                "‫לְהַשווֹת‬‬"
            ),
            (
                # translation_word
                "становиться (сделаться)",
                # pronunciation_word
                "lahafoχ le...",
                # hebrew_word_nikud
                "לַהֲפוֹך‬‬ ‫ל‬‬"
            ),
            (
                # translation_word
                "стирать (бельё)",
                # pronunciation_word
                "leχabes",
                # hebrew_word_nikud
                "‬‫לְכַבֵּס‬"
            ),
            (
                # translation_word
                "стоить",
                # pronunciation_word
                "laʿalot",
                # hebrew_word_nikud
                "‫לַעֲלוֹת‬‬"
            ),
            (
                # translation_word
                "страдать",
                # pronunciation_word
                "lisbol",
                # hebrew_word_nikud
                "‫לִסבּוֹל‬‬"
            ),
            (
                # translation_word
                "стрелять",
                # pronunciation_word
                "lirot",
                # hebrew_word_nikud
                "‬‫לִירוֹת‬"
            ),
            (
                # translation_word
                "стремиться (желать)",
                # pronunciation_word
                "liʃʾof",
                # hebrew_word_nikud
                "‫לִשאוֹף‬‬"
            ),
            (
                # translation_word
                "существовать",
                # pronunciation_word
                "lehitkayem",
                # hebrew_word_nikud
                "‫לְהִתקַייֵם‬‬"
            ),
            (
                # translation_word
                "сушить",
                # pronunciation_word
                "leyabeʃ",
                # hebrew_word_nikud
                "‫לְייַבֵּש‬‬"
            ),
            (
                # translation_word
                "терпеть (боль и т.п.)",
                # pronunciation_word
                "lisbol",
                # hebrew_word_nikud
                "‫לִסבּוֹל‬‬"
            ),
            (
                # translation_word
                "терять",
                # pronunciation_word
                "leʾabed",
                # hebrew_word_nikud
                "‫לְאַבֵּד‬‬"
            ),
            (
                # translation_word
                "торопиться",
                # pronunciation_word
                "lemaher",
                # hebrew_word_nikud
                "‫לְמַהֵר‬‬"
            ),
            (
                # translation_word
                "требовать",
                # pronunciation_word
                "lidroʃ",
                # hebrew_word_nikud
                "‫לִדרוֹש‬‬"
            ),
            (
                # translation_word
                "тренироваться",
                # pronunciation_word
                "lehitʾamen",
                # hebrew_word_nikud
                "‫לְהִתאַמֵן‬‬"
            ),
            (
                # translation_word
                "тушить ",
                # pronunciation_word
                "leχabot",
                # hebrew_word_nikud
                "‬‫לְכַבּוֹת‬"
            ),
            (
                # translation_word
                "убеждать",
                # pronunciation_word
                "leʃaχ'neʿa",
                # hebrew_word_nikud
                "‬‫לְשַכנֵע‬"
            ),
            (
                # translation_word
                "убивать",
                # pronunciation_word
                "laharog",
                # hebrew_word_nikud
                "‬‫לַהֲרוֹג‬"
            ),
            (
                # translation_word
                "убирать (наводить порядок)",
                # pronunciation_word
                "lesader",
                # hebrew_word_nikud
                "‫לְסַדֵר‬‬"
            ),
            (
                # translation_word
                "удивлять",
                # pronunciation_word
                "lehaf'tiʿa",
                # hebrew_word_nikud
                "‫לְהַפתִיע‬‬"
            ),
            (
                # translation_word
                "удовлетворять",
                # pronunciation_word
                "lesapek",
                # hebrew_word_nikud
                "‫לְסַפֵּק‬‬"
            ),
            (
                # translation_word
                "уезжать",
                # pronunciation_word
                "laʿazov",
                # hebrew_word_nikud
                "‫לַעֲזוֹב‬‬"
            ),
            (
                # translation_word
                "ужинать",
                # pronunciation_word
                "leʾeχol aruχat 'erev",
                # hebrew_word_nikud
                "לֶאֱכוֹל‬‬ ‫אֲרוּחַת‬ ‫עֶרֶב‬‬"
            ),
            (
                # translation_word
                "украшать (дом и т.п.)",
                # pronunciation_word
                "lekaʃet",
                # hebrew_word_nikud
                "‫לְקַשֵט‬‬"
            ),
            (
                # translation_word
                "улыбаться",
                # pronunciation_word
                "leχayeχ",
                # hebrew_word_nikud
                "‬‫לְחַייֵך‬"
            ),
            (
                # translation_word
                "уменьшать",
                # pronunciation_word
                "lehaktin",
                # hebrew_word_nikud
                "‫לְהַקטִין‬‬"
            ),
            (
                # translation_word
                "упрекать",
                # pronunciation_word
                "linzof",
                # hebrew_word_nikud
                "‫לִנזוֹף‬‬"
            ),
            (
                # translation_word
                "успокаивать",
                # pronunciation_word
                "lehar'giʿa",
                # hebrew_word_nikud
                "‫לְהַרגִיע‬"
            ),
            (
                # translation_word
                "уступать",
                # pronunciation_word
                "levater",
                # hebrew_word_nikud
                "‫לְווַתֵר‬‬"
            ),
            (
                # translation_word
                "участвовать",
                # pronunciation_word
                "lehiʃtatef",
                # hebrew_word_nikud
                "‫לְהִשתַתֵף‬‬"
            ),
            (
                # translation_word
                "фотографировать",
                # pronunciation_word
                "leʦalem",
                # hebrew_word_nikud
                "‫לְצַלֵם‬‬"
            ),
            (
                # translation_word
                "хвастаться",
                # pronunciation_word
                "lehitravrev",
                # hebrew_word_nikud
                "‬‫לְהִתרַברֵב‬"
            ),
            (
                # translation_word
                "хотеть",
                # pronunciation_word
                "lirʦot",
                # hebrew_word_nikud
                "‫לִרצוֹת‬‬"
            ),
            (
                # translation_word
                "хранить",
                # pronunciation_word
                "liʃmor",
                # hebrew_word_nikud
                "‫לִשמוֹר‬‬"
            ),
            (
                # translation_word
                "чистить",
                # pronunciation_word
                "lenakot",
                # hebrew_word_nikud
                "‬‫לְנַקוֹת‬"
            ),
            (
                # translation_word
                "читать",
                # pronunciation_word
                "likro",
                # hebrew_word_nikud
                "‫לִקרוֹא‬‬"
            ),
            (
                # translation_word
                "чувствовать (опасность)",
                # pronunciation_word
                "laχuʃ",
                # hebrew_word_nikud
                "‬‫לָחוּש‬"
            ),
            (
                # translation_word
                "шутить",
                # pronunciation_word
                "lehitba'deaχ",
                # hebrew_word_nikud
                "‬‫לְהִתבַּדֵח‬"
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