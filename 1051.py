salario = float(input())

if(0 < salario <= 2000):
	print("Isento")
elif(2000 < salario <= 3000):
	resto = salario - 2000
	imposto = resto * 0.08
	print("R$ %.2f" %imposto)
elif(3000 < salario < 4500):
	resto = salario - 3000
	imposto = (resto * 0.18) + (1000 * 0.08)
	print("R$ %.2f" %imposto)
else:
    resto = salario - 4500
    imposto = (resto * 0.28) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %.2f" %imposto)
