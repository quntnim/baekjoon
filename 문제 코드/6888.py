a,b=int(input()),int(input())
for i in range(a,b+1):
    t = a-i
    if not t%4 and not t%2 and not t%3 and not t%5:print('All positions change in year',i)