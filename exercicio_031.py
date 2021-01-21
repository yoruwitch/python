# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = int(input("Digite a distância de sua viagem: "))
if viagem <= 200:
    print("Sua viagem vai custar R${}.".format(viagem * 0.50))
else:
    print("Sua viagem vai custar R${}.".format(viagem * 0.45))
