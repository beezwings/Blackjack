# Python End-of-Week Project:: Black Jack Game
# Version 4.0 by Jessie Litven

# import modules for shuffle and pausing
import random
import time

# Intro
print "\n\n::::::::Welcome to Blackjack::::::::\n\n"
print "  _________ \n |2        |\n |+        |\n |    +    |\n |         |\n |        +|\n |        Z|\n  ~~~~~~~~~ "

# Establish suits, names of cards, and creates and empty deck
suits = ["Hearts", "Clubs" , "Diamonds" , "Spades"]
names = ["Ace" , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , "Jack" , "Queen" , "King" ]

deck = []

# Creates the "Card" class
class Card(object):

    name = "No value"
    suit = "No suit"
    value = "No value"
    cardtype = "No value"

    def __init__(self, name, suit, value, cardtype):
        self.name = name
        self.suit = suit
        self.value = value
        self.cardtype = cardtype

# Creates the 52 card-objects by looping over each suit and then each names, and then appending it to the deck
# First loop over each suit
for counter, suit in enumerate(suits):
    # Then loop over each type of card
    for counter, name in enumerate(names):

        #If it's the ace, it gets a default value of 1 so as not to bust
        if name == "Ace":
            newCard = Card(name = str(name) + " of " + suit, suit = suit, value = 11, cardtype = "Ace")
        elif name == "Jack" or name == "Queen" or name == "King":
            newCard = Card(name = str(name) + " of " + suit, suit = suit, value = 10, cardtype = "Facecards")
        else:
            newCard = Card(name = str(name) + " of " + suit, suit = suit, value = int(name), cardtype = "Numbered Cards")
        deck.append(newCard)

# GAME STARTS!!
playerMoney = 100

# DEALER SHUFFLES THE DECK
raw_input(" Hit ENTER to shuffle the deck")
# Some fun "graphics"
shufflegraphics = 0
while shufflegraphics<7:
    print ":::~~~~:::::~~~~:::::~~~~:::::~~~~"
    time.sleep(.15)
    shufflegraphics +=1
random.shuffle(deck) # This is the code that actually shuffles the deck (imported at file start)

# PLAYER MAKES A BET
while len(deck)>10 and playerMoney>=1: # makes sure there's at least 6 cards in the deck to play, and at least $1 dollar to bet
    print "\nYou have $%s." %(playerMoney)
    while True:
        try:
            playerBet = int(raw_input(" How much would you like to bet? $")) # Prompts the player to enter a bet amount
            if playerBet > playerMoney: #Won't allow a bet larger than the player's current money total
                print "I'm sorry, you aren't that rich. You only have $%s." %(playerMoney)
                continue
            else:
                break
        except:
            print "You typed an invalid amount. Please try again.\n" # Error message in case player enters a non-numerical value
            continue

    # Calculates player's money remaining balance (total minus bet)
    playerMoney = playerMoney-playerBet
    print "Your remaining balance is: $%s" %(playerMoney)
    print "\nGreat! Let's get started.\n"
    time.sleep(.25) # Short pause

    # Sets the initial hand-totals to 0
    playerhandTotal = 0
    dealerhandTotal = 0

    # MORE FUNCTIONS FOR THE GAME

    # Function for taking a card out of the deck and placing it into a hands
    def dealCard(playerHand):
        playerHand.append(deck.pop())

    # Function for dealing the initial hand
    def dealHand():

        # Establishes empty arrays for each player and the dealer
        playerHand = []
        dealerHand = []

        # Deals a total of 4 cards
        dealCard(playerHand)
        dealCard(dealerHand)
        dealCard(playerHand)
        dealCard(dealerHand)

        # Dispays player's hand and dealers hand
        print "\n  MY HAND:"
        for card in playerHand:
            print "   %s" %(card.name)

        time.sleep(.15) #Short pause
        print "\n  DEALER'S HAND:\n   X \n   %s" %(dealerHand[1].name)

        return {"playerHand" : playerHand, "dealerHand": dealerHand}

    # Calculates the hand's total, taking into account the ace
    def calcTotal(hand):
        total = 0
        for card in hand: # First total the non-aces
            total = total + int(card.value)

        for card in hand: # Then deals with the aces. Aces are initially set to a value of 11, but if it makes the hand
            if total > 21 and card.cardtype == "Ace":
                total = total -10 # recalculates the total with the new ace value

        return total

    # Displays the cards in the hands
    def displayHand(hand, player):
        print "\n  %s HAND:" %(player) # Prints updated hand and calculates the hand total
        for card in hand:
            print "   %s" %(card.name)


    hands = dealHand() # Runs the function and returns an array

    # Player decides to stay or hit. Note hands["playerHand"] refers to player's hand while hands["dealerHand"] refers to dealer's hand
    while True:

        # Calculates the initial total of the player's hands
        playerhandTotal = calcTotal(hands["playerHand"])
        #print "playerhand total = %s" %(playerhandTotal)

        # As long as player doesn't have blackjack, cpu prompts user to hit or stay.
        if playerhandTotal != 21:

            # First, player decides to hit or stay
            playerDecision = raw_input("\nEnter H to hit or S to stay.")
            if playerDecision == "H" or playerDecision == "h":
                time.sleep(.45) #short pause
                dealCard(hands["playerHand"]) # Takes next card in deck and appends it to the player's hand
                displayHand(hands["playerHand"], "MY") # Display's the player's hand
                playerhandTotal = calcTotal(hands["playerHand"]) # Calculates the player's total
                if playerhandTotal > 21: # Automatically the player loses if they bust
                    # playerMoney stays the same since it was deducted at betting time (no code required)
                    time.sleep(.25) #short pause
                    displayHand(hands["dealerHand"], "DEALER'S") # Displays the dealer's hand, just to show what they had
                    print "\n You bust! Your hand totals:%s \n You lose your money, wahnwahn." %(playerhandTotal)
                    break
                elif playerhandTotal == 21: # If the player gets to 21, there are no more hits, and goes to the dealer...
                    print "No more hits! You're at 21. Let's see how the hands compare..."
                    time.sleep(.55) #short pause
                    pass
                else:
                    # print "\nYour hand total is:%s" %(playerhandTotal) # Prints player total. Uncomment this if you don't want the user to do their own math
                    continue
            elif playerDecision == "S" or playerDecision == "s":
                    pass
            else:
                print "You didn't choose a valid option. Please try it again."
                continue

        # If the player has 21, ie blackjack, it's either a win (if dealer has less) or a push (if dealer also has blackjack)
        else:
            time.sleep(.65) #short pause
            print "\n  You have blackjack! Let's see how the hands compare..."
            time.sleep(.65) #short pause
            pass

        # Dealer's turn enclosed in its own while loop
        while True:

            # First, it's established that the dealer will hit with a hand of 16 or lower, regardless of player's decisions
            dealerhandTotal = calcTotal(hands["dealerHand"]) # Calculate total
            if dealerhandTotal<=16:
                dealCard(hands["dealerHand"]) # takes next card in deck and appends it to the dealer's hand
                continue
            else:
                break

        # DETERMINE THE WINNER

        # Shows players hand and gets value of hand total using "displayHand" function
        displayHand(hands["playerHand"], "MY")
        playerhandTotal = calcTotal(hands["playerHand"]) # Deals with the Ace

        print "\n  MY TOTAL: %s" %(playerhandTotal)
        time.sleep(.25) # Short pause

        # Shows dealer's hand and gets value of hand total using "displayHand" function
        displayHand(hands["dealerHand"], "DEALER'S")
        dealerhandTotal = calcTotal(hands["dealerHand"]) # Deals with the Ace

        print "\n  DEALER TOTAL: %s" %(dealerhandTotal)
        time.sleep(.25) # Short pause

        # If dealer busts, player wins money
        if dealerhandTotal > 21:
            playerMoney = playerMoney + playerBet*2
            print "\n  Dealer Busts! Congrats! You won that round. Yay!"
            break
        # If player hand is higher than dealer's without busting, player wins money
        elif dealerhandTotal < playerhandTotal:
            playerMoney = playerMoney + playerBet*2
            print "\n  Congrats! You won that round as you had higher cards. Yay!"
            break
        # If dealer's hand and player's hand are equal, it's a push. No money is lost.
        elif dealerhandTotal == playerhandTotal:
            playerMoney = playerMoney + playerBet
            print "\n  It's a push. You get your bet money back."
            break
        # Only alternative is dealer has higher cards and player loses money
        else:
            print "\n  Boo! You lose! Dealer had higher cards"
            break
        continue
else:
    print "The game is over. Either there aren't any more cards, or you ran out of money (you ended up with $%s). Either way, time to go outside." %(playerMoney)


# :::::: NOTES:
# Here is the format for:
# examplCard1 = Card(name = str(names[0]) + " of " + suits[0], suit = suits[0], value = (1,11))
# deck.append(card1.name)

#this code keeps editor window open
raw_input()
