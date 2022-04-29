import sys
c = int(sys.stdin.readline());n = [0]*10001
for _ in range(c):a = int(sys.stdin.readline());n[a] += 1
for i in range(10001): 
    if (n[i] != 0):
        for j in range(n[i]): print(i)