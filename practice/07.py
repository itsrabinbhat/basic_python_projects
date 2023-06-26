import string
def print_rangoli(size):
    patt = string.ascii_lowercase[:size]
    filler = '-'
    for i in range(1-size,size):
        k = size - abs(i)
        centr = filler.join(patt[size-1:size-k:-1] + patt[size - k:size])
        padding = filler * abs(i) * 2
        print(padding + centr + padding)
        




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)