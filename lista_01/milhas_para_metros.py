#Enuciado: Leia uma distancia em milhas e apresente-a convertida em quilômetros. A formula de 
#conversão é:  ́K = 1, 61 ∗ M, sendo K a distancia em quilômetros e M em milhas.
#
#Algoritmo: Convertendo Milhas em Metros
#
#Var
#   milhas : real
#   km : real
#
#Inicioalgoritmo
#   escreva("Digite a distãncia em milhas: ")
#   leia(milhas)
#   
#   km = 1.61 * milhas 
#   escreva(km)
#Fimdoalgoritmo

milhas = float(input("Digite a distãncia em milhas: "))
km = 1.61 * milhas
print(f'A distância em km é {km}')
