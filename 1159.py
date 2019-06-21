step = 0
val = 0
while True:
    x = int(input())
    if x == 0:
        break
    else:
        while step < 5:
            if x % 2 == 0:
                val += x
                step += 1
                x += 1
            else:
                x += 1
        print(val)
        val,step = 0,0
