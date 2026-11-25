"""Точка входа для Варианта 6 (акции)."""
from __future__ import annotations
import argparse
import sys
import csv
from typing import List, Optional, Tuple

from num_series import (
    random_series, sine_series, trend_series, stock_price_series,
    summarize, max_drawdown,
    simple_moving_average, centered_moving_average, exponential_moving_average,
    benchmark_moving_average,
    save_series_json,
)
from num_series.io_file import load_series_auto

def build_series(kind: str, n: int, seed: int) -> List[float]:
    if kind == "random": return random_series(n, low=-50, high=50, seed=seed)
    if kind == "sine": return sine_series(n, amplitude=10, frequency=2, noise=1.5, seed=seed)
    if kind == "trend": return trend_series(n, start=0, step=1.0, noise=0.5, seed=seed)
    if kind == "stock": return stock_price_series(n, start_price=100.0, seed=seed)
    raise ValueError(f"Неизвестный тип: {kind}")

def obtain_series(args: argparse.Namespace) -> Tuple[List[float], str]:
    if args.load:
        return load_series_auto(args.load), f"файл: {args.load}"
    return build_series(args.kind, args.n, args.seed), f"сгенерирован ({args.kind}, n={args.n})"

def export_series_csv(path: str, data: List[float], sma: List[float], ema: List[float]) -> None:
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["i", "value", "sma", "ema"])
            for i in range(len(data)):
                sma_val = sma[i] if i < len(sma) else ""
                ema_val = ema[i] if i < len(ema) else ""
                w.writerow([i, data[i], sma_val, ema_val])
    except OSError as err:
        raise ValueError(f"Ошибка записи CSV: {err}") from err

def print_series(title: str, values: List[float], fmt: str = "{:>10.3f}") -> None:
    if not values:
        print(f"\n{title}: [пусто]")
        return
    print(f"\n{title} (n={len(values)}):")
    print(" " + " ".join(fmt.format(v) for v in values))

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Обработка рядов")
    parser.add_argument("--kind", choices=["random", "sine", "trend", "stock"], default="stock")
    parser.add_argument("--n", type=int, default=800)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--load", metavar="PATH")
    parser.add_argument("--save", metavar="PATH")
    parser.add_argument("--export", metavar="FILE")
    parser.add_argument("--window", type=int, default=10)
    parser.add_argument("--alpha", type=float, default=0.3)
    parser.add_argument("--benchmark", action="store_true")
    return parser

def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        data, source = obtain_series(args)
    except ValueError as err:
        print(f"Ошибка получения: {err}", file=sys.stderr)
        return 1

    if args.save:
        try:
            save_series_json(data, args.save, meta={"source": source})
            print(f"[сохранено] {args.save}")
        except ValueError as err:
            print(f"Ошибка сохранения: {err}", file=sys.stderr)
            return 1

    try:
        stats = summarize(data)
        if args.window > len(data):
            print(f"\n[ВНИМАНИЕ] Окно ({args.window}) больше ряда ({len(data)}). SMA/EMA пусты.")
            sma, ema, cma = [], [], []
        else:
            sma = simple_moving_average(data, args.window)
            ema = exponential_moving_average(data, args.alpha)
            cma = centered_moving_average(data, args.window) if args.window % 2 == 1 else None
    except ValueError as err:
        print(f"Ошибка анализа: {err}", file=sys.stderr)
        return 1

    if args.export:
        try:
            export_series_csv(args.export, data, sma, ema)
            print(f"[экспортировано] {args.export}")
        except ValueError as err:
            print(f"Ошибка экспорта: {err}", file=sys.stderr)
            return 1
    print("=" * 60)
    print(f"Источник: {source}")
    print(f"Среднее: {stats['mean']:.4f}, Медиана: {stats['median']:.4f}")
    
    if args.kind == "stock":
        print(f"Максимальная просадка: {max_drawdown(data):.4f}")
        
    print_series("Исходный ряд", data)
    if sma:
        print_series(f"SMA ({args.window})", sma)
        print_series(f"EMA ({args.alpha})", ema)
        if cma is not None:
            print_series(f"Центр. MA ({args.window})", cma)

    if args.benchmark and sma:
        print("-" * 60)
        print("Замер времени (1000 повторов):")
        t = benchmark_moving_average(data, args.window, repeats=1000)
        print(f" list : {t['list']:.8f} c")
        print(f" deque: {t['deque']:.8f} c")

    print("=" * 60)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
