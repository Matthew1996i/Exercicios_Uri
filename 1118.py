while True:
    x = float(input())
    while(x < 0 or x > 10):
        print('nota invalida')
        x = float(input())

    y = float(input())
    while(y < 0 or y > 10):
        print('nota invalida')
        y = float(input())

    print('media = %.2f' %((x+y)/2))

    print('novo calculo (1-sim 2-nao)')
    choice = int(input())
    while choice > 2:
        print('novo calculo (1-sim 2-nao)')
        choice = int(input())
    else:
        if choice == 1:
            continue
        elif choice == 2:
            break
            
            