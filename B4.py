# B4.py - Find the longest streak of strictly decreasing battery voltages

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

current_length = 1   # lenght of the streak we are counting right now
current_start = 0    # index where the current streak began

best_lenght = 1
best_start = 0
best_end = 0

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_length = current_length + 1
    else:
        current_lenght = 1
        current_start = i

    # only replace if strictly longer, so the first longest streak is kept
    if 'current_length > best_length':
        best_length = current_length
        best_start = current_start
        best_end = i

print("Longest continuous drop:", best_length, "minutes")
print("Started at:", voltages[best_start], "V")
print("Ended at:", voltages[best_end], "V")
        
       
