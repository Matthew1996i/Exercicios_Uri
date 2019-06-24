A = []
for i in range(20):
    x = float(input())
    A.append(x)
A.reverse()

for j, n in enumerate(A):
        print('N[%d] = %d' %(j, n))