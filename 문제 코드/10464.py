def xum(n):
	m = n % 4
	if (m == 0): return n
	if (m == 1): return 1
	if (m == 2): return n + 1
	return 0

def xorSum(left,right):
    return xum(left-1)^xum(right);

for i in range(int(input())):
    a,b = map(int,input().split())
    print(xorSum(a,b))