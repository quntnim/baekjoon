import sys
input = sys.stdin.readline

n, k = map(int,input().split()); money = [];left = k;cnt = 0
for _ in range(n):
    money.append(int(input()))
money.sort(reverse=True)

for i in money:
    if i <= k:
        while True:
            if i > left:break
            else: left -= i;cnt+=1  
    if left == 0:break
print(cnt)