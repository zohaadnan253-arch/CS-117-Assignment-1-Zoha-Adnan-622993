# C2.py - Equivalent resistance of resistors connected in parallel

def parallel_resistance(resistors):
    reciprocal_sum = 0
    for r in resistors:
        reciprocal_sum = reciprocal_sum + 1 / r
    return round(1 / reciprocal_sum, 2)

print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))
