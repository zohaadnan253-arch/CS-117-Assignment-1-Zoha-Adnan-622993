# A1.py - Fuse check using Ohm's law

voltage = int(input("Enter voltage (v): "))
resistance = int(input("Enter resistance (ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
    
    
