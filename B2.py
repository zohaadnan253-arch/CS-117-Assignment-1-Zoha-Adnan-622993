# B2.py - Total resistance of resistors connected in series

count = int(input("How many resistors? "))
total = 0

for i in range(1, count + 1):
    value = int(input("Enter R" + str(i) + ": "))
    total = total + value

print("Total resistance ", total, "ohm")
