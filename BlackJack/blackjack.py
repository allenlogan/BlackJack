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


def player(players):
    for i in range(2):
        players.append(deck())
    return players

# Count the users cards


def countCards(players):
    for player in players:
        result = 0
        for cardname in player:
            result += cards[cardname]
    total_result = 0
    for hand in players:
        result = 0
        for cardname in hand:
            result += cards[cardname]
        total_result += result
    return total_result


# Append a card to when the player wants a hit
def hits(players):
    for i in range(1):
        players.append(deck())
    return players

# Main code to run the game
def play():

    print("---Welcome To BlackJack---\n")

    # Print out the cards to the terminal
    print("Users hand:", str(player(userhand)).replace('[', '').replace(
        ']', '').replace("'", ''), "\nCard Total:", countCards(userhand))
    print("Dealers hand:", str(hits(dealerHand)).replace('[', '').replace(
        ']', '').replace("'", ''), "\nCard Total:", countCards(dealerHand))

    # player card counting configuration
    while countCards(userhand) < 21:
        # Ask if the player wants to hit or stand
        hit = input("\nWould you like to hit or stand? h or s\n")
        time.sleep(0.5)
        if hit == "h":
            print("Users new hand:", str(hits(userhand)).replace('[', '').replace(
                ']', '').replace("'", ''), "\nCard total after hit:", countCards(userhand))
        if hit == "s":
            print("User stands on: ", countCards(userhand))
            break
        if countCards(userhand) > 21:
            print("BUSTED! Too many cards.")
            print("Dealer wins.")
            return userBust
        if countCards(userhand) == 21:
            print("Congratulations you got BlackJack :)")

    # Dealer card counting configuration
    while countCards(dealerHand) <= 17:
        time.sleep(0.5)
        print("Dealers new hand:", str(hits(dealerHand)).replace('[', '').replace(
            ']', '').replace("'", ''), "\nDealers total:", countCards(dealerHand))
        if countCards(dealerHand) > 21:
            print("The dealer went bust!")
            print("Congratulations you win!")
        if countCards(dealerHand) == 21:
            print("Dealer got BlackJack, maybe next time :(")

    # Print if it there is a push
    if countCards(userhand) == countCards(dealerHand):
        print("Dealer has the same as user. Push.")
    if countCards(dealerHand) > countCards(userhand) and countCards(dealerHand) < 21:
        print("Dealer wins, sorry.")
    if countCards(dealerHand) < countCards(userhand) and countCards(userhand) < 21:
        print("Congratulations you win!")

    print("--- Thanks for playing ---")

play()
