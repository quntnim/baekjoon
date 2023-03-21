def numchange(n):
    if n == 0:return;

    numchange(n/9);

    if n % 9 >= 10:print("%c", 'A' + n % 9 - 10);
    else: print("%d", n % 9);
print(numchange(int(input())))