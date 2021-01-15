# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o seu salário? "))
novsal = salario + (salario*0.15)
print("Parabéns, você recebeu um aumento de 15%, logo seu novo salário é de R${:.2f}".format(novsal))
