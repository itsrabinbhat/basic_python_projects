import random
def play():
    print("Enter (R) for rock, (P) for paper & (S) for scissor!")
    user=input("Enter your choice: ").strip().lower()
    comp = random.choice(['r','p','s'])
    if user == comp:
        return("It's a draw!")
    elif is_win(user,comp):
        return("You win!")
    return "You lost!"


def is_win(user,comp):
    #r>s, p>r & s>p
    if user == 'r' and comp == 's':
        return True
    elif user == 'p' and comp == 'r':
        return True
    elif user == 's' and comp == 'p':
        return True

print(play())
