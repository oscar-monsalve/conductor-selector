from conductor_selector.helpers import power_system_information

POWER_SYSTEM_TYPE_1 = 1
POWER_SYSTEM_TYPE_2 = 2
POWER_SYSTEM_TYPE_3 = 3


def test_return_class_power_system_information():
    assert isinstance(power_system_information(POWER_SYSTEM_TYPE_1), tuple)
    assert isinstance(power_system_information(POWER_SYSTEM_TYPE_2), tuple)
    assert isinstance(power_system_information(POWER_SYSTEM_TYPE_3), tuple)


def test_each_return_type_power_system_information_single_phase():
    (
        circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles
    ) = power_system_information(POWER_SYSTEM_TYPE_1)

    assert isinstance(circuit, str)
    assert isinstance(system_type, str)
    assert isinstance(number_of_phases, int)
    assert isinstance(total_number_of_conductors, int)
    assert isinstance(number_of_poles, int)

    assert (
        circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles
    ) == ("1", "single-phase", 1, 3, 1)


def test_each_return_type_power_system_information_two_phase():
    (
        circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles
    ) = power_system_information(POWER_SYSTEM_TYPE_2)

    assert isinstance(circuit, str)
    assert isinstance(system_type, str)
    assert isinstance(number_of_phases, int)
    assert isinstance(total_number_of_conductors, int)
    assert isinstance(number_of_poles, int)

    assert (
        circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles
    ) == ("1-2", "two-phase", 2, 4, 2)


def test_each_return_type_power_system_information_three_phase():
    (
        circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles
    ) = power_system_information(POWER_SYSTEM_TYPE_3)

    assert isinstance(circuit, str)
    assert isinstance(system_type, str)
    assert isinstance(number_of_phases, int)
    assert isinstance(total_number_of_conductors, int)
    assert isinstance(number_of_poles, int)

    assert (
        circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles
    ) == ("1-2-3", "three-phase", 3, 5, 3)
