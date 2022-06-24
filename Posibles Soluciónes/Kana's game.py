import math
class Quest():

    def __init__(self, _hitpoints, _voidAbSpells, _lightningStrikeSpells):
        self.hitPoints = _hitpoints
        self.voidAbSpells = _voidAbSpells
        self.lightningStrikeSpells = _lightningStrikeSpells

    def UseVoidAbsorptionSpell(self, _hitPoints):
        hitPoints = int(_hitPoints / 2) + 10
        self.voidAbSpells = self.voidAbSpells - 1
        return hitPoints

    def UseLightningStrikeSpell(self, _hitPoints):
        hitPoints = _hitPoints - 10
        self.lightningStrikeSpells = self.lightningStrikeSpells - 1
        return hitPoints

    def IsDead(self):
        if self.hitPoints <= 0:
            return True
        else:
            return False

def Game():
    totalCases = 0
    while totalCases < 1 or totalCases >= 1000:
        totalCases = int(input())

    cases = []
    for i in range(totalCases):
        cases.append([])
        for j in range(3):
            cases[i].append(-100)

    for i in range(totalCases):

        """ Values
            cases[i][0] = hitPoints = life points
            cases[i][1] = voidAbSpells = (hitPoints / 2) + 10
            cases[i][2] = lightningStrikeSpells = hitPoints - 10
        """

        values = input().split(" ")
        values = list(map(int, values))

        while cases[i][0] < 1 or cases[i][0] > math.pow(10, 5):
            cases[i][0] = values[0]
            if cases[i][0] < 1 or cases[i][0] > math.pow(10, 5):
                cases[i][0] = int(input("Valid Hitpoints: "))

        while cases[i][1] < 0 or cases[i][1] > 30:
            cases[i][1] = values[1]
            if cases[i][1] < 0 or cases[i][1] > 30:
                cases[i][1] = int(input("Valid Void Absorption Spells: "))

        while cases[i][2] < 0 or cases[i][2] > 30:
            cases[i][2] = values[2]
            if cases[i][2] < 0 or cases[i][2] > 30:
                cases[i][2] = int(input("Valid Lightning Strike Spells: "))

    for i in range(totalCases):
        quest = Quest(cases[i][0], cases[i][1], cases[i][2])
        
        while quest.voidAbSpells > 0 and quest.hitPoints > 10:
            quest.hitPoints = quest.UseVoidAbsorptionSpell(quest.hitPoints)
            
        while quest.lightningStrikeSpells > 0:
            quest.hitPoints = quest.UseLightningStrikeSpell(quest.hitPoints)
            if quest.IsDead():
                break
            
        if quest.IsDead():
            print("YES")
        else:
            print("NO")
            
Game()