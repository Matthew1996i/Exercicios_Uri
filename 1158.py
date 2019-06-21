n = int(input())
step = 0
val = 0
for i in range(n):
    x,y = map(int, input().split())

    while step != y:
        if x % 2 == 1:
            val += x
            x += 1
            step += 1
        else:
            x += 1
    print(val)

    step = 0
    val = 0
    

    