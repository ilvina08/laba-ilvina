import time 
from collections import deque 
from typing import List, Sequence 
from typing import Sequence


def check_window(window: int, n: int) -> None:
    """Window — целое >= 1; window <= n (иначе окно больше ряда)."""
    if window < 1:
        raise ValueError("Размер окна должен быть целым числом >= 1")
    if window > n:
        raise ValueError("Размер окна не может превышать длину ряда")


def simple_moving_average(data: Sequence[float], window: int) -> list:
    """SMA через бегущую сумму, O(n). Длина результата: len(data) - window + 1."""
    if len(data) == 0:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    check_window(window, len(data))

    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result


def centered_moving_average(data: Sequence[float], window: int) -> list:
    """Центрированная скользящая средняя: окно нечётное, выход выровнен по центру."""
    if len(data) == 0:
        raise ValueError("Ряд пуст: расчёт центрированной скользящей средней невозможен")
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError("Окно должно быть нечётным")

    half = window // 2
    return [
        sum(data[i - half:i + half + 1]) / window
        for i in range(half, len(data) - half)
    ]


def exponential_moving_average(data: Sequence[float], alpha: float) -> list:
    """EMA: EMA[0] = data[0]; EMA[i] = alpha * data[i] + (1 - alpha) * EMA[i-1]."""
    if len(data) == 0:
        raise ValueError("Ряд пуст: расчёт экспоненциальной скользящей средней невозможен")
    if not (0 < alpha <= 1):
        raise ValueError("Коэффициент alpha должен быть в диапазоне (0, 1]")

    result = [float(data[0])]
    for x in data[1:]:
        result.append(alpha * x + (1 - alpha) * result[-1])
    return result

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:
    """SMA с использованием deque (двусторонней очереди)"""
    check_window(window, len(data))
    result = []
    d = deque()
    running_sum = 0.0
    for x in data:
        d.append(x)
        running_sum += x
        if len(d) > window:
                 running_sum -= d.popleft()
        if len(d) == window:
            result.append(running_sum / window)
    return result
def benchmark_moving_average(data: Sequence[float], window: int, repeats: int = 1000) -> dict:
    """
    Замеряет среднее время выполнения SMA для реализаций на list и deque.
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах).
    """
    # Проверка корректности окна (выбросит ValueError при необходимости)
    check_window(window, len(data))

    # Замер для list-реализации (существующая simple_moving_average)
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average(data, window)
    t_list = (time.perf_counter() - t0) / repeats

    # Замер для deque-реализации
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average_deque(data, window)
    t_deque = (time.perf_counter() - t0) / repeats

    return {"list": t_list, "deque": t_deque}
