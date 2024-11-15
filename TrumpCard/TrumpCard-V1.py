import random

# Define the suits and ranks for a standard deck of cards
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

# Create a full deck of cards
deck = [{'rank': rank, 'suit': suit, 'value': value} for rank, value in ranks.items() for suit in suits]

# Function to draw a random card
def draw_card():
    return random.choice(deck)

# Main game logic
def run():
    # Player's card
    my_card = draw_card()
    print(f"You were dealt the {my_card['rank']} of {my_card['suit']}.")

    # Let the player choose to compare rank or suit
    choice = input("Do you want to compare by 'rank' or 'suit'? ").strip().lower()
    while choice not in ['rank', 'suit']:
        choice = input("Invalid choice. Please choose 'rank' or 'suit': ").strip().lower()

    # Opponent's card
    opponent_card = draw_card()
    print(f"The opponent was dealt the {opponent_card['rank']} of {opponent_card['suit']}.")

    # Compare based on player's choice
    if choice == 'rank':
        my_value = my_card['value']
        opponent_value = opponent_card['value']
        if my_value > opponent_value:
            print("You Win!")
        elif my_value < opponent_value:
            print("You Lose!")
        else:
            print("It's a Draw!")
    elif choice == 'suit':
        # Compare suits alphabetically (Clubs < Diamonds < Hearts < Spades)
        my_suit_value = suits.index(my_card['suit'])
        opponent_suit_value = suits.index(opponent_card['suit'])
        if my_suit_value > opponent_suit_value:
            print("You Win!")
        elif my_suit_value < opponent_suit_value:
            print("You Lose!")
        else:
            print("It's a Draw!")

# Run the game
run()
