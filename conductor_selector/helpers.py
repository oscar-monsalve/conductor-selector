# input data:
# power system: single-phase or three-phase
# voltage_from_trafo: 208 V, 214 V, or 220 V.
# Active power P
# power factor
# distance to the distribution board (DDB)

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
