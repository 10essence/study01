n, m = map(int, input().split())

Route = [[0 for i in range(n)] for i in range(n)]
Answer = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    A = list(map(int, input().split()))
    for j in range(n):
        Route[i][j] = A[j]
        if m <= Route[i][j]:
            Answer[i][j] = 1

W = 0
B = []

for i in range(n):
    Work = 0
    for j in range(n):
        if Answer[j][i] == 1:
            Work += 1
    if Work == 0:
        B.append(i + 1)
    else:
        W += 1
if W == n:
    print("wait")
else:
    print(*B, sep = " ")