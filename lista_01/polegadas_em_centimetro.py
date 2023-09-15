#Enuciado: Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
#A formula de conversão e: C = P ∗ 2, 54, sendo C o comprimento em centrímetros e P o comprimento em polegadas.
#
#Algoritmo: Convertendo polegadas em centimetros
#
#Var
#
#   cm : real 
#   p : real
#
#Iniciodoalgoritmo
#
#   escreva("Polegadas:")
#   leia(p)
#   c = p * 2.54
#   escreva(c)
#
#Fimdoalgoritmo

p = float(input("Polegadas:"))
c = p * 2.54
print("O valor digitado em centimetros é ", c)