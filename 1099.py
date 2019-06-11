cont = 0
goal = int(input())
total = []
while cont < goal:
    x,y = map(int, input().split())
    newList = []
    soma = 0
    if(x < y):
        for i in range(x+1,y):

            if(i % 2 == 1):
                newList.append(i)
                soma += i
        total.append(soma)
        soma = 0

    elif(x > y):
        for i in range(y+1,x):
            if(i % 2 == 1):
                newList.append(i)
                soma += i
        total.append(soma)
        soma = 0
    elif(x == y):
        for i in range(y+1,x):
            if(i % 2 == 1):
                newList.append(i)
                soma += i
        total.append(soma)
        soma = 0

    cont += 1

for i in range(goal):
    print('{}'.format(total[i]))
