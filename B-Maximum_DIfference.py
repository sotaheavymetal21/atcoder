N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0

print(abs(A[0] - A[-1]))
