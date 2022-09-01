while True:
    low = 0;up = 0;num = 0;space = 0
    try:
        s = input()
    except:
        break
    for i in s:
        if i.islower():low+=1
        elif i.isupper():up+=1
        elif i == ' ':space+=1
        else:num+=1
    print(low,up,num,space)