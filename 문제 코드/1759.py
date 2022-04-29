import sys 
from itertools import * 
input = sys.stdin.readline 

l,c= map(int, input().split()) 
arr = list(input().split());arr.sort() 
result = combinations(arr, l) 
aeiou = ['a', 'e', 'i', 'o', 'u'] 

for c in result: 
    jaum = 0 ;cnt = 0 
    for i in range(l): 
        if c[i] in aeiou: cnt += 1 
        else: jaum += 1 
    if cnt > 0 and jaum >= 2 : 
        print(''.join(c))