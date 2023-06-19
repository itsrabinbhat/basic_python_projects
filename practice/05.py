'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.'''
import string
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase

user_input = input("Enter a string: ")

def swap_case(str):
    swapped_str = ''
    for i in str:
        if i in upper_letters:
            swapped_str += i.lower()
        elif i in lower_letters:
            swapped_str += i.upper()
        else:
            swapped_str += i
    print(swapped_str)
            
swap_case(user_input)