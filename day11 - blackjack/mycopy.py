from typing import List
import random

blackjack_card = {
    "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5,
    "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9,
    "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10,
    "Ace of Hearts": 11,
    
    "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5,
    "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9,
    "10 of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10,
    "Ace of Diamonds": 11,
    
    "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5,
    "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9,
    "10 of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10,
    "Ace of Clubs": 11,
    
    "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5,
    "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9,
    "10 of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10,
    "Ace of Spades": 11
}

blackjack_list = list(blackjack_card.keys())

def playgame() -> None:
    """
    Simulates a game of blackjack between a player and a dealer.
    """
    blackjack_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    blackjack_card = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    # First randomly give two cards to each: Dealer and Player
    player = random.sample(blackjack_list, k=2)
    dealer = random.sample(blackjack_list, k=2)
    print(f"Player cards: {player}   Dealer cards: [{dealer[0]}, hidded card]")

    want_to_continue = input("Do you want to continue: y/n \n")
    
    if want_to_continue == 'y':
        player.append(random.choice(blackjack_list))
        dealer.append(random.choice(blackjack_list))
        
    player_score = calculate_score(player, blackjack_card)
    dealer_score = calculate_score(dealer, blackjack_card)

    print(f"Final Scores are: You as the Player {player_score}   --- Dealer {dealer_score} --- hence:")

    if player_score > 21:
        print("You lost, Sorry")
    elif dealer_score > 21 or player_score == 21:
        print("You won")
    elif player_score > dealer_score:
        print("You won")
    elif dealer_score > player_score:
        print("You lost, Sorry")
    else:
        print("It is a Draw")

def calculate_score(cards: List[str], blackjack_card: dict) -> int:
    """
    Calculates the score of a player or dealer based on the values of their cards.
    """
    return sum(blackjack_card[card] for card in cards)

hit_to_start = input("Do you want to play? HIT to start: (y/n):\n")

if hit_to_start.lower() == 'y':
    playgame()
else:
    print("No problem, come later when you are ready")
