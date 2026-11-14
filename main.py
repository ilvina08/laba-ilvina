import argparse
import sys
from typing import List

from num_series import (
    random_series, sine_series, trend_series, summarize,
    simple_moving_average, centered_moving_average, exponential_moving_average,
)

def build_series(kind: str, n: int, seed: int) -> List[float]:
    """Фабрика для генерации ряда в зависимости от типа."""
    if kind == "random":
        return random_series(n, low=-50, high=50, seed=seed)
    if kind == "sine":
        return sine_series(n, amplitude=10, frequency=2, noise=1.5, seed=seed)
    if kind == "trend":
        return trend_series(n, start=0, step=1.0, noise=0.5, seed=seed)
    raise ValueError(f"Неизвестный тип ряда: {kind!r}")

def print_series(title: str, values: List[float]) -> None:
    """Печатает ряд в одну строку с выравниванием."""
    print(f"\n{title} (n={len(values)}):")
    print(" " + " ".join(f"{v:>10.3f}" for v in values))

def main(argv: List[str] | None = None) -> int:
    """Точка входа. Возвращает код выхода (0 — успех, 1 — ошибка)."""
    parser = argparse.ArgumentParser(
        description="Алгоритмическая обработка числовых рядов",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--kind", choices=["random", "sine", "trend"], default="sine", help="тип генерируемого ряда")
    parser.add_argument("--n", type=int, default=20, help="количество точек в ряде")
    parser.add_argument("--window", type=int, default=3, help="размер окна для скользящей средней")
    parser.add_argument("--alpha", type=float, default=0.3, help="коэффициент сглаживания для EMA, 0 < alpha <= 1")
    parser.add_argument("--seed", type=int, default=42, help="зерно ГПСЧ для воспроизводимости")
    
    args = parser.parse_args(argv)

    try:
        data = build_series(args.kind, args.n, args.seed)
        stats = summarize(data)
        sma = simple_moving_average(data, args.window)
        ema = exponential_moving_average(data, args.alpha)
        cma = centered_moving_average(data, args.window) if args.window % 2 == 1 else None
        
    except ValueError as err:
        print(f"Ошибка: {err}", file=sys.stderr)
        return 1

    print("=" * 60)
    print(f"Тип ряда: {args.kind}, n = {args.n}")
    print("-" * 60)
    
    print(f"Среднее арифметическое : {stats['mean']:>10.4f}")
    print(f"Медиана                : {stats['median']:>10.4f}")
    print(f"Размах (max - min)     : {stats['spread']:>10.4f}")
    print(f"min / max              : {stats['min']:>10.4f} / {stats['max']:>10.4f}")
    
    print_series("Исходный ряд", data)
    print_series(f"SMA (window={args.window})", sma)
    print_series(f"EMA (alpha={args.alpha})", ema)
    
    if cma is not None:
        print_series(f"Центрированное MA (window={args.window})", cma)
    else:
        print(f"\n[!] Центрированное MA не рассчитано (окно {args.window} — четное)")
        
    print("=" * 60)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())