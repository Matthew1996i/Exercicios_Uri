lista = []
for i in range(10):
    x = int(input())
    if x < 1:
        x = 1
        lista.append(x)
    else:
        lista.append(x)

    
    print("X[%d] = %d" %(i, x))
