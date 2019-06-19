x = int(input())
for l in range(1, x+1):
    for c in range(3):
        if c == 1:
            print(l, end=" ")        
            print(l ** 2, end=" ")
            print(l ** 3)
        elif c == 2:
            print(l, end=" ")  
            print((l ** 2)+1, end=" ")
            print((l ** 3)+1)