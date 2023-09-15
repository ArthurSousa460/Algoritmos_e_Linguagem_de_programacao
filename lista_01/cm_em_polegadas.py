#Leia um valor de comprimento em cent ́ımetros e apresente-o convertido em polegadas.A formula de conversão ̃é: 
#P =C2,54 , sendo C o comprimento em cent ́ımetros e P o comprimento em polegadas.


#Algoritmo: Convertendo centimetros em polegadas
#
#Var
#
#   cm : real 
#   p : real
#
#Iniciodoalgoritmo
#
#   escreva("Centimetros:")
#   leia(cm)
#   p = cm / 2.54
#   escreva(p)
#
#Fimdoalgoritmo

cm = float(input("Centimetros:"))
p = cm / 2.54
print("O valor digitado em polegadas é ", p)