dividend = int(input("Dividendo:"))
divisor = int(input("Divisor:"))
quotient = dividend // divisor
remainder = dividend % divisor
if remainder == 0:
    print("La división es exacta. Cociente:", quotient)
else:
    print("La división no es exacta. Cociente:", quotient, "Residuo:", remainder)