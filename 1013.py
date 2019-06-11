val = input().split(" ")
a,b,c = val
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorBC = (maiorAB+c+abs(maiorAB-c))/2

print("%.0d eh o maior" %maiorBC)
