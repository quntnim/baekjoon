n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n):
    for l in range(i):
        if (arr[l] > arr[i]):
            dp[i] = max(dp[i], dp[l]+1)
print(max(dp))