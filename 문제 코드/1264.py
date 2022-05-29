moum = ['a','e','i','o','u','A','E','I','O','U']
while True:
    cnt = 0
    s = input()
    if s == '#':break
    for m in moum:
        cnt += s.count(m)
    print(cnt)