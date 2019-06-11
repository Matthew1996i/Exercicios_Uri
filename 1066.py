x = 0
impar = 0
par = 0
posi = 0
nega = 0

while x < 5:
    val = int(input())

    if(val % 2 == 0):
        par += 1
    if(val % 2 == 1):
        impar += 1
    if(val > 0):
        posi += 1
    if(val < 0):
        nega += 1
    x += 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(posi, "valor(es) positivo(s)")
print(nega, "valor(es) negativo(s)")
