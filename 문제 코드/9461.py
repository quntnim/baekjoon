from random import *
# original code by koosaga 
mod = 1000000000007
def ipow(x, p):
    ret, piv = 1, x
    while p:
        if p & 1:
            ret = ret * piv % mod
        piv = piv * piv % mod
        p >>= 1
    return ret
def berlekamp_massey(x):
    ls, cur = [], []
    lf, ld = 0, 0
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t = (t + 1 * x[i-j-1] * cur[j]) % mod
        if (t - x[i]) % mod == 0:
            continue
        if not cur:
            cur, lf, ld = [0] * (i+1), i, (t - x[i]) % mod
            continue
        k = -(x[i] - t) * ipow(ld, mod - 2) % mod
        c = [0] * (i-lf-1) + [k]
        for j in ls:
            c.append(-j * k % mod)
        if len(c) < len(cur):
            c += [0] * (len(cur) - len(c))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % mod
        if i-lf+len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % mod
        cur = c
    return cur
def get_nth(rec, dp, n):
    m = len(rec)
    s, t = [0] * m, [0] * m
    s[0] = 1
    if m != 1:
        t[1] = 1
    else:
        t[0] = rec[0]
    def mul(v, w):
        t = [0] * (2 * m)
        for j in range(m):
            for k in range(m):
                t[j+k] += 1 * v[j] * w[k] % mod
                if t[j+k] >= mod:
                    t[j+k] -= mod
        for j in range(2 * m - 1, m - 1, -1):
            for k in range(1, m + 1):
                t[j - k] += 1 * t[j] * rec[k-1] % mod
                if t[j-k] >= mod:
                    t[j-k] -= mod
        return t[:m]
    while n:
        if n & 1:
            s = mul(s, t)
        t = mul(t, t)
        n >>= 1
    ret = 0
    for i in range(m):
        ret += 1 * s[i] * dp[i] % mod
    return ret % mod
def guess_nth_term(x, n):
    if n < len(x):
        return x[n]
    v = berlekamp_massey(x)
    if not v:
        return 0
    return get_nth(v, x, n)
def get_min_poly(n, M):
    r1, r2 = [0] * n, [0] * n
    for i in range(n):
        r1[i] = randint(1, mod - 1)
        r2[i] = randint(1, mod - 1)
    gobs = [0] * (2 * n + 2)
    for i in range(2 * n + 2):
        tmp = 0
        for j in range(n):
            tmp += 1 * r2[j] * r1[j] % mod
            if tmp >= mod:
                tmp -= mod
        gobs[i] = tmp
        nxt = [0] * n
        for i in M:
            nxt[i[0]] += 1 * i[2] * r1[i[1]] % mod
            if nxt[i[0]] >= mod:
                nxt[i[0]] -= mod
        r1 = nxt
    sol = berlekamp_massey(gobs)
    sol.reverse()
    return sol
def det(n, M):
    rnd = [0] * n
    for i in range(n):
        rnd[i] = randint(1, mod - 1)
    for i in range(len(M)):
        M[i][2] = 1 * M[i][2] * rnd[M[i][1]] % mod
    sol = get_min_poly(n, M)[0]
    if n % 2 == 0:
        sol = mod - sol
    for i in rnd:
        sol = 1 * sol * ipow(i, mod - 2) % mod
    return sol

for _ in range(int(input())):
    print(guess_nth_term([0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9], int(input())))