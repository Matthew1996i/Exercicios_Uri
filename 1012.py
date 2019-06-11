valores = input().split(" ")
a,b,c = valores

a = float(a)
b = float(b)
c = float(c)

triangulo = (a*c)/2
raio = 3.14159 * pow(c,2)
trapezio = (a + b)*c/2
quadrado = b*b
retangulo = a*b

print("TRIANGULO: %.3f" %triangulo)
print("CIRCULO: %.3f" %raio)
print("TRAPEZIO: %.3f" %trapezio)
print("QUADRADO: %.3f" %quadrado)
print("RETANGULO: %.3f" %retangulo)
