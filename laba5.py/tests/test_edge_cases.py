import pytest
from num_series.moving_average import simple_moving_average

class TestEdgeCasesVariant6:
    def test_sma_window_bigger_than_data_returns_empty(self):
        data = [1.0, 2.0, 3.0]
        with pytest.raises(ValueError, match="Размер окна не может превышать"):
            simple_moving_average(data, window=5)