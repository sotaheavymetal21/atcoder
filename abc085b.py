# 入力
N = int(input())
d = [int(input()) for _ in range(N)]

# dのうち重複する要素を削除し、要素数を求める
num_d = len((set(d)))

# 出力
print(num_d)