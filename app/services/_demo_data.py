"""Демо-данные для экранов, пока сервисы — заглушки.

# DEMO — все ФИО и контакты вымышленные.
"""

from __future__ import annotations

from datetime import date, timedelta

DEMO_ATHLETES = [
    {"id": 1, "full_name": "Северный Артём Тестович", "disciplines": "Алгоритмическое программирование", "rank": "1 юношеский", "email": "artem.demo@example.test"},
    {"id": 2, "full_name": "Заозёрная Мария Учебная", "disciplines": "Робототехника", "rank": "КМС", "email": "maria.demo@example.test"},
    {"id": 3, "full_name": "Приречный Илья Примерный", "disciplines": "Продуктовое программирование", "rank": "2 взрослый", "email": "ilya.demo@example.test"},
    {"id": 4, "full_name": "Волкова Нина Макетная", "disciplines": "Информационная безопасность", "rank": "1 взрослый", "email": "nina.demo@example.test"},
    {"id": 5, "full_name": "Камский Олег Стендовый", "disciplines": "Программирование БАС", "rank": "Без разряда", "email": "oleg.demo@example.test"},
    {"id": 6, "full_name": "Луговая Софья Фиктивная", "disciplines": "Алгоритмическое программирование", "rank": "3 юношеский", "email": "sofia.demo@example.test"},
    {"id": 7, "full_name": "Борский Павел Условный", "disciplines": "Продуктовое программирование", "rank": "2 юношеский", "email": "pavel.demo@example.test"},
    {"id": 8, "full_name": "Речная Дарья Модельная", "disciplines": "Робототехника", "rank": "3 взрослый", "email": "daria.demo@example.test"},
]

DEMO_COMPETITIONS = [
    {"id": 101, "name": "Кубок Северного округа", "discipline": "Алгоритмическое программирование", "event_date": "12.03.2026", "city": "Северск", "status": "finished"},
    {"id": 102, "name": "Хакатон Приречья", "discipline": "Продуктовое программирование", "event_date": "05.04.2026", "city": "Приреченск", "status": "planned"},
    {"id": 103, "name": "Робото-спринт", "discipline": "Робототехника", "event_date": "18.02.2026", "city": "Заозёрск", "status": "finished"},
    {"id": 104, "name": "Старт БАС", "discipline": "Программирование БАС", "event_date": "22.05.2026", "city": "Северск", "status": "planned"},
    {"id": 105, "name": "CTF Учебный", "discipline": "Информационная безопасность", "event_date": "01.03.2026", "city": "Приреченск", "status": "running"},
    {"id": 106, "name": "Осенний контест", "discipline": "Алгоритмическое программирование", "event_date": "10.10.2025", "city": "Северск", "status": "cancelled"},
]

DEMO_RESULTS = [
    {"id": 1, "competition": "Кубок Северного округа", "athlete": "Северный Артём Тестович", "discipline": "Алгоритмическое программирование", "r_n": 91.25, "place": 1, "year": 2026},
    {"id": 2, "competition": "Кубок Северного округа", "athlete": "Луговая Софья Фиктивная", "discipline": "Алгоритмическое программирование", "r_n": 80.00, "place": 2, "year": 2026},
    {"id": 3, "competition": "Робото-спринт", "athlete": "Заозёрная Мария Учебная", "discipline": "Робототехника", "r_n": 88.50, "place": 1, "year": 2026},
    {"id": 4, "competition": "CTF Учебный", "athlete": "Волкова Нина Макетная", "discipline": "Информационная безопасность", "r_n": 76.00, "place": 3, "year": 2026},
    {"id": 5, "competition": "Хакатон Приречья", "athlete": "Приречный Илья Примерный", "discipline": "Продуктовое программирование", "r_n": 70.10, "place": 2, "year": 2026},
    {"id": 6, "competition": "Осенний контест", "athlete": "Борский Павел Условный", "discipline": "Алгоритмическое программирование", "r_n": 65.00, "place": 4, "year": 2025},
]

DEMO_USERS = [
    {"full_name": "Системный администратор", "role": "admin", "region": "Северный учебный округ", "email": "admin@example.test", "status": "active"},
    {"full_name": "Тренер Северный Иван Макетный", "role": "trainer", "region": "Северный учебный округ", "email": "trainer.north@example.test", "status": "active"},
    {"full_name": "Северный Артём Тестович", "role": "athlete", "region": "Северный учебный округ", "email": "artem.demo@example.test", "status": "active"},
    {"full_name": "Заозёрная Мария Учебная", "role": "athlete", "region": "Заозёрная область", "email": "maria.demo@example.test", "status": "pending"},
    {"full_name": "Приречный Илья Примерный", "role": "athlete", "region": "Приречный край", "email": "ilya.demo@example.test", "status": "blocked"},
]

DEMO_AUDIT = [
    {"created_at": "15.03.2026 10:11", "action": "LOGIN", "entity": "users", "entity_id": "1", "details": "успешный вход"},
    {"created_at": "16.03.2026 12:40", "action": "CREATE_TRAINER", "entity": "users", "entity_id": "2", "details": "создан тренер"},
    {"created_at": "18.03.2026 09:05", "action": "BLOCK_USER", "entity": "users", "entity_id": "5", "details": "блокировка"},
]

DEMO_HOME = {
    "athletes_count": 8,
    "about": "Учебный контур учёта статистики спортсменов региональной федерации спортивного программирования.",
    "year": date.today().year,
}

DEMO_RATING = [
    {"place": 1, "full_name": "Заозёрная Мария Учебная", "r_n_avg": 88.50, "starts": 4},
    {"place": 2, "full_name": "Северный Артём Тестович", "r_n_avg": 85.10, "starts": 5},
    {"place": 3, "full_name": "Волкова Нина Макетная", "r_n_avg": 76.00, "starts": 3},
    {"place": 4, "full_name": "Приречный Илья Примерный", "r_n_avg": 70.10, "starts": 2},
    {"place": 5, "full_name": "Луговая Софья Фиктивная", "r_n_avg": 68.40, "starts": 4},
]
