'''Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1. Keep calling the function until it returns 1'''

try:
    num = int(input("Enter an integer: "))

    def collatz(val):
        if val % 2 == 1:
            val = 3 * val + 1
        elif val % 2 == 0:
            val = val // 2
        return val

    while num != 1:
        num = collatz(num)
        print(num)
        
except ValueError:
    print("Enter a valid integer")

