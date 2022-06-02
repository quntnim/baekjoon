n = int(input())
cnt=1
while True:
    if n == 1:
        break
    if n%2==0:
        n//=2
    elif n%2==1:
        n=n*3+1
    cnt+=1
print(cnt)