x = int(input())
c = 0
for l in range(x):
    while True:
        c += 1
        if c % 4 == 0:
            print('PUM', end="")
            break
        else:
            print(c, end=" ")
    print('')