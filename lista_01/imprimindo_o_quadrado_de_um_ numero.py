#Algoritmo Imprimindo um numéro real ao quadrado
#var
#   num : real 
#   num_quadrado : real
#
#Inciodoalgoritmo
#   escreva("Digite um número:")
#   leia(num)
#   
#   num_quadrado = num ** 2
#
#   escreva("O numero que foi digitado levado ao quadrado é:", num_quadrado)
#
#Fimalgoritmo

num = float(input("Digite um número:"))
num_quadrado = num ** 2
print(f"O número digitado elevado ao quadrado é: {num_quadrado:.2f}")