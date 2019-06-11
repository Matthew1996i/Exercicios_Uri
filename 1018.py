valor = int(input())

print(valor)

#notas de R$100
n100 = valor / 100
r100 = valor % 100
#notas de R$50
n50 = r100 / 50
r50 = r100 % 50
#notas de R$20
n20 = r50 / 20
r20 = r50 % 20
#notas de R$10
n10 = r20 / 10
r10 = r20 % 10
#notas de R$5
n5 = r10 / 5
r5 = r10 % 5
#notas de R$2
n2 = r5 / 2
r2 = r5 % 2
#notas de R$1
n1 = r2 / 1
r1 = r2 % 1

print(int(n100), "nota(s) de R$ 100,00")
print(int(n50), "nota(s) de R$ 50,00")
print(int(n20), "nota(s) de R$ 20,00")
print(int(n10), "nota(s) de R$ 10,00")
print(int(n5), "nota(s) de R$ 5,00")
print(int(n2), "nota(s) de R$ 2,00")
print(int(n1), "nota(s) de R$ 1,00")
