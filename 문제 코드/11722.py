n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
for i in range(n):
    for l in range(i):
        if (arr[i] < arr[l]):
            dp[i] = max(dp[i], dp[l]+1)
print(max(dp))