# ---- Input description ----
# POWER_SYSTEM_TYPE : 1 for single-phase or 3 for three-phase.
# TRAFO_VOLTAGE     : Transformer voltage: 208 V, 214 V, or 220 V.
# ACTIVE_POWER      : Active power numerical value.
# ACTIVE_POWER_UNIT : Active power unit as "watts", "hp", or "cv".
# POWER_FACTOR      : Power factor of the load in a range of 0.8 <= POWER_FACTOR <= 1.
# Distance          : Distance to the distribution board in meters.
# ---- Input description ----
#
# ---- Notes ----
#   - Maximum allowable current : <= 195 A. if higher, the program must throw an exception error.
#   - Voltage drop              : <= 3%. If higher, the program must throw an exception error.
#   - DT distance               : <= 100. If higher, the program must throw an exception error.
#   - Conductors                : only for copper conductors at 60 °C.
#   - Maximum caliber           : 4/0 AWG.
# ---- Notes ----

import helpers as h

# ---- Inputs ----
POWER_SYSTEM_TYPE:   int = 3
TRAFO_VOLTAGE:       int = 208
ACTIVE_POWER:      float = 5
ACTIVE_POWER_UNIT:   str = "hp"
POWER_FACTOR:      float = 0.9
DT:                float = 100
# ---- Inputs ----


def main() -> None:
    # Check data input
    h.check_power_system_type(POWER_SYSTEM_TYPE)
    h.check_trafo_voltage(TRAFO_VOLTAGE)
    h.check_power_factor(POWER_FACTOR)
    h.check_dt_distance(DT)

    # Power system information
    (
        circuit,
        system_type,
        number_of_phases,
        total_number_of_conductors,
        number_of_poles,
    ) = h.power_system_information(POWER_SYSTEM_TYPE)

    # Initiate calculations
    voltage_level = h.voltage_level(POWER_SYSTEM_TYPE, TRAFO_VOLTAGE)
    active_power_watts = h.active_power_conversion(ACTIVE_POWER, ACTIVE_POWER_UNIT)
    apparent_power = h.apparent_power(active_power_watts, POWER_FACTOR)
    load_current = h.load_current(POWER_SYSTEM_TYPE, apparent_power, voltage_level)
    h.check_load_current(load_current)

    (
        # TODO: add the variable "conduit type: str" for PVC type A or EMT and replace it in the printing of "Conduit commercial diameter"
        selected_phase_caliber,
        nominal_current_selected_caliber,
        final_voltage_drop
    ) = h.select_proper_caliber(load_current, POWER_SYSTEM_TYPE, voltage_level, DT)

    thermoelectric_protection = h.find_thermoelectric_protection(load_current, selected_phase_caliber)
    selected_ground_caliber = h.find_ground_caliber(thermoelectric_protection)
    area_of_highest_caliber = h.find_phase_caliber_cross_sectional_area(selected_phase_caliber)
    total_conductor_area = total_number_of_conductors * area_of_highest_caliber
    conduit_diameter_pvc_type_A = h.find_conduit_diameter_pvc_type_A(total_conductor_area)
    conduit_diameter_emt = h.find_conduit_diameter_emt(total_conductor_area)

    # Print results
    print(f"System type                 : {system_type}")
    print(f"System voltage              : {voltage_level:.2f} V.")
    print(f"Active power                : {active_power_watts:.2f} W.")
    print(f"Apparent power              : {apparent_power:.2f} VA.")
    print(f"Load current                : {load_current:.2f} A.")
    print(f"Thermoelectric protection   : {thermoelectric_protection} A.")
    print(f"Voltage drop                : {final_voltage_drop:.2f} % (for {selected_phase_caliber}).")
    print(f"Phase caliber               : {number_of_phases} x {selected_phase_caliber} ({nominal_current_selected_caliber} A).")
    print(f"Neutral caliber             : 1 x {selected_phase_caliber}.")
    print(f"Ground caliber              : 1 x {selected_ground_caliber}.")
    print(f"Individual conductor area   : {area_of_highest_caliber} mm^2 ({selected_phase_caliber}).")
    print(f"Total conductor area        : {total_conductor_area:.2f} mm^2.")
    print(f"Conduit PVC type A diameter : {conduit_diameter_pvc_type_A}.")
    print(f"Conduit EMT diameter        : {conduit_diameter_emt}.")


if __name__ == "__main__":
    main()
