print("Gnomes:")
for i in range(int(input())):
    n = list(map(int,input().split()))
    print("Ordered"if n == sorted(n) or n == sorted(n)[::-1] else"Unordered")