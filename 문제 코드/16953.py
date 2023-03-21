def hirschberg(X, Y):
    if len(X) == 0:
        return []
    if len(X) == 1:
        if X[0] in Y:
            return X
        else:
            return []
    if len(Y) == 1:
        if Y[0] in X:
            return Y
        else:
            return []

    x_mid = len(X) // 2
    L = [0] * (len(Y) + 1)
    R = [0] * (len(Y) + 1)
    for i in range(len(Y) - 1, -1, -1):
        if Y[i] == X[x_mid]:
            L[i] = 1 + L[i + 1]
        else:
            L[i] = L[i + 1]

    for i in range(len(Y)):
        if Y[i] == X[x_mid]:
            R[i] = 1 + R[i - 1]
        else:
            R[i] = R[i - 1]

    y_mid = max(range(len(Y)), key=lambda i: L[i] + R[i] - 1)
    L = hirschberg(X[:x_mid], Y[:y_mid])
    R = hirschberg(X[x_mid:], Y[y_mid:])
    return L + R

X = "AGCAT"
Y = "GAC"
print("Longest Common Subsequence:", ''.join(hirschberg(X, Y)))
