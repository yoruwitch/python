# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input("Digite a altura da parede: "))
lar = float(input("Digite a largura da parede: "))
area = alt * lar

print("Sua parede tem dimensões {}x{} e sua área é de {}m²".format(alt, lar, area))

totaltinta = area / 2

print("Para pintar essa parede, serão necessários {}l de tinta".format(totaltinta))



