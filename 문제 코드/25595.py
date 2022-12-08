n = int(input())
arr = []
for i in range(n):
    arr += input().split()
    arr += ['.',''][n%2]

breaker = False
res = "Lena"
for i in range(len(arr)):
    if arr[i] == '2':
        for j in range(i%2,len(arr),2):
            if arr[j] == '1':
                res = "Kiriya"
                breaker = True
                break
    if breaker:break

print(res)  