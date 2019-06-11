valores = input().split(" ")

a,b,c = valores
a = float(a)
b = float(b)
c = float(c)

if(a+b > c and b+c > a and c+a > b):
    print("Perimetro = %.1f" %(a+b+c))
else:
    print("Area = %.1f" %((a+b)/2*c))
