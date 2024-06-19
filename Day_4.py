# Rock, Paper, Scissors Random game
import random 

#create a random integer betwee 0-2
#representing rock (0),paper(1),scissors(2)

# Rock (0)
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper (1)
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors (2)
scissors = """
    _______
---'   ____)_______
          _________)
       _____)
      (____)
---.__(___)
"""

computer_choice = random.randint(0,2)

#user chooses rock paper scissors

player_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#print out the computer's choice and the player's choic
game_images =[rock,paper,scissors]


print("Computer")
print(game_images[computer_choice])

#if computer_choice == 0:
#    print(rock)
#elif computer_choice == 1:
#    print(paper)
#else: computer_choice == 2:
#    print(scissors)

#print out player's choice

print("Player")
print(game_images[player_choice])
#if player_choice == 0:
#    print(rock)
#elif player_choice == 1:
#    print(paper)
#else:
#    print(scissors)



#if the both choices are the same then its a tie
if player_choice == computer_choice:
    print ("its a draw")
elif player_choice == 0 and computer_choice == 2:
    print("Player wins")
elif player_choice == 0 and computer_choice == 1:
    print("Computer wins")
elif player_choice == 1 and computer_choice == 0:
    print("Player Wins")
elif player_choice == 1 and computer_choie == 2:
    print("Computer Wins")
