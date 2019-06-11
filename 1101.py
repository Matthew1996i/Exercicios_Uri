cont = 0

while(cont == 0):
    a,b = map(int, input().split())
    newList = []

    if(a > 0 and b > 0):
        if(a < b):
            for x in range(a,b+1):
                newList.append(x)
                printList = " ".join(map(str, newList))
                soma = sum(newList)
            print(printList, "Sum=%d" %soma)
        elif(a > b):
            for x in range(b, a+1):
                newList.append(x)
                printList = " ".join(map(str, newList))
                soma = sum(newList)
            print(printList, "Sum=%d" %soma)

    else:
        cont = 1
