city = "narva"

estonianPopulation = [
    ["tallinn", 441000],
    ["tartu", 94000],
    ["narva", 58000],
    ["parnu", 41000]
]

for p in estonianPopulation:
    if p[0] == city:
        print("Population of " + p[0].capitalize() + ": " + str(p[1]))
        break
