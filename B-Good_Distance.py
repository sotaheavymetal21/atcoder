# mathをimportする
import math

# 標準入力
N,D = map(int,input().split())
X=[tuple(map(int,input().split()))for _ in range(N)]

ans= 0

# iはx座標を示す。
for i in range(N - 1):
    # jはi + 1を示す。ここでresを0にリセットする。
    for j in range(i + 1, N):
        res = 0
        # kはy座標を示す。差の絶対値を二乗し、平方根を取得。整数であればカウントする。
        for k in range(D):
            res += abs(X[i][k] - X[j][k]) ** 2
        if math.sqrt(res) % 1 == 0:
            ans += 1
print(ans)