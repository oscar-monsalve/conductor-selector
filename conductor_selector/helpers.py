# Inputs:
#   - power_system: single-phase or three-phase
#   - voltage_from_trafo: 208 V, 214 V, or 220 V.
#   - active_power P: in hp or watts
#   - power_factor: 0.8 <= fp <= 1
#   - DT: distance to the distribution board (DDB)
#
# Notes:
#   - Maximum allowable current: <= 195 A. if higher, the program must throw an exception error.
#   - Voltage drop: <= 3%. If higher, the program must throw an exception error.
#   - DT distance: <= 100. If higher, the program must throw an exception error.
#   - Calculations only for copper conductors at 60 °C.
#   - Maximum caliber: 4/0 AWG.
#
# Outputs:
#   - Number of the circtuit depending the type of power system: 1, 1-2, 1-2-3.
#   - Voltage.
#   - Current.
#   - Thermomagnetic protection.
#   - Number of poles.
#   - DT distance.
#   - Voltage drop.
#   - Caliber of the phase conductor.
#   - Caliber of the neutral conductor.
#   - Caliber of the ground conductor.
#   - Diameter of conduit in EMT and PCV type A.

from math import sqrt

# Conductor caliber for Copper at 60 °C, Table 310.15(B)(16), NTC 2050 segunda actualización, pag. 191.
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

# Conductor resistance for Copper (coated, "recubierto") given in ohms/km, Table 8 NTC 2050, pag. 962.
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


def find_caliber(load_current: float) -> dict[str, int]:
    for caliber, nominal_caliber_current in copper_caliber.items():
        if load_current <= nominal_caliber_current:
            return caliber, nominal_caliber_current


def find_conductor_resistance(phase_caliber: str) -> float:
    for caliber, resistance in conductor_resistance.items():
        if phase_caliber == caliber:
            return resistance


def voltage_drop(power_system_type: str, voltage_level: float, load_current: float, distance_to_board: float,
                 conductor_resistance: float, nc=1) -> float:
    if power_system_type == 1:
        return (2 * distance_to_board * conductor_resistance * load_current) / (1000 * voltage_level * nc) * 100
    if power_system_type == 3:
        return (sqrt(3) * distance_to_board * conductor_resistance * load_current) / (1000 * voltage_level * nc) * 100


def find_thermoelectric_protection():
    pass


def find_ground_caliber():
    pass
