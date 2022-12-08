d,h,m = map(int,input().split())
print(res if (res:=(d-11)*1440+(h-11)*60+m-11) >= 0 else -1)