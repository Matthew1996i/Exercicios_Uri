entry = int(input())

for i in range(entry):
    a,b = map(int, input().split())
    try:
        if(a / b):
            print(a / b)
        elif(a / b == 0.0):
            print(float(a/b))
    except:
        print('divisao impossivel')
