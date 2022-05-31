for _ in range(int(input())):
    n = input()
    m = n[::-1]
    s = int(n)+int(m)
    s = str(s)
    print('YES'if s==s[::-1] else'NO')