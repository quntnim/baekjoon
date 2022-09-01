n = int(input())
while True:
    a = int(input())
    if not a:break
    print(f'{a} is a multiple of {n}.'if not a%n else f'{a} is NOT a multiple of {n}.')
    