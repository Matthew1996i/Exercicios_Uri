a,b,c = map(float, input().split())

maior = sorted((a,b,c),reverse=True)
a,b,c = maior
if(a >= b + c):
    print("NAO FORMA TRIANGULO")
    if(a == b and b == c and c == a):
        print("TRIANGULO EQUILATERO")
    elif(a == b or b == c or c == a):
        print("TRIANGULO ISOSCELES")
elif(a**2 == b**2 + c**2):
    print("TRIANGULO RETANGULO")
    if(a == b and b == c and c == a):
        print("TRIANGULO EQUILATERO")
    elif(a == b or b == c or c == a):
        print("TRIANGULO ISOSCELES")
elif(a**2 > b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
    if(a == b and b == c and c == a):
        print("TRIANGULO EQUILATERO")
    elif(a == b or b == c or c == a):
        print("TRIANGULO ISOSCELES")
elif(a**2 < b**2 + c**2):
    print("TRIANGULO ACUTANGULO")
    if(a == b and b == c and c == a):
        print("TRIANGULO EQUILATERO")
    elif(a == b or b == c or c == a):
        print("TRIANGULO ISOSCELES")
