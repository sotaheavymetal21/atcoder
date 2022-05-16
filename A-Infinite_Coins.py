N = int(input())
A = int(input())

# N -= 500 * (N //500)
if N % 500 <= A:
    print("Yes")
else:
    print("No")