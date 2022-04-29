import sys
c = int(sys.stdin.readline());n = []
for _ in range(c):n.append(int(sys.stdin.readline()))
n.sort(reverse=True)
for i in range(c): print(n[i])