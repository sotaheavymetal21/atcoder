N =int(input())


counter = 0
flag = True
for i in range(1, N+1):
    if i % 2 == 0:
        while flag == True:
            if i % 2 == 1:
                print(counter)
                flag = False
                break
        else:
            i = i / 2
    counter += 1