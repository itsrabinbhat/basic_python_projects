import random
from words import words
import string
from hangman_visuals import lives_visual_dict

print("- - - - - - - - - H A N G M A N - - - - - - - - - -\n")

#function that selects a random word from the word_list
def select_word(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in words:
        word = random.choice(words_list)
    return word.upper()
#Function that runs the game
def play():
    word = select_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("Your used letters are: ",' '.join(used_letters))

        #current word (W - R D)
        word_list=[letter if letter in used_letters else '-' for letter in word]

        print('Current word: ', ' '.join(word_list))
        print(lives_visual_dict[lives])

        user_input = input("Guess a letter: ").upper()

        if user_input in alphabets:
            if user_input in used_letters:
                print(f"You have already used the letter {user_input}, Guess another letter.")
            elif user_input in alphabets - used_letters:
                used_letters.add(user_input)
                if user_input in word_letters:
                    word_letters.remove(user_input)
                else:
                    lives -= 1
                    print(f"Your letter {user_input} is not in the word.")
        else:
            print("Please enter a valid alphabet!")

    if lives == 0:
        print(lives_visual_dict[0])
        print(f"You lost, Try again!\nThe word was {word}")
    else:
        print("\nYay, You guessed the word", word,"correctly!!!")



play()
