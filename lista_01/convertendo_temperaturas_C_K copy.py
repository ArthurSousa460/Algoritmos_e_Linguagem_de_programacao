#Enuciado: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
#formula de conversão ̃é: ́ K = C + 273.15, sendo C a temperatura em Celsius e K a
#temperatura em Kelvin.


##Algoritmo: Convertendo temperaturas
#var
#   k : real
#   c : real
#
#Iniciodoalgoritmo
#   escreva("Digite a temperatura em Celsius: ")
#   leia(c)   
#   k = c + 273.15
#   escreva("A temperatura em Kelvin é: ", k)
#Fimdoalogoritmo

c = float(input("Digite a termperatura em Celsius: "))
k = c  + 273.15
print(f"A temperatura em Kelvin é: {k}")
