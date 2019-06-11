x = 6
contador = 0
i = 0
e = 0
while i < x:
    valor = float(input())
    if(valor >= 0):
        e += valor
        contador += 1
    i += 1

media = e / contador
print(contador, "valores positivos")
print("%.1f" %media)
