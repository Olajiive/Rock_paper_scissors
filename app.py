import random

def play():
    user= input("Whats your choice?'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it is a tie'

    # r > s, s > p
    if is_win(user, computer):
        return "you won!"
    
    return "You lost!"

def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
        return True

print(play())