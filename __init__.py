"""Пакет алгоритмической обработки числовых рядов."""
from .generator import random_series, sine_series, trend_series,stock_price_series
from .stats import mean, median, spread, summarize,max_drawdown
from .moving_average import (
    simple_moving_average,
    simple_moving_average_deque, 
    centered_moving_average,
    exponential_moving_average,
    benchmark_moving_average,
)     
from .deque_average import (     
    simple_moving_average_deque as sma_deque_alt,
    centered_moving_average_deque,
    exponential_moving_average_deque,
)
from .io_json import save_series_json, load_series_json
from .io_file import load_series_auto

__all__ = [
    # генерация
    "random_series", "sine_series", "trend_series",
    # статистика
    "mean", "median", "spread", "summarize",
    # скользящие средние (старые)
    "simple_moving_average",
    "centered_moving_average",
    "exponential_moving_average",
    # скользящие средние (НОВЫЕ)
    "simple_moving_average_deque",
    "sma_deque_alt",
    "centered_moving_average_deque",
    "exponential_moving_average_deque",
    "benchmark_moving_average",
    # ввод/вывод
    "save_series_json", "load_series_json", "load_series_auto",
    "stock_price_series",
    "max_drawndown"
]

__version__ = "1.0.0"
