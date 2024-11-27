import random
import requests

#Creates a new deck + shuffles
deck_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(deck_url)
deck_data = response.json()
#extracts the deck ID
deck_id = deck_data['deck_id']

#Draws a random card
def draw_card():
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
    response = requests.get(draw_url)
    if response.status_code == 200:
        draw_data = response.json()
        return draw_data['cards'][0]
    else:
        print("Error fetching card!")
        return None

suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']

#Gives value to each rank
def rank_value(rank):
    face_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12,
                  'King': 13, 'Ace': 14}
    return face_cards.get(rank.upper(), 0)


# Main game logic
def run():

    ##my attempt on scoreboard
    player_score = 0
    opponents_score = 0

    while True:
        # Player's card
        my_card = draw_card()
        print(f"\nYou were dealt the {my_card['value']} of {my_card['suit']}.")

        # Let the player choose to compare rank or suit, or exit
        choice = input("Do you want to compare by 'rank', 'suit', or 'exit' to leave the game? ").strip().lower()
        if choice == 'exit':
            print('\n' + '-' * 24)
            print(f'| {"SCORE BOARD":^20} |')
            print('=' * 24)
            print(f'|👤 YOUR SCORE    : {player_score:>3}|')
            print(f'|🤖 OPPONENT SCORE: {opponents_score:>3}|')
            print('-' * 24)
            print("Thanks for playing! Goodbye!")
            break
        while choice not in ['rank', 'suit']:
            choice = input("Invalid choice. Please choose 'rank', 'suit', or 'exit': ").strip().lower()
            if choice == 'exit':
                print('\n' + '-' * 24)
                print(f'| {"SCORE BOARD":^20} |')
                print('=' * 24)
                print(f'|👤 YOUR SCORE    : {player_score:>3}|')
                print(f'|🤖 OPPONENT SCORE: {opponents_score:>3}|')
                print('-' * 24)
                print("Thanks for playing! Goodbye!")
                return

        # Opponent's card
        opponent_card = draw_card()
        print(f"The opponent was dealt the {opponent_card['value']} of {opponent_card['suit']}.")

        # Compare based on player's choice
        if choice == 'rank':
            my_value = rank_value(my_card['value'])
            opponent_value = rank_value(opponent_card['value'])
            if my_value > opponent_value:
                player_score += 1
                print("You Win!")
            elif my_value < opponent_value:
                opponents_score += 1
                print("You Lose!")
            else:
                print("It's a Draw!")
        elif choice == 'suit':
            # Compare suits alphabetically (Clubs < Diamonds < Hearts < Spades)
            my_suit_value = suits.index(my_card['suit'].upper())
            opponent_suit_value = suits.index(opponent_card['suit'].upper())
            if my_suit_value > opponent_suit_value:
                player_score += 1
                print("You Win!")
            elif my_suit_value < opponent_suit_value:
                opponents_score += 1
                print("You Lose!")
            else:
                print("It's a Draw!")

# Run the game
run()
