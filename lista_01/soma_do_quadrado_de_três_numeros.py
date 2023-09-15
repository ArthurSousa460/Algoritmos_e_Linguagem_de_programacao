#Enuciado: Faça a leitura de tres valores e apresente como resultado a soma dos quadrados dos
#três valores lidos

#Algoritmo: soma do quadrado de três números
#
#Var
#
#   i : inteiro
#   num_ : real
#   num : real
#
#Iniciodoalgoritmo
#   soma = 0
#   para i, i=0 ate i=2 passo i++ faça:
#          escreva("digite um valor: ")
#          leia(num)
#          num_ = num ** 2
#          soma += num_
#   escreva(soma)
#Fimdoalgoritmo

soma = 0 
for i in range(3):
    num = float(input("Digite um valor: "))
    num_ = num ** 2
    soma += num_

print(f"A soma do quadrado dos numeros digitados é: {soma}")