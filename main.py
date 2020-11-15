############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import art
import random

cards = [u"\u2660 A", u"\u2660 2", u"\u2660 3", u"\u2660 4", u"\u2660 5", u"\u2660 6", u"\u2660 7", u"\u2660 8",
         u"\u2660 9", u"\u2660 10", u"\u2660 J", u"\u2660 Q", u"\u2660 K",
         u"\u2665 A", u"\u2665 2", u"\u2665 3", u"\u2665 4", u"\u2665 5", u"\u2665 6", u"\u2665 7", u"\u2665 8",
         u"\u2665 9", u"\u2665 10", u"\u2665 J", u"\u2665 Q", u"\u2665 K",
         u"\u2666 A", u"\u2666 2", u"\u2666 3", u"\u2666 4", u"\u2666 5", u"\u2666 6", u"\u2666 7", u"\u2666 8",
         u"\u2666 9", u"\u2666 10", u"\u2666 J", u"\u2666 Q", u"\u2666 K",
         u"\u2663 A", u"\u2663 2", u"\u2663 3", u"\u2663 4", u"\u2663 5", u"\u2663 6", u"\u2663 7", u"\u2663 8",
         u"\u2663 9", u"\u2663 10", u"\u2663 J", u"\u2663 Q", u"\u2663 K"]
drawn_cards = []


def card_draw(input_player):
    valid_hand = False
    while not valid_hand:
        temp_draw = random.choice(cards)
        # print(f"{input_player['title'].title()} attempts to draw {temp_draw}.\n")
        if temp_draw not in drawn_cards:
            input_player['hand'].append(temp_draw)
            drawn_cards.append(temp_draw)
            # print(f"{temp_draw} is drawn by {input_player['title']}.")
            print(f"{input_player['title']} draws a card.")
            valid_hand = True
        else:
            card_draw(input_player)


def count_score(input_player):
    input_player['score'] = 0
    for card in input_player['hand']:
        if card[len(card) - 1] in ["J", "Q", "K"]:
            input_player['score'] += 10
        elif card[len(card) - 1] == "A" and input_player['score'] + 11 > 21:
            input_player['score'] += 1
        elif card[len(card) - 1] == "A":
            input_player['score'] += 11
        elif card[len(card) - 2] + card[len(card) - 1] == "10":
            input_player['score'] += 10
        else:
            input_player['score'] += int(card[len(card) - 1])


def display_state():
    count_score(dealer)
    count_score(player)
    if not game_ended():
        print(f"Dealer's first card: {dealer['hand'][0]}. Dealer has {len(dealer['hand'])} cards in total.")
    else: print(f"Dealer's hand: {dealer['hand']}. Dealer has {len(dealer['hand'])} cards in total, and score is {dealer['score']}")
    print(f"Player's hand: {player['hand']} (total cards: {len(player['hand'])}), and score: {player['score']}.")


def game_ended():
    winner, buster, draw = "", "", False
    if dealer['score'] == 21 != player['score']:
        winner = dealer['title']
    elif dealer['score'] == 21 == player['score']:
        draw = True
    elif dealer['score'] != 21 == player['score']:
        winner = player['title']
    elif dealer['score'] > 21 > player['score']:
        winner = player['title']
        buster = dealer['title']
    elif dealer['score'] < 21 < player['score']:
        winner = dealer['title']
        buster = player['title']
    elif dealer['score'] > 21 < player['score']:
        draw = True
    elif dealer['score'] < player['score'] and dealer['stands'] and player['stands']:
        winner = player['title']
    elif dealer['score'] > player['score'] and dealer['stands'] and player['stands']:
        winner = dealer['title']
    elif dealer['score'] == player['score'] and dealer['stands'] and player['stands']:
        draw = True
    if len(winner) > 0 and len(buster) > 0:
        print(f"\n{winner.title()} is a winner, {buster.title()} is a bust.")
        return True
    elif len(winner) > 0:
        print(f"\n{winner.title()} is a winner.")
        return True
    elif draw:
        print("\nThe game is a draw.")
        return True
    else:
        return False


print(art.logo)
print("Welcome to Blackjack Python.")
print("Let's play.\n")

dealer = {'hand': [], 'score': 0, 'title': "Dealer", 'stands': False}
player = {'hand': [], 'score': 0, 'title': "Player", 'stands': False}
trading_round = 0
for i in range(2):
    card_draw(dealer)
    card_draw(player)
display_state()
while not game_ended():
    trading_round += 1
    print(f"\nTrading round {trading_round} begins.\n")
    if dealer['score'] < 17 and not dealer['stands']:
        card_draw(dealer)
    else:
        print("Dealer stands.\n")
        dealer['stands'] = True
    if not player['stands']:
        if input("Hit? (Type \"y\" to draw a card.) ").lower() == "y":
            card_draw(player)
        else:
            player['stands'] = True
    display_state()