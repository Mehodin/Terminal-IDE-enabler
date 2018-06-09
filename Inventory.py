from random import choice, randint
def GetItemCount(ID):
    return randint(0, 1000)

def GetItemSlotCount(InventoryType):
    return randint(16, 64)

def GetEmptySlotCount(InventoryType):
    return randint(1, 5)

#class FindItemByID():
