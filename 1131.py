t = 0
inter = 0
gremio = 0
empate = 0 
while True:
    a,b = map(int, input().split())

    if a > b:
        inter += 1
        t += 1
    elif b > a:
        gremio += 1
        t += 1
    elif a == b:
        empate += 1
        t += 1

    print('Novo grenal (1-sim 2-nao)')
    choice = int(input())

    if choice == 1:
        continue
    elif choice == 2:
        break

if(inter > gremio):
    win = 'Inter'
else:
    win = 'Gremio'

print(t, 'grenais')
print('Inter:%d' %inter)
print('Gremio:%d' %gremio)
print('Empates:%d' %empate)
print(win, 'venceu mais')


