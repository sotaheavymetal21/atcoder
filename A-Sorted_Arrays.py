# N = int(input())
# A = list(map(int, input().split()))

# flag = "NA"
# ans = 0

# for i in range(N - 1):
#     if A[i] < A[i + 1]:










































# ans = 1
# flag = "NA"  # True,False,NAの3パターン

# for i in range(N - 1):
#     if A[i] < A[i + 1]:
#         if flag == False:
#             ans += 1
#             flag = "NA"
#         else:
#             flag = True
#     elif A[i] > A[i + 1]:
#         if flag == True:
#             ans += 1
#             flag="NA"
#         else:
#             flag=False

# print(ans)


# # --------------------------------------
# flag = "NA"
# count = 1
# for i in range(N - 1):
#     if flag == "NA":
#         if A[i] < A[i + 1]:
#             flag = True
#         elif A[i] > A[i + 1]:
#             flag = -1
#     elif flag == True:
#         if A[i] > A[i + 1]:
#             count += 1
#             flag = 0
#     elif flag == False:
#         if A[i] < A[i + 1]:
#             count += 1
#             flag = 0
# print(count)