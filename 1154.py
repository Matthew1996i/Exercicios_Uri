step = 0
tt = 0
while True:
    x = int(input())
    if x < 0:
        break
    else:
        tt += x
        step += 1
        

media = tt / step
print('%.2f' %media)