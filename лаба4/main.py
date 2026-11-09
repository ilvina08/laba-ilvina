from __future__ import annotations

from menu import choose_type, print_result
from validation import input_massa


def main() -> None:
    """Главная функция программы."""
    print('Меню')
    print('бетон')
    print('керамика')
    print('сплав')

    
    tip = choose_type()
    
    
    mass = input_massa()
    
    
    print("\n--- Результат ---")
    print_result(tip, mass)


if __name__ == "__main__":
    main()
