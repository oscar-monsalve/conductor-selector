import helpers as h

# Inputs
POWER_SYSTEM_TYPE:   int = 3  # 1 if single-phase. 3 if three-phase
TRAFO_VOLTAGE:       int = 220  # 208 V, 214 V, or 220 V.
ACTIVE_POWER:      float = 20
ACTIVE_POWER_UNIT:   str = "hp"  # "watts", "hp", or "cv".
POWER_FACTOR:      float = 0.85  # 0.8 <= fp <= 1
DT:                float = 70  # distance to the distribution board in meters.


def main() -> None:
    # Check data input
    h.check_power_system_type(POWER_SYSTEM_TYPE)
    h.check_trafo_voltage(TRAFO_VOLTAGE)
    h.check_power_factor(POWER_FACTOR)
    h.check_dt_distance(DT)

    # Initiate calculations
    voltage_level = h.voltage_level(POWER_SYSTEM_TYPE, TRAFO_VOLTAGE)
    active_power_watts = h.active_power_conversion(ACTIVE_POWER, ACTIVE_POWER_UNIT)
    apparent_power = h.apparent_power(active_power_watts, POWER_FACTOR)
    load_current = h.load_current(POWER_SYSTEM_TYPE, apparent_power, voltage_level)
    h.check_load_current(load_current)
    phase_caliber, nominal_caliber_current = h.find_caliber(load_current)
    conductor_resistance = h.find_conductor_resistance(phase_caliber)
    voltage_drop = h.voltage_drop(POWER_SYSTEM_TYPE, voltage_level, load_current, DT, conductor_resistance)

    # if voltage_drop > 3:
    #     current_index = list(h.copper_caliber).index(phase_caliber)
    #     for i,

    # Print results
    if POWER_SYSTEM_TYPE == 1:
        system_type = "single-phase"
        number_of_phases = 1
    if POWER_SYSTEM_TYPE == 3:
        system_type = "three-phase"
        number_of_phases = 3

    print(f"Sytem type          : {system_type}")
    print(f"Sytem voltage       : {voltage_level} V.")
    print(f"Active power        : {active_power_watts:.2f} W.")
    print(f"Apparent power      : {apparent_power:.2f} VA.")
    print(f"Load current        : {load_current:.2f} A.")
    print(f"Phase caliber       : {number_of_phases} x {phase_caliber} ({nominal_caliber_current} A).")
    print(f"Neutral caliber     : 1 x {phase_caliber} ({nominal_caliber_current} A).")
    print(f"Conductor resistance: {conductor_resistance} ohm/km.")
    print(f"Voltage drop: {voltage_drop:.2f} %.")


if __name__ == "__main__":
    main()
