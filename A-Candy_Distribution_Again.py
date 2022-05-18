N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
print(a)
ans = 0
count = 0
for i in range(N):
    ans = x - a[i]
    
    print(ans)