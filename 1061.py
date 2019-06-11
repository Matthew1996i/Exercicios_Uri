diaI = int(input().split()[1])
horaI, minI, segI = map(int, input().split(':'))
diaF = int(input().split()[1])
horaF, minF, segF = map(int, input().split(':'))

diaT = diaF - diaI
horaT = horaF - horaI
minT = minF - minI
segT = segF - segI

if(horaT < 0):
    horaT += 24
    diaT -= 1

if(minT < 0):
    minT += 60
    horaT -= 1
if(segT < 0):
    segT += 60
    minT -= 1
print(diaT,'dia(s)')
print(horaT,'hora(s)')
print(minT,'minuto(s)')
print(segT,'segundo(s)')
