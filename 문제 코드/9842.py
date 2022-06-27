res = []
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, n+1):
        if arr[i] == True:
            res.append(i)
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return res
is_prime(10**7)
print(res[int(input())-1])