from collections import deque
numb = deque(input())
if len(numb)==1:numb.appendleft(0)
mainn = numb[0]+numb[1]
print(mainn)
print(numb)