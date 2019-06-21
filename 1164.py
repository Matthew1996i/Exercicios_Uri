n = int(input())
val = 0
for i in range(n):
    x = int(input())
    
    while True:
        if x % 2 == 0:
            val += x
            x -= 1
        
    print(val)
            

