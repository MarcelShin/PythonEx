salario = int(input("Insira seu salário: "))
porcentagem = float(input("Qual a porcetagem da promoção em % :"))

final = porcentagem / 100

print("O seu bonus foi de: ",salario * final + salario)
