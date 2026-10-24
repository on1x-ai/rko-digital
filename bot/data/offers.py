"""
Партнёрские офферы для бота подбора РКО.
Все ссылки из ТЗ.
"""

OFFERS = {
    # Уже есть ИП/ООО — нужен только счёт
    "tochka": {
        "name": "Точка",
        "url": "https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
        "description": "Лучше для: фриланс, старт, мало операций, онлайн"
    },
    "alpha_rko": {
        "name": "Альфа-Банк (только РКО)",
        "url": "https://go.leadgid.ru/aff_c?aff_id=155793&offer_id=5289&p=adnetwork",
        "description": "Лучше для: агентства, средний+ оборот, «большой банк»"
    },
    "psb_activation": {
        "name": "ПСБ — активация",
        "url": "https://trk.ppdu.ru/click/agjLg6LF?erid=Kra23mn2h",
        "description": ""
    },
    "psb_opening": {
        "name": "ПСБ — открытие р/с",
        "url": "https://go.leadgid.ru/aff_c?aff_id=155793&offer_id=7029&p=adnetwork",
        "description": ""
    },
    "ak_bars": {
        "name": "Ак Барс",
        "url": "https://trk.ppdu.ru/click/DEkn7EXf?erid=2SDnjecx1YU",
        "description": ""
    },
    "bspb": {
        "name": "Банк Санкт-Петербург (БСПБ)",
        "url": "https://trk.ppdu.ru/click/U8RDyGWj?erid=2SDnjeLA2cx",
        "description": ""
    },
    "loko": {
        "name": "Локо-Банк",
        "url": "https://trk.ppdu.ru/click/A9KwCptP?erid=Kra23ute7",
        "description": "Лучше для: совсем маленький оборот / минимум операций"
    },
    
    # Ещё нет ИП/ООО — регистрация + счёт
    "alpha_regbiz": {
        "name": "Альфа — РегБиз + РКО",
        "url": "https://trk.ppdu.ru/click/8FDG8LXT?erid=2SDnjeEA46e",
        "description": ""
    },
    "vtb_regbiz": {
        "name": "ВТБ — РегБиз + РКО",
        "url": "https://trk.ppdu.ru/click/SpRfgWha?erid=Kra23bNL5",
        "description": ""
    }
}

# Маппинг для быстрого доступа по ключам логики рекомендаций
OFFER_KEYS = {
    "tochka": "tochka",
    "alpha_rko": "alpha_rko",
    "loko": "loko",
    "ak_bars": "ak_bars",
    "bspb": "bspb",
    "alpha_regbiz": "alpha_regbiz",
    "vtb_regbiz": "vtb_regbiz"
}