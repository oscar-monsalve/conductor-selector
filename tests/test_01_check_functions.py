import pytest
from conductor_selector.helpers import (
    check_power_system_type,
    check_trafo_voltage,
    check_load_current,
    check_power_factor,
    check_dt_distance,
)


def test_check_power_system_correct_input():
    SINGLE_PHASE, TWO_PHASE, THREE_PHASE = 1, 2, 3
    assert isinstance(check_power_system_type(SINGLE_PHASE), type(None))
    assert isinstance(check_power_system_type(TWO_PHASE), type(None))
    assert isinstance(check_power_system_type(THREE_PHASE), type(None))


def test_check_power_system_incorrect_input():
    INCORRECT_POWER_SYSTEM_1 = 0
    INCORRECT_POWER_SYSTEM_2 = 4
    with pytest.raises(ValueError):
        check_power_system_type(INCORRECT_POWER_SYSTEM_1)
    with pytest.raises(ValueError):
        check_power_system_type(INCORRECT_POWER_SYSTEM_2)


def test_check_trafo_voltage_correct_input():
    TRAFO_VOLTAGE_1, TRAFO_VOLTAGE_2, TRAFO_VOLTAGE_3 = 208, 214, 220
    assert isinstance(check_trafo_voltage(TRAFO_VOLTAGE_1), type(None))
    assert isinstance(check_trafo_voltage(TRAFO_VOLTAGE_2), type(None))
    assert isinstance(check_trafo_voltage(TRAFO_VOLTAGE_3), type(None))


def test_check_trafo_voltage_incorrect_input():
    INCORRECT_TRAFO_VOLTAGE_1 = 0
    INCORRECT_TRAFO_VOLTAGE_2 = 120
    with pytest.raises(ValueError):
        check_trafo_voltage(INCORRECT_TRAFO_VOLTAGE_1)
    with pytest.raises(ValueError):
        check_trafo_voltage(INCORRECT_TRAFO_VOLTAGE_2)


def test_check_power_factor_correct_input():
    CORRECT_POWER_FACTOR_1 = 0.8
    CORRECT_POWER_FACTOR_2 = 1
    CORRECT_POWER_FACTOR_3 = 0.96
    assert isinstance(check_power_factor(CORRECT_POWER_FACTOR_1), type(None))
    assert isinstance(check_power_factor(CORRECT_POWER_FACTOR_2), type(None))
    assert isinstance(check_power_factor(CORRECT_POWER_FACTOR_3), type(None))


def test_check_power_factor_incorrect_input():
    INCORRECT_POWER_FACTOR_1 = 1.2
    INCORRECT_POWER_FACTOR_2 = 0.6
    with pytest.raises(ValueError):
        check_power_factor(INCORRECT_POWER_FACTOR_1)
    with pytest.raises(ValueError):
        check_power_factor(INCORRECT_POWER_FACTOR_2)


def test_check_dt_distance_correct_input():
    CORRECT_DT_1 = 1.5
    CORRECT_DT_2 = 10
    CORRECT_DT_3 = 110
    assert isinstance(check_dt_distance(CORRECT_DT_1), type(None))
    assert isinstance(check_dt_distance(CORRECT_DT_2), type(None))
    assert isinstance(check_dt_distance(CORRECT_DT_3), type(None))


def test_check_dt_distance_incorrect_input():
    INCORRECT_DT_1 = 201
    INCORRECT_DT_2 = 600.5
    with pytest.raises(ValueError):
        check_dt_distance(INCORRECT_DT_1)
    with pytest.raises(ValueError):
        check_dt_distance(INCORRECT_DT_2)


def test_check_load_current_valid_result():
    valid_load_current_1 = 2
    valid_load_current_2 = 10.5
    valid_load_current_3 = 195
    assert isinstance(check_load_current(valid_load_current_1), type(None))
    assert isinstance(check_load_current(valid_load_current_2), type(None))
    assert isinstance(check_load_current(valid_load_current_3), type(None))


def test_check_load_current_invalid_result():
    invalid_load_current_1 = 196
    invalid_load_current_2 = 500.5
    with pytest.raises(ValueError):
        check_load_current(invalid_load_current_1)
    with pytest.raises(ValueError):
        check_load_current(invalid_load_current_2)
