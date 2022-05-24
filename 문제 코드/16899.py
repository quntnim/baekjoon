def xum(n):
	m = n % 4
	if (m == 0): return n
	if (m == 1): return 1
	if (m == 2): return n + 1
	return 0

def xorSum(left,right):
    return xum(left-1)^xum(right);

res = 0
n = int(input())
for i in range(n):
    x,m = map(int,input().split())
    res ^= xorSum(x,x+m-1)

print('cubelover'if res==0 else'koosaga')