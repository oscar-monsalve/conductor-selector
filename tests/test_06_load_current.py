from conductor_selector.helpers import load_current


def test_load_current_single_phase_result():
    POWER_SYSTEM_TYPE_SINGLE_PHASE = 1
    APPARENT_POWER = 2000
    VOLTAGE_LEVEL = 220
    assert load_current(POWER_SYSTEM_TYPE_SINGLE_PHASE, APPARENT_POWER, VOLTAGE_LEVEL) == 9.090909090909092


def test_load_current_two_phase_result():
    POWER_SYSTEM_TYPE_TWO_PHASE = 2
    APPARENT_POWER = 2000
    VOLTAGE_LEVEL = 220
    assert load_current(POWER_SYSTEM_TYPE_TWO_PHASE, APPARENT_POWER, VOLTAGE_LEVEL) == 9.090909090909092


def test_load_current_three_phase_result():
    POWER_SYSTEM_TYPE_THREE_PHASE = 3
    APPARENT_POWER = 2000
    VOLTAGE_LEVEL = 220
    assert load_current(POWER_SYSTEM_TYPE_THREE_PHASE, APPARENT_POWER, VOLTAGE_LEVEL) == 5.24863881081478
