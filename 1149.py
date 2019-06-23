lista = input().split()
itens = []
soma = 0

for i in lista:
    if i > '0':
        itens.append(i)
        if len(itens) == 2:
            break

a = int(itens[0])
n = int(itens[1])

for x in range(n):
    soma += a+x

print(soma)
