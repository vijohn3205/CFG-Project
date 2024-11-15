# Game Rules

1. Each card has a rank (e.g., 2, 3, ..., King, Ace) and a suit (Hearts, Diamonds, Clubs, Spades).
2. Players can compare either the rank (higher rank wins) or suit (e.g., alphabetical: Clubs < Diamonds < Hearts < Spades).
3. If the ranks or suits are the same, it's a draw.

# Code overview
* Deck Initialization: A full deck is created with all combinations of ranks and suits.
* Stat Comparison: Players choose whether to compare by rank (numerical value of the card) or suit (alphabetical order of the suits).
* Random Draw: Each card is drawn randomly, ensuring fairness.
* Winner Determination: The program compares the chosen attribute and declares the winner or a draw.

# How to Play
1. Run the game.
2. The program deals a random card to the player and the opponent.
3. Choose whether to compare rank or suit.
4. The result is displayed based on the comparison.

# Key Additions in version 2
* Game Loop: The game now runs in a while True loop to allow multiple rounds.
* Exit Option: Players can type exit to leave the game.
* Replay Prompt: After each round, the game returns to the start unless the player chooses to exit.
