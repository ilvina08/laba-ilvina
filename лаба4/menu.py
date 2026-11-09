

from __future__ import annotations

from connstans import beton_1,beton_2,beton_3,keramika_1,keramika_2,keramika_3,splav_1,splav_2,splav_3
from validation import input_massa
from operations import get_category, check_sum

def choose_type() -> str:
    """Запрашивает тип смеси, пока не будет введен корректный."""
    while True:
        tip = input("Тип смеси: ")
        if tip=="бетон" or tip=="керамика" or tip=="сплав":
            return tip
        print("Ошибка: введите бетон, керамика или сплав")

def print_result(tip: str, mass: float) -> None:
    """Выполняет расчёт и выводит результат на экран."""

    if tip == 'бетон':
        d1, d2, d3 = beton_1, beton_2, beton_3
        names = ["цемент", "песок", "щебень"]
    elif tip == 'керамика':
        d1, d2, d3 = keramika_1, keramika_2, keramika_3
        names = ["глина", "песок", "щебень"]
    else: # сплав
        d1, d2, d3 = splav_1, splav_2, splav_3
        names = ["Cu", "Zn", "Pb"]

    m1 = round(mass * d1, 2)
    m2 = round(mass * d2, 2)
    m3 = round(mass * d3, 2)

    print(f"{names[0]} {m1} кг")
    print(f"{names[1]} {m2} кг")
    print(f"{names[2]} {m3} кг")

    print(get_category(mass))

    if check_sum(d1, d2, d3):
        print("Сумма долей равна 1")
    else:
        print("Сумма долей не равна 1")

if __name__ == "__main__":
    print("Меню")
    print("бетон")
    print("керамика")
    print("сплав")  

    user_tip = choose_type()
    user_mass = input_massa()
    print("\n--- Результат ---")
    print_result(user_tip, user_mass)
