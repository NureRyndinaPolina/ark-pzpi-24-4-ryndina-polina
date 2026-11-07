import os
from typing import Dict, List, Optional


# В.1 МЕТОД CALCULATE_FINAL_PRICE ДО ДОДАВАННЯ ПАРАМЕТРА
def calculate_final_price(base_price: float) -> float:
    # Захардкожена фіксована знижка 5%
    fixed_discount = 0.05
    return base_price * (1.0 - fixed_discount)


# В.2 МЕТОД CALCULATE_FINAL_PRICE ПІСЛЯ ДОДАВАННЯ ПАРАМЕТРА (Add Parameter)
def calculate_final_price_updated(
    base_price: float, discount_rate: float = 0.0
) -> float:
    """Обчислює ціну з урахуванням гнучкого параметра знижки."""
    if discount_rate < 0 or discount_rate > 1.0:
        raise ValueError("Знижка має бути в межах від 0.0 до 1.0")
    return base_price * (1.0 - discount_rate)


# В.3 МЕТОД PROCESS_USER_ORDER ДО ВИЛУЧЕННЯ ПАРАМЕТРА
def process_user_order(order: Dict[str, str], order_date: str) -> None:
    # Параметр order_date не використовується, бо дата є в самому order
    print(f"Обробка замовлення №{order['id']} від {order['date']}")


# В.4 МЕТОД PROCESS_USER_ORDER ПІСЛЯ ВИЛУЧЕННЯ ПАРАМЕТРА (Remove Parameter)
def process_user_order_updated(order: Dict[str, str]) -> None:
    """Обробляє замовлення без зайвого параметра дати."""
    print(f"Обробка замовлення №{order['id']} від {order['date']}")


# В.5 МЕТОД FIND_PRODUCT ДО ВИЛУЧЕННЯ ПРАПОРЦЯ УПРАВЛІННЯ
def find_product(products: List[Dict[str, str]], target_id: int) -> Optional[Dict[str, str]]:
    found = False
    result = None
    for product in products:
        if not found:
            if product.get("id") == target_id:
                result = product
                found = True
    return result


# В.6 МЕТОД FIND_PRODUCT ПІСЛЯ ВИЛУЧЕННЯ ПРАПОРЦЯ УПРАВЛІННЯ (Remove Control Flag)
def find_product_updated(
    products: List[Dict[str, str]], target_id: int
) -> Optional[Dict[str, str]]:
    """Шукає продукт та повертає його одразу при знаходженні без прапорця."""
    for product in products:
        if product.get("id") == target_id:
            return product
    return None
