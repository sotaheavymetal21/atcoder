N = int(input())
A = list(map(int, input().split()))

odd_num = 0
for i in A:
    if i % 2 == 1:
        odd_num += 1

if odd_num % 2:
    print('NO')
else:
    print('YES')

# ----------------------------
# N = int(input())
# A = list(map(int,input().split()))
# count = 0
# for i in A:
#     if i % 2 != 0:
#         count += 1

# if count % 2 == 0:
#     print("YES")
# else:
#     print("NO")