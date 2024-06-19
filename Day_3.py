#Choose your own adventure game where
#you the player will be asked a series of questions
#and based on the answer the direction of the game will change

#intro
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure.")

#1st input - choose whether left or right
left_or_right = input("You're at  a cross road.  Where do you want to go?  Type \"left\" or  \"right\":\n")


if left_or_right.upper() == "LEFT":
      wait_or_swim = input("You come to a lake. There is a island in the middle of the lake.  Type \"wait\" to wait for a boat.  Type \"swim\" to swim across.")
    

    #2nd input - choose whether to wait or swim
      if wait_or_swim.upper() == "WAIT":
            choose_door = input("You arrive at the island unharmed.  there is a house with 3 doors.  One red, one yellow, and one blue.  Which colour do you choose:/n")
      else:
            print("Attacked by Trout.\nGame Over.\n")

            #3rd input - choose which color door blue, yellow, or red
            if choose_door.upper() == "YELLOW":
                  print("You Win!")
            elif choose_door.upper() == "RED":
                  print("Burned by fire.\nGame Over\n")
            else:
                  print("You enter a room of beasts. Game Over.")           
else:
    print("Fall into a hole.\nGame Over.\n")
    

