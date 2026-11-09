from __future__ import annotations
import math

def get_category(mass: float) -> str:
    if mass < 100:
        return "Малая партия"
    elif mass <= 1000:
        return "Средняя партия"
    else:
        return "Крупная партия"

def check_sum(d1: float, d2: float, d3: float) -> bool:
    return math.isclose(d1 + d2 + d3, 1.0)
