import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_cards = random.choice(cards)
    return random_cards
def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards)==2:
        return 0
    if score >21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return score
def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0 :
        return "Win with a blackjack"
    elif c_score == 0:
        return "Oops you lose"
    elif u_score>21:
        return "OOps you lose"
    elif c_score >21:
        return "You won"
    elif u_score >c_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    user_cards = []
    computer_score = -1
    user_score = -1
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards = {user_cards} and your score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            draw_another_card = input("Do you want to draw another card (yes/no) : \n").lower()
            if draw_another_card == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score <17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand :{user_cards} and your final score is : {user_score}")
    print(f"Computer final hand :{computer_cards} and computer's final score is : {computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play game (y/n)").lower() == "y":
    play_game()
