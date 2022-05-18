N = int(input())

ans = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        print(j)
        if i + j == N:
            print(i, j)