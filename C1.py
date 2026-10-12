# C1.py - Functions for current and power in a resistor

def ohms_current(v, r):
    return v/r

def power_dissipated(i, r):
    return i ** 2 * r

voltage = 12
resistance = 6

current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)

print("Current =", current, "A")
print("Power =", power, "W")
