# # これはTLE
# import itertools

# n,w = map(int,input().split())
# a = list(map(int,input().split()))

# good = set()

# for i in range(1,4):
#     for j in itertools.combinations(a,i):
#         print(j)
#         if sum(j) <= w:
#             good.add(sum(j))
#             #print(good)
# print(len(good))


N, W = map(int,input().split())
A = [0 ,0] + list(map(int,input().split()))

N += 2
S = set()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                S.add(A[i] + A[j] + A[k])
print(len(S))