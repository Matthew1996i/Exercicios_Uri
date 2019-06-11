salario = float(input())

if(0 <= salario <= 400):
    perce = 0.15
    salariof = salario + (salario * perce)
    reajuste = salariof - salario
    print("Novo salario: {:.2f}".format(salariof))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    perce = perce * 100
    print("Em percentual: {:.0f} %".format(perce))
elif(400.01 <= salario <= 800):
    perce = 0.12
    salariof = salario + (salario * perce)
    reajuste = salariof - salario
    print("Novo salario: {:.2f}".format(salariof))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    perce = perce * 100
    print("Em percentual: {:.0f} %".format(perce))
elif(800.01 <= salario <= 1200.00):
    perce = 0.10
    salariof = salario + (salario * perce)
    reajuste = salariof - salario
    print("Novo salario: {:.2f}".format(salariof))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    perce = perce * 100
    print("Em percentual: {:.0f} %".format(perce))
elif(1200.01 <= salario <= 2000.00):
    perce = 0.07
    salariof = salario + (salario * perce)
    reajuste = salariof - salario
    print("Novo salario: {:.2f}".format(salariof))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    perce = perce * 100
    print("Em percentual: {:.0f} %".format(perce))
elif(2000 <= salario):
    perce = 0.04
    salariof = salario + (salario * perce)
    reajuste = salariof - salario
    print("Novo salario: {:.2f}".format(salariof))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    perce = perce * 100
    print("Em percentual: {:.0f} %".format(perce))
