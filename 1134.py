cont = 0
alcool, gasolina, diesel = 0,0,0


while(cont != 1):
    typeComb = int(input())

    if(typeComb == 1):
        alcool += 1
    elif(typeComb == 2):
        gasolina += 1
    elif(typeComb == 3):
        diesel += 1
    elif(typeComb == 4):
        cont += 1

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)
