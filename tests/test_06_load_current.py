from conductor_selector.helpers import load_current


def test_load_current_single_two_phase_result():
    APPARENT_POWER = 2000
    VOLTAGE_LEVEL = 220
    power_system_type_single_two_phase = [1, 2]

    for i in power_system_type_single_two_phase:
        assert load_current(i, APPARENT_POWER, VOLTAGE_LEVEL) == 9.090909090909092


def test_load_current_three_phase_result():
    POWER_SYSTEM_TYPE_THREE_PHASE = 3
    APPARENT_POWER = 2000
    VOLTAGE_LEVEL = 220
    assert load_current(POWER_SYSTEM_TYPE_THREE_PHASE, APPARENT_POWER, VOLTAGE_LEVEL) == 5.24863881081478
