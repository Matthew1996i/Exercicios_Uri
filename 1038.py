item = input().split(" ")

a,b = item
a = int(a)
b = int(b)

if(a == 1):
    valor = b * 4
elif(a == 2):
    valor = b * 4.50
elif(a == 3):
    valor = b * 5.00
elif(a == 4):
    valor = b * 2.00
elif(a == 5):
    valor = b * 1.50


print("Total: R$ %.2f" %valor)
