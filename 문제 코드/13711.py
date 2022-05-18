from bisect import *

n = int(input())
s = [0]+list(input())
x = [0]+list(input())
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

i = ls-1
l = lx-1
res = []
while i>0 and l>0:
    if LCS[i][l] == LCS[i][l-1]:
        l-=1
    elif LCS[i][l] == LCS[i-1][l]:
        i-=1
    else:
        res.append(s[i])
        i-=1;l-=1
        
la = len(res)

dp = [res[0]]
for i in range(la):
    if res[i] > dp[-1]:
        dp.append(res[i])
    else:
        index = bisect_left(dp,res[i])
        dp[index] = res[i]

print(len(dp))