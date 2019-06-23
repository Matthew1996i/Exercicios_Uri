x = int(input())
z = 0
cont = 0
soma = 0
while z <= x:
    z = int(input())

while soma < z:
    soma += x + cont
    cont += 1

print(cont)