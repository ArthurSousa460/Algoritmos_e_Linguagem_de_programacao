#Enuciado: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#A formula de conversão é:  ́ C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
#e F a temperatura em Fahrenheit.


#Algoritmo: Convertendo temperaturas
#var
#   c : real
#   f : real
#
#Iniciodoalgoritmo
#   escreva("Digite a temperatura em Fahrenheit: ")
#   leia(f)   
#   c = 5.0 * (f - 32.0) / 9.0
#   escreva("A temperatura em Celsius é: ", c)
#Fimdoalogoritmo


f = float(input("Digite a termperatura em Fahrenheit: "))
c = 5 * (f - 32)/ 9
print(f"A temperatura em Celsius é: {c}")