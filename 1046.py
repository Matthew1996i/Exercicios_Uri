hora = input().split()
i,f = hora
i = int(i)
f = int(f)
cont = 0

if(i < f):
    while i < f:
        cont += 1
        i += 1
elif(i == f):
    cont = 24
elif(i > f):
    cont = 24 - i
    cont = cont + f
print("O JOGO DUROU %d HORA(S)" %cont)
