#Enuciado: Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s
#(metros por segundo). A formula de conversão é :  ́ M = K/3.6, sendo K a velocidade em
#km/h e M em m/s.
#
#Algoritmo: Km/h em m/s
#
#Var
#   km : real
#   ms : real 
#
#Inciodoalgoritmo
#
#escreva("Digite a velociadade em km/h: ")
#leia(km)
#
#ms = km / 3.6
#
#escreva(ms)
#Fimdoalgoritmo

km = float(input("Digite a velociade em km/h: "))
ms = km / 3.6
print(f'A velocidade {km} Km/h convertida em M/S é {ms:.2f}')


