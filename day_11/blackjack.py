#a simple game of blackjack
#programmed by Je Nolan 
#7/6/2024
# 

import random
from art import blackjack
from replit import clear

#logo of blackjack




#play blackjackfunction
def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #card values of the deck with Ace being 11
    return random.choice(cards)
''' Calculcate score of players and dealer'''

def calculateSum(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(playerScore, dealerScore):
    if playerScore >21 and dealerScore>21:
        return ("You went over. You lose. 😤")
    
    if playerScore == dealerScore:
        return "Draw 🙃"
    elif dealerScore == 0:
        return "Lose, opponent has Blackjack 😱"
    elif playerScore == 0:
        return "Win with a Blackjack 😎"
    elif playerScore >21:
        return "You went over. You Lose 😭"
    elif dealerScore > 21:
        return "Opponent went over. You win 😁"
    elif playerScore>dealerScore:
        return "You win 😃"
    else:
        return "You lose 😤"

def playBlackJack():
    print(blackjack)
    
       
    #define dealer and the player, the player is dealt the first card, dealer is given the second card
    #player is given the third card, the dealer is given the fourth card ...... at random

    #place holders for the player and dealer
    dealer = []
    player = []
    game_over = False

    #select random value from the cards values and place it into the players lists
    for cardLoop in range(2):   
        player.append(deal_cards())
        dealer.append(deal_cards())
'''    
    print(player)
    print(f"[{dealer[0]}, X]")
'''
    #calculate sums of both the player and the dealer but only show the player sum
    while not game_over:
    
        playerScore = calculateSum(player)
        dealerScore = calculateSum(dealer)

        print(f"   Player's cards: {player}, Player's score: {playerScore}")
        print(f"   Dealer's cards: {dealer[0]})")
    if playerScore == 0 or dealerScore == 0 or playerScore > 21:
        game_over = True
    else:
        dealAnotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
        if dealAnotherCard.upper() == 'Y':
            player.append(deal_cards())
        else:
            game_over = True

    while dealerScore !=0 and dealerScore <17:
        dealer.append(deal_cards())
        dealerScore = calculateSum(dealer)

        print(f" Your final hand: {player}, final score: {playerScore}")
        print(f" Dealer's final hand:{dealer}, dealer score: {dealerScore}")
        print(compare(playerScore,dealerScore))

 #inital variable of true
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    playBlackJack()
