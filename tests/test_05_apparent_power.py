from conductor_selector.helpers import apparent_power


def test_apparent_power_result():
    assert apparent_power(1500, 1) == 1500
    assert apparent_power(1500, 0.9) == 1666.6666666666665


def test_apparent_power_return_value():
    assert isinstance(apparent_power(1500, 0.9), float)
