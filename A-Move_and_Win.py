# 勝敗は二つのコマの偶奇に依存する。
N, A, B = map(int,input().split())
if (B - A) % 2 == 0:
    print("Alice")
else:
    print("Borys")