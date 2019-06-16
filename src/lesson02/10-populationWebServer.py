from simpleWebServer import SimpleWebServer

#---------------------------------------------------

usersCount = 0

estonianPopulation = {
    "tallinn" : 441000,
    "tartu" : 94000,
    "narva" : 58000,
    "parnu" : 41000
}

def getPopulation(path):
    global usersCount
    usersCount += 1

    city = path[1:]

    if city in estonianPopulation:
        return "Population of " + city + ": " + str(estonianPopulation[city]) + ". Users count: " + str(usersCount)
    else:
        return "I don't know such city: '" + city + "'"


#---------------------------------------------------

SimpleWebServer().serve(8088, getPopulation)