import numpy as np
import random as rm

# Determine whether or not the pulled card is red or black
def red_or_black(card_pulled):
    card_pulled = card_pulled[1]

    if card_pulled == "D" or card_pulled == "H":
        card_color = "red"
    else:
        card_color = "black"
    return card_color

# Determine whether or not the pulled card is higher or lower than the first card
def higher_or_lower(higher_lower_card_pulled, red_black_card_pulled):
    higher_lower_card_pulled = higher_lower_card_pulled[0]
    red_black_card_pulled = red_black_card_pulled[0]


    if higher_lower_card_pulled >= red_black_card_pulled:
        lower_or_higher = "higher"
    else:
        lower_or_higher = "lower"
    return lower_or_higher

# Determine whether or not the third pulled card is between the first two pulled cards
def inside_or_outside(pulled_red_black, pulled_higher_lower, pulled_inside_outside):
    pulled_red_black = pulled_red_black[0]
    pulled_higher_lower = pulled_higher_lower[0]
    pulled_inside_outside = pulled_inside_outside[0]

    if pulled_red_black >= pulled_inside_outside >= pulled_higher_lower: #or pulled_red_black <= pulled_inside_outside <= pulled_higher_lower:
        outside_or_inside = "inside"
    else:
        outside_or_inside = "outside"
    return outside_or_inside

# Determine whether or not the fourth pulled card is the predicted suit
def suit(pulled_card):
    pulled_card = pulled_card[1]

    if pulled_card == 'H':
        pulled_card = 'hearts'
    elif pulled_card == 'D':
        pulled_card == 'diamonds'
    elif pulled_card == "C":
        pulled_card = 'clubs'
    else:
        pulled_card = 'spades'

    return pulled_card

deck = [['C', '1'], ['C', '2'], ['C', '3'], ['C', '4'], ['C', '5'], ['C', '6'], ['C', '7'], ['C', '8'], ['C', '9'], ['C', '11'], ['C', '12'], ['C', '13'], ['C', '10'], ['D', '1'], ['D', '2'], ['D', '3'], ['D', '4'], ['D', '5'], ['D', '6'], ['D', '7'], ['D', '8'], ['D', '9'], ['D', '11'], ['D', '12'], ['D', '13'], ['D', '10'], ['H', '1'], ['H', '2'], ['H', '3'], ['H', '4'], ['H', '5'], ['H', '6'], ['H', '7'], ['H', '8'], ['H', '9'], ['H', '11'], ['H', '12'], ['H', '13'], ['H', '10'], ['S', '1'], ['S', '2'], ['S', '3'], ['S', '4'], ['S', '5'], ['S', '6'], ['S', '7'], ['S', '8'], ['S', '9'], ['S', '11'], ['S', '12'], ['S', '13'], ['S', '10']]



#determine positions of pulled cards
position_in_deck_red_or_black = rm.randint(0, len(deck)-1)
position_in_deck_higher_or_lower = rm.randint(0, len(deck)-1)
position_in_deck_inside_or_outside = rm.randint(0, len(deck)-1)
position_in_deck_suit = rm.randint(0, len(deck)-1)

# Pull first card
pulled_card_red_or_black = str(deck[position_in_deck_red_or_black])
pulled_card_red_or_black = pulled_card_red_or_black[7] + pulled_card_red_or_black[2]

# Pull second card
pulled_card_higher_or_lower = str(deck[position_in_deck_higher_or_lower])
pulled_card_higher_or_lower = pulled_card_higher_or_lower[7] + pulled_card_higher_or_lower[2]

# Pull third card
pulled_card_inside_or_outside = str(deck[position_in_deck_inside_or_outside])
pulled_card_inside_or_outside = pulled_card_inside_or_outside[7] + pulled_card_inside_or_outside[2]

# Pull fourth card
pulled_card_suit = str(deck[position_in_deck_suit])
pulled_card_suit = pulled_card_suit[7] + pulled_card_suit[2]



# If any two cards are the same, redraw
while pulled_card_red_or_black == pulled_card_higher_or_lower or pulled_card_red_or_black == pulled_card_inside_or_outside or pulled_card_inside_or_outside == pulled_card_higher_or_lower or pulled_card_red_or_black == pulled_card_suit or pulled_card_higher_or_lower == pulled_card_suit or pulled_card_inside_or_outside == pulled_card_suit:
    
    if pulled_card_red_or_black == pulled_card_higher_or_lower:
        position_in_deck_higher_or_lower = rm.randint(0, len(deck)-1)
        pulled_card_higher_or_lower = str(deck[position_in_deck_higher_or_lower])
        pulled_card_higher_or_lower = pulled_card_higher_or_lower[7] + pulled_card_higher_or_lower[2]
    
    if pulled_card_red_or_black == pulled_card_inside_or_outside:
        position_in_deck_inside_or_outside = rm.randint(0, len(deck)-1)
        pulled_card_inside_or_outside = str(deck[position_in_deck_inside_or_outside])
        pulled_card_inside_or_outside = pulled_card_inside_or_outside[7] + pulled_card_inside_or_outside[2]

    if pulled_card_inside_or_outside == pulled_card_higher_or_lower:
        position_in_deck_higher_or_lower = rm.randint(0, len(deck)-1)
        pulled_card_higher_or_lower = str(deck[position_in_deck_higher_or_lower])
        pulled_card_higher_or_lower = pulled_card_higher_or_lower[7] + pulled_card_higher_or_lower[2]

    if pulled_card_red_or_black == pulled_card_suit:
        position_in_deck_suit = rm.randint(0, len(deck)-1)
        pulled_card_suit = str(deck[position_in_deck_suit])
        pulled_card_suit = pulled_card_suit[7] + pulled_card_suit[2]

    if pulled_card_higher_or_lower == pulled_card_suit:
        position_in_deck_suit = rm.randint(0, len(deck)-1)
        pulled_card_suit = str(deck[position_in_deck_suit])
        pulled_card_suit = pulled_card_suit[7] + pulled_card_suit[2]

    if pulled_card_inside_or_outside == pulled_card_suit:
        position_in_deck_suit = rm.randint(0, len(deck)-1)
        pulled_card_suit = str(deck[position_in_deck_suit])
        pulled_card_suit = pulled_card_suit[7] + pulled_card_suit[2]
    
''' print(pulled_card_red_or_black)
    print(pulled_card_higher_or_lower)
    print(pulled_card_inside_or_outside)
    print(pulled_card_suit)'''



# Have user predict whether the first card will be red or black
red_or_black_input = input('red or black? ')

# determine whether or not user's prediction was correct and exit if wrong
if red_or_black_input == red_or_black(pulled_card_red_or_black):
    print('pulled card was,', pulled_card_red_or_black)
else:
    print('pulled card was', red_or_black(pulled_card_red_or_black), "try again next time!")
    exit()

# Have the user predict whether the second card will be higher or lower than the first card
higher_or_lower_input = input('higher or lower? ')

# determine whether or not user's prediction was correct and exit if wrong
if higher_or_lower_input == higher_or_lower(pulled_card_higher_or_lower, pulled_card_red_or_black):
    print('pulled card was,', pulled_card_higher_or_lower)
else:
    print('pulled card was', higher_or_lower(pulled_card_higher_or_lower, pulled_card_red_or_black), 'try again next time!')
    exit()

# Have the user predict whether or not the third card will be between the first two
inside_or_outside_input = input('inside or outside? ')

# Determine whether inside/outside prediction was correct
if inside_or_outside_input == inside_or_outside(pulled_card_red_or_black, pulled_card_higher_or_lower, pulled_card_inside_or_outside):
    print('pulled card was,', pulled_card_inside_or_outside)
else:
    print('pulled card was', inside_or_outside(pulled_card_red_or_black, pulled_card_higher_or_lower, pulled_card_inside_or_outside), 'try again next time!')
    exit()

# Have user predict suit of next card
suit_input = input('What is the suit of the next card?')

# Determine whether suit prediction was correct
if suit_input == suit(pulled_card_suit):
    print('pulled card was,', pulled_card_suit, 'You won, congratulations!')
else:
    print('pulled card was', suit(pulled_card_suit), 'So close! Try again next time!')
    exit()




print(red_or_black(pulled_card_red_or_black))
print(pulled_card_red_or_black)