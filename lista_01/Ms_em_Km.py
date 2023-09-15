#Enuciado: Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
#(quilometros por hora). A formula de conversão é: K = M ∗ 3.6, sendo K a velocidade
#em km/h e M em m/s.
#
#Algoritmo: M/s em K/m
#
#Var
#   km : real
#   ms : real
#
#inciodoalgoritmo
#   escreva("Digite a velocidade em M/s: ")
#   leia(ms)
#   
#   km = ms * 3.6
#   escreva(km)
#
#Fimdoalgoritmo

ms = float(input("Digite a velocidade em M/s: "))
km = ms * 3.6
print(f'A velocidade {ms} Km/h convertida em M/S é {km:.2f}')
