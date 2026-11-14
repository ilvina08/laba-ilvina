from typing import List,Sequence

def check_window(window:int,n:int)->None:
    if not isinstance(window,int) or window<1:
        raise ValueError(f"window должно быть целым >=1(получено:{window!r})")
    if window>n:
        raise ValueError(f"window({window}) не может быть больше длины ряда({n})")
def simple_moving_average(data:Sequence[float],window:int)->List[float]:
    if not data:
        raise ValueError("Ряд пуст:расчет SMA невозможен")
    check_window(window,len(data))
    running=sum(data[:window])
    result=[running/window]
    for i in range(window,len(data)):
        running+=data[i]-data[i-window]
        result.append(running/window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное MA. Окно должно быть нечётным."""
    if not data:
        raise ValueError("Ряд пуст: расчёт MA невозможен")
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError("Для центрированного MA окно должно быть нечётным")
    half = window // 2  
    result = []
    for i in range(half, len(data) - half):
        window_slice = data[i - half : i + half + 1]
        result.append(sum(window_slice) / window)
        
    return result

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: EMA[0] = data[0]; EMA[i] = alpha*data[i] + (1-alpha)*EMA[i-1]."""
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    if not (0 < alpha <= 1):
        raise ValueError(f"alpha должна быть в (0, 1] (получено: {alpha})")
    result = [float(data[0])]
    for i in range(1, len(data)):
        ema_value = alpha * data[i] + (1 - alpha) * result[-1]
        result.append(ema_value)
        
    return result
    