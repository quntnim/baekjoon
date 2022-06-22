def lps(s):
    n = len(s)
    p = [[0] * (n + 1), [0] * n]

    for z, pz in enumerate(p):
        left=0
        right=0
        for i in range(n):
            temp = right - i + 1 - z
            if i < right:
                pz[i] = min(temp,pz[left+temp])
            L, R = i - pz[i], i + pz[i] - 1 + z
            while L >= 1 and R + 1 < n and s[L-1] == s[R+1]:
                pz[i] += 1
                L -= 1
                R += 1
            if R > right:
                left, right = L, R

    i1, x1 = max(enumerate(p[0]), key=lambda x: x[1])
    i2, x2 = max(enumerate(p[1]), key=lambda x: x[1])
    return s[i1 - x1:i1 + x1], s[i2 - x2:i2 + x2 + 1]

print(lps(input()))