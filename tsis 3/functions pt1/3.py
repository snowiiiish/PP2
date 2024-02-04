def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return (chickens, rabbits)
    return (None, None)

numheads = int(input("Enter the number of heads: "))
numlegs = int(input("Enter the number of legs: "))
print(solve(numheads, numlegs))
