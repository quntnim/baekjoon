n = int(input())
if not n:
    print('divide by zero')
    exit(0)
arr = list(map(int,input().split()))
avg = sum(arr)/n
exp = 0
for i in arr:
    exp += i*(1/n)
print(f'{avg/exp:.2f}')