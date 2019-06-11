x = int(input())
a = 0
dentro = 0
fora = 0

while a < x:
    val = int(input())
    if(10 <= val <= 20):
        dentro += 1
    else:
        fora += 1
    a += 1

print(dentro, "in")
print(fora, "out")
