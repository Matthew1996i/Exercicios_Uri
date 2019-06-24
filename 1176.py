lista = [0,1]
proximo = 0
anterior = 1

for i in range(60):
    t = proximo + anterior
    lista.append(t)
    proximo, anterior = anterior, t
a = int(input())
for i in range(a):
    b = int(input())
    print('Fib(%d) = %d' %(b, lista[b]))