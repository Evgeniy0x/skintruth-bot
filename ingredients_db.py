"""
SkinTruth — База данных косметических ингредиентов.
150+ ингредиентов с данными о безопасности, стоимости и функциях.
"""

# Каждый ингредиент:
# name — INCI название
# name_ru — русское название
# safety_score — безопасность 1-10 (10 = идеально безопасен)
# category — "green" / "yellow" / "red"
# function — основная функция
# description — описание простым языком
# cost_per_gram — оптовая цена в рублях за грамм
# typical_concentration — типичная концентрация в % в готовом продукте
# comedogenic_rating — 0-5 (0 = не забивает поры)
# skin_types — кому подходит
# concerns — предупреждения
# alternatives — альтернативы
# aliases — другие написания

INGREDIENTS = {
    # ============================================================
    # БАЗОВЫЕ / РАСТВОРИТЕЛИ
    # ============================================================
    "aqua": {
        "name": "Aqua", "name_ru": "Вода",
        "safety_score": 10, "category": "green",
        "function": "Растворитель, основа",
        "description": "Обычная очищенная вода — основа почти любого косметического средства. Составляет 60-85% формулы.",
        "cost_per_gram": 0.0, "typical_concentration": 70.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["water", "eau", "вода"]
    },
    "glycerin": {
        "name": "Glycerin", "name_ru": "Глицерин",
        "safety_score": 9, "category": "green",
        "function": "Увлажнитель",
        "description": "Натуральный увлажнитель, притягивает влагу из воздуха к коже. Один из самых безопасных и эффективных ингредиентов.",
        "cost_per_gram": 0.03, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["При очень сухом воздухе (<30% влажности) может вытягивать влагу из кожи"],
        "alternatives": ["Butylene Glycol", "Propanediol"],
        "aliases": ["glycerol", "glycerine", "глицерол"]
    },
    "butylene glycol": {
        "name": "Butylene Glycol", "name_ru": "Бутиленгликоль",
        "safety_score": 8, "category": "green",
        "function": "Увлажнитель, растворитель",
        "description": "Увлажняет кожу и помогает другим ингредиентам лучше впитываться. Легче глицерина, не липкий.",
        "cost_per_gram": 0.05, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Glycerin", "Propanediol"],
        "aliases": ["1,3-butanediol"]
    },
    "propanediol": {
        "name": "Propanediol", "name_ru": "Пропандиол",
        "safety_score": 9, "category": "green",
        "function": "Увлажнитель, растворитель",
        "description": "Растительный аналог пропиленгликоля. Увлажняет, улучшает текстуру. Безопасен для чувствительной кожи.",
        "cost_per_gram": 0.06, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Glycerin", "Butylene Glycol"],
        "aliases": ["1,3-propanediol"]
    },
    "propylene glycol": {
        "name": "Propylene Glycol", "name_ru": "Пропиленгликоль",
        "safety_score": 6, "category": "yellow",
        "function": "Увлажнитель, растворитель, проводник",
        "description": "Увлажняет и помогает другим веществам проникать в кожу. У небольшого % людей может вызывать раздражение.",
        "cost_per_gram": 0.02, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily", "combination"],
        "concerns": ["Может раздражать чувствительную кожу", "Потенциальный аллерген у 2-5% людей"],
        "alternatives": ["Propanediol", "Glycerin"],
        "aliases": ["pg", "1,2-propanediol"]
    },

    # ============================================================
    # АКТИВНЫЕ ИНГРЕДИЕНТЫ
    # ============================================================
    "niacinamide": {
        "name": "Niacinamide", "name_ru": "Ниацинамид (Витамин B3)",
        "safety_score": 10, "category": "green",
        "function": "Осветление, сужение пор, укрепление барьера",
        "description": "Универсальный активный ингредиент: осветляет пигментацию, сужает поры, укрепляет защитный барьер кожи, регулирует жирность.",
        "cost_per_gram": 0.15, "typical_concentration": 4.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["При концентрации >10% может вызвать покраснение"],
        "alternatives": ["Arbutin", "Tranexamic Acid"],
        "aliases": ["nicotinamide", "vitamin b3", "витамин b3"]
    },
    "retinol": {
        "name": "Retinol", "name_ru": "Ретинол (Витамин A)",
        "safety_score": 7, "category": "yellow",
        "function": "Антивозрастной, обновление клеток",
        "description": "Золотой стандарт антивозрастного ухода. Ускоряет обновление клеток, разглаживает морщины, выравнивает тон. Требует привыкания.",
        "cost_per_gram": 2.5, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily", "combination"],
        "concerns": ["Повышает чувствительность к солнцу", "Может вызвать шелушение при первом использовании", "Нельзя при беременности"],
        "alternatives": ["Bakuchiol", "Retinal", "Retinyl Palmitate"],
        "aliases": ["vitamin a", "витамин а"]
    },
    "retinal": {
        "name": "Retinal", "name_ru": "Ретиналь",
        "safety_score": 7, "category": "yellow",
        "function": "Антивозрастной (сильнее ретинола)",
        "description": "На один шаг ближе к ретиноевой кислоте, чем ретинол. Работает быстрее, но и раздражает больше.",
        "cost_per_gram": 5.0, "typical_concentration": 0.05,
        "comedogenic_rating": 0, "skin_types": ["normal", "combination"],
        "concerns": ["Сильнее раздражает, чем ретинол", "Нельзя при беременности"],
        "alternatives": ["Retinol", "Bakuchiol"],
        "aliases": ["retinaldehyde"]
    },
    "bakuchiol": {
        "name": "Bakuchiol", "name_ru": "Бакучиол",
        "safety_score": 9, "category": "green",
        "function": "Растительная альтернатива ретинолу",
        "description": "Натуральный антивозрастной ингредиент из растения бабчи. Действует как ретинол, но без раздражения. Подходит беременным.",
        "cost_per_gram": 3.0, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Retinol"],
        "aliases": []
    },
    "hyaluronic acid": {
        "name": "Hyaluronic Acid", "name_ru": "Гиалуроновая кислота",
        "safety_score": 10, "category": "green",
        "function": "Глубокое увлажнение",
        "description": "Удерживает воду в 1000 раз больше своего веса. Мгновенно увлажняет и делает кожу упругой. Натуральный компонент нашей кожи.",
        "cost_per_gram": 0.8, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Низкомолекулярная ГК может раздражать повреждённую кожу"],
        "alternatives": ["Sodium Hyaluronate", "Polyglutamic Acid"],
        "aliases": ["ha", "гиалуронка", "sodium hyaluronate", "гиалуроновая кислота"]
    },
    "sodium hyaluronate": {
        "name": "Sodium Hyaluronate", "name_ru": "Натрия гиалуронат",
        "safety_score": 10, "category": "green",
        "function": "Увлажнение",
        "description": "Соль гиалуроновой кислоты. Молекула меньше, поэтому лучше проникает в кожу. По сути — улучшенная гиалуроновая кислота.",
        "cost_per_gram": 1.0, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Hyaluronic Acid"],
        "aliases": []
    },
    "ascorbic acid": {
        "name": "Ascorbic Acid", "name_ru": "Аскорбиновая кислота (Витамин C)",
        "safety_score": 8, "category": "green",
        "function": "Антиоксидант, осветление, стимуляция коллагена",
        "description": "Чистый витамин C — мощнейший антиоксидант. Осветляет пигментацию, стимулирует выработку коллагена, защищает от фотостарения.",
        "cost_per_gram": 0.1, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Нестабилен, быстро окисляется", "При высоких концентрациях может щипать"],
        "alternatives": ["Ascorbyl Glucoside", "Ethyl Ascorbic Acid"],
        "aliases": ["vitamin c", "l-ascorbic acid", "витамин с"]
    },
    "ascorbyl glucoside": {
        "name": "Ascorbyl Glucoside", "name_ru": "Аскорбил глюкозид",
        "safety_score": 9, "category": "green",
        "function": "Стабильная форма витамина C",
        "description": "Стабильный водорастворимый витамин C. Мягче чистой аскорбиновой кислоты, подходит чувствительной коже.",
        "cost_per_gram": 0.5, "typical_concentration": 2.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Ascorbic Acid"],
        "aliases": ["aa2g"]
    },
    "tocopherol": {
        "name": "Tocopherol", "name_ru": "Токоферол (Витамин E)",
        "safety_score": 9, "category": "green",
        "function": "Антиоксидант, защита кожи",
        "description": "Витамин E — защищает клетки от повреждений, увлажняет, помогает заживлению. Часто используется как стабилизатор формулы.",
        "cost_per_gram": 0.2, "typical_concentration": 1.0,
        "comedogenic_rating": 2, "skin_types": ["dry", "normal", "sensitive"],
        "concerns": ["Может забивать поры при жирной коже"],
        "alternatives": ["Tocopheryl Acetate"],
        "aliases": ["vitamin e", "витамин е", "tocopheryl acetate"]
    },
    "salicylic acid": {
        "name": "Salicylic Acid", "name_ru": "Салициловая кислота (BHA)",
        "safety_score": 8, "category": "green",
        "function": "Отшелушивание, очищение пор",
        "description": "BHA-кислота, проникает внутрь пор и очищает их изнутри. Лучшее средство от акне и чёрных точек.",
        "cost_per_gram": 0.08, "typical_concentration": 1.5,
        "comedogenic_rating": 0, "skin_types": ["oily", "combination"],
        "concerns": ["Может сушить", "Повышает чувствительность к солнцу"],
        "alternatives": ["Betaine Salicylate"],
        "aliases": ["bha", "бха", "салицилка"]
    },
    "glycolic acid": {
        "name": "Glycolic Acid", "name_ru": "Гликолевая кислота (AHA)",
        "safety_score": 7, "category": "yellow",
        "function": "Отшелушивание, выравнивание тона",
        "description": "AHA-кислота с самой маленькой молекулой, проникает глубже всех. Отшелушивает мёртвые клетки, осветляет, разглаживает.",
        "cost_per_gram": 0.1, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily", "combination"],
        "concerns": ["Обязательно SPF!", "Может вызвать раздражение у чувствительной кожи"],
        "alternatives": ["Lactic Acid", "Mandelic Acid"],
        "aliases": ["aha", "аха"]
    },
    "lactic acid": {
        "name": "Lactic Acid", "name_ru": "Молочная кислота (AHA)",
        "safety_score": 8, "category": "green",
        "function": "Мягкое отшелушивание, увлажнение",
        "description": "Мягкая AHA-кислота, которая одновременно отшелушивает и увлажняет. Идеальна для новичков в кислотах.",
        "cost_per_gram": 0.06, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Повышает чувствительность к солнцу"],
        "alternatives": ["Glycolic Acid", "Mandelic Acid"],
        "aliases": ["молочная кислота"]
    },
    "mandelic acid": {
        "name": "Mandelic Acid", "name_ru": "Миндальная кислота",
        "safety_score": 9, "category": "green",
        "function": "Мягкое отшелушивание",
        "description": "Самая мягкая AHA-кислота с крупной молекулой. Работает медленнее, но почти не раздражает. Подходит тёмной коже.",
        "cost_per_gram": 0.15, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Lactic Acid"],
        "aliases": []
    },
    "azelaic acid": {
        "name": "Azelaic Acid", "name_ru": "Азелаиновая кислота",
        "safety_score": 9, "category": "green",
        "function": "Противовоспалительное, осветление, от акне",
        "description": "Мультифункциональный ингредиент: борется с акне, осветляет пигментацию, снимает воспаление. Безопасен при беременности.",
        "cost_per_gram": 0.2, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Может немного щипать при первом использовании"],
        "alternatives": ["Niacinamide"],
        "aliases": []
    },
    "ceramide np": {
        "name": "Ceramide NP", "name_ru": "Церамид NP",
        "safety_score": 10, "category": "green",
        "function": "Восстановление барьера кожи",
        "description": "Липид, идентичный натуральным церамидам кожи. Восстанавливает защитный барьер, удерживает влагу.",
        "cost_per_gram": 5.0, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Ceramide AP", "Ceramide EOP"],
        "aliases": ["ceramide 3", "церамиды"]
    },
    "ceramide ap": {
        "name": "Ceramide AP", "name_ru": "Церамид AP",
        "safety_score": 10, "category": "green",
        "function": "Восстановление барьера кожи",
        "description": "Один из ключевых церамидов кожи. Вместе с другими церамидами укрепляет защитный барьер.",
        "cost_per_gram": 5.0, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Ceramide NP"],
        "aliases": ["ceramide 6 ii"]
    },
    "peptides": {
        "name": "Peptides", "name_ru": "Пептиды",
        "safety_score": 9, "category": "green",
        "function": "Стимуляция коллагена, антивозрастной уход",
        "description": "Маленькие белковые цепочки, которые сигнализируют коже вырабатывать больше коллагена. Мягкая антивозрастная стратегия.",
        "cost_per_gram": 8.0, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Retinol", "Bakuchiol"],
        "aliases": ["palmitoyl tripeptide", "acetyl hexapeptide", "matrixyl", "argireline"]
    },
    "centella asiatica extract": {
        "name": "Centella Asiatica Extract", "name_ru": "Экстракт центеллы азиатской",
        "safety_score": 10, "category": "green",
        "function": "Заживление, противовоспалительное",
        "description": "Легендарный ингредиент корейской косметики. Ускоряет заживление, успокаивает воспаления, укрепляет кожу.",
        "cost_per_gram": 0.3, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Madecassoside"],
        "aliases": ["cica", "центелла", "madecassoside", "asiaticoside"]
    },
    "arbutin": {
        "name": "Arbutin", "name_ru": "Арбутин",
        "safety_score": 9, "category": "green",
        "function": "Осветление пигментации",
        "description": "Натуральный осветлитель из растения толокнянка. Блокирует выработку меланина, безопаснее гидрохинона.",
        "cost_per_gram": 0.5, "typical_concentration": 2.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Niacinamide", "Vitamin C"],
        "aliases": ["alpha-arbutin", "альфа-арбутин"]
    },
    "tranexamic acid": {
        "name": "Tranexamic Acid", "name_ru": "Транексамовая кислота",
        "safety_score": 9, "category": "green",
        "function": "Осветление, от пигментации",
        "description": "Мощный осветляющий ингредиент. Особенно эффективен против мелазмы и пост-воспалительной пигментации.",
        "cost_per_gram": 0.3, "typical_concentration": 2.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Arbutin", "Niacinamide"],
        "aliases": []
    },
    "squalane": {
        "name": "Squalane", "name_ru": "Сквалан",
        "safety_score": 10, "category": "green",
        "function": "Увлажнение, смягчение",
        "description": "Лёгкое масло, идентичное натуральному компоненту кожи. Увлажняет без жирности. Подходит даже жирной коже.",
        "cost_per_gram": 0.15, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Jojoba Oil"],
        "aliases": ["сквалан"]
    },
    "panthenol": {
        "name": "Panthenol", "name_ru": "Пантенол (Витамин B5)",
        "safety_score": 10, "category": "green",
        "function": "Заживление, увлажнение",
        "description": "Провитамин B5 — увлажняет, успокаивает, ускоряет заживление. Основа пантенол-спреев от ожогов.",
        "cost_per_gram": 0.1, "typical_concentration": 2.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Allantoin"],
        "aliases": ["dexpanthenol", "d-panthenol", "provitamin b5", "пантенол"]
    },
    "allantoin": {
        "name": "Allantoin", "name_ru": "Аллантоин",
        "safety_score": 10, "category": "green",
        "function": "Успокаивающий, заживляющий",
        "description": "Мягкий успокаивающий ингредиент. Смягчает кожу, ускоряет регенерацию, снимает раздражение.",
        "cost_per_gram": 0.08, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Panthenol"],
        "aliases": ["аллантоин"]
    },
    "urea": {
        "name": "Urea", "name_ru": "Мочевина",
        "safety_score": 9, "category": "green",
        "function": "Интенсивное увлажнение, отшелушивание",
        "description": "Натуральный увлажнитель кожи. При концентрации 5-10% — увлажняет, при 20-40% — отшелушивает. Спасение для сухой кожи.",
        "cost_per_gram": 0.02, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["dry", "normal"],
        "concerns": ["При высоких концентрациях может щипать на повреждённой коже"],
        "alternatives": ["Glycerin"],
        "aliases": ["мочевина", "carbamide"]
    },
    "zinc oxide": {
        "name": "Zinc Oxide", "name_ru": "Оксид цинка",
        "safety_score": 9, "category": "green",
        "function": "Минеральный UV-фильтр, противовоспалительный",
        "description": "Физический солнцезащитный фильтр. Отражает UV-лучи, подсушивает, успокаивает. Безопасен для детей и беременных.",
        "cost_per_gram": 0.05, "typical_concentration": 15.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Может оставлять белый след"], "alternatives": ["Titanium Dioxide"],
        "aliases": ["цинк оксид"]
    },
    "titanium dioxide": {
        "name": "Titanium Dioxide", "name_ru": "Диоксид титана",
        "safety_score": 8, "category": "green",
        "function": "Минеральный UV-фильтр",
        "description": "Физический солнцезащитный фильтр. Безопасен, не впитывается в кожу. Защищает от UVB-лучей.",
        "cost_per_gram": 0.04, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Белый след", "Нано-форма — вопросы безопасности при вдыхании"],
        "alternatives": ["Zinc Oxide"],
        "aliases": ["ci 77891"]
    },

    # ============================================================
    # МАСЛА И ЭМОЛЕНТЫ
    # ============================================================
    "shea butter": {
        "name": "Shea Butter", "name_ru": "Масло ши",
        "safety_score": 9, "category": "green",
        "function": "Питание, смягчение",
        "description": "Богатое питательное масло из орехов дерева ши. Содержит витамины A, E, F. Идеально для сухой кожи.",
        "cost_per_gram": 0.08, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["dry", "normal"],
        "concerns": ["Аллергия при чувствительности к орехам (редко)"],
        "alternatives": ["Cocoa Butter", "Mango Butter"],
        "aliases": ["butyrospermum parkii butter", "масло ши", "масло карите"]
    },
    "jojoba oil": {
        "name": "Jojoba Oil", "name_ru": "Масло жожоба",
        "safety_score": 9, "category": "green",
        "function": "Увлажнение, баланс кожи",
        "description": "Технически — воск, а не масло. По составу ближе всего к кожному салу. Балансирует жирность.",
        "cost_per_gram": 0.15, "typical_concentration": 3.0,
        "comedogenic_rating": 2, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Squalane"],
        "aliases": ["simmondsia chinensis seed oil", "масло жожоба"]
    },
    "coconut oil": {
        "name": "Coconut Oil", "name_ru": "Кокосовое масло",
        "safety_score": 7, "category": "yellow",
        "function": "Питание, смягчение",
        "description": "Питательное масло, хорошо увлажняет. Но сильно забивает поры — не подходит для жирной и склонной к акне кожи.",
        "cost_per_gram": 0.05, "typical_concentration": 5.0,
        "comedogenic_rating": 4, "skin_types": ["dry"],
        "concerns": ["Высокая комедогенность!", "Может провоцировать акне"],
        "alternatives": ["Jojoba Oil", "Squalane"],
        "aliases": ["cocos nucifera oil", "кокосовое масло"]
    },
    "argan oil": {
        "name": "Argan Oil", "name_ru": "Аргановое масло",
        "safety_score": 9, "category": "green",
        "function": "Питание, антиоксидант",
        "description": "Марокканское золото — богато витамином E и жирными кислотами. Питает, не забивая поры.",
        "cost_per_gram": 0.4, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Jojoba Oil"],
        "aliases": ["argania spinosa kernel oil", "аргановое масло"]
    },
    "rosehip oil": {
        "name": "Rosehip Oil", "name_ru": "Масло шиповника",
        "safety_score": 9, "category": "green",
        "function": "Регенерация, осветление рубцов",
        "description": "Богато витамином A и жирными кислотами. Осветляет рубцы и пигментацию, восстанавливает кожу.",
        "cost_per_gram": 0.3, "typical_concentration": 3.0,
        "comedogenic_rating": 1, "skin_types": ["dry", "normal", "combination"],
        "concerns": [], "alternatives": ["Argan Oil"],
        "aliases": ["rosa canina fruit oil", "масло шиповника"]
    },
    "dimethicone": {
        "name": "Dimethicone", "name_ru": "Диметикон",
        "safety_score": 8, "category": "green",
        "function": "Смягчение, защитная плёнка",
        "description": "Силикон, создающий гладкую защитную плёнку на коже. Делает кожу шелковистой, не впитывается.",
        "cost_per_gram": 0.02, "typical_concentration": 3.0,
        "comedogenic_rating": 1, "skin_types": ["all"],
        "concerns": ["Может мешать впитыванию других средств", "Требует тщательного очищения"],
        "alternatives": ["Squalane", "Cyclomethicone"],
        "aliases": ["диметикон", "pdms"]
    },
    "cyclomethicone": {
        "name": "Cyclomethicone", "name_ru": "Циклометикон",
        "safety_score": 7, "category": "yellow",
        "function": "Лёгкий силикон, растворитель",
        "description": "Летучий силикон — испаряется после нанесения, оставляя шелковистое ощущение. Облегчает нанесение.",
        "cost_per_gram": 0.03, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Вопросы экологической безопасности"],
        "alternatives": ["Isododecane"],
        "aliases": ["cyclopentasiloxane", "cyclotetrasiloxane"]
    },
    "mineral oil": {
        "name": "Mineral Oil", "name_ru": "Минеральное масло",
        "safety_score": 6, "category": "yellow",
        "function": "Окклюзив, смягчение",
        "description": "Нефтепродукт, создаёт барьер на коже. Очень дешёвый. Хорошо удерживает влагу, но вызывает споры.",
        "cost_per_gram": 0.01, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["dry"],
        "concerns": ["Продукт нефтепереработки", "Может ощущаться тяжёлым"],
        "alternatives": ["Squalane", "Jojoba Oil"],
        "aliases": ["paraffinum liquidum", "petrolatum", "вазелиновое масло"]
    },
    "petrolatum": {
        "name": "Petrolatum", "name_ru": "Вазелин",
        "safety_score": 7, "category": "yellow",
        "function": "Окклюзив, защита",
        "description": "Создаёт мощный защитный барьер. Используется дерматологами для заживления. Дешёвый, но спорный по происхождению.",
        "cost_per_gram": 0.01, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["dry"],
        "concerns": ["Продукт нефтепереработки", "Неприятная текстура"],
        "alternatives": ["Shea Butter", "Beeswax"],
        "aliases": ["petroleum jelly", "вазелин"]
    },
    "caprylic/capric triglyceride": {
        "name": "Caprylic/Capric Triglyceride", "name_ru": "Каприлик/каприк триглицерид",
        "safety_score": 9, "category": "green",
        "function": "Лёгкий эмолент",
        "description": "Лёгкое масло из кокоса. Быстро впитывается, не оставляет жирности. Прекрасная альтернатива минеральным маслам.",
        "cost_per_gram": 0.06, "typical_concentration": 5.0,
        "comedogenic_rating": 1, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Squalane"],
        "aliases": ["cct", "mct oil"]
    },
    "isopropyl myristate": {
        "name": "Isopropyl Myristate", "name_ru": "Изопропилмиристат",
        "safety_score": 5, "category": "yellow",
        "function": "Эмолент, растворитель",
        "description": "Делает текстуру средства лёгкой и шелковистой. Но сильно забивает поры — один из самых комедогенных ингредиентов.",
        "cost_per_gram": 0.03, "typical_concentration": 5.0,
        "comedogenic_rating": 5, "skin_types": ["dry"],
        "concerns": ["Очень высокая комедогенность!", "Может провоцировать акне"],
        "alternatives": ["Caprylic/Capric Triglyceride"],
        "aliases": ["ipm"]
    },

    # ============================================================
    # ЭМУЛЬГАТОРЫ И СТАБИЛИЗАТОРЫ
    # ============================================================
    "cetearyl alcohol": {
        "name": "Cetearyl Alcohol", "name_ru": "Цетеариловый спирт",
        "safety_score": 8, "category": "green",
        "function": "Эмульгатор, загуститель",
        "description": "Жирный спирт (НЕ сушащий!). Делает кремы кремообразными. Совершенно безопасен, не имеет ничего общего со спиртом-антисептиком.",
        "cost_per_gram": 0.03, "typical_concentration": 3.0,
        "comedogenic_rating": 2, "skin_types": ["all"],
        "concerns": ["Редко — аллергия у очень чувствительной кожи"],
        "alternatives": ["Cetyl Alcohol"],
        "aliases": ["цетеариловый спирт"]
    },
    "cetyl alcohol": {
        "name": "Cetyl Alcohol", "name_ru": "Цетиловый спирт",
        "safety_score": 8, "category": "green",
        "function": "Эмульгатор, смягчитель",
        "description": "Жирный спирт — смягчает кожу и стабилизирует формулы. Безопасный, не сушит.",
        "cost_per_gram": 0.03, "typical_concentration": 2.0,
        "comedogenic_rating": 2, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Cetearyl Alcohol"],
        "aliases": ["цетиловый спирт"]
    },
    "stearic acid": {
        "name": "Stearic Acid", "name_ru": "Стеариновая кислота",
        "safety_score": 8, "category": "green",
        "function": "Эмульгатор, загуститель",
        "description": "Жирная кислота, которая стабилизирует кремы и придаёт им густую текстуру. Натуральный компонент.",
        "cost_per_gram": 0.02, "typical_concentration": 2.0,
        "comedogenic_rating": 2, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["стеариновая кислота"]
    },
    "polysorbate 20": {
        "name": "Polysorbate 20", "name_ru": "Полисорбат 20",
        "safety_score": 7, "category": "green",
        "function": "Эмульгатор, солюбилизатор",
        "description": "Помогает смешивать масла с водой. Мягкий, часто используется в средствах для чувствительной кожи.",
        "cost_per_gram": 0.04, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Может содержать следы этиленоксида"],
        "alternatives": ["Polysorbate 60"],
        "aliases": ["tween 20"]
    },
    "polysorbate 60": {
        "name": "Polysorbate 60", "name_ru": "Полисорбат 60",
        "safety_score": 7, "category": "green",
        "function": "Эмульгатор",
        "description": "Стабилизирует кремовые текстуры. Широко используется в косметике и пищевой промышленности.",
        "cost_per_gram": 0.04, "typical_concentration": 1.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Polysorbate 20"],
        "aliases": ["tween 60"]
    },
    "polysorbate 80": {
        "name": "Polysorbate 80", "name_ru": "Полисорбат 80",
        "safety_score": 7, "category": "green",
        "function": "Эмульгатор",
        "description": "Помогает маслам растворяться в воде. Используется в косметике и медицине.",
        "cost_per_gram": 0.04, "typical_concentration": 1.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Polysorbate 20"],
        "aliases": ["tween 80"]
    },
    "carbomer": {
        "name": "Carbomer", "name_ru": "Карбомер",
        "safety_score": 8, "category": "green",
        "function": "Загуститель, стабилизатор",
        "description": "Создаёт гелевую текстуру. Прозрачный, безопасный полимер. Именно он делает гели гелями.",
        "cost_per_gram": 0.05, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Xanthan Gum"],
        "aliases": ["карбомер", "carbopol"]
    },
    "xanthan gum": {
        "name": "Xanthan Gum", "name_ru": "Ксантановая камедь",
        "safety_score": 9, "category": "green",
        "function": "Загуститель, стабилизатор",
        "description": "Натуральный загуститель из ферментации сахара. Безопасен, широко используется в еде и косметике.",
        "cost_per_gram": 0.04, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Carbomer"],
        "aliases": ["ксантановая камедь"]
    },

    # ============================================================
    # КОНСЕРВАНТЫ
    # ============================================================
    "phenoxyethanol": {
        "name": "Phenoxyethanol", "name_ru": "Феноксиэтанол",
        "safety_score": 7, "category": "green",
        "function": "Консервант",
        "description": "Один из самых безопасных консервантов. Основная альтернатива парабенам. Используется в детской косметике.",
        "cost_per_gram": 0.05, "typical_concentration": 0.8,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["В редких случаях может раздражать чувствительную кожу"],
        "alternatives": [], "aliases": ["феноксиэтанол"]
    },
    "methylparaben": {
        "name": "Methylparaben", "name_ru": "Метилпарабен",
        "safety_score": 5, "category": "yellow",
        "function": "Консервант",
        "description": "Самый безопасный из парабенов. Споры вокруг парабенов: связь с гормонами не доказана при косметических концентрациях, но осадок остался.",
        "cost_per_gram": 0.02, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Спорная безопасность (гормональная активность)", "Запрещён в ЕС выше 0.4%"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["метилпарабен", "e218"]
    },
    "ethylparaben": {
        "name": "Ethylparaben", "name_ru": "Этилпарабен",
        "safety_score": 5, "category": "yellow",
        "function": "Консервант",
        "description": "Парабен. Эффективный консервант, но с репутационными проблемами из-за исследований о гормональной активности.",
        "cost_per_gram": 0.02, "typical_concentration": 0.2,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Спорная безопасность"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["этилпарабен"]
    },
    "propylparaben": {
        "name": "Propylparaben", "name_ru": "Пропилпарабен",
        "safety_score": 4, "category": "yellow",
        "function": "Консервант",
        "description": "Парабен с более сильным консервирующим действием. Вызывает больше опасений, чем метилпарабен.",
        "cost_per_gram": 0.02, "typical_concentration": 0.2,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Гормональная активность", "Запрещён в некоторых странах в детской косметике"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["пропилпарабен"]
    },
    "butylparaben": {
        "name": "Butylparaben", "name_ru": "Бутилпарабен",
        "safety_score": 3, "category": "red",
        "function": "Консервант",
        "description": "Парабен с самой высокой гормональной активностью среди парабенов. Многие бренды отказались от него.",
        "cost_per_gram": 0.02, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Гормональный разрушитель", "Запрещён в ЕС выше 0.14%", "Избегать!"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["бутилпарабен"]
    },
    "benzisothiazolinone": {
        "name": "Benzisothiazolinone", "name_ru": "Бензизотиазолинон",
        "safety_score": 3, "category": "red",
        "function": "Консервант",
        "description": "Сильный консервант, но частый аллерген. Вызывает контактный дерматит. Не рекомендуется для leave-on продуктов.",
        "cost_per_gram": 0.03, "typical_concentration": 0.01,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Сильный аллерген", "Вызывает контактный дерматит", "Избегать в несмываемой косметике"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["bit"]
    },
    "methylisothiazolinone": {
        "name": "Methylisothiazolinone", "name_ru": "Метилизотиазолинон",
        "safety_score": 2, "category": "red",
        "function": "Консервант",
        "description": "Опасный аллерген! Запрещён в ЕС в несмываемых средствах с 2016 года. Вызывает тяжёлые аллергические реакции.",
        "cost_per_gram": 0.03, "typical_concentration": 0.01,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["ЗАПРЕЩЁН в ЕС в leave-on!", "Сильнейший аллерген", "Дерматит"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["mit", "mi"]
    },
    "ethylhexylglycerin": {
        "name": "Ethylhexylglycerin", "name_ru": "Этилгексилглицерин",
        "safety_score": 8, "category": "green",
        "function": "Со-консервант, кондиционер",
        "description": "Усиливает действие других консервантов. Также смягчает кожу. Часто идёт в паре с феноксиэтанолом.",
        "cost_per_gram": 0.05, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["octoxyglycerin"]
    },
    "sodium benzoate": {
        "name": "Sodium Benzoate", "name_ru": "Бензоат натрия",
        "safety_score": 7, "category": "green",
        "function": "Консервант",
        "description": "Мягкий консервант, широко используется в еде и косметике. Работает при низком pH.",
        "cost_per_gram": 0.02, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["бензоат натрия", "e211"]
    },
    "potassium sorbate": {
        "name": "Potassium Sorbate", "name_ru": "Сорбат калия",
        "safety_score": 8, "category": "green",
        "function": "Консервант",
        "description": "Мягкий консервант из рябины. Широко используется в еде и натуральной косметике.",
        "cost_per_gram": 0.02, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["сорбат калия", "e202"]
    },

    # ============================================================
    # ПАВ (ПОВЕРХНОСТНО-АКТИВНЫЕ ВЕЩЕСТВА)
    # ============================================================
    "sodium lauryl sulfate": {
        "name": "Sodium Lauryl Sulfate", "name_ru": "Лаурилсульфат натрия (SLS)",
        "safety_score": 3, "category": "red",
        "function": "ПАВ, пенообразователь",
        "description": "Агрессивный пенообразователь. Отлично пенится, но разрушает защитный барьер кожи. Частая причина сухости и раздражения.",
        "cost_per_gram": 0.01, "typical_concentration": 10.0,
        "comedogenic_rating": 5, "skin_types": [],
        "concerns": ["Разрушает барьер кожи", "Сушит", "Раздражает глаза", "Высокая комедогенность"],
        "alternatives": ["Cocamidopropyl Betaine", "Sodium Cocoyl Glutamate"],
        "aliases": ["sls", "слс", "содиум лаурил сульфат"]
    },
    "sodium laureth sulfate": {
        "name": "Sodium Laureth Sulfate", "name_ru": "Лауретсульфат натрия (SLES)",
        "safety_score": 4, "category": "yellow",
        "function": "ПАВ, пенообразователь",
        "description": "Мягче SLS, но всё равно может сушить. Самый распространённый ПАВ в шампунях и гелях для душа. Дешёвый.",
        "cost_per_gram": 0.01, "typical_concentration": 10.0,
        "comedogenic_rating": 3, "skin_types": ["oily", "normal"],
        "concerns": ["Сушит при частом использовании", "Может содержать следы 1,4-диоксана"],
        "alternatives": ["Cocamidopropyl Betaine"],
        "aliases": ["sles", "слес"]
    },
    "cocamidopropyl betaine": {
        "name": "Cocamidopropyl Betaine", "name_ru": "Кокамидопропилбетаин",
        "safety_score": 8, "category": "green",
        "function": "Мягкий ПАВ",
        "description": "Мягкий ПАВ из кокосового масла. Хорошо пенится, не сушит. Отличная замена SLS/SLES.",
        "cost_per_gram": 0.04, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Очень редко — аллергия на примеси"],
        "alternatives": ["Decyl Glucoside"],
        "aliases": ["capb"]
    },
    "sodium cocoyl glutamate": {
        "name": "Sodium Cocoyl Glutamate", "name_ru": "Кокоилглутамат натрия",
        "safety_score": 9, "category": "green",
        "function": "Мягкий ПАВ (аминокислотный)",
        "description": "Аминокислотный ПАВ — один из самых мягких. pH близок к коже. Идеален для чувствительной кожи.",
        "cost_per_gram": 0.08, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Cocamidopropyl Betaine"],
        "aliases": []
    },
    "decyl glucoside": {
        "name": "Decyl Glucoside", "name_ru": "Децилглюкозид",
        "safety_score": 9, "category": "green",
        "function": "Мягкий ПАВ (сахарный)",
        "description": "Мягкий ПАВ из сахара и кокоса. Подходит для самой чувствительной кожи и детской косметики.",
        "cost_per_gram": 0.06, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Cocamidopropyl Betaine"],
        "aliases": []
    },

    # ============================================================
    # ОТДУШКИ И КРАСИТЕЛИ
    # ============================================================
    "fragrance": {
        "name": "Fragrance", "name_ru": "Отдушка",
        "safety_score": 3, "category": "red",
        "function": "Ароматизатор",
        "description": "За словом Fragrance/Parfum скрывается коктейль из 50-200 химических веществ, которые производитель не обязан раскрывать. Частая причина аллергии.",
        "cost_per_gram": 0.1, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Первая причина аллергии в косметике!", "Скрытый состав", "Может содержать фталаты"],
        "alternatives": [],
        "aliases": ["parfum", "aroma", "отдушка", "парфюм"]
    },
    "linalool": {
        "name": "Linalool", "name_ru": "Линалоол",
        "safety_score": 5, "category": "yellow",
        "function": "Ароматический компонент",
        "description": "Ароматическое вещество, часто из лаванды. При окислении на воздухе становится аллергеном.",
        "cost_per_gram": 0.05, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Потенциальный аллерген", "Обязательно указывается в ЕС"],
        "alternatives": [],
        "aliases": ["линалоол"]
    },
    "limonene": {
        "name": "Limonene", "name_ru": "Лимонен",
        "safety_score": 5, "category": "yellow",
        "function": "Ароматический компонент",
        "description": "Ароматическое вещество с цитрусовым запахом. Натуральный, но потенциальный аллерген.",
        "cost_per_gram": 0.03, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Потенциальный аллерген", "Фотосенсибилизатор"],
        "alternatives": [],
        "aliases": ["d-limonene", "лимонен"]
    },
    "citronellol": {
        "name": "Citronellol", "name_ru": "Цитронеллол",
        "safety_score": 5, "category": "yellow",
        "function": "Ароматический компонент",
        "description": "Ароматический спирт с розовым запахом. Встречается в эфирных маслах. Аллерген ЕС.",
        "cost_per_gram": 0.04, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["normal"],
        "concerns": ["Потенциальный аллерген"],
        "alternatives": [],
        "aliases": ["цитронеллол"]
    },
    "geraniol": {
        "name": "Geraniol", "name_ru": "Гераниол",
        "safety_score": 5, "category": "yellow",
        "function": "Ароматический компонент",
        "description": "Ароматическое вещество с запахом розы. Натуральный, но частый аллерген.",
        "cost_per_gram": 0.05, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["normal"],
        "concerns": ["Аллерген"], "alternatives": [],
        "aliases": ["гераниол"]
    },
    "ci 77491": {
        "name": "CI 77491", "name_ru": "Оксид железа (красный)",
        "safety_score": 8, "category": "green",
        "function": "Краситель",
        "description": "Минеральный красный пигмент. Безопасен, не впитывается в кожу.",
        "cost_per_gram": 0.02, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["iron oxide red"]
    },
    "ci 77492": {
        "name": "CI 77492", "name_ru": "Оксид железа (жёлтый)",
        "safety_score": 8, "category": "green",
        "function": "Краситель",
        "description": "Минеральный жёлтый пигмент. Безопасный, используется в тональных средствах.",
        "cost_per_gram": 0.02, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["iron oxide yellow"]
    },
    "ci 77499": {
        "name": "CI 77499", "name_ru": "Оксид железа (чёрный)",
        "safety_score": 8, "category": "green",
        "function": "Краситель",
        "description": "Минеральный чёрный пигмент. Безопасный, используется в тушах и подводках.",
        "cost_per_gram": 0.02, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["iron oxide black"]
    },

    # ============================================================
    # UV-ФИЛЬТРЫ (ХИМИЧЕСКИЕ)
    # ============================================================
    "avobenzone": {
        "name": "Avobenzone", "name_ru": "Авобензон",
        "safety_score": 6, "category": "yellow",
        "function": "Химический UV-A фильтр",
        "description": "Один из немногих фильтров UVA-лучей. Но нестабилен на солнце — разрушается без стабилизатора.",
        "cost_per_gram": 0.1, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Нестабилен без стабилизатора", "Может раздражать чувствительную кожу"],
        "alternatives": ["Zinc Oxide"],
        "aliases": ["butyl methoxydibenzoylmethane"]
    },
    "octinoxate": {
        "name": "Octinoxate", "name_ru": "Октиноксат",
        "safety_score": 4, "category": "yellow",
        "function": "Химический UV-B фильтр",
        "description": "Распространённый UVB-фильтр. Вызывает опасения из-за гормональной активности и вреда коралловым рифам.",
        "cost_per_gram": 0.06, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Потенциальный эндокринный разрушитель", "Токсичен для кораллов", "Запрещён на Гавайях"],
        "alternatives": ["Zinc Oxide", "Titanium Dioxide"],
        "aliases": ["ethylhexyl methoxycinnamate", "octyl methoxycinnamate"]
    },
    "octocrylene": {
        "name": "Octocrylene", "name_ru": "Октокрилен",
        "safety_score": 5, "category": "yellow",
        "function": "Химический UV-фильтр, стабилизатор",
        "description": "Защищает от UVB, стабилизирует авобензон. Но накапливает бензофенон при хранении.",
        "cost_per_gram": 0.05, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Накапливает бензофенон со временем", "Аллерген у некоторых людей"],
        "alternatives": ["Zinc Oxide"],
        "aliases": []
    },
    "homosalate": {
        "name": "Homosalate", "name_ru": "Гомосалат",
        "safety_score": 5, "category": "yellow",
        "function": "Химический UV-B фильтр",
        "description": "UVB-фильтр. Вызывает опасения из-за потенциальной гормональной активности.",
        "cost_per_gram": 0.04, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Потенциальный гормональный разрушитель", "ЕС ограничил до 7.34%"],
        "alternatives": ["Zinc Oxide"],
        "aliases": []
    },

    # ============================================================
    # СПИРТЫ
    # ============================================================
    "alcohol denat": {
        "name": "Alcohol Denat", "name_ru": "Денатурированный спирт",
        "safety_score": 3, "category": "red",
        "function": "Растворитель, обезжириватель",
        "description": "Обычный спирт, высушивающий кожу. Создаёт ощущение лёгкости, но разрушает барьер. При частом использовании ускоряет старение.",
        "cost_per_gram": 0.01, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Сушит кожу", "Разрушает барьер", "Ускоряет старение"],
        "alternatives": [],
        "aliases": ["alcohol", "ethanol", "sd alcohol", "спирт", "этанол"]
    },
    "benzyl alcohol": {
        "name": "Benzyl Alcohol", "name_ru": "Бензиловый спирт",
        "safety_score": 6, "category": "yellow",
        "function": "Консервант, растворитель",
        "description": "Ароматический спирт, используется как мягкий консервант. В малых дозах безопасен.",
        "cost_per_gram": 0.04, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Может раздражать чувствительную кожу", "Аллерген ЕС"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["бензиловый спирт"]
    },

    # ============================================================
    # РАСТИТЕЛЬНЫЕ ЭКСТРАКТЫ
    # ============================================================
    "aloe barbadensis leaf juice": {
        "name": "Aloe Barbadensis Leaf Juice", "name_ru": "Сок алоэ вера",
        "safety_score": 10, "category": "green",
        "function": "Успокаивающий, увлажняющий",
        "description": "Легендарное растение для кожи. Успокаивает, увлажняет, ускоряет заживление. Идеален после загара.",
        "cost_per_gram": 0.02, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["aloe vera", "алоэ", "алоэ вера", "aloe barbadensis"]
    },
    "camellia sinensis leaf extract": {
        "name": "Camellia Sinensis Leaf Extract", "name_ru": "Экстракт зелёного чая",
        "safety_score": 10, "category": "green",
        "function": "Антиоксидант, противовоспалительный",
        "description": "Мощный антиоксидант из зелёного чая. Защищает от фотостарения, успокаивает воспаления.",
        "cost_per_gram": 0.15, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["green tea extract", "зелёный чай", "egcg"]
    },
    "chamomilla recutita extract": {
        "name": "Chamomilla Recutita Extract", "name_ru": "Экстракт ромашки",
        "safety_score": 10, "category": "green",
        "function": "Успокаивающий, противовоспалительный",
        "description": "Ромашка — классическое средство для успокоения кожи. Снимает покраснение и раздражение.",
        "cost_per_gram": 0.1, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Аллергия при чувствительности к астровым (редко)"],
        "alternatives": [],
        "aliases": ["chamomile extract", "ромашка", "bisabolol"]
    },
    "melaleuca alternifolia leaf oil": {
        "name": "Melaleuca Alternifolia Leaf Oil", "name_ru": "Масло чайного дерева",
        "safety_score": 7, "category": "green",
        "function": "Антибактериальное, от акне",
        "description": "Натуральный антисептик. Эффективен против акне (доказано!). Но может раздражать при высоких концентрациях.",
        "cost_per_gram": 0.2, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["oily", "combination"],
        "concerns": ["Может раздражать при >5%", "Не наносить чистым!"],
        "alternatives": [],
        "aliases": ["tea tree oil", "чайное дерево"]
    },
    "rosa damascena flower water": {
        "name": "Rosa Damascena Flower Water", "name_ru": "Розовая вода",
        "safety_score": 9, "category": "green",
        "function": "Тонизирование, лёгкое увлажнение",
        "description": "Гидролат розы — мягко тонизирует, освежает, слегка увлажняет. Ароматерапия в бутылке.",
        "cost_per_gram": 0.05, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["rose water", "розовая вода"]
    },
    "calendula officinalis extract": {
        "name": "Calendula Officinalis Extract", "name_ru": "Экстракт календулы",
        "safety_score": 9, "category": "green",
        "function": "Заживляющий, противовоспалительный",
        "description": "Календула — заживляет, снимает воспаление, успокаивает. Часто используется в детской косметике.",
        "cost_per_gram": 0.1, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["calendula", "календула"]
    },
    "lavandula angustifolia oil": {
        "name": "Lavandula Angustifolia Oil", "name_ru": "Масло лаванды",
        "safety_score": 6, "category": "yellow",
        "function": "Ароматический, успокаивающий",
        "description": "Эфирное масло лаванды — приятный аромат и лёгкое антисептическое действие. Но содержит линалоол (аллерген).",
        "cost_per_gram": 0.2, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["normal"],
        "concerns": ["Содержит линалоол — аллерген", "Может раздражать чувствительную кожу"],
        "alternatives": [],
        "aliases": ["lavender oil", "лаванда"]
    },

    # ============================================================
    # ФОРМАЛЬДЕГИД И ЕГО ДОНОРЫ
    # ============================================================
    "formaldehyde": {
        "name": "Formaldehyde", "name_ru": "Формальдегид",
        "safety_score": 1, "category": "red",
        "function": "Консервант",
        "description": "Канцероген! Запрещён в ЕС в косметике. Если видите в составе — не покупайте этот продукт.",
        "cost_per_gram": 0.01, "typical_concentration": 0.05,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["КАНЦЕРОГЕН!", "Запрещён в ЕС", "Сильный аллерген", "Токсичен"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["формальдегид", "formalin"]
    },
    "dmdm hydantoin": {
        "name": "DMDM Hydantoin", "name_ru": "ДМДМ Гидантоин",
        "safety_score": 2, "category": "red",
        "function": "Консервант (донор формальдегида)",
        "description": "Высвобождает формальдегид! Эффективный консервант, но из-за выделения формальдегида считается опасным.",
        "cost_per_gram": 0.02, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Выделяет формальдегид!", "Аллерген", "Избегать!"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": []
    },
    "imidazolidinyl urea": {
        "name": "Imidazolidinyl Urea", "name_ru": "Имидазолидинилмочевина",
        "safety_score": 3, "category": "red",
        "function": "Консервант (донор формальдегида)",
        "description": "Выделяет формальдегид при разложении. Распространённый консервант, но вызывает всё больше опасений.",
        "cost_per_gram": 0.02, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Выделяет формальдегид", "Аллерген"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["germall 115"]
    },
    "diazolidinyl urea": {
        "name": "Diazolidinyl Urea", "name_ru": "Диазолидинилмочевина",
        "safety_score": 2, "category": "red",
        "function": "Консервант (донор формальдегида)",
        "description": "Мощный консервант, но высвобождает формальдегид. Один из самых распространённых доноров формальдегида.",
        "cost_per_gram": 0.02, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Выделяет формальдегид!", "Сильный аллерген"],
        "alternatives": ["Phenoxyethanol"],
        "aliases": ["germall ii"]
    },

    # ============================================================
    # ПРОЧИЕ
    # ============================================================
    "citric acid": {
        "name": "Citric Acid", "name_ru": "Лимонная кислота",
        "safety_score": 8, "category": "green",
        "function": "Регулятор pH",
        "description": "Регулирует кислотность формулы. В минимальных количествах — полностью безопасна.",
        "cost_per_gram": 0.01, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["лимонная кислота"]
    },
    "edta": {
        "name": "Disodium EDTA", "name_ru": "Динатрий ЭДТА",
        "safety_score": 7, "category": "green",
        "function": "Хелатирующий агент",
        "description": "Связывает ионы металлов, стабилизируя формулу. Безопасен в косметических концентрациях.",
        "cost_per_gram": 0.03, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Вопросы экологии (не разлагается)"],
        "alternatives": ["Phytic Acid"],
        "aliases": ["disodium edta", "tetrasodium edta", "эдта"]
    },
    "bht": {
        "name": "BHT", "name_ru": "Бутилгидрокситолуол",
        "safety_score": 4, "category": "yellow",
        "function": "Антиоксидант (стабилизатор формулы)",
        "description": "Синтетический антиоксидант, защищает формулу от окисления. Спорная безопасность при регулярном контакте.",
        "cost_per_gram": 0.02, "typical_concentration": 0.05,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Потенциальный гормональный разрушитель", "Канцерогенность обсуждается"],
        "alternatives": ["Tocopherol"],
        "aliases": ["butylated hydroxytoluene"]
    },
    "bha preservative": {
        "name": "BHA (preservative)", "name_ru": "Бутилгидроксианизол",
        "safety_score": 3, "category": "red",
        "function": "Антиоксидант (стабилизатор)",
        "description": "Не путать с BHA-кислотой! Это синтетический антиоксидант-консервант с подозрением на канцерогенность.",
        "cost_per_gram": 0.02, "typical_concentration": 0.05,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Потенциальный канцероген", "Гормональный разрушитель"],
        "alternatives": ["Tocopherol"],
        "aliases": ["butylated hydroxyanisole"]
    },
    "triclosan": {
        "name": "Triclosan", "name_ru": "Триклозан",
        "safety_score": 2, "category": "red",
        "function": "Антибактериальный",
        "description": "Антибактериальный агент. Запрещён FDA в мыле с 2017. Нарушает гормональный баланс, создаёт устойчивость бактерий.",
        "cost_per_gram": 0.03, "typical_concentration": 0.3,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Гормональный разрушитель", "Запрещён FDA в мыле", "Устойчивость бактерий"],
        "alternatives": [],
        "aliases": ["триклозан"]
    },
    "hydroquinone": {
        "name": "Hydroquinone", "name_ru": "Гидрохинон",
        "safety_score": 3, "category": "red",
        "function": "Осветлитель",
        "description": "Мощный отбеливатель кожи. Эффективен, но токсичен при длительном использовании. Запрещён в ЕС в косметике.",
        "cost_per_gram": 0.1, "typical_concentration": 2.0,
        "comedogenic_rating": 0, "skin_types": [],
        "concerns": ["Запрещён в ЕС", "Токсичен при длительном использовании", "Может вызвать охроноз"],
        "alternatives": ["Arbutin", "Niacinamide"],
        "aliases": ["гидрохинон"]
    },
    "talc": {
        "name": "Talc", "name_ru": "Тальк",
        "safety_score": 5, "category": "yellow",
        "function": "Абсорбент, наполнитель",
        "description": "Минеральный порошок, поглощает жир. Споры о безопасности из-за возможного загрязнения асбестом.",
        "cost_per_gram": 0.01, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["oily"],
        "concerns": ["Риск загрязнения асбестом", "Споры о канцерогенности", "Судебные иски"],
        "alternatives": ["Silica", "Zinc Oxide"],
        "aliases": ["тальк"]
    },
    "silica": {
        "name": "Silica", "name_ru": "Кремнезём",
        "safety_score": 8, "category": "green",
        "function": "Абсорбент, текстура",
        "description": "Минеральный порошок, поглощает жир. Безопасная альтернатива тальку. Создаёт матовый финиш.",
        "cost_per_gram": 0.02, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["кремнезём", "silicon dioxide"]
    },
    "mica": {
        "name": "Mica", "name_ru": "Слюда",
        "safety_score": 8, "category": "green",
        "function": "Блеск, пигмент",
        "description": "Натуральный минерал, даёт перламутровый блеск. Безопасен для кожи.",
        "cost_per_gram": 0.03, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Этические вопросы добычи (детский труд в некоторых странах)"],
        "alternatives": [],
        "aliases": ["слюда", "ci 77019"]
    },
    "collagen": {
        "name": "Collagen", "name_ru": "Коллаген",
        "safety_score": 8, "category": "green",
        "function": "Увлажнение (поверхностное)",
        "description": "Молекула слишком большая, чтобы проникнуть в кожу. Работает как увлажнитель на поверхности. Маркетинг преувеличивает эффект.",
        "cost_per_gram": 0.3, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Не проникает глубоко — маркетинговый ингредиент"],
        "alternatives": ["Peptides"],
        "aliases": ["коллаген", "hydrolyzed collagen"]
    },
    "snail secretion filtrate": {
        "name": "Snail Secretion Filtrate", "name_ru": "Фильтрат секрета улитки (муцин)",
        "safety_score": 8, "category": "green",
        "function": "Регенерация, увлажнение",
        "description": "Хит корейской косметики. Содержит аллантоин, гликолевую кислоту и коллаген. Реально ускоряет заживление.",
        "cost_per_gram": 0.2, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["snail mucin", "муцин улитки"]
    },
    "salicylate": {
        "name": "Sodium Salicylate", "name_ru": "Салицилат натрия",
        "safety_score": 7, "category": "green",
        "function": "Консервант, кератолитик",
        "description": "Соль салициловой кислоты. Мягкое отшелушивание и консервирующий эффект.",
        "cost_per_gram": 0.04, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Salicylic Acid"],
        "aliases": []
    },
    "bisabolol": {
        "name": "Bisabolol", "name_ru": "Бисаболол",
        "safety_score": 9, "category": "green",
        "function": "Противовоспалительный, успокаивающий",
        "description": "Активный компонент ромашки. Мощное противовоспалительное действие, ускоряет заживление.",
        "cost_per_gram": 0.3, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Centella Asiatica"],
        "aliases": ["alpha-bisabolol", "альфа-бисаболол"]
    },
    "polyglutamic acid": {
        "name": "Polyglutamic Acid", "name_ru": "Полиглутаминовая кислота",
        "safety_score": 9, "category": "green",
        "function": "Супер-увлажнение",
        "description": "Удерживает в 5 раз больше влаги, чем гиалуроновая кислота! Новый хит увлажнения.",
        "cost_per_gram": 1.5, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Hyaluronic Acid"],
        "aliases": ["pga"]
    },
    "adenosine": {
        "name": "Adenosine", "name_ru": "Аденозин",
        "safety_score": 9, "category": "green",
        "function": "Антивозрастной, разглаживание",
        "description": "Разглаживает морщины, ускоряет заживление. Основной антивозрастной ингредиент в корейской косметике.",
        "cost_per_gram": 0.5, "typical_concentration": 0.04,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Peptides"],
        "aliases": ["аденозин"]
    },
    "sodium pca": {
        "name": "Sodium PCA", "name_ru": "PCA натрия",
        "safety_score": 9, "category": "green",
        "function": "Увлажнитель",
        "description": "Натуральный увлажняющий фактор кожи (NMF). Притягивает и удерживает влагу естественным образом.",
        "cost_per_gram": 0.08, "typical_concentration": 2.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Glycerin"],
        "aliases": ["pca"]
    },
    "lecithin": {
        "name": "Lecithin", "name_ru": "Лецитин",
        "safety_score": 9, "category": "green",
        "function": "Эмульгатор, увлажнитель",
        "description": "Натуральный фосфолипид из сои или подсолнечника. Восстанавливает барьер, помогает доставке активов.",
        "cost_per_gram": 0.05, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Аллергия при чувствительности к сое (редко)"],
        "alternatives": [],
        "aliases": ["лецитин", "soy lecithin"]
    },
    "witch hazel": {
        "name": "Hamamelis Virginiana Water", "name_ru": "Гамамелис (ведьмин орех)",
        "safety_score": 6, "category": "yellow",
        "function": "Вяжущее, тонизирующее",
        "description": "Природное вяжущее средство. Сужает поры, уменьшает жирность. Но часто содержит спирт и может сушить.",
        "cost_per_gram": 0.03, "typical_concentration": 10.0,
        "comedogenic_rating": 0, "skin_types": ["oily"],
        "concerns": ["Часто содержит денатурированный спирт", "Может сушить"],
        "alternatives": ["Niacinamide"],
        "aliases": ["witch hazel", "гамамелис"]
    },
    "kojic acid": {
        "name": "Kojic Acid", "name_ru": "Койевая кислота",
        "safety_score": 7, "category": "yellow",
        "function": "Осветление пигментации",
        "description": "Натуральный осветлитель из грибов. Эффективен против пигментации, но может раздражать.",
        "cost_per_gram": 0.3, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["normal", "oily"],
        "concerns": ["Может вызвать раздражение", "Нестабилен"],
        "alternatives": ["Arbutin", "Niacinamide"],
        "aliases": ["койевая кислота"]
    },
    "benzoyl peroxide": {
        "name": "Benzoyl Peroxide", "name_ru": "Бензоилпероксид",
        "safety_score": 6, "category": "yellow",
        "function": "Антибактериальное, от акне",
        "description": "Мощное средство от акне — убивает бактерии. Но сильно сушит и может отбеливать одежду.",
        "cost_per_gram": 0.1, "typical_concentration": 2.5,
        "comedogenic_rating": 0, "skin_types": ["oily"],
        "concerns": ["Сильно сушит", "Отбеливает ткани", "Может шелушиться"],
        "alternatives": ["Salicylic Acid", "Azelaic Acid"],
        "aliases": ["bpo", "бензоилпероксид"]
    },
    "sulfur": {
        "name": "Sulfur", "name_ru": "Сера",
        "safety_score": 7, "category": "green",
        "function": "От акне, подсушивающее",
        "description": "Древнее средство от прыщей. Подсушивает воспаления, убивает бактерии. Имеет характерный запах.",
        "cost_per_gram": 0.02, "typical_concentration": 3.0,
        "comedogenic_rating": 0, "skin_types": ["oily"],
        "concerns": ["Сушит", "Неприятный запах"],
        "alternatives": ["Salicylic Acid"],
        "aliases": ["сера"]
    },
    "retinyl palmitate": {
        "name": "Retinyl Palmitate", "name_ru": "Ретинил пальмитат",
        "safety_score": 7, "category": "green",
        "function": "Мягкая форма витамина A",
        "description": "Самая мягкая форма ретинола. Подходит новичкам. Менее эффективна, но и менее раздражает.",
        "cost_per_gram": 0.5, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Фотосенсибилизатор — обязательно SPF"],
        "alternatives": ["Retinol", "Bakuchiol"],
        "aliases": ["ретинил пальмитат"]
    },
    "ferulic acid": {
        "name": "Ferulic Acid", "name_ru": "Феруловая кислота",
        "safety_score": 9, "category": "green",
        "function": "Антиоксидант, стабилизатор витамина C",
        "description": "Мощный антиоксидант из растений. Стабилизирует и усиливает действие витаминов C и E.",
        "cost_per_gram": 1.0, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": [],
        "aliases": ["феруловая кислота"]
    },
    "resveratrol": {
        "name": "Resveratrol", "name_ru": "Ресвератрол",
        "safety_score": 9, "category": "green",
        "function": "Антиоксидант, антивозрастной",
        "description": "Мощный антиоксидант из красного винограда. Защищает от фотостарения и свободных радикалов.",
        "cost_per_gram": 2.0, "typical_concentration": 0.5,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Green Tea Extract"],
        "aliases": ["ресвератрол"]
    },
    "copper peptide": {
        "name": "Copper Peptide", "name_ru": "Медный пептид (GHK-Cu)",
        "safety_score": 8, "category": "green",
        "function": "Регенерация, антивозрастной",
        "description": "Стимулирует выработку коллагена и эластина, ускоряет регенерацию кожи. Один из самых изученных пептидов.",
        "cost_per_gram": 15.0, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Не сочетается с витамином C и кислотами"],
        "alternatives": ["Peptides"],
        "aliases": ["ghk-cu", "copper tripeptide"]
    },
    "saccharomyces ferment filtrate": {
        "name": "Saccharomyces Ferment Filtrate", "name_ru": "Ферментированный экстракт дрожжей",
        "safety_score": 8, "category": "green",
        "function": "Увлажнение, укрепление барьера",
        "description": "Ферментированные дрожжи — основа легендарных азиатских эссенций. Увлажняет, укрепляет, осветляет.",
        "cost_per_gram": 0.2, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": ["Может не подходить при грибковом акне"],
        "alternatives": [],
        "aliases": ["galactomyces ferment filtrate", "pitera", "ферментированные дрожжи"]
    },
    "cica": {
        "name": "Madecassoside", "name_ru": "Мадекассосид",
        "safety_score": 10, "category": "green",
        "function": "Заживление, от воспалений",
        "description": "Активный компонент центеллы. Мощное заживляющее и противовоспалительное действие.",
        "cost_per_gram": 2.0, "typical_concentration": 0.1,
        "comedogenic_rating": 0, "skin_types": ["all"],
        "concerns": [], "alternatives": ["Centella Asiatica Extract"],
        "aliases": ["madecassic acid", "asiatic acid"]
    },
    "tea tree": {
        "name": "Tea Tree Oil", "name_ru": "Масло чайного дерева",
        "safety_score": 7, "category": "green",
        "function": "Антибактериальное",
        "description": "Натуральный антисептик от акне. Используется в разведённом виде.",
        "cost_per_gram": 0.2, "typical_concentration": 1.0,
        "comedogenic_rating": 0, "skin_types": ["oily", "combination"],
        "concerns": ["Раздражает в чистом виде"],
        "alternatives": ["Salicylic Acid"],
        "aliases": ["melaleuca alternifolia"]
    },
    "vitamin e": {
        "name": "Tocopheryl Acetate", "name_ru": "Витамин E (ацетат)",
        "safety_score": 8, "category": "green",
        "function": "Антиоксидант",
        "description": "Стабильная форма витамина E. Антиоксидант, увлажняет, защищает от фотостарения.",
        "cost_per_gram": 0.1, "typical_concentration": 1.0,
        "comedogenic_rating": 2, "skin_types": ["dry", "normal"],
        "concerns": [], "alternatives": ["Tocopherol"],
        "aliases": ["tocopheryl acetate"]
    },
    "shea": {
        "name": "Butyrospermum Parkii Butter", "name_ru": "Масло ши",
        "safety_score": 9, "category": "green",
        "function": "Питание",
        "description": "Питательное масло ши — богато витаминами, смягчает и защищает кожу.",
        "cost_per_gram": 0.08, "typical_concentration": 5.0,
        "comedogenic_rating": 0, "skin_types": ["dry", "normal"],
        "concerns": [], "alternatives": ["Cocoa Butter"],
        "aliases": ["shea butter", "масло ши"]
    },
    "cocoa butter": {
        "name": "Theobroma Cacao Seed Butter", "name_ru": "Масло какао",
        "safety_score": 8, "category": "green",
        "function": "Питание, смягчение",
        "description": "Богатое шоколадное масло. Питает и смягчает, но довольно тяжёлое. Может забивать поры.",
        "cost_per_gram": 0.06, "typical_concentration": 5.0,
        "comedogenic_rating": 4, "skin_types": ["dry"],
        "concerns": ["Высокая комедогенность"],
        "alternatives": ["Shea Butter", "Mango Butter"],
        "aliases": ["cocoa butter", "какао масло"]
    },
    "beeswax": {
        "name": "Cera Alba", "name_ru": "Пчелиный воск",
        "safety_score": 8, "category": "green",
        "function": "Окклюзив, загуститель",
        "description": "Натуральный воск, создаёт защитную плёнку. Удерживает влагу, загущает формулы.",
        "cost_per_gram": 0.05, "typical_concentration": 3.0,
        "comedogenic_rating": 2, "skin_types": ["dry", "normal"],
        "concerns": ["Не подходит веганам"],
        "alternatives": ["Candelilla Wax"],
        "aliases": ["beeswax", "пчелиный воск"]
    },
}


def find_ingredient(name: str) -> dict | None:
    """Ищет ингредиент по названию или алиасу (без учёта регистра)."""
    name_lower = name.lower().strip()

    # Прямой поиск по ключу
    if name_lower in INGREDIENTS:
        return INGREDIENTS[name_lower]

    # Поиск по aliases
    for key, data in INGREDIENTS.items():
        if name_lower == data["name"].lower():
            return data
        for alias in data.get("aliases", []):
            if name_lower == alias.lower():
                return data

    # Нечёткий поиск — проверяем вхождение
    for key, data in INGREDIENTS.items():
        if name_lower in key or key in name_lower:
            return data
        if name_lower in data["name"].lower() or data["name"].lower() in name_lower:
            return data
        for alias in data.get("aliases", []):
            if name_lower in alias.lower() or alias.lower() in name_lower:
                return data

    return None


def get_all_ingredients() -> dict:
    """Возвращает всю базу ингредиентов."""
    return INGREDIENTS


def get_stats() -> dict:
    """Статистика базы."""
    total = len(INGREDIENTS)
    green = sum(1 for i in INGREDIENTS.values() if i["category"] == "green")
    yellow = sum(1 for i in INGREDIENTS.values() if i["category"] == "yellow")
    red = sum(1 for i in INGREDIENTS.values() if i["category"] == "red")
    return {"total": total, "green": green, "yellow": yellow, "red": red}
