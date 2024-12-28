import math

n = int(input())

A_dict = {}

for i in range(n):
    a = input().split()
    A_dict[a[0]] = int(a[1])

m = int(input())
A = input().split()
Answer = 0

for i in range(m):
    if len(A[i]) == 1:
        Answer += A_dict[A[i]]
    else:
        l = len(A[i])
        x = 0
        for j in range(l):
            x += 1 / A_dict[A[i][j]]
        W = 1 / x
        Answer += W

print(math.floor(Answer))