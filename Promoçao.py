salario_ant = 1500
porcentagem = 15 / 100
porcentagem1 = 5 / 100
aumento = (salario_ant * porcentagem)
salario_prom = salario_ant + aumento
desconto = aumento - porcentagem1
salario_des = salario_prom - desconto
print("O aumento de salário foi de:", salario_prom)
print("Você obteve um aumento de","R$", aumento )
print("Infelizmente você obteve 5% de deconto no valor de:", "R$", desconto )
print("Seu salario atual é de", salario_des) # salarios
