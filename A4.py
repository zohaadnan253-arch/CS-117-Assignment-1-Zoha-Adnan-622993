# A4.py-AND, OR and XOR gate outputs for two input bits

a = int(input("Enter A: "))
b = int(input("Enter b: "))

if (a != 0 and a != 1) or (b != 0 and b!= 1):
    print("Bits must  be 0 or 1")
else:
    
    # AND is 1 only when both inputs are 1
    if a == 1 and b == 1:
        and_out = 1
    else:
        and_out = 0
        
    # OR is 0 only when both inputs are 0
    if a == 0 and b == 0:
        or_out = 0
    else:
        or_out = 1

    #XOR is 1 when the inputs are different
    if a != b:
        xor_out = 1
    else:
        xor_out = 0
  
print("AND=", and_out)
print("OR =", or_out)
print("XOR=", xor_out)
