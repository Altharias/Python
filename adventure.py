import random

random.seed()

#location dir declaration
#cords - first one is column, second one is row
houseLocations = \
                [
                    ['Entrance', 0,0],
                    ['Living Room', 0,1],
                    ['Kitchen', 1,1],
                    ['Bedroom', 1,0],
                    ['Corridor', 1,-1],
                    ['Bathroom', 1,-2],
                ]

#location list length
houseLocationsLength = len(houseLocations)


#current location
currentLocationCords = [0,0]
currentLocation = houseLocations

class Character(object):
    def __init__(self, name, lvl, exp, gold, attack, defense, health, curr_hp, att_points, str, agi, con, int, wis, cha):
        self.name = name
        self.lvl = attack
        self.exp = exp
        self.gold = gold
        self.attack = attack
        self.defense = defense
        self.health = health
        self.curr_hp = curr_hp
        self.att_points = att_points
        self.str = str
        self.agi = agi
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

class Slots(object):
    def __init__(self, head, torso, legs, left_hand, right_hand, ring1, ring2, necklace, cape):
        self.head = head
        self.torso = torso
        self.legs = legs
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.ring1 = ring1
        self.ring2 = ring2
        self.necklace = necklace
        self.cape = cape

class Item(object):
    def __init__(self, name, attack, armor, weight, price, slot):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price
        self.slot = slot

class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def del_item(self, item):
        del self.items[item.name]

    def __str__(self):
        out = '\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val', 'Slot'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price, item.slot]])
        return out
#Functions declaration
#Check where player is
def whereAmI():
    i = 0
    while(i<=houseLocationsLength-1):
        if currentLocationCords[0:2] == currentLocation[i][1:3]:
            print("Nazwa lokacji: " + str(currentLocation[i][0]) + "\nCords: " + str(currentLocationCords[0:2]))
            break
        i += 1

#eq actions
def showEq():
    exit = False;
    while(exit == False):
        print("This is your current equipment list: ")
        print(Inventory)
        choice = input("\nWhat you want to do?\n1. Equip new item.\n2. Unequip one of items.\n3. Exit from equipment\n")
        if(choice == "3"):
            exit = True
            break;
        elif(choice == "1"):
            equip = input("Insert name of item to equip: ")
            for item in Inventory.items.keys():
                if equip in Inventory.items.keys():
                    Protagonist.attack += Inventory.items.get(equip).attack
                    Protagonist.defense += Inventory.items.get(equip).armor
                    item_slot = Inventory.items.get(equip).slot

                    if (item_slot == "head"):
                        Equipment.head = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "torso"):
                        Equipment.torso = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "legs"):
                        Equipment.legs = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "left_hand"):
                        Equipment.left_hand = Inventory.items.get(equip).name
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "right_hand"):
                        Equipment.right_hand = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "ring1"):
                        Equipment.ring1 = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "ring2"):
                        Equipment.ring2 = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "necklace"):
                        Equipment.necklace = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    elif (item_slot == "cape"):
                        Equipment.cape = Inventory.items.get(equip)
                        Inventory.del_item(Inventory.items.get(equip))
                    else:
                        print("This item is not wearable.")
                    print(Equipment.head);
                    print(Equipment.torso);
                    print(Equipment.legs);
                    print(Equipment.left_hand);
                    print(Equipment.right_hand);
                    print(Equipment.ring1);
                    print(Equipment.ring2);
                    print(Equipment.necklace);
                    print(Equipment.cape);
                    break
                else:
                    print("Not implemented yet")
                    break
        elif(choice == "2"):
            print("Not implemented yet")
        else:
            print("Wrong input. Try again.")



#Check if new location exist
def ifCordsExist(cords):
    i = 0
    while(i<=houseLocationsLength-1):
        if currentLocationCords[0:2] == currentLocation[i][1:3]:
            return True
        i += 1
    return False

def action(action):
    desiredLocation = currentLocationCords

    if action == "N":
        desiredLocation[0] += 1
        if ifCordsExist(desiredLocation[0:2])==False:
            print("Nie możesz udać się w tym kierunku")
            desiredLocation[0] -= 1

    elif action == "S":
        desiredLocation[0] -= 1
        if ifCordsExist(desiredLocation[0:2])==False:
            print("Nie możesz udać się w tym kierunku")
            desiredLocation[0] += 1

    elif action == "W":
        desiredLocation[1] -= 1
        if ifCordsExist(desiredLocation[0:2])==False:
            print("Nie możesz udać się w tym kierunku")
            desiredLocation[1] += 1

    elif action == "E":
        desiredLocation[1] += 1
        if ifCordsExist(desiredLocation[0:2])==False:
            print("Nie możesz udać się w tym kierunku")
            desiredLocation[1] -= 1

    elif action == "Eq":
        showEq()

    elif action == "Where":
        whereAmI()
    else:
        print("Invalid input. Insert N//S/W/E to move in desired directon, Eq if you want to see your equipment or"
              " Where to get information about where is your character")

#class objects
Inventory = Inventory()

Empty = Item("Empty", 0, 0, 0, 0, 'universal')
Sword = Item("Sword", 3, 0, 5, 5, 'left_hand')
Armor = Item("Armor", 0, 10, 5, 20, 'torso')
Shield = Item("Shield", 2, 5, 5, 5, "right_hand")

Protagonist = Character("1", 1, 0, 0, 0, 0, 10, 10, 1, 0, 0, 0, 0, 0, 0)
Goblin = Character("Goblin", 1, 600, 0, 10, 10, 20, 20, 0, 2, 4, 4, 1, 1, 1)
Equipment = Slots(Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty)

Inventory.add_item(Empty)
#lvl up thing
def doLvlUp():
    Protagonist.lvl += 1;
    Protagonist.att_points += 2
    chosenAttribute = input("Choose attribute you want to increase: ")
    attributeUp(chosenAttribute)

def recalculateHP():
    Protagonist.health = (10+Protagonist.con)*Protagonist.lvl
    Protagonist.curr_hp = Protagonist.health

def checkForLvlUp():
    if Protagonist.exp == Protagonist.lvl*(Protagonist.lvl-1)*500:
        doLvlUp()
        recalculateHP()
    else:
        return

def doRoll():
    roll = random.randint(1, 20)
    return roll

def attTest(att, dc):
    print("Not implemented yet.")

def attributeUp(att):
    if att == "Strength" : Protagonist.str += 1
    elif att == "Agility" : Protagonist.str += 1
    elif att == "Constitution" : Protagonist.str += 1
    elif att == "Inteligence" : Protagonist.str += 1
    elif att == "Wisdom" : Protagonist.str += 1
    elif att == "Charisma" : Protagonist.str += 1
    else:
        print("Invalid input.")
        return
    Protagonist.att_points -= 1;

#main game
play = True
#welcome message
print("Hello, welcome to the 'Adventure'. It is a text based RPG game.\n"
      "Firstly, you need to distribute 12 point between attributes, which are:\n"
      "Strength - it increases your melee damage and helps you in Strength tests.\n"
      "Agility - increases your ranged damage, your chance to dodge attack and helps you in Agility tests.\n"
      "Constitution - increases your hp and helps you in Constitution tests.\n"
      "Inteligence - increases your exp gain and helps you in Inteligence tests.\n"
      "Wisdom - helps you in Wisdom tests, which can provide some info about situation. It's your intuition, basicly.\n"
      "Charisma - helps you in Charisma test. Persuade someone etc.\n\n"
      "Now, write attribute that you want to increase.")

#character creation
while(Protagonist.att_points!=0):
    chosenAttribute = input("Choose attribute: ")
    attributeUp(chosenAttribute)
recalculateHP()
print('Strength: ' + str(Protagonist.str))
print('Agility: ' + str(Protagonist.agi))
print('Constitution: ' + str(Protagonist.con))
print('Inteligence: ' + str(Protagonist.int))
print('Wisdom: ' + str(Protagonist.wis))
print('Charisma: ' + str(Protagonist.cha))

Protagonist.name = input("And now tell me your name... ")

#start of the game
print("You are in home, in your beedrom. For the purpose of this test I'll give you some equipment...")
Inventory.add_item(Sword)
Inventory.add_item(Armor)
Inventory.add_item(Shield)
print("And now try to equip them in EQ menu.")
while(play == True):

    action(input("What you want to do?\n"))
