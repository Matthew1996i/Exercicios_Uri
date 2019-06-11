testes = int(input())
medias = []
for i in range(testes):
    valores = map(float, input().split())
    a,b,c = valores
    m = (a*2 + b*3 + c*5)/10
    medias.append(m)
    i += 1

for i in range(testes):
	print('{:.1f}'.format(medias[i]))
