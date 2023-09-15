#Algoritmo: Imprimindo a soma de três valores
#var
#   num1 : real
#   num2 : real
#   num3 : real
#   soma : real
#
#Iniciodoalgoritmo
#   escreva("Digite o primeiro número:")
#   leia(num1)
#   escreva("Digite o segundo número:")
#   leia(num2)
#   escreva("Digite o ultimo número:")
#   leia(num3)
#   soma = num1 + num2 + num3
#   escreva("A soma dos três números é: ", soma)


#Algoritmo: Imprimindo a soma de três valores
#var
#   i : inteiro
#   soma : real
#   num : real 
#
#Iniciodoalgoritmo
#   soma = 0
#   para i de i=0 ate i=2 passo i++ faça
#          escreva("Digite um número:")
#          leia(num)
#          soma += num
#   fim-para
#   escreva("A soma do três números digitados é: ", soma)
#
#
#Fimdoalgoritmo


soma = 0
for i in range(0,3):
    num = float(input("Digite um número:"))
    soma += num
print(soma)