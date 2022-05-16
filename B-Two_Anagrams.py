S = input()
T = input()
S_sorted = sorted(S)
T_sorted_reverse = sorted(T, reverse=True)

if S_sorted < T_sorted_reverse:
    print("Yes")
else:
    print("No")