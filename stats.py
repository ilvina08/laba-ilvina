from typing import Dict, Sequence
import json
from pathlib import Path
from typing import Any, Union
import math 



def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")


def mean(data: Sequence[float]) -> float:
    """Среднее арифметическое."""
    _ensure_not_empty(data)
    return sum(data) / len(data)


def median(data: Sequence[float]) -> float:
    """Медиана (устойчива к выбросам)."""
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0


def spread(data: Sequence[float]) -> float:
    """Размах ряда: max - min."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))

PathLike = Union[str, Path]

def save_to_json(data: dict, path: PathLike) -> None:
    """Сохраняет словарь в JSON-файл с корректным кодированием и отступами."""
    path = Path(path)
    # Гарантируем существование папки (создаст output/, если нет)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
def variance(data: Sequence[float]) -> float:
    """Выборочная дисперсия (несмещённая, делим на n - 1)."""
    n = len(data)
    if n < 2:
        raise ValueError("Для дисперсии нужно минимум 2 значения")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (n - 1)

def stdev(data: Sequence[float]) -> float:
    """Выборочное СКО — корень из выборочной дисперсии."""
    return math.sqrt(variance(data))
def summarize(data):
    return {
        "mean": mean(data),
        "median": median(data),
        "count":len(data),
        "spread":spread(data),
        "min":min(data),
        "max":max(data)
    }
def max_drawdown(data: Sequence[float]) -> float:
    """Максимальная просадка: максимальное падение от локального максимума к минимуму."""
    _ensure_not_empty(data)  # ваша функция проверки на пустоту
    max_so_far = data[0]
    max_dd = 0.0
    
    for x in data:
        if x > max_so_far:
            max_so_far = x
        dd = max_so_far - x
        if dd > max_dd:
            max_dd = dd
            
    return float(max_dd)
