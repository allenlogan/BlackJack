import random
from random import shuffle
import time

cards = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
         "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
userhand = []
dealerHand = []
userBust = False
dealerBust = False


# Define the deck
def deck():
    hand = []
    keys = list(cards.keys())
    random.shuffle(keys)
    shuffled = keys.pop()
    hand.append(shuffled)
    return hand

# Deal out the users cards


def user():
    for i in range(2):
        userhand.append(deck())
    return userhand

# Count the users cards


def countUser():
    for player in userhand:
        result = 0
        for cardname in player:
            result += cards[cardname]
    total_result = 0
    for hand in userhand:
        result = 0
        for cardname in hand:
            result += cards[cardname]
        total_result += result
    return total_result

# Deal the dealer the first card


def dealer():
    for i in range(1):
        dealerHand.append(deck())
    return dealerHand

# Count the dealers cards


def countDealer():
    for player in dealerHand:
        result = 0
        for cardname in player:
            result += cards[cardname]
        total_result = 0
    for hand in dealerHand:
        result = 0
        for cardname in hand:
            result += cards[cardname]
        total_result += result
    return total_result


# Append a card to when the user wants a hit
def userHit():
    for i in range(1):
        userhand.append(deck())
    return userhand

# Keep adding cards to the dealer until either bust or stand is initiated


def dealerHit():
    for i in range(1):
        dealerHand.append(deck())
    return dealerHand

# Main code to run the game
def play():

    print("---Welcome To BlackJack---\n")

    # Print out the cards to the terminal
    print("Users hand:", str(user()).replace('[', '').replace(
        ']', '').replace("'", ''), "\nCard Total:", countUser())
    print("Dealers hand:", str(dealer()).replace('[', '').replace(
        ']', '').replace("'", ''), "\nCard Total:", countDealer())

    # User card counting configuration
    while countUser() < 21:
        # Ask if the user wants to hit or stand
        hit = input("\nWould you like to hit or stand? h or s\n")
        time.sleep(0.5)
        if hit == "h":
            print("Users new hand:", str(userHit()).replace('[', '').replace(
                ']', '').replace("'", ''), "\nCard total after hit:", countUser())
        if hit == "s":
            print("User stands on: ", countUser())
            break
        if countUser() > 21:
            print("BUSTED! Too many cards.")
            print("Dealer wins.")
            return userBust
        if countUser() == 21:
            print("Congratulations you got BlackJack :)")

    # Dealer card counting configuration
    while countDealer() <= 17:
        time.sleep(0.5)
        print("Dealers new hand:", str(dealerHit()).replace('[', '').replace(
            ']', '').replace("'", ''), "\nDealers total:", countDealer())
        if countDealer() > 21:
            print("The dealer went bust!")
            print("Congratulations you win!")
            dealerBust = True
        if countDealer() == 21:
            print("Dealer got BlackJack, maybe next time :(")

    # Print if it there is a push
    if countUser() == countDealer():
        print("Dealer has the same as user. Push.")
    if countDealer() > countUser() and countDealer() < 21:
        print("Dealer wins, sorry.")
    if countDealer() < countUser() and countUser() < 21:
        print("Congratulations you win!")


play()
