city = "parnu"

estonianPopulation = {
    "tallinn" : 441000,
    "tartu" : 94000,
    "narva" : 58000,
    "parnu" : 41000
}

if city in estonianPopulation:
    print("Population of", city.capitalize(), ":", estonianPopulation[city])
else:
    print("Не знаю такого города: '" + city + "'")