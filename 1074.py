x = int(input())
a = 0
arr = []
while a < x:
    val = int(input())

    if(val > 0):
        if(val % 2 == 0 ):
            tipo = "EVEN POSITIVE"
        elif(val % 2 == 1):
            tipo = "ODD POSITIVE"
    elif(val < 0):
        if(val % 2 == 0):
            tipo = "EVEN NEGATIVE"
        elif(val % 2 == 1):
            tipo = "ODD NEGATIVE"
    elif(val == 0):
        tipo = "NULL"
    arr.append(tipo)
    a += 1
print(*arr, sep = "\n")
