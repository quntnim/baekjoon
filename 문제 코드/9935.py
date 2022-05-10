import sys
input = sys.stdin.readline

s = list(input().rstrip())
ex = list(input().rstrip())

stac = []
if len(ex) == 1:
    for i in range(len(s)):
        if s[i] != ex[0]:
            stac.append(s[i])
else:
    for i in range(len(s)):
        stac.append(s[i])
        if stac[-1]==ex[-1] and stac[-len(ex):]==ex:
            for _ in range(len(ex)):
                stac.pop()

if not stac:
    print("FRULA")
else:
    print(''.join(stac))