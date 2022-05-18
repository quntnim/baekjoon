n,w,h,l = map(int,input().split())
h//=l
w//=l
print(min(h*w,n))