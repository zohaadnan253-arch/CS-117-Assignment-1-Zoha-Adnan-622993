# C4.py - Voltage divider output with an without a load resitor

def loaded_divider(vs, r1, r2, rl):
    # unloaded output
    unloaded = vs * r2 / (r1 + r2)

    # r2 an the load are in parallel
    r_parallel = (r2 * r1) / (r2 + r1)

    # divider formula again, using the parallel value instead of r2
    loaded = vs * r_parallel / (r1 + r_parallel)

    return round(unloaded, 2), round(loaded, 2)

print("loaded_divider(12, 1000, 1000, 500) ->", loaded_divider(12, 1000, 1000, 500))
