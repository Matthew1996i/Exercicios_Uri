horaI, minI, horaF, minF = map(int, input().split())

hTotal = horaF - horaI
minTotal = minF - minI

if(hTotal < 0):
    hTotal += 24
if(minTotal < 0):
    minTotal += 60
    hTotal -= 1
if(minTotal == 0 and hTotal == 0):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hTotal, minTotal))
