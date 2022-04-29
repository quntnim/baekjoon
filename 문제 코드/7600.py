alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    cnt = 0
    arr = list(input().lower())
    if arr[0] == '#': break
    for i in alpha:
        if i in arr: cnt+=1;
    print(cnt)