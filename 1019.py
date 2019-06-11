tempo = int(input())

horas = tempo / 3600
rhoras = tempo % 3600

minutos = rhoras / 60
rminutos = rhoras % 60

segundos = rminutos / 1

print("%.0d:%.0d:%.0d" %(horas, minutos, segundos))
