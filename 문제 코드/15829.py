n = int(input())
s = input()
arr = []
res = 0
for i in s:
    arr.append(ord(i)-96)
for i in range(n):
    res+=arr[i]*31**i
print(res%1234567891)