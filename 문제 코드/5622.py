s = input()
cnt = 0
for i in s:
    if i in ['A','B','C']:cnt+=3
    elif i in ['D','E','F']:cnt+=4
    elif i in ['G','H','I']:cnt+=5
    elif i in ['J','K','L']:cnt+=6
    elif i in ['M','N','O']:cnt+=7
    elif i in ['P','Q','R','S']:cnt+=8
    elif i in ['T','U','V']:cnt+=9
    elif i in ['W','X','Y','Z']:cnt+=10
    else:cnt+=11
print(cnt)