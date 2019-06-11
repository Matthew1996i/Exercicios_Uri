dias = int(input())

ano = dias / 365
rAno = dias % 365

mes = rAno / 30
rMes = rAno % 30

dias = rMes / 1
rDias = rMes % 1

print(int(ano),"ano(s)")
print(int(mes),"mes(es)")
print(int(dias),"dia(s)")
