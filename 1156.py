s = 0
y = 0

for i in range(1, 40, 2):
    s += i/(2**y)
    y += 1
print('%.2f' %s)