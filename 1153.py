n = int(input())
fibo = 0
result = 1

for i in range(n):
    val = n - i
    result = result * val
print(result)