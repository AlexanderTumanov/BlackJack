import random
playerIn = True
dealerIn = True
replayN = False
# make deck and hands

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K']
playerHand = []
dealerHand = []

# deal cards

def deal(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

# calculate total

def total(turn):
        total = 0
        faces = ['J', 'Q', 'K']
        for card in turn:
                if card in range(1, 11):
                        total += card
                elif card in faces:
                        total += 10
                else:
                        if total + 11 > 21:
                                total += 1
                        else:
                                total += 11
        return total

# reveal dealer hand

def revealDealerHand():
        if len(dealerHand) == 2:
                return dealerHand[0]
        elif len(dealerHand) > 2:
                return dealerHand[0], dealerHand[1]

def checkForWin():
    if total(playerHand) and total(dealerHand) == 21:
        print(
            f"\nYou have {playerHand} for a total of 21 and the dealer has {dealerHand} for a total of 21")
        print("Push! Both have 21!")
    elif total(playerHand) == 21:
        print(
            f"\nYou have {playerHand} for a total of 21 and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! You win!")
    elif total(dealerHand) == 21:
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of 21")
        print("Blackjack! Dealer wins!")
    elif total(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You bust! Dealer wins!")
    elif total(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer bust! You win!")
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer wins!")
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You win!")



# replay functionality

def replay():
    global playerIn
    global dealerIn
    global playerHand
    global dealerHand
    global replayN
    global deck
    
    asking = True

    while asking == True:
        replayAsk = input("Would you like to play again? (y/n): ")

        if replayAsk == "y":
            asking = False
            playerIn = True
            dealerIn = True
            playerHand.clear()
            dealerHand.clear()
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K']
            main()
        elif replayAsk == "n":
            print("Thank you for playing!")
            replayN = True
            asking = False
        else:
            print("Please enter y or n")

# game loop
def main():
    global playerIn
    global dealerIn
    for _ in range(2):
        deal(playerHand)
        deal(dealerHand)

    while playerIn == True or dealerIn == True:
        print(f"Dealer had {revealDealerHand()} and X")
        print(f"You have {playerHand} for a total of {total(playerHand)}")
        if playerIn:
            stayOrHit = input("1: Stand\n2: Hit\n")
        if total(dealerHand) > 16:
            dealerIn = False
        else:
            deal(dealerHand)
        if stayOrHit == '1':
            playerIn = False
        else:
            deal(playerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break
        
    checkForWin()


if replayN == False:
    main()
    replay()








