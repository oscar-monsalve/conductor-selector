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
thermomagnetic_protection_values = [
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

# EMT conduit's commercial diameter in inches for more than 2 threads at 40%, Table 5, NTC 2050 segunda actualización, pag. 958.
conduit_emt_commercial_diameter = {
    "1/2 inch": 78,
    "3/4 inch": 137,
    "1 inch": 222,
    "1 1/4 inch": 387,
    "1 1/2 inch": 526,
    "2 inch": 866,
    "2 1/2 inch": 1513,
    "3 inch": 2280,
    "3 1/2 inch": 2980,
    "4 inch": 3808,
}

# PVC type A conduit's commercial diameter in inches for more than 2 threads at 40%, Table 5, NTC 2050 segunda actualización, pag. 958.
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
