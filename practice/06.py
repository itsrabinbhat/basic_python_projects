def draw_patt(n,m):
    pattern = '.|.'
    filler = '-'

    #Top
    for i in range(1, n, 2):
        print((pattern * i).center(m, filler))

    #Middle
    print("WELCOME".center(m, filler))

    #Bottom
    for i in range(n-2, -1, -2):
        print((pattern * i).center(m, filler))


if __name__ == "__main__":
    a,b = input().split()
    draw_patt(int(a),int(b))