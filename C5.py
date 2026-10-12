# C5.py - Converts a start (Y) resistor network to its delta equivalent

def star_to_delta(ra, rb, rc):
    #common numerator, calculate onece
    numerator = ra * rb + rb * rc + rc * ra

    rab = numerator / rc
    rbc = numerator / ra
    rca = numerator / rb

    return round(rab, 2), round(rbc, 2), round(rca, 2)

print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))
