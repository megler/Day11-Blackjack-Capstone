# blackjack.py
#
# Python Bootcamp Day 11 - Blackjack
# Usage:
#      Play some blackjack
#
# Marceia Egler October 5, 2021


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from replit import clear
from art import logo
import random

def game_loop(): 
    '''Game runs until user chooses to stop playing'''
    clear()
    print(logo) 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hands = {
        "p1": { 
            "cards": [],
            "score":0,
        },
        "dealer": {
            "cards": [],
            "score":0,
        },    
    }

    which_player = ["p1", "dealer"]
    game = True

    def test_bj():
        '''Test for blackjack''' 
        for player in which_player:              
            if hands[player]['score'] == 21 and len(hands[player]["cards"]) == 2:
                print(f'{player} has {hands[player]["cards"]} for blackjack!')
                return True           
        else:
            return False 

    def test_ace():
        '''Test if ace is treated as 1 or 11'''
        for player in which_player:
            if len(hands[player]["cards"]) > 1:
                if hands[player]["cards"][-1] == 11:
                    if sum(hands[player]["cards"]) > 21:
                        hands[player]["cards"][-1] = 1
                    else:
                        hands[player]["cards"][-1] = 11

    def opening_hand(): 
        '''Deal opening hand'''       
        if len(hands["p1"]["cards"]) < 2:
            for player in which_player:
                hands[player]["cards"] = [random.choice(cards), random.choice(cards)]
                test_ace()
                hands[player]["score"] = sum(hands[player]["cards"])

    def deal():
        '''Deal additional card if player chooses'''
        if hands["p1"]['score'] < 21:            
            hands["p1"]["cards"].append(random.choice(cards))
            test_ace()
            hands["p1"]["score"] = sum(hands["p1"]["cards"])

    def dealer_turn(): 
        '''Handle dealer\'s hand after user is done''' 
        deal = True 
        while deal:
            if hands["dealer"]["score"] <= 16:

                hands["dealer"]["cards"].append(random.choice(cards))
                test_ace()
                hands["dealer"]["score"] = sum(hands["dealer"]["cards"])

            elif 21 >= hands["dealer"]["score"] > hands["p1"]['score']:

                print(f'Dealer has {hands["dealer"]["cards"]} for a total of {hands["dealer"]["score"]}\nand you have {hands["p1"]["cards"]} for a total of {hands["p1"]["score"]}. Dealer wins.')
                deal = False

            elif hands["dealer"]["score"] == hands["p1"]["score"]:

                print(f'Dealer has {hands["dealer"]["cards"]} for a total of {hands["dealer"]["score"]}\nand you have {hands["p1"]["cards"]} for a total of {hands["p1"]["score"]}. You tie.')
                deal = False

            else:

                print(f'Dealer has {hands["dealer"]["cards"]} for a total of {hands["dealer"]["score"]}\nand you have {hands["p1"]["cards"]} for a total of {hands["p1"]["score"]}. You win.')
                deal = False
 
    while game:  
        opening_hand()      
        if test_bj():
            game = False
        elif hands["p1"]['score'] > 21:
            print(f"You have {hands['p1']['cards']} for a total of {hands['p1']['score']}.\nYou bust. Game over")
            game = False
        elif hands["p1"]['score'] <= 21:
            if input(f"The dealer has {hands['dealer']['cards'][0]} showing.\nYou have {hands['p1']['cards']} for a total of {hands['p1']['score']}.\nDo you want to hit or stay? ").lower() == 'hit':                
                deal()
            else:                
                dealer_turn()
                game = False
    if input('Do you want to play again? Y/N ').lower() == 'y':
        game_loop()
    else:
        return "Thanks for playing!"

game_loop()