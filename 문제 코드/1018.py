w_chess = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
b_chess = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
n,m = map(int,input().split())
arr = []
res = []
for i in range(n):
    arr.append(input())
for y in range(n-7):
    for x in range(m-7):
        w,b=0,0
        for i in range(8):
            for j in range(8):
                if arr[y+i][x+j] != w_chess[i][j]:w+=1
                if arr[y+i][x+j] != b_chess[i][j]:b+=1
        res.append(min(w,b))
print(min(res))