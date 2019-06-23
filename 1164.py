n = int(input())
soma = []
total = 0
for i in range(1, n+1):
    x = int(input())
    for j in range(1, x+1):
        if x % j == 0 and x != j:
            soma.append(j)
    for result in soma:
        total += result

    if total == x:
        print(x, 'eh perfeito')
    elif total != x:
        print(x, 'nao eh perfeito')
    soma = []
    total = 0
    