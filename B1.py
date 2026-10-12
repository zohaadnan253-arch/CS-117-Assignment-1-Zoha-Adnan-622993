# B1.py - Current through a 10 ohm resistor for supply voltages 1V to 10V

resistance = 10

for voltage in range(1, 11):
    current = voltage / resistance
    print("V =", voltage, "V", "I =", current, "A")
