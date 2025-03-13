VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    if len(hand) > 5 or any(card not in VALID_CARDS for card in hand): #If the hand has more than 5 cards, return "Invalid" (too many cards).
        return "Invalid"                                               #If any card in the hand is not in VALID_CARDS, return "Invalid" (invalid card detected).

    values = {'Jack': 10, 'Queen': 10, 'King': 10}
    total = 0 #will store the total points of the hand.
    ace_count = 0 #will count the number of Aces in the hand.

    for card in hand: # Loops through each card in the hand.
        if isinstance(card, int): #If the card is a number(2-10)add its value to total.
            total += card
        elif card in values: #If the card is a face card (Jack, Queen, King), add 10 points to total.
            total += values[card]
        elif card == "Ace": #If the card is an Ace, increase ace_count by 1.
            ace_count += 1 # Aces can be 1 or 11, so we handle them separately.

    total += ace_count * 11  # Assume all Aces are 11 first
    while total > 21 and ace_count > 0:
        total -= 10  # Convert an Ace from 11 to 1
        ace_count -= 1

    return "Bust" if total > 21 else total #If the total score is over 21 and there are Aces, change one Ace from 11 to 1.