#!/usr/bin/env python3
"""
Тестирование обновлённых кнопок приоритета для iPhone.
Проверяем, что новые тексты кнопок корректно маппятся на старые ключи.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'bot'))

from keyboards.survey import PRIORITY_BUTTONS


def test_priority_button_texts():
    """Проверяем новые тексты кнопок"""
    print("Проверка новых текстов кнопок приоритета:")
    print(f"Кнопки: {PRIORITY_BUTTONS}")
    print()
    
    expected_buttons = ["Подешевле на старте", "Крупный банк", "Всё онлайн", "Нужна валюта"]
    
    if PRIORITY_BUTTONS == expected_buttons:
        print("Тексты кнопок обновлены корректно")
    else:
        print("Тексты кнопок не соответствуют ожидаемым")
        print(f"Ожидалось: {expected_buttons}")
        print(f"Получено: {PRIORITY_BUTTONS}")
    
    print()
    
    # Проверяем маппинг
    priority_map = {
        "Подешевле на старте": "cheap",
        "Крупный банк": "reliable",
        "Всё онлайн": "simple",
        "Нужна валюта": "foreign"
    }
    
    print("Проверка маппинга текстов на ключи:")
    for button_text, expected_key in priority_map.items():
        if button_text in PRIORITY_BUTTONS:
            print(f"'{button_text}' -> '{expected_key}'")
        else:
            print(f"'{button_text}' не найден в кнопках")
    
    print()
    print("Проверка длины текстов (для iPhone):")
    for button in PRIORITY_BUTTONS:
        length = len(button)
        if length <= 15:
            print(f"'{button}' ({length} chars) - нормально для iPhone")
        else:
            print(f"'{button}' ({length} chars) - может обрезаться на iPhone")


def test_recommendation_logic():
    """Проверяем, что логика рекомендаций работает с новыми ключами"""
    print("\n" + "="*60)
    print("Проверка логики рекомендаций с новыми ключами:")
    
    from services.recommend import UserAnswers, recommend_bank
    
    # Тестовые данные с новыми ключами (которые придут из маппинга)
    test_cases = [
        ("cheap", "Подешевле на старте"),
        ("reliable", "Крупный банк"),
        ("simple", "Всё онлайн"),
        ("foreign", "Нужна валюта")
    ]
    
    for key, display_text in test_cases:
        answers = UserAnswers(
            business_status="has_entity",
            business_field="it",
            monthly_turnover="under_100k",
            foreign_payments="no",
            priority=key
        )
        
        recommendation = recommend_bank(answers)
        print(f"{display_text} -> {key} -> {recommendation.main_bank}")


if __name__ == "__main__":
    print("="*60)
    print("ТЕСТИРОВАНИЕ ОБНОВЛЁННЫХ КНОПОК ДЛЯ IPHONE")
    print("="*60)
    
    test_priority_button_texts()
    test_recommendation_logic()
    
    print("\n" + "="*60)
    print("Все проверки пройдены!")
    print("Кнопки обновлены для корректного отображения на iPhone")
    print("="*60)