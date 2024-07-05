#a simple game of blackjack
#programmed by Je Nolan 
#7/6/2024
# 

import random


#logo of blackjack


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#print(logo)

#play blackjackfunction
def playBlackJack():
    print(logo)
    
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #card values of the deck with Ace being 11
    
    #define dealer and the player, the player is dealt the first card, dealer is given the second card
    #player is given the third card, the dealer is given the fourth card ...... at random

    #place holders for the player and dealer
    dealer = []
    player = []

    #select random value from the cards values and place it into the players lists
    for cardLoop in range(2):
        randomCard = random.choice(cards)
        player.append(randomCard)
        randomCard = random.choice(cards)
        dealer.append(randomCard)
    
    print(player)
    print(dealer)


#ask the user if they want to play blackjack and continue the loop until they say no.

play = True #inital variable of true
while play:
    wantToPlay = input("Do you want to play a game of blackjack? Type 'y' or 'n' ")
    if wantToPlay.upper() == 'Y': #if the player wants to play then call play function
        
        playBlackJack()
    else:
        break #end game
