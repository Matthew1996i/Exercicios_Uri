import math

entrada = input().split(" ")
a,b,c = entrada
a = float(a)
b = float(b)
c = float(c)

if (a != 0):
    delta = pow(b,2) - (4*a*c)
    if(delta > 0):
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)

        print("R1 = %.5f" %x1)
        print("R2 = %.5f" %x2)
    elif(delta < 0):
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
