N = int(input())

flag = False
for i in range(N):
    for j in range(N):
        if i * 4 + j * 7 == N:
            flag = True

if flag:
    print("Yes")
else:
    print("No")