import random
playerIn = True
dealerIn = True

# Deck of cards / player-dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
         'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

# deal cards
def deal(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# get total of player-dealer's hands
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# reveal dealer's hand
def reavealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# game loop
for _ in range(2):
    deal(dealerHand)
    deal(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had {reavealDealerHand()} and X")
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
    elif total(dealerHand):
        break

# determine winner
if total(playerHand) == 21:
    print(f"\nYou have {playerHand} for a total of 21 and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! You win!")
elif total(dealerHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of 21")
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






