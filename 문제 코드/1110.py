n = int(input())
cnt = 1
if n<10:n*=10
now = int(str(n)[0]) + int(str(n)[1])
print(now)
while True:
    cnt +=1
    if now < 10:now*=10
    now = int(str(now)[-1] + str(int(str(now)[0]) + int(str(now)[1]))[-1])
    print(now)
    if n == now:break
print(cnt)