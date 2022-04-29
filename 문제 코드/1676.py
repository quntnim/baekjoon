from math import factorial
n = str(factorial(int(input())))
arr = list(n)
arr.reverse()
cnt=0
for i in arr:
    if i == '0':
        cnt+=1
    else:
        break
print(cnt)