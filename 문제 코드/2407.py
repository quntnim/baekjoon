n,m = map(int,input().split())

def count_2(n):
    cnt = 0
    while n!=0:
        n=n//2
        cnt+=n
    return cnt

def count_5(n):
    cnt = 0
    while n!=0:
        n=n//5
        cnt+=n
    return cnt
two=count_2(n)-count_2(n-m)-count_2(m)
five=count_5(n)-count_5(n-m)-count_5(m)

print(min(two,five))