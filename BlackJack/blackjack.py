import random

# Set out the deck and assign the values of the picture cards
import time


def deck():
    hand = []
    cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    totalCards = list(cards.items())
    random.shuffle(totalCards)
    card = totalCards.pop()
    hand.append(card)
    return hand


# Deal the hands to the user and dealer
def dealTheHand():
    userHand = []
    dealerHand = []
    # Deal the user
    for i in range(2):
        userHand.append(deck())
    print("Users current hand:", str(userHand).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("'", "").replace("'", ""), "\nTotal:")#, sum(listuserHand))
    # Deal the dealer
    for dealer in range(1):
        dealerHand.append(deck())
    print("Dealer current hand:", str(dealerHand).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("'", "").replace("'", ""), "\nTotal:")
    # If the user doesnt want another card, deal the next card to the dealer
    # if stand():
    #     dealerHand.append(deck())
    # print(dealerHand)


# Deal another card to the user
def hit():
    print("Card dealt")


# User wants to stand on current cards
def stand():
    print("User stands.")
    return False


def userHitOrStand():
    hitOrStand = input("Would you like to hit of stand. \n").lower()
    if hitOrStand == 'hit':
        time.sleep(0.5)
        hit()
    if hitOrStand == 'stand':
        time.sleep(0.5)
        stand()


def play():
    print("---Welcome to BlackJack!---")
    time.sleep(0.5)
    dealTheHand()
    userHitOrStand()


play()