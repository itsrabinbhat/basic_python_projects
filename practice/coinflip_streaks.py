# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.

import random
streaks = 0
results = []
#generate a list of 'heads' and 'tails'
for i in range(10000):
    flip = random.randint(0,1)
    if flip == 0:
        results.append("T")
    else:
        results.append("H")

#check for the streaks in the list
heads = 0
tails = 0
for x in results:
    if x == "H":
        tails = 0
        heads += 1
        if heads == 6:
            streaks +=1
            heads = 0
    else:
        heads = 0
        tails += 1
        if tails == 6:
            streaks +=1
            tails = 0


print(streaks)