'''You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.'''
from itertools import permutations

S,k = input().split()
permute_list = list(permutations(S,int(k)))
# print(permute_list)
for i in permute_list:
    print("".join(i).upper())