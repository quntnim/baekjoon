import sys
input = sys.stdin.readline
def ccw_comp(a,b,c):
    crs = (a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0])
    d = (a[0]-b[0])*(c[0]-b[0])+(a[1]-b[1])*(c[1]-b[1])
    if crs < 0 or crs == 0 and d <= 0:
        return 1
    else: return 0

def convex_hull(pts):
    pts = sorted(pts)
    hull = []
    for p in pts + pts[::-1]:
        while len(hull) >= 2 and ccw_comp(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull

arr = []
n = int(input())
for i in range(n):
    a,b,c = input().split()
    if c == 'Y':
        arr.append([int(a),int(b)])

res = convex_hull(arr)
print(len(res))
print(res)