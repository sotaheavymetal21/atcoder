S = input()

ATCG = ["A", "T", "C", "G"]

count = 0
ans = 0
for i in range(len(S)):
    if S[i] in ATCG:
        count += 1
        ans = max(ans, count)
    else:
        count = 0
print(ans)

# S = input()
# result = 0

# tmp = 0
# for i in range(len(S)):
#     if S[i] in "ACGT":
#         tmp += 1
#     else:
#         tmp = 0
#     result = max(result, tmp)
# print(result)
