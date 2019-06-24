A = []
for i in range(100):
    x = float(input())
    A.append(x)

for j, n in enumerate(A):
    if n <= 10:
        print('A[%d] = %.1f' %(j, n))