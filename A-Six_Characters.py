S = input()

for i in range(6):
    S += S[i]
    if len(S) == 6:
        break
print(S)