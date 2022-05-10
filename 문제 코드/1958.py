import sys
input = sys.stdin.readline

str1 = [0]+list(input().rstrip())
str2 = [0]+list(input().rstrip())
str3 = [0]+list(input().rstrip())
la = len(str1)
lb = len(str2)
lc = len(str3)
LCS = [[[0 for _ in range(lc)] for _ in range(lb)] for _ in range(la)]
for a in range(1,la):
    for b in range(1,lb):
        for c in range(1,lc):
            if a == 0 or b == 0 or c == 0:
                LCS[a][b][c] = 0
            elif str1[a] == str2[b] == str3[c]:
                LCS[a][b][c] = LCS[a-1][b-1][c-1]+1
            else:
                LCS[a][b][c] = max(LCS[a-1][b][c], LCS[a][b-1][c], LCS[a][b][c-1])

print(LCS[la-1][lb-1][lc-1])