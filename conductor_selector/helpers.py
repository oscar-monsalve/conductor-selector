# Inputs:
#   - power_system: single-phase or three-phase
#   - voltage_from_trafo: 208 V, 214 V, or 220 V.
#   - active_power P
#   - power_factor: 0.8 <= fp <= 1
#   - DT: distance to the distribution board (DDB)
#
#   - Additional_notes:
#       - Maximum allowable current: <= 195 A. if higher, the program must throw an exception error.
#       - Voltage drop: <= 3%. If higher, the program must throw an exception error.
#       - DT distance: <= 100. If higher, the program must throw an exception error.
#       - Calculations only for copper conductors at 60 °C.
#       - Maximum caliber: 4/0 AWG.
#
# Outputs:
#   - Number of the circtuit depending the type of power system: 1, 1-2, 1-2-3.
#   - Voltage.
#   - Current.
#   - Thermomagnetic protection.
#   - Number of poles.
#   - DT distance.
#   - Caliber of the phase conductor.
#   - Caliber of the neutral conductor.
#   - Caliber of the ground conductor.

from math import sqrt


def voltage_level(power_system: int, voltage_from_trafo: float) -> float:
    if power_system == 1:
        return voltage_from_trafo / sqrt(3)
    if power_system == 3:
        return voltage_from_trafo


def apparent_power(active_power: float, power_factor: float) -> float:
    return active_power / power_factor


def current(power_system: int, apparent_power: float, voltage_level: float):
    if power_system == 1:
        return apparent_power / (voltage_level)
    if power_system == 3:
        return apparent_power / (sqrt(3) * voltage_level)


def voltage_drop(power_system: str, voltage_level: float, current: float, distance_to_board: float,
                 conductor_r: float, nc: int) -> float:
    if power_system == 1:
        return (2 * distance_to_board * conductor_r * current) / (1000 * voltage_level * nc)
    if power_system == 3:
        return (sqrt(3) * distance_to_board * conductor_r * current) / (1000 * voltage_level * nc)
