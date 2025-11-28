from math import sqrt
from conductor_selector import ntc2050_data as ntc

# Define program limits
MAXIMUM_LOAD_CURRENT:               float = 195.0   # amps
MAXIMUM_DT_DISTANCE:                float = 110.0   # meters
MAXIMUM_VOLTAGE_DROP:               float = 3.0     # volts
LOWER_FP_LIMIT:                     float = 0.65    # -
UPPER_FP_LIMIT:                     float = 1.0     # -
MAX_AREA_PVC_TYPE_A_AT_40_PERCENT:  float = 3543.0  # mm^2
MAX_AREA_EMT_AT_40_PERCENT:         float = 3808.0  # mm^2


def power_system_information(power_system_type: int) -> tuple[str, str, int, int, int]:
    if power_system_type == 1:
        circuit = "1"
        system_type = "single-phase"
        number_of_phases = 1
        total_number_of_conductors = 3
        number_of_poles = 1
    elif power_system_type == 2:
        circuit = "1-2"
        system_type = "two-phase"
        number_of_phases = 2
        total_number_of_conductors = 4
        number_of_poles = 2
    elif power_system_type == 3:
        circuit = "1-2-3"
        system_type = "three-phase"
        number_of_phases = 3
        total_number_of_conductors = 5
        number_of_poles = 3
    return circuit, system_type, number_of_phases, total_number_of_conductors, number_of_poles


def check_power_system_type(power_system_type: float) -> None:
    if power_system_type not in (1, 2, 3):
        raise ValueError("Insert 1 for single-phase, 2 for two-phase, or 3 for three-phase.")
    else:
        return


def check_trafo_voltage(trafo_voltage: float) -> None:
    if trafo_voltage not in (208, 214, 220):
        raise ValueError("The voltage of the transformer can only be 208 V, 214 V, or 220 V. Insert a valid value.")
    else:
        return


def check_power_factor(fp: float) -> None:
    if fp < LOWER_FP_LIMIT:
        raise ValueError(f"The fp is less than {LOWER_FP_LIMIT}. It must range between {LOWER_FP_LIMIT} and {UPPER_FP_LIMIT} (both inclusive). Insert again the fp value.")
    if fp > UPPER_FP_LIMIT:
        raise ValueError("The fp is greater than {UPPER_FP_LIMIT}. It must range between {LOWER_FP_LIMIT} and {UPPER_FP_LIMIT} (both inclusive). Insert again the fp value.")
    else:
        return


def check_dt_distance(dt_distance: float) -> None:
    if dt_distance > MAXIMUM_DT_DISTANCE:
        raise ValueError(f"The maximum distance to the distribution board is {MAXIMUM_DT_DISTANCE:.0f} m. Insert a new distance.")
    else:
        return


def check_load_current(load_current: float) -> None:
    if load_current > MAXIMUM_LOAD_CURRENT:
        raise ValueError(f"The load current is {load_current:.2f} A. The maximum allowable current is {MAXIMUM_LOAD_CURRENT} A. Reduce the input active power until this condition is met.")
    else:
        return


def check_voltage_drop(voltage_drop: float) -> None:
    if voltage_drop > MAXIMUM_VOLTAGE_DROP:
        raise ValueError(f"The resulting voltage drop ({voltage_drop:.2f}%) is greater than {MAXIMUM_VOLTAGE_DROP}%. Lower it by increasing the conductor caliber.")
    else:
        print("The voltage drop is within an acceptable range")
        return


def voltage_level(power_system_type: int, voltage_from_trafo: float) -> float:
    if power_system_type == 1:
        return voltage_from_trafo / sqrt(3)
    if power_system_type in (2, 3):
        return voltage_from_trafo
    raise ValueError("Invalid power system type.")


def active_power_conversion(active_power: float, active_power_unit: str) -> float:
    if active_power_unit not in ("watts", "hp", "cv"):
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
    if power_system_type in (1, 2):
        return apparent_power / voltage_level
    if power_system_type == 3:
        return apparent_power / (sqrt(3) * voltage_level)


def find_caliber(load_current: float) -> list[tuple[str, int]]:
    caliber_list = []
    for caliber, nominal_caliber_current in ntc.copper_caliber.items():
        if load_current <= nominal_caliber_current:
            caliber_list.append((caliber, nominal_caliber_current))
    return caliber_list


def find_conductor_resistance(phase_caliber: str) -> float:
    return ntc.conductor_resistance.get(phase_caliber, None)


def voltage_drop(power_system_type: str, voltage_level: float, load_current: float, distance_to_board: float,
                 conductor_resistance: float, nc=1) -> float:
    if voltage_level == 0:
        raise ValueError("Voltage level cannot be zero. Othewise there will be division by zero")
    if power_system_type in (1, 2):
        return (2 * distance_to_board * conductor_resistance * load_current) / (1000 * voltage_level * nc) * 100
    if power_system_type == 3:
        return (sqrt(3) * distance_to_board * conductor_resistance * load_current) / (1000 * voltage_level * nc) * 100
    else:
        raise ValueError("Invalid power system type. Insert 1 for single-phase, 2 for two-phase, or 3 for three-phase.")


def select_proper_caliber(load_current: float, power_system_type: int, voltage_level: float,
                          distance_to_board: float, nc=1) -> tuple[str, float, float]:
    caliber_options = find_caliber(load_current)  # List of calibers that can handle the load current

    for caliber, nominal_current in caliber_options:
        conductor_resistance = find_conductor_resistance(caliber)
        if conductor_resistance is None:
            raise ValueError(f"No resistance data available for {caliber}.")

        drop = voltage_drop(power_system_type, voltage_level, load_current, distance_to_board, conductor_resistance, nc)
        if drop <= MAXIMUM_VOLTAGE_DROP:
            return caliber, nominal_current, drop

    raise ValueError(f"No available conductor meets the voltage drop requierement (<{MAXIMUM_VOLTAGE_DROP}%). With a caliber of {caliber}, the voltage drop is {drop:.2f}%.")


def find_thermoelectric_protection(load_current: float, caliber: str) -> int:
    protection_default_values = {
        "14 AWG": 15,
        "12 AWG": 20,
        "10 AWG": 30,
    }

    if load_current > MAXIMUM_LOAD_CURRENT:
        raise ValueError(f"The load current ({load_current} A) surpasses the limit current of {MAXIMUM_LOAD_CURRENT} A.")

    elif caliber in protection_default_values:
        return protection_default_values[caliber]

    for i in reversed(ntc.thermomagnetic_protection_values):
        if i <= load_current:
            return i

    # If load_current is < to the smallest value in thermoelectric_protection_values, return the smallest available protection
    return ntc.thermomagnetic_protection_values[0]


def find_ground_caliber(thermomagnetic_protection_current: int) -> str:
    for ground_caliber, nominal_current in list(ntc.copper_ground_caliber.items()):
        if nominal_current >= thermomagnetic_protection_current:
            return ground_caliber


def find_phase_caliber_cross_sectional_area(phase_caliber: str) -> float:
    return ntc.single_conductor_area.get(phase_caliber, None)


def find_conduit_diameter_pvc_type_A(total_conductor_area: float) -> str:
    if total_conductor_area > MAX_AREA_PVC_TYPE_A_AT_40_PERCENT:
        raise ValueError(f"No commercial conduit available in PVC type A for {total_conductor_area} mm^2 because is greater than {MAX_AREA_PVC_TYPE_A_AT_40_PERCENT} mm^2.")
    else:
        for commercial_diameter, conduit_standard_area in list(ntc.conduit_pvc_type_A_commercial_diameter.items()):
            if conduit_standard_area >= total_conductor_area:
                return commercial_diameter


def find_conduit_diameter_emt(total_conductor_area: float) -> str:
    if total_conductor_area > MAX_AREA_EMT_AT_40_PERCENT:
        raise ValueError(f"No commercial conduit available in EMT for {total_conductor_area} mm^2 because is greater than {MAX_AREA_EMT_AT_40_PERCENT} mm^2.")
    else:
        for commercial_diameter, conduit_standard_area in list(ntc.conduit_emt_commercial_diameter.items()):
            if conduit_standard_area >= total_conductor_area:
                return commercial_diameter
