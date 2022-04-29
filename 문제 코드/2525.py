h, m = map(int,input().split());t = int(input())
m += t
while True:
    if(m >= 60): m -= 60; h += 1
    elif(h >= 24): h -= 24
    else: break
print(h, m)