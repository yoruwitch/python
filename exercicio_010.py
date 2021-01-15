# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input("Quantos reais você tem? "))
dolar = din / 5.30
print("Você tem R${} e com isso pode comprar U${:.2f}.".format(din, dolar))
