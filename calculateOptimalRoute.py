from random import randint
from itertools import permutations
import math
from csvParse import csvParse

# graph = [[randint(1,10) for i in range(4)] for j in range(4)]
graph = csvParse("distanceMatrix.csv")

n = len(graph)

routes = list(permutations([i for i in range(n)]))

bestRoute = ()

minDistance = math.inf

for curRoute in routes:
    distance = 0
    prevCity = -1
    for curCity in curRoute:
        if prevCity != -1:
            distance += graph[prevCity][curCity]
        prevCity = curCity
    if distance < minDistance:
        minDistance = distance
        bestRoute = curRoute

print(minDistance)
print(bestRoute)

