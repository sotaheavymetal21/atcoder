N = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)

Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        Alice += a[i]
    else:
        Bob += a[i]

print(Alice - Bob)


# # Alice = sum(a[::2])
# # Bob = sum(a[1::2]) これもいける。賢いやり方

# print(Alice - Bob)
