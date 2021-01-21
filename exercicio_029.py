# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do carro? "))
multa = 7 * (velocidade - 80)
if velocidade > 80.0:
    print("Você ultrapasssou o limite permitido. Você receberá uma multa de R${:.2f}".format(multa))
else:
    print("Muito bem! Você está dirigindo conscientemente!")
