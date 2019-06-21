x = int(input())
proximo = 1
anterior = 0
for i in range(0,x):
    if i == x-1:
        print(anterior)
    else:
        print(anterior, end=" ")
        anterior = anterior + proximo
        proximo, anterior = anterior, proximo
