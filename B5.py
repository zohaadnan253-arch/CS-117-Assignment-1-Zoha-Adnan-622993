#B5.py - Sorts measure 100 ohm resistors into tolerance bins (enter 0 to stop)

one_percent = 0
five_percent = 0
rejected = 0

resistance = float(input("Enter measured resistance (0 to stop): "))

while resistance != 0:
    if resistance >= 99.0 and resistance <= 101.0:
        one_percent = one_percent + 1
    elif resistance >= 95.0 and resistance <= 105.0:
        five_percent = five_percent + 1
    else:
        rejected = rejected + 1

    resistance = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance:", one_percent)
print("5% tolerance:", five_percent)
print("Rejected:", rejected)
