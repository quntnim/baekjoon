while True:
    a = list(input());
    stack = [];c = 1
    if a[0] == '.' :break
    for i in range(len(a)):
        if a[i] == '(': stack.append('(')
        elif a[i] == '[': stack.append('[')
        elif a[i] == ')':
            if stack == [] or stack[-1] == '[':
                c = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif a[i] == ']':
            if stack == [] or stack[-1] == '(':
                c = 0
                break
            elif stack[-1] == '[':
                stack.pop()
    if stack==[] and c != 0:print('yes')
    else : print('no')