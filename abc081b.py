N = int(input())
A = list(map(int, input().split()))

ans = 0
flag = True

while flag == True:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i] / 2
        else:
            flag = False
            print(ans)
            break
    ans += 1


# counter = 0
# flag = True

# while flag == True:
#     for i in range(N):
#         if A[i] % 2 == 1:
#             print(counter)
#             flag = False
#             break
#         else:
#             A[i] = A[i] / 2
#     counter += 1
