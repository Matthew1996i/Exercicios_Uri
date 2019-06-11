notas = input().split(" ")

a,b,c,d = notas

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = (a*2 + b*3 + c*4 + d*1)/10
final = 0.0

print("Media: %.1f" %media)

if(media >= 7):
    print("Aluno aprovado.")

elif(media < 5):
    print("Aluno reprovado.")

elif(5 <= media <= 6.9):
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" %exame)
    final = (media + exame)/2
    if(final > 5):
        print("Aluno aprovado.")
        print("Media final: %.1f" %final)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" %final)
