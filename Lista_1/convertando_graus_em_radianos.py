#Enuciado: Leia um angulo em graus e apresente-o convertido em radianos. A formula de conversão ̃
#e: R = G ∗ π/180, sendo G o angulo em graus e ˆ R em radianos e π = 3.14.
#
#Algoritmo: Convertendo graus em radianos 
#
#Var
#   graus : real
#   rad : real
#   pi : real
#
#Iniciodoalgoritmo
#   
#   pi = 3.14
#   escreva("Graus:")
#   leia(graus)
#
#   rad = graus * pi / 180
#   escreva(rad)
#Fimdoalgoritmo

graus = float(input("Graus:"))
pi = 3.14
rad = graus * pi / 180
print(f"O valor em radianos é {rad}")
