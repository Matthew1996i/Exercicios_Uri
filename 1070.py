a = int(input())
x = 0

if(a % 2 == 1):
    print(a)
    x += 1

while x < 6:
    if(a % 2 == 0):
        a += 1
        print(a)
    elif(a % 2 == 1):
        a += 2
        print(a)
    x += 1
