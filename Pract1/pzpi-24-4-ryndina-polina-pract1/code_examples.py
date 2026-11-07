import os
import sys
import time
from typing import List, Optional


# В.1 ЕТАЛОННИЙ ПРИКЛАД ОФОРМЛЕННЯ КОДУ (PEP 8)
def calculate_shipping_cost(weight_kg: float, distance_km: float) -> float:
    """Обчислює вартість доставки товару на основі ваги та відстані."""
    if weight_kg <= 0 or distance_km <= 0:
        raise ValueError("Вага та відстань повинні бути більшими за нуль.")
    base_rate = 50.0
    return base_rate + (weight_kg * 12.5) + (distance_km * 3.0)


# В.2 ПРИКЛАД ПРОГРАМНОГО КОДУ ДО РЕФАКТОРИНҐУ
def calc(w, d):
    c = 50  # base cost
    if w > 10:
        c = c + w * 15
    else:
        c = c + w * 10
    if d > 100:
        c = c + d * 4
    else:
        c = c + d * 2
    return c


# В.3 ПРИКЛАД ПРОГРАМНОГО КОДУ ПІСЛЯ РЕФАКТОРИНҐУ
BASE_DELIVERY_FEE: float = 50.0
HEAVY_WEIGHT_THRESHOLD_KG: float = 10.0
LONG_DISTANCE_THRESHOLD_KM: float = 100.0

HIGH_WEIGHT_RATE: float = 15.0
STANDARD_WEIGHT_RATE: float = 10.0
LONG_DISTANCE_RATE: float = 4.0
STANDARD_DISTANCE_RATE: float = 2.0


def compute_delivery_price(weight_kg: float, distance_km: float) -> float:
    """Обчислює підсумкову вартість доставки з урахуванням констант тарифів."""
    if weight_kg <= 0 or distance_km <= 0:
        raise ValueError("Параметри ваги та відстані мають бути додатними.")

    weight_rate = (
        HIGH_WEIGHT_RATE
        if weight_kg > HEAVY_WEIGHT_THRESHOLD_KG
        else STANDARD_WEIGHT_RATE
    )
    distance_rate = (
        LONG_DISTANCE_RATE
        if distance_km > LONG_DISTANCE_THRESHOLD_KM
        else STANDARD_DISTANCE_RATE
    )

    return BASE_DELIVERY_FEE + (weight_kg * weight_rate) + (distance_km * distance_rate)


# В.4 СТРУКТУРА ІМПОРТІВ ТА МОДУЛІВ
class UserSession:
    def __init__(self, user_id: int, token: str) -> None:
        self.user_id = user_id
        self.token = token


# В.5 ІМЕНУВАННЯ ТА КОНСТАНТИ
MAX_LOGIN_ATTEMPTS: int = 3


class SecurityGuard:
    def __init__(self, failed_attempts: int) -> None:
        self._failed_attempts = failed_attempts

    @property
    def is_blocked(self) -> bool:
        return self._failed_attempts >= MAX_LOGIN_ATTEMPTS


# В.6 КОМЕНТАР ПРО ПРИЧИНУ, А НЕ ПРО ДІЮ
class DatabaseConnector:
    def __init__(self) -> None:
        self.connected = False

    def connect((self) -> None:
        # Неправильно: connect to db
        # self.connected = True

        # Правильно: сервер бази даних потребує паузи в 500мс між запитами
        # через обмеження пулу з'єднань на хостингу.
        time.sleep(0.5)
        self.connected = True


# В.7 DOCSTRINGS (ДОКУМЕНТУВАННЯ МЕТОДУ ЗА GOOGLE STYLE)
def evaluate_average_score(scores: List[float]) -> float:
    """Обчислює середній балл студентської групи.

    Args:
        scores (List[float]): Список балів студентів.

    Returns:
        float: Середнє арифметичне значення.

    Raises:
        ValueError: Якщо список балів порожній.
    """
    if not scores:
        raise ValueError("Список оцінок не може бути порожнім.")
    return sum(scores) / len(scores)


# В.8 НАЛАШТУВАННЯ ТУЛІНГУ (.pyproject.toml)
# [tool.black]
# line-length = 88
# target-version = ['py310']
# [tool.flake8]
# max-line-length = 88


# В.9 МОДУЛЬНЕ ТЕСТУВАННЯ З PYTEST (ARRANGE-ACT-ASSERT)
def test_evaluate_average_score_valid_list():
    # Arrange (Підготовка даних)
    test_scores = [90.0, 80.0, 100.0]

    # Act (Виконання дії)
    result = evaluate_average_score(test_scores)

    # Assert (Перевірка результату)
    assert result == 90.0


# В.10 АВТОМАТИЗАЦІЯ ПЕРЕВІРОК У КОМАНДНОМУ РЯДКУ
# black code_examples.py
# flake8 --max-line-length=88 code_examples.py


# В.11 ШОВ ТА ЗАЛЕЖНОСТІ ДЛЯ ТЕСТУВАННЯ (MOCK/INTERFACE)
class NotificationService:
    def is_service_available(self) -> bool:
        return True


def send_user_alert(user_email: str, notifier: NotificationService) -> bool:
    if notifier.is_service_available():
        # Надсилання сповіщення
        return True
    return False


# В.12 КОНФІГУРАЦІЯ LINTING/TYPING ПІД ЧАС ЗБІРКИ
# mypy --strict code_examples.py


# В.13 ПАРАМЕТРИЗОВАНИЙ ТЕСТ В PYTEST
# @pytest.mark.parametrize("scores, expected", [([10, 20], 15.0), ([100], 100.0)])
# def test_average_parametrized(scores, expected):
#     assert evaluate_average_score(scores) == expected
