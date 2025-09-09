import random
CURRENCIES = [20,50,100,200,500]
STARTING_BALANCE = 500
ascii_cards = {
    '??': """.--------.
|        |
|  ??    |
|        |
'--------'""",
    'A♠': """.--------.
|A       |
|   ♠    |
|       A|
'--------'""",
    '2♠': """.--------.
|2       |
|   ♠    |
|       2|
'--------'""",
    '3♠': """.--------.
|3       |
|   ♠    |
|       3|
'--------'""",
    '4♠': """.--------.
|4       |
|   ♠    |
|       4|
'--------'""",
    '5♠': """.--------.
|5       |
|   ♠    |
|       5|
'--------'""",
    '6♠': """.--------.
|6       |
|   ♠    |
|       6|
'--------'""",
    '7♠': """.--------.
|7       |
|   ♠    |
|       7|
'--------'""",
    '8♠': """.--------.
|8       |
|   ♠    |
|       8|
'--------'""",
    '9♠': """.--------.
|9       |
|   ♠    |
|       9|
'--------'""",
    '10♠': """.--------.
|10      |
|   ♠    |
|      10|
'--------'""",
    'J♠': """.--------.
|J       |
|   ♠    |
|       J|
'--------'""",
    'Q♠': """.--------.
|Q       |
|   ♠    |
|       Q|
'--------'""",
    'K♠': """.--------.
|K       |
|   ♠    |
|       K|
'--------'""",
    'A♥': """.--------.
|A       |
|   ♥    |
|       A|
'--------'""",
    '2♥': """.--------.
|2       |
|   ♥    |
|       2|
'--------'""",
    '3♥': """.--------.
|3       |
|   ♥    |
|       3|
'--------'""",
    '4♥': """.--------.
|4       |
|   ♥    |
|       4|
'--------'""",
    '5♥': """.--------.
|5       |
|   ♥    |
|       5|
'--------'""",
    '6♥': """.--------.
|6       |
|   ♥    |
|       6|
'--------'""",
    '7♥': """.--------.
|7       |
|   ♥    |
|       7|
'--------'""",
    '8♥': """.--------.
|8       |
|   ♥    |
|       8|
'--------'""",
    '9♥': """.--------.
|9       |
|   ♥    |
|       9|
'--------'""",
    '10♥': """.--------.
|10      |
|   ♥    |
|      10|
'--------'""",
    'J♥': """.--------.
|J       |
|   ♥    |
|       J|
'--------'""",
    'Q♥': """.--------.
|Q       |
|   ♥    |
|       Q|
'--------'""",
    'K♥': """.--------.
|K       |
|   ♥    |
|       K|
'--------'""",
    'A♦': """.--------.
|A       |
|   ♦    |
|       A|
'--------'""",
    '2♦': """.--------.
|2       |
|   ♦    |
|       2|
'--------'""",
    '3♦': """.--------.
|3       |
|   ♦    |
|       3|
'--------'""",
    '4♦': """.--------.
|4       |
|   ♦    |
|       4|
'--------'""",
    '5♦': """.--------.
|5       |
|   ♦    |
|       5|
'--------'""",
    '6♦': """.--------.
|6       |
|   ♦    |
|       6|
'--------'""",
    '7♦': """.--------.
|7       |
|   ♦    |
|       7|
'--------'""",
    '8♦': """.--------.
|8       |
|   ♦    |
|       8|
'--------'""",
    '9♦': """.--------.
|9       |
|   ♦    |
|       9|
'--------'""",
    '10♦': """.--------.
|10      |
|   ♦    |
|      10|
'--------'""",
    'J♦': """.--------.
|J       |
|   ♦    |
|       J|
'--------'""",
    'Q♦': """.--------.
|Q       |
|   ♦    |
|       Q|
'--------'""",
    'K♦': """.--------.
|K       |
|   ♦    |
|       K|
'--------'""",
    'A♣': """.--------.
|A       |
|   ♣    |
|       A|
'--------'""",
    '2♣': """.--------.
|2       |
|   ♣    |
|       2|
'--------'""",
    '3♣': """.--------.
|3       |
|   ♣    |
|       3|
'--------'""",
    '4♣': """.--------.
|4       |
|   ♣    |
|       4|
'--------'""",
    '5♣': """.--------.
|5       |
|   ♣    |
|       5|
'--------'""",
    '6♣': """.--------.
|6       |
|   ♣    |
|       6|
'--------'""",
    '7♣': """.--------.
|7       |
|   ♣    |
|       7|
'--------'""",
    '8♣': """.--------.
|8       |
|   ♣    |
|       8|
'--------'""",
    '9♣': """.--------.
|9       |
|   ♣    |
|       9|
'--------'""",
    '10♣': """.--------.
|10      |
|   ♣    |
|      10|
'--------'""",
    'J♣': """.--------.
|J       |
|   ♣    |
|       J|
'--------'""",
    'Q♣': """.--------.
|Q       |
|   ♣    |
|       Q|
'--------'""",
    'K♣': """.--------.
|K       |
|   ♣    |
|       K|
'--------'"""
}
deck = [rank + suit for suit in ['♥', '♣', '♠', '♦'] for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
random.shuffle(deck)

def print_ascii_cards(hand):
    lines = [""] * 5
    for card in hand:
        dash = ascii_cards.get(card, ascii_cards['??']).splitlines()
        for i in range(5):
            lines[i] += dash[i] + " "
    for line in lines:
        print(line)

def get_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank in ['J','Q','K']:
            value += 10
        elif rank == 'A':
            value += 11
            aces += 1
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_balance(balance):
    print(f"Player Current Balance: {balance}")

def get_initial_cards():
    player_hand = [deck.pop() for x in range(2)]
    dealer_hand = [deck.pop() for x in range(2)]
    return player_hand, dealer_hand

def player_turn(player_hand):
    while True:
        act = input("Choose action: (Hit, Stand, Split): ").lower()
        if act == 'hit':
            player_hand.append(deck.pop())
            print("Player Hand:")
            print_ascii_cards(player_hand)
            print(f"Value: {get_hand_value(player_hand)}")
            if get_hand_value(player_hand) > 21:
                return 'Bust'
            print("Dealer's Hand:")
            print_ascii_cards(dealer_hand)
            print(f"Value: {get_hand_value(dealer_hand)}")
        elif act == 'stand':
            return 'Stand'
        elif act == 'split' and player_hand[0][:-1] == player_hand[1][:-1]:
            return 'Split'
        else:
            print("Invalid Action!!")

def dealer_turn(dealer_hand):
    while get_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deck.pop())
    return dealer_hand

def game_winner(player_hand, dealer_hand):
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    if player_value > 21:
        return 'Dealer'
    elif player_value > dealer_value or dealer_value > 21:
        return 'Player'
    elif player_value < dealer_value:
        return 'Dealer'
    else:
        return 'Push'

player_balance = STARTING_BALANCE
display_balance(player_balance)
while player_balance > 0:
    if len(deck) < 15:
        deck = [rank + suit for suit in ['♥', '♣', '♠', '♦'] for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(deck)
    bet = int(input(f"Enter the bet ({'/'.join(map(str,CURRENCIES))}): "))
    if bet not in CURRENCIES or bet > player_balance:
        print("Invalid bet amount")
        continue
    player_hand, dealer_hand = get_initial_cards()
    print("Player Hand:")
    print_ascii_cards(player_hand)
    print(f"Value: {get_hand_value(player_hand)}")
    print("Dealer's Hand:")
    print_ascii_cards([dealer_hand[0],'??'])
    result = player_turn(player_hand)
    if result == 'Bust':
        print("Bust! You Lose.")
        player_balance -= bet
    elif result == 'Split':
        hand1 = [player_hand[0],deck.pop()]
        hand2 = [player_hand[1],deck.pop()]
        while True:
            print("Hand 1:")
            print_ascii_cards(hand1)
            print(f"Value: {get_hand_value(hand1)}")
            act1 = input("Choose action for Hand 1: (Hit, Stand): ").lower()
            if act1 == 'hit':
                hand1.append(deck.pop())
                if get_hand_value(hand1) > 21:
                    print("Bust! You Lose.")
                    player_balance -= bet
                    break
            elif act1 == 'stand':
                break
        while True:
            print("Hand 2:")
            print_ascii_cards(hand2)
            print(f"Value: {get_hand_value(hand2)}")
            act2 = input("Choose action for Hand 2: (Hit, Stand): ").lower()
            if act2 == 'hit':
                hand2.append(deck.pop())
                if get_hand_value(hand1) > 21:
                    print("Bust! You Lose.")
                    player_balance -= bet
                    break
            elif act2 == 'stand':
                break
        player_hand = [hand1, hand2]
        for hand in player_hand:
            dealer_hand = dealer_turn(dealer_hand)
            print("Dealer's Hand:")
            print_ascii_cards(dealer_hand)
            print(f"value: {get_hand_value(dealer_hand)}")
            winner = game_winner(hand,dealer_hand)
            if winner == 'Player':
                print("You Win!")
                player_balance += bet
            elif winner == 'Dealer':
                print("You Lose.")
                player_balance -= bet
            else:
                print("Push.")
    else:
        dealer_hand = dealer_turn(dealer_hand)
        print("Dealer's Hand:")
        print_ascii_cards(dealer_hand)
        print(f"value: {get_hand_value(dealer_hand)}")
        winner = game_winner(player_hand, dealer_hand)
        if winner == 'Player':
            print("You Win!")
            player_balance += bet
        elif winner == 'Dealer':
            print("You Lose.")
            player_balance -= bet
        else:
            print("Push.")
    display_balance(player_balance)
    if player_balance <= 0:
        print("You're Bankrupt!. {Game Over}")
        break
print("Thanks for playing.")