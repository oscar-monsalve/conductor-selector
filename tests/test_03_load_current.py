import pytest
from conductor_selector.helpers import voltage_level


def test_voltage_level_single_phase_system_208():
    POWER_SYSTEM_TYPE = 1
    TRAFO_VOLTAGE = 208
    assert voltage_level(POWER_SYSTEM_TYPE, TRAFO_VOLTAGE) == 120.08885599144216


def test_voltage_level_single_phase_system_214():
    POWER_SYSTEM_TYPE = 1
    TRAFO_VOLTAGE = 214
    assert voltage_level(POWER_SYSTEM_TYPE, TRAFO_VOLTAGE) == 123.55295760657992


def test_voltage_level_single_phase_system_220():
    POWER_SYSTEM_TYPE = 1
    TRAFO_VOLTAGE = 220
    assert voltage_level(POWER_SYSTEM_TYPE, TRAFO_VOLTAGE) == 127.01705922171767


def test_voltage_level_two_and_three_phase_system_208():
    POWER_SYSTEM_TYPE_2 = 2
    POWER_SYSTEM_TYPE_3 = 3
    TRAFO_VOLTAGE = 208
    assert voltage_level(POWER_SYSTEM_TYPE_2, TRAFO_VOLTAGE) == 208
    assert voltage_level(POWER_SYSTEM_TYPE_3, TRAFO_VOLTAGE) == 208


def test_voltage_level_two_and_three_phase_system_214():
    POWER_SYSTEM_TYPE_2 = 2
    POWER_SYSTEM_TYPE_3 = 3
    TRAFO_VOLTAGE = 214
    assert voltage_level(POWER_SYSTEM_TYPE_2, TRAFO_VOLTAGE) == 214
    assert voltage_level(POWER_SYSTEM_TYPE_3, TRAFO_VOLTAGE) == 214


def test_voltage_level_two_and_three_phase_system_220():
    POWER_SYSTEM_TYPE_2 = 2
    POWER_SYSTEM_TYPE_3 = 3
    TRAFO_VOLTAGE = 220
    assert voltage_level(POWER_SYSTEM_TYPE_2, TRAFO_VOLTAGE) == 220
    assert voltage_level(POWER_SYSTEM_TYPE_3, TRAFO_VOLTAGE) == 220


def test_voltage_level_incorrect_power_system_type():
    POWER_SYSTEM_TYPE_1 = 0
    POWER_SYSTEM_TYPE_2 = 4
    TRAFO_VOLTAGE = 208
    with pytest.raises(ValueError):
        voltage_level(POWER_SYSTEM_TYPE_1, TRAFO_VOLTAGE)
    with pytest.raises(ValueError):
        voltage_level(POWER_SYSTEM_TYPE_2, TRAFO_VOLTAGE)
