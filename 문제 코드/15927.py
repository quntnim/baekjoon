import sys
input = sys.stdin.readline
s = input().rstrip()
if len(s) == 1:print(-1)
elif s.count(s[0]) == len(s):print(-1)
elif s == s[::-1]:print(len(s)-1)
else: print(len(s))