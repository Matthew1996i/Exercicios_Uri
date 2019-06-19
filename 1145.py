a,b = map(int, input().split())
cont = 0
stop = 0
while stop == 0:
    
    for i in range(a):
        cont += 1
        if cont == b:
            print(cont)
            break
        elif(i+1 == a):
            print(cont)
        else:
            print(cont, end=" ")
    if cont == b:
        stop = 1