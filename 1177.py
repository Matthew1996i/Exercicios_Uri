a = int(input())
b = 0
for i in range(1000):
    if b < a:
        print('N[%d] = %d' %(i, b))
        b += 1
    elif b == a:
        b = 0
        print('N[%d] = %d' %(i, b))
        b = 1