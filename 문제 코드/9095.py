t=int(input());arr=[1,2,4]
for i in range(3, 10):arr.append(arr[i-3]+arr[i-2]+arr[i-1])
for _ in range(t):n=int(input());print(arr[n-1])