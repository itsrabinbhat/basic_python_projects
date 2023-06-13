import string
import random
# Function to generate strong random password
def pwd_generator(num,len):
    alphabets = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation
    chars = alphabets + numbers + special_chars

    print("\n- - - - - - - - - Your passwords are: - - - - - - - - - -".upper())
    for i in range(num):
        pwd = ''
        for j in range(len):
            pwd += random.choice(chars)
        print(pwd)

print("- - - - - - - - - - Welcome to password generator! - - - - - - - - - -".upper())
num = int(input("Enter number of passwords: "))
len = int(input("Enter length of password: "))
pwd_generator(num,len)