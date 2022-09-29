import sys
input = sys.stdin.readline

mod = 10**9

def fibo(n):
    def multiply(m1,m2):
        res = []
        for x in range(len(m1)):
            res.append([])
            for y in range(len(m2[0])):
                t=0
                for z in range(len(m1[0])):
                    t += m1[x][z] * m2[z][y]
                res[x].append(t % mod)
        return res

    def power(m,p):
        if p == 1:
            return m
        else:
            t = power(m,p//2)
            if p%2==0:
                return multiply(t,t)  
            else:
                return multiply(multiply(t,t), m)

    return power([[1,1],[1,0]],n)[0][1]

for i in range(int(input())):
    print(fibo(int(input())))