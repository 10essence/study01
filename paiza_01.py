n = input()

A = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

for i in range(len(n)):
    a = int(n[i])
    if a // 3 == 2:
        a = a % 3
        A[0:1] = ["#", "#", "#"]
        for j in range(a):
            A[2][j] = "#"
        print(A[_] for _ in A)
    elif a // 3 == 1:
        a = a % 3
        A[0] = ["#", "#", "#"]
        for j in range(a):
            A[1][j] = "#"
        print(A[_] for _ in A)
    else:
        for j in range(a):
            A[0][j] = "#"
        print(A[_] for _ in A)
    if i // 3 == 0:
        print()

# 与えられた文字列から自動で電話番号を取得するプログラムを作成しようと考えました。
# 文字列からいきなり電話番号を取得するのは難しいと考えた paiza 君は、最初の文字と最後の文字が数字(0~9)であるような文字列を「疑似数字」として取り出すコードを作成することにしました。
# 文字列 S が与えられるので、そこに含まれる疑似数字を全て出力してください。
# 数字 1 文字の場合であっても疑似数字とみなされる点に注意してください。

s = list(input())

n = list(map(str, range(10)))

for i in range(len(s)):
    if s[i] in n:
        s[i] = int(s[i])

for i in range(len(s)):
    for j in range(i, len(s)):
        if type(s[i]) == int and type(s[j]) == int:
            print(*s[i : j + 1], sep = "")
        