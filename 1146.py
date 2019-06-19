x = 1
while x != 0:
    x = int(input())
    if(x == 0):
        break
    else:
        for i in range(1,x+1):
            if i == x:
                print(i)
            else:
                print(i, end=" ")