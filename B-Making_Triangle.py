N = int(input())
X = sorted(list(map(int,input().split())))
ans = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if X[i] != X[j] != X[k] and X[k]< X[i] + X[j]:
                ans += 1
print(ans)

# N = int(input())
# A = [int(i) for _ in input().split()]

# ans = 0

# for i in range(len(A)):
#     for j in range(len(A)):
#         for k in range(len(A)):
#             if i != j and i != k and j != k:
#                 if A[i] + A[j] > A[k] and A[i] < A[k] and A[j] < A[k] and A[i] < A[j]:
#                     ans += 1
# print(ans)