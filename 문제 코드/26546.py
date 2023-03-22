for i in range(int(input())):
    s,a,b = input().split()
    for i in range(len(s)):
        if i not in range(int(a),int(b)):
            print(s[i],end='')
    print()