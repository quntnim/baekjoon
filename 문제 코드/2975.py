while True:
    q = input().split()
    if q[0] == '0' and q[1] == 'W' and q[0] == q[2]:break
    if q[1] == 'W':res = int(q[0]) - int(q[2])
    if q[1] == 'D':res = int(q[0]) + int(q[2])
    print('Not allowed'if res < -200 else res)