import time

roomArray = []
itemArray = []
for i in range(999):
    roomArray.append(False)
    itemArray.append(False)
roomArray[601] = "There is an antique box here with a jewel inside. There is a couch to the south and you see something shiny to the east."
roomArray[701] = "You are in the north east corner of the study"
roomArray[702] = "There is a chair to the south and a couch to the west. You see something shiny to the north."
roomArray[703] = "There is a chair here with a hat sitting on it. There is a door to the west."
roomArray[202] = "There is a table to your east and a TV to your south."
roomArray[203] = "The TV is all static and doesn't work, there is a remote on the tv. It looks like there is a hallway to your east."
roomArray[302] = "There is a interesting painting on the table. There is opening in the wall to the south."
roomArray[303] = "There is echoing coming down the hallway to your east and a tv to your west."
roomArray[403] = "You have entered the hallway. There is something on the ground. There are more rooms east. An echo is getting slightly louder."
roomArray[503] = "You are close to the end of the hallway. There is a window here and the echo is louder. There is a coin on the window sill and a room to your east."
roomArray[603] = "You are not in the hallway anymore, you are in a study. There is a chair to the east, a couch to the north, and a door to the south."
roomArray[602] = "There is a couch here with a couch and a scarf. There is an antique box to the north."
roomArray[604] = "You are now in the kitchen. There is a table in front of you."
roomArray[605] = "There is a table here. There is a counter to the east."
roomArray[606] = "You found your brother!"
roomArray[705] = "There is a "
roomArray[706] = "There is"
itemArray[601] = "Jewel"
itemArray[703] = "Hat"
itemArray[602] = "Scarf"
itemArray[503] = "Coin"
itemArray[203] = "Remote"
itemArray[302] = "Painting"
roomArray[705] = "knife"
roomArray[706] = "bowl"
itemArray[604] = "spoon"
itemArray[605] = "plate"
itemArray[403] = "glove"
itemArray[701] = "key"

def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print("You can't go there.")
            return False
        else:
            return True
    except:
        print("You can't go there.")
        return False

def moveFunction(userInput, room):
    if userInput == "n" and doesRoomExist(room - 1) == True:
        room = room - 1
    elif userInput == "s" and doesRoomExist(room + 1) == True:
        room = room + 1
    elif userInput == "e" and doesRoomExist(room + 100) == True:
        room = room + 100
    elif userInput == "w" and doesRoomExist(room - 100) == True:
        room = room - 100
    return room

def doesItemExist(itemNumber):
    try:
        if not itemArray[itemNumber] == False:
            print("Item" + itemArray[room])
    except:
      return

def main():
    room = 202
    print("Welcome to Mansion Mystery!")
    time.sleep(1)
    print("By Callie, Shayan, and Dalton.")
    time.sleep(1)
    print("You are in the living room of a mansion. You're brother has been captured by some angry ghosts, and it is your job to save him.")
    time.sleep(2)
    while True:
      print(roomArray[room])
      if not itemArray[room] == False:
        print(itemArray[room])
        print("Please type: n, s, e, w, take or quit.")
      else:
        print("Please type: n, s, e, w,  or quit.")
      userInput = input()
      room = moveFunction(userInput, room)
      if userInput == "take":
        print("You have taken this item: " + itemArray[room])
      if userInput == "quit":
        break
