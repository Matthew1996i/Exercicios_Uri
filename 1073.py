x = int(input())
i = 1
if(x % 2 == 1):
    x += 1

while i <= x:
    a = i**2
    if(a % 2 == 0):
        print("{}^2 = {}".format(i, a))
    i+=1
