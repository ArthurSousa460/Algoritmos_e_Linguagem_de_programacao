#Enuciado: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
#formula de conversão ̃é: ́ C = K − 273.15, sendo C a temperatura em Celsius e K a
#temperatura em Kelvin.


#Algoritmo: Convertendo temperaturas
#var
#   k : real
#   c : real
#
#Iniciodoalgoritmo
#   escreva("Digite a temperatura em Kelvin: ")
#   leia(K)   
#   c = k - 273.15
#   escreva("A temperatura em Celsius é: ", c)
#Fimdoalogoritmo


k = float(input("Digite a termperatura em Kelvin: "))
c = k - 273.15
print(f"A temperatura em Fahrenheit é: {c}")