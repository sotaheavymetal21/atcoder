A,B = map(int,input().split())
N = B - A + 1

answer = 0

for i in range(N):
    N = A + i
    N_list = list(str(N))
    print(N_list)
    n_list = []
    for j in range(len(N_list)):
        n_list.append(N_list[-(j + 1)])
    if N_list == n_list:
        answer += 1
print(answer)
# ----------------------------------

A,B = map(int,input().split())
count = 0

for i in range(A,B+1):
    i = str(i)
    if i == i[::-1]:
        count += 1
print(count)