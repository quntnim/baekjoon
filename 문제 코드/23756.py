n = int(input())
now = int(input())
temp = 0
for i in range(n):
    des = int(input())
    temp += min(abs(now-des),360-now+des,now-des+360)
    now = des
print(temp)