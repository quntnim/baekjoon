def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = 1

    col = 2
    for i in range(2, n+1):
        if arr[i] == True:
            arr[i] = col
            j = 2
            while (i * j) <= n:
                arr[i*j] = col
                j += 1
            col+=1
    print(col-1)
    return arr
arr = is_prime(int(input()))
print(*arr[1::])