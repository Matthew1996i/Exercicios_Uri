cont = 0

while(cont == 0):
    a,b = map(int, input().split())

    if(a < b):
        print("Crescente")
    elif(a > b):
        print("Decrescente")
    elif(a == b):
        cont += 1
