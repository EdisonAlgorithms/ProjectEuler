import random

class Chest:
    def __init__(self):
        deck = ['GO', 'JAIL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
        random.shuffle(deck)
        self.d = deck
    def draw(self):    #draw top card off chest deck, then place in bottom of deck
        temp = self.d
        topCard = temp[0]
        newTemp = []
        for i in range(len(temp)-1):
            newTemp.append(temp[i+1])
        newTemp.append(topCard)
        self.d = newTemp
        self.tc = topCard
        return self
        
class Chance:
    def __init__(self):
        deck = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'nextR', 'nextR', 'nextU', 'back3', 0, 0, 0, 0, 0, 0]
        random.shuffle(deck)
        self.d = deck
    def draw(self):    #draw top card off chance deck, then place in bottom of deck
        temp = self.d
        topCard = temp[0]
        newTemp = []
        for i in range(len(temp)-1):
            newTemp.append(temp[i+1])
        newTemp.append(topCard)
        self.d = newTemp
        self.tc = topCard
        return self

class Dice:    #n is number of sides
    def __init__(self, n):
        self.doubles = [0, 0]   # initialize last 2 rolls, 0 no double
        self.sides = n
        self.result = 0
    def roll(self):
        a = random.randint(1, self.sides)
        b = random.randint(1, self.sides)
        if a != b:    #normal roll
            self.doubles = [0, 0] #initialize doubles list again
            self.result = a + b
            return self
        elif a == b:
            if self.doubles == [1, 1]:  # last 2 were doubles
                self.result = 'JAIL'
                self.doubles = [0, 0]  # reset doubles
                return self
            elif self.doubles[0] == 0:  # most recent roll was not double
                self.doubles = [1, 0]
                self.result = a + b
                return self
            elif self.doubles[0] == 1:  # most recent roll was a double
                self.doubles = [1, 1]
                self.result = a + b
                return self

moveInstructions = {'GO':0, 'JAIL':10, 'C1':11, 'E3':24, 'H2':39, 'R1':5}
chestLoc = [2, 17, 33]
chanceLoc = {7:(15,12), 22:(25,28), 36:(5,12)}  #make this a dictionary, mapped to tuple (nextR, nextU)
chest1 = Chest()
chance1 = Chance()
dice1 = Dice(4)
railroads = [5, 15, 25, 35]
utilities = [12, 28]

class Player:
    def __init__(self):
        self.position = 0   #start at Go
    def move(self):
        dice1.roll()
        if dice1.result == 'JAIL':
            self.position = 10
            return self
        else:
            testPosition = self.position + dice1.result
            # there are only 39 positions, so check testPosition, 40 is same as 0
            if testPosition >= 40:
                testPosition = testPosition - 40
            if testPosition == 30:  # go to Jail
                self.position = 10
                return self
            elif testPosition in chestLoc:   #landed on community chest
                chest1.draw()
                if chest1.tc in moveInstructions:
                    self.position = moveInstructions[chest1.tc]
                    return self
                else:
                    self.position = testPosition
                    return self
            elif testPosition in chanceLoc:  #landed on chance
                chance1.draw()
                if chance1.tc in moveInstructions:
                    self.position = moveInstructions[chance1.tc]
                    return self
                elif chance1.tc == 'back3':
                    check = testPosition - 3  #no need to worry about negatives here
                    if check != 33:  #back 3 moved you on to community chest
                        self.position = check
                        return self
                    elif check == 33:
                        chest1.draw()
                        if chest1.tc in moveInstructions:
                            self.position = moveInstructions[chest1.tc]
                            return self
                        else:
                            self.position = check
                            return self
                elif chance1.tc == 'nextR':
                    self.position = chanceLoc[testPosition][0]
                    return self
                elif chance1.tc == 'nextU':
                    self.position = chanceLoc[testPosition][1]
                    return self
                else:
                    self.position = testPosition
                    return self
            else:
                self.position = testPosition
                return self

landed = [0 for x in range(40)]   #initialize list of indices 0 to 39 with value 0

rob = Player()
for moves in range(100000):
    rob.move()
    landed[rob.position] += 1

psorted = landed[:]
psorted = sorted(psorted)

# looks like each index is 2 digits, so you don't need to write a script to convert single digits like '1' to '01
answer = str(landed.index(psorted[-1])) + str(landed.index(psorted[-2])) + str(landed.index(psorted[-3]))

print answer
