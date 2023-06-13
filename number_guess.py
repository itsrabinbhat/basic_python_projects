import random

#function for user guess
def user_guess(upper_limit):
    num = random.randint(1,upper_limit)
    guess = 0
    while guess != num:
        guess= int(input("Enter you guess: "))
        if guess < num:
            print("Your guess is too low!")
        elif guess > num:
            print("Your guess is too high!")
    if guess == num:
        print(f"Yay, Your guessed number {num} correctly, Congrats!\n" )
        print('')

#function for computer guess
def com_guess(low,high):
    num = int(input("Enter your num: "))
    guess = 0
    while guess != num:
        guess = random.randint(low,high)
        print(f"My guess is {guess}")
        user_res = input("Enter (H) for too high, (L) for too low and (C) for correct guess: ").lower()
        if user_res == "h":
            high -= 1
        elif user_res == "l":
            low = guess
    
    print(f"Yay, I guessed your number {num} correctly!\n")

#Asking user for player turn
count = 1
while count != 0:
    choice = input("Enter (G) to guess the number or (C) to let computer guess your number: ").lower()
    if choice == 'g':
        user_guess(10)
        count = 0
    elif choice == 'c':
        print('Enter your upper and lower limit!')
        low = int(input("Lower limit: "))
        high = int(input("Upper limit: "))
        com_guess(low,high) 
        count = 0
    else:
        print("Enter a valid choice!")
