lista = []

for i in range(100):
    val = int(input())
    lista.append(val)

valMax = max(lista)
position = lista.index(valMax)

print(valMax)
print(position + 1)
