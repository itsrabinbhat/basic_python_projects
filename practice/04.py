'''Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).'''

x = input()
int_list = map(int,x.split())
t = tuple(int_list)

print(hash(t))