#Enuciado: Leia uma distancia em quilômetros e apresente-a convertida em milhas. A formula de conversao ̃ e:  ́
# M =K / 1,61 , sendo K a distancia em quilômetros e M em milhas.
#
#Algoritmo: convertendo km em milhas
#Var
#   m : real
#   km : real 
#
#Iniciodoalgoritmo
#
#   escreva("Digite a distância em Km: ")
#   leia(km)
#
#   m = km / 1.61
#   escreva(m)
#Fimdoalgoritmo

km = float(input("Digite a distância em Km: "))
m = km / 1.61
print(f"A distância em milhas é {m}")

