import sys
input = sys.stdin.readline

s = [0]+list(input().rstrip())
x = [0]+list(input().rstrip())
ls = len(s)
lx = len(x)
LCS = [[0] * lx for _ in range(ls)]
for i in range(1,ls):
    for l in range(1,lx):
        if i == 0 or l == 0:
            LCS[i][l] = 0
        elif s[i] == x[l]:
            LCS[i][l] = LCS[i-1][l-1]+1
        else:
            LCS[i][l] = max(LCS[i-1][l], LCS[i][l-1])

print(LCS[ls-1][lx-1])