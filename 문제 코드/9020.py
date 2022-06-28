def goldbach(n):
    def is_prime(n):
        arr = [True] * (n + 1)
        arr[0] = False;arr[1] = False

        for i in range(2, n+1):
            if arr[i] == True:
                j = 2
                while (i * j) <= n:arr[i*j] = False;j += 1

        return [i for i in range(2,n+1) if arr[i] == True]

    res = []
    arr = is_prime(n)
    for i in arr:
        if (n-i) in arr:
            val = sorted([i, n-i])
            if val in res:
                return res
            res.append(val)
    return res

temp = 12345
for _ in range(int(input())):
    gb = goldbach(int(input()))
    for i in gb:
        if abs(i[0] - i[1]) < temp:
            r1,r2 = i[0],i[1]
    print(r1,r2)