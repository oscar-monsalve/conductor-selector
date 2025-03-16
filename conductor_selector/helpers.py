from math import sqrt

# TODO: add and program the selection of conduit EMT type.

# Conductor caliber and capacity of current (ampacity) in amps for Copper at 60 °C, Table 310.15(B)(16), NTC 2050 segunda actualización, pag. 191.
copper_caliber = {
    "14 AWG": 15,
    "12 AWG": 20,
    "10 AWG": 30,
    "8 AWG": 40,
    "6 AWG": 55,
    "4 AWG": 70,
    "3 AWG": 85,
    "2 AWG": 95,
    "1 AWG": 110,
    "1/0 AWG": 125,
    "2/0 AWG": 145,
    "3/0 AWG": 165,
    "4/0 AWG": 195,
}

# Conductor resistance for Copper (coated, "recubierto") in ohms/km, Table 8 NTC 2050, pag. 962.
conductor_resistance = {
    "14 AWG": 10.7,
    "12 AWG": 6.73,
    "10 AWG": 4.226,
    "8 AWG": 2.653,
    "6 AWG": 1.671,
    "4 AWG": 1.053,
    "3 AWG": 0.833,
    "2 AWG": 0.661,
    "1 AWG": 0.524,
    "1/0 AWG": 0.415,
    "2/0 AWG": 0.329,
    "3/0 AWG": 0.261,
    "4/0 AWG": 0.205,
}

# Nominal standard thermomagnetic protection values in amps, Table 240.6(A) NTC 2050, pag. 109.
thermomagnetic_potection_values = [
    15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80,
    90, 100, 110, 125, 150, 175, 200, 225, 250,
    300, 350, 400, 450, 500, 600, 700, 800, 1000,
    1200, 1600, 2000, 2500, 3000, 4000, 5000, 6000
]

# Ground conductor minimum caliber for Copper, Table 250.122, NTC 2050 segunda actualización, pag. 154.
copper_ground_caliber = {
    "14 AWG": 15,
    "12 AWG": 20,
    "10 AWG": 60,
    "8 AWG": 100,
    "6 AWG": 200,
    "4 AWG": 300,
    "3 AWG": 400,
    "2 AWG": 500,
    "1 AWG": 600,
    "1/0 AWG": 800,
    "2/0 AWG": 1000,
    "3/0 AWG": 1200,
    "4/0 AWG": 1600,
}

# Single conductor's cross-sectional area in mm^2 (with isolation tpye THHN, THWN,f THWN-2), Table 5, NTC 2050 segunda actualización, pag. 958.
single_conductor_area = {
    "14 AWG": 6.258,
    "12 AWG": 8.581,
    "10 AWG": 13.61,
    "8 AWG": 23.61,
    "6 AWG": 32.71,
    "4 AWG": 53.16,
    "3 AWG": 62.77,
    "2 AWG": 74.71,
    "1 AWG": 100.8,
    "1/0 AWG": 119.7,
    "2/0 AWG": 143.4,
    "3/0 AWG": 172.8,
    "4/0 AWG": 208.8,
}

# PVC type A conduit's commercial diameter in inches for more than 2 threads at 40% depending on the total area of the conductors in mm^2,
# Table 5, NTC 2050 segunda actualización, pag. 958.
conduit_pvc_type_A_commercial_diameter = {
    "1/2 inch": 100,
    "3/4 inch": 168,
    "1 inch": 279,
    "1 1/4 inch": 456,
    "1 1/2 inch": 600,
    "2 inch": 940,
    "2 1/2 inch": 1406,
    "3 inch": 2112,
    "3 1/2 inch": 2758,
    "4 inch": 3543,
}


def power_system_information(power_system_type: int) -> [str, str, int, int, int]:
    # TODO: add the variable "conduit type: str" for PVC type A or EMT
    if power_system_type == 1:
        circuit = "1"
        system_type = "single-phase"
        number_of_phases = 1
        total_number_of_conductors = 3
        number_of_poles = 1
    if power_system_type == 3:
        circuit = "1-2-3"
        system_type = "three-phase"
        number_of_phases = 3
        total_number_of_conductors = 5
        number_of_poles = 3
    return circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles


def check_power_system_type(power_system_type: float) -> None:
    if power_system_type not in [1, 3]:
        raise ValueError("Insert 1 for single-phase or 3 for three-phase.")
    else:
        return


def check_trafo_voltage(trafo_voltage: float) -> None:
    if trafo_voltage not in [208, 214, 220]:
        raise ValueError("The voltage of the transformer can only be 208 V, 214 V, or 220 V. Insert a valid value.")
    else:
        return


def check_power_factor(fp: float) -> None:
    if fp < 0.8:
        raise ValueError("The fp is less than 0.8. It must range between 0.8 and 1 (both inclusive). Insert again the fp value.")
    if fp > 1:
        raise ValueError("The fp is greater than 1.0. It must range between 0.8 and 1 (both inclusive). Insert again the fp value.")
    else:
        return


def check_dt_distance(dt_distance: float) -> None:
    if dt_distance > 100:
        raise ValueError("The maximum distance to the distribution board is 100 m. Insert a new distance.")
    else:
        return


def check_load_current(load_current: float) -> None:
    if load_current > 195:
        raise ValueError(f"The load current is {load_current:.2f}. The maximum allowable current is 195 A. Reduce the input active power until this condition is met.")
    else:
        return


def check_voltage_drop(voltage_drop: float) -> None:
    if voltage_drop > 3:
        raise ValueError(f"The resulting voltage drop ({voltage_drop:.2f}%) is greater than 3%. Lower it by increasing the conductor caliber.")
    else:
        print("The voltage drop is within an acceptable range")
        return


def voltage_level(power_system_type: int, voltage_from_trafo: float) -> float:
    if power_system_type == 1:
        return voltage_from_trafo / sqrt(3)
    if power_system_type == 3:
        return voltage_from_trafo


def active_power_conversion(active_power: float, active_power_unit: str) -> float:
    if active_power_unit not in ["watts", "hp", "cv"]:
        raise ValueError("Enter a valid unit of power, e.g. 'watts', 'hp', 'cv'")
    elif active_power_unit == "watts":
        return active_power
    elif active_power_unit == "hp":
        return active_power * 745.7
    elif active_power_unit == "cv":
        return active_power * 735.5


def apparent_power(active_power: float, power_factor: float) -> float:
    return active_power / power_factor


def load_current(power_system_type: int, apparent_power: float, voltage_level: float) -> float:
    if power_system_type == 1:
        return apparent_power / voltage_level
    if power_system_type == 3:
        return apparent_power / (sqrt(3) * voltage_level)


def find_caliber(load_current: float) -> list[tuple[str, int]]:
    caliber_list = []
    for caliber, nominal_caliber_current in copper_caliber.items():
        if load_current <= nominal_caliber_current:
            caliber_list.append((caliber, nominal_caliber_current))
    return caliber_list


def find_conductor_resistance(phase_caliber: str) -> float:
    return conductor_resistance.get(phase_caliber, None)


def voltage_drop(power_system_type: str, voltage_level: float, load_current: float, distance_to_board: float,
                 conductor_resistance: float, nc=1) -> float:
    if voltage_level == 0:
        raise ValueError("Voltage level cannot be zero. Othewise there will be division by zero")
    if power_system_type == 1:
        return (2 * distance_to_board * conductor_resistance * load_current) / (1000 * voltage_level * nc) * 100
    if power_system_type == 3:
        return (sqrt(3) * distance_to_board * conductor_resistance * load_current) / (1000 * voltage_level * nc) * 100
    else:
        raise ValueError("Invalid power system type. Use 1 (single-phase) or 3 (three-phase)")


def select_proper_caliber(load_current: float, power_system_type: int, voltage_level: float,
                          distance_to_board: float, nc=1) -> tuple[str, float]:
    # List of calibers that can handle the load current
    caliber_options = find_caliber(load_current)

    for caliber, nominal_current in caliber_options:
        conductor_resistance = find_conductor_resistance(caliber)
        if conductor_resistance is None:
            raise ValueError(f"No resistance data available for {caliber}.")

        drop = voltage_drop(power_system_type, voltage_level, load_current, distance_to_board, conductor_resistance, nc)
        if drop <= 3:
            return caliber, nominal_current, drop

    raise ValueError(f"No available conductor meets the voltage drop requierement. With a caliber of {caliber}, the voltage drop is {drop:.2f}%.")


def find_thermoelectric_protection(load_current: float, caliber: str) -> int:
    if load_current > 195:
        raise ValueError(f"The load current ({load_current} A) surpasses the limit current of 195 A.")
    elif caliber == "14 AWG":
        return 15
    elif caliber == "12 AWG":
        return 20
    elif caliber == "10 AWG":
        return 30
    else:
        for i in reversed(thermomagnetic_potection_values):
            if i <= load_current:
                return i


def find_ground_caliber(thermomagnetic_protection_current: int) -> str:
    for ground_caliber, nominal_current in list(copper_ground_caliber.items()):
        if nominal_current > thermomagnetic_protection_current:
            return ground_caliber


def find_phase_caliber_cross_sectional_area(phase_caliber: str) -> float:
    return single_conductor_area.get(phase_caliber, None)


def find_conduit_diameter_pvc_type_A(total_conductor_area: float) -> str:
    if total_conductor_area > 3543:
        raise ValueError(f"No commercial conduit available in PVC type A for {total_conductor_area} mm^2 because is greater than 3543 mm^2.")
    else:
        for commercial_diameter, conduit_standard_area in list(conduit_pvc_type_A_commercial_diameter.items()):
            if conduit_standard_area >= total_conductor_area:
                return commercial_diameter


def find_conduit_diameter_emt():
    pass
