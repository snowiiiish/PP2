def ftoc(F):
    C = (5 / 9) * (F - 32)
    return C

F = int(input("temperature in Fahrenheit: "))
print(ftoc(F))
