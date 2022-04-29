import sys
input = sys.stdin.readline
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11=map(int,input().rstrip().split())
arr = [[[[[[[[[[list(map(int,input().rstrip().split())) for _ in range(n2)] for _ in range(n3)] for _ in range(n4)] for _ in range(n5)] for _ in range(n6)] for _ in range(n7)] for _ in range(n8)] for _ in range(n9)] for _ in range(n10)] for _ in range(n11)]
cnt = 0;tomato = []
for a in range(n11):
    for b in range(n10):
        for c in range(n9):
            for d in range(n8):
                for e in range(n7):
                    for f in range(n6):
                        for g in range(n5):
                            for h in range(n4):
                                for i in range(n3):
                                    for j in range(n2):
                                        for k in range(n1):
                                            if arr[a][b][c][d][e][f][g][h][i][j][k] == 1:tomato.append((a,b,c,d,e,f,g,h,i,j,k))
dk = [-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dj = [0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
di = [0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dh = [0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dg = [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0]
df = [0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0]
de = [0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0]
dd = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0]
dc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0]
db = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0]
da = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]
day = 0
while True:
    tomato2 = []
    for a,b,c,d,e,f,g,h,i,j,k in tomato:
        for l in range(22):
            nA = a + da[l];nB = b + db[l];nC = c + dc[l];nD = d + dd[l];nE = e + de[l];nF = f + df[l];nG = g + dg[l];nH = h + dh[l];nI = i + di[l];nJ = j + dj[l];nK = k + dk[l]
            if 0<=nA<n11 and 0<=nB<n10 and 0<=nC<n9 and 0<=nD<n8 and 0<=nE<n7 and 0<=nF<n6 and 0<=nG<n5 and 0<=nH<n4 and 0<=nI<n3 and 0<=nJ<n2 and 0<=nK<n1:
                if not arr[nA][nB][nC][nD][nE][nF][nG][nH][nI][nJ][nK]:arr[nA][nB][nC][nD][nE][nF][nG][nH][nI][nJ][nK] = 1;tomato2.append((nA,nB,nC,nD,nE,nF,nG,nH,nI,nJ,nK))
    if len(tomato2):
        tomato = tomato2[:];day += 1
    else:
        for a in range(n11):
            for b in range(n10):
                for c in range(n9):
                    for d in range(n8):
                        for e in range(n7):
                            for f in range(n6):
                                for g in range(n5):
                                    for h in range(n4):
                                        for i in range(n3):
                                            for j in range(n2):
                                                for k in range(n1):
                                                    if arr[a][b][c][d][e][f][g][h][i][j][k] == 0:day = -1
        break
print(day)