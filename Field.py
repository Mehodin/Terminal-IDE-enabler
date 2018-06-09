from random import choice, randint
from collections import namedtuple

def GetID():
    return randint(100000000, 1000000000)

class FindItem():
    def __init__(self, id):
        self.valid = choice([True, False])
        if self.valid:
            self.x = randint(-1500, 1500)
            self.y = randint(-3000, 3000)

class FindMob():
    def __init__(self, id):
        self.valid = choice([True, False])
        if self.valid:
            self.x = randint(-1500, 1500)
            self.y = randint(-3000, 3000)

class FindNpc():
    def __init__(self, id):
        self.valid = choice([True, False])
        if self.valid:
            self.x = randint(-1500, 1500)
            self.y = randint(-3000, 3000)

class FindPortal():
    def __init__(self, name):
        self.valid = choice([True, False])
        if self.valid:
            self.x = randint(-1500, 1500)
            self.y = randint(-3000, 3000)

class GetCharacters():
    possibleID = [0, 100, 110, 111, 112, 120, 121, 122, 130, 131, 132, 200, 210, 211, 212, 220, 221, 222, 230, 231, 232, 300, 310, 311, 312, 320, 321, 322, 400, 410, 411, 412, 420, 421, 422, 430, 431, 432, 433, 434, 500, 501, 508, 510, 511, 512, 520, 521, 522, 530, 531, 532, 570, 571, 572, 1000, 1100, 1110, 1111, 1112, 1200, 1210, 1211, 1212, 1300, 1310, 1311, 1312, 1400, 1410, 1411, 1412, 1500, 1510, 1511, 1512, 2000, 2001, 2002, 2003, 2004, 2100, 2110, 2111, 2112, 2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2300, 2310, 2311, 2312, 2400, 2410, 2411, 2412, 2500, 2510, 2511, 2512, 2700, 2710, 2711, 2712, 3000, 3001, 3002, 3100, 3101, 3110, 3111, 3112, 3120, 3121, 3122, 3200, 3210, 3211, 3212, 3300, 3310, 3311, 3312, 3500, 3510, 3511, 3512, 3600, 3610, 3611, 3612, 3700, 3710, 3711, 3712, 4001, 4002, 4100, 4110, 4111, 4112, 4200, 4210, 4211, 4212, 5000, 5100, 5110, 5111, 5112, 6000, 6001, 6100, 6110, 6111, 6112, 6500, 6510, 6511, 6512, 10000, 10100, 10110, 10111, 10112, 11000, 11200, 11210, 11211, 11212, 13000, 13100, 14000, 14200, 14210, 14211, 14212, 15000, 15200, 15210, 15211, 15212, 6002, 6400, 6410, 6411, 6412]

    class Buffer:
        Buffer = namedtuple('Buffer', ['valid', 'x', 'y', 'level', 'jobid', 'id', 'name'])

    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.valid = True
        self.x = randint(-1500, 1500)
        self.y = randint(-3000, 3000)
        self.id = randint(10000000, 100000000)
        self.level = randint(1, 250)
        self.jobid = choice(GetCharacters.possibleID)
        self.name = "CharacterName{}".format(self.count)
        self.count += 1
        if self.count > 5:
            raise StopIteration
        return self.Buffer.Buffer(self.valid, self.x, self.y, self.id, self.level, self.jobid, self.name)

class FindCharacter():
    def __init__(self, ID):
        self.valid = choice([True, False])
        self.x = randint(-1500, 1500)
        self.y = randint(-3000, 3000)
        self.id = randint(10000000, 100000000)
        self.level = randint(1, 250)
        self.jobid = choice(GetCharacters.possibleID)
        self.name = "CharacterName"

class FindCharacter():
    def __init__(self, strName):
        self.valid = choice([True, False])
        self.x = randint(-1500, 1500)
        self.y = randint(-3000, 3000)
        self.id = randint(10000000, 100000000)
        self.level = randint(1, 250)
        self.jobid = choice(GetCharacters.possibleID)
        self.name = "CharacterName"

def GetCharacterCount():
    return randint(0, 20)

def GetEliteState():
    return choice([0, 1, 2, 3])
