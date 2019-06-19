x = int(input())
C = 0
R = 0
S = 0

for a in range(x):
    a,b = input().split()

    if(b == 'C'):
        C += int(a)
    elif(b == 'R'):
        R += int(a)
    elif(b == 'S'):
        S += int(a)

t = C+R+S
print('Total:', t, 'cobaias')
print('Total de coelhos:', C)
print('Total de ratos:', R)
print('Total de sapos:', S)
print('Percentual de coelhos: %.2f'%(C*100/t),'%')
print('Percentual de ratos: %.2f'%(R*100/t),'%')
print('Percentual de sapos: %.2f'%(S*100/t),'%')