W, H, N = map(int,input().split())
x_left = 0
x_right = W
y_up = H
y_down = 0

for _ in range(N):
    x, y, a = map(int,input().split())
    if a == 1:
        x_left = max(x_left, x)
    elif a == 2:
        x_right = min(x_right, x)
    elif a == 3:
        y_down = max(y_down, y)
    else:
        y_up = min(y_up, y)

#print(x_left, x_right, y_down, y_up)
print(max(0,(y_up - y_down)) * max(0,(x_right - x_left)))