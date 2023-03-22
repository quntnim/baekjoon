for _ in range(int(input())):
    res = 0
    for _ in range(int(input())):
        s,a,b = input().split()
        res += int(a)*float(b)
    print(f"${res:.2f}")