import random

def deal_card():
    """Return a random card from the deck."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the total value of a player's hand."""
    score = 0
    num_aces = cards.count('A')
    
    for card in cards:
        if card == 'A':
            score += 11
        elif card in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(card)
    
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
        
    return score

def blackjack():
    player_cards = []
    computer_cards = []
    game_over = False
    
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if player_score == 21:
            print("Blackjack! You win!")
            game_over = True
        elif player_score > 21:
            print("Bust! You lose.")
            game_over = True
        else:
            action = input("Type 'hit' to get another card, or 'stand' to pass: ").lower()
            
            if action == 'hit':
                player_cards.append(deal_card())
            elif action == 'stand':
                game_over = True
        
        if not game_over:
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            
            print(f"Computer's cards: {computer_cards}, score: {computer_score}")
            
            if computer_score == 21:
                print("Computer has Blackjack! You lose.")
            elif computer_score > 21:
                print("Computer busts! You win!")
            elif computer_score > player_score:
                print("Computer wins.")
            elif computer_score < player_score:
                print("You win!")
            else:
                print("It's a draw!")
            
            game_over = True

if __name__ == "__main__":
    blackjack()
