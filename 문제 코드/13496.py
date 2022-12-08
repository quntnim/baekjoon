for tc in range(int(input())):
    n,s,d = map(int,input().split())
    res = 0
    for i in range(n):
        a,b = map(int,input().split())
        if a <= s*d:res += b
    print(f"Data Set {tc+1}:")
    print(res)
    print()
