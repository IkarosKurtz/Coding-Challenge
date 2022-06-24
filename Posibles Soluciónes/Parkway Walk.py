class Benchs:
    def __init__(self, _benchs, _energy, _distance):
        self.totalBenchs = _benchs
        self.energy = _energy
        self.distanceBewteenBenchs = _distance
        
    def Walk(self, distance):
        totalDistance = 0
        for i in range(self.distanceBewteenBenchs.__len__()):
            totalDistance = totalDistance + self.distanceBewteenBenchs[i] 
            
        if self.energy >= totalDistance:
            self.energy = 0
            return
        
        self.energy = self.energy - distance

        totalDistance = totalDistance - self.distanceBewteenBenchs[0]
        self.energy = totalDistance - self.energy

cases = int(input())
results = []
for i in range(cases):
    benchsAndEnergy = list(map(int, input().split(" ")))
    distanceBetweenBenchs = list(map(int, input().split(" ")))

    calculateMinEnergy = Benchs(benchsAndEnergy[0], benchsAndEnergy[1], distanceBetweenBenchs)
    calculateMinEnergy.Walk(distanceBetweenBenchs[0])

    results.append(calculateMinEnergy.energy)

for i in range(results.__len__()):
    print(results[i])