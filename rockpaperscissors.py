import random


def play():
    user = input('R for Rock, P for paper, S for scissors').lower()
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    
    if is_win(user, computer):
        return f'You win with {user} from {computer} of computer'
    else:
        return f'You lost with {user} from {computer} of computer'

    

def is_win(player, opponent):
    PlayerWin = (player == 'r' and opponent == 's') \
        or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p')
    
    return PlayerWin
    
    
    
print(play())