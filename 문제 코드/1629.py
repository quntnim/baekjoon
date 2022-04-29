a,b,c=map(int,input().split())
print(pow(a,b,c))



def multiply(a,b,c):
    if b==1:return a%c
    else:
        if b%2:return ((multiply(a,b//2,c)**2)*a)%c
        else:return ((multiply(a,b//2,c)**2))%c