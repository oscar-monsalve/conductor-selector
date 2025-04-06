import pytest
from conductor_selector.helpers import active_power_conversion


def test_active_power_conversion_incorrect_input():
    POWER_SYSTEM_UNIT_INCORRECT_INPUT = ["vapor power", "horse power"]
    for i in POWER_SYSTEM_UNIT_INCORRECT_INPUT:
        with pytest.raises(ValueError):
            active_power_conversion(1200, i)


def test_active_power_conversion_watts_input():
    POWER_SYSTEM_UNIT_WATTS = "watts"
    assert active_power_conversion(1220, POWER_SYSTEM_UNIT_WATTS) == 1220


def test_active_power_conversion_hp_input():
    POWER_SYSTEM_UNIT_HP = "hp"
    assert active_power_conversion(5, POWER_SYSTEM_UNIT_HP) == 3728.5


def test_active_power_conversion_cv_input():
    POWER_SYSTEM_UNIT_CV = "cv"
    assert active_power_conversion(5, POWER_SYSTEM_UNIT_CV) == 3677.5


def test_active_power_conversion_return_value():
    assert isinstance(active_power_conversion(745.7, "watts"), float)
    assert isinstance(active_power_conversion(1220, "hp"), float)
    assert isinstance(active_power_conversion(2, "cv"), float)
