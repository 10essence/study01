n, m, k = map(int, input().split())

A = [i + 1 for i in range(n)]
B = []

a = n // m
b = n % m

for i in range(k):
    if b == 0:
        next
        B.extend(A[-m:])
        for j in range(1, a):
            B.extend(A[- m * (j + 1) : - m * j ])
        A = B
        if i == k - 1:
            next
        else:
            B = []
    else:
        B.extend(A[-b:])
        for j in range(1, a + 1):
            B.extend(A[- m * j - b: - m * (j - 1) - b])
        A = B
        if i == k - 1:
            next
        else:
            B = []

for i in range(n):
    print(B[i])