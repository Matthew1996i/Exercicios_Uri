n = int(input())
lista = list(map(int, input().split()))

menor = min(lista)
posicao = lista.index(menor)


print('Menor valor: %d' %menor)
print('Posicao: %d' %posicao)





