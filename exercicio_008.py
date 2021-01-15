# Escreva um programa que leia um valor em metros e converta e exiba em centímetros e milímetros

valor= float (input("Digite um valor em metros: "))
cent = valor * 100
mili = valor * 1000

print("A medida {} em metros tem valores de {} centímetros e {} milímetros".format(valor, cent, mili))
