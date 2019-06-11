x = 6
contador = 0
i = 0
while i < x:
    valor = float(input())
    if(valor >= 0):
        contador += 1
    i += 1
print(contador, "valores positivos")
