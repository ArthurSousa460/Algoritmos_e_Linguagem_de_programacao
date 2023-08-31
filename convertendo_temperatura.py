# Enuciado: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
# A formula de conversão é:  ́ F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celsius.


#Algoritmo: Convertendo temperaturas
#var
#   c : real
#   f : real
#
#Iniciodoalgoritmo
#   escreva("Digite a temperatura em Celsius: ")
#   leia(c)   
#   f = c *(9.0 / 5.0) + 32.0
#   escreva("A temperatura em Fahrenheit é: ", f)
#Fimdoalogoritmo

c = float(input("Digite a termperatura em Celsius: "))
f = c * (9 / 5) + 32
print(f"A temperatura em Fahrenheit é: {f}")