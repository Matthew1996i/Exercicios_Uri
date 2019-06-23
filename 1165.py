n = int(input())
validador = 0

for i in range(n):
    x = int(input())
    for i in range(1, x+1):
        if x % i == 0:
            validador += 1

    if validador > 2:
        print(x, 'nao eh primo')
    elif validador == 2:
        print(x, 'eh primo')

    validador = 0