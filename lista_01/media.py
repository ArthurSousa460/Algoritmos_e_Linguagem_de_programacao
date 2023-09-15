#Enuciado: Leia quatro notas, calcule a media aritm  ́ etica e imprima o resultado.

#Algoritmo: Média de quatro notas 
#
#Var
#
#   i : inteiro
#   soma : real
#   nota : real
#   
#
#Iniciodoalgoritmo
#   soma = 0
#   para i, i=0 ate i=5 passo i++ faça:
#          escreva("digite a nota : ")
#          leia(nota)
#          soma += nota
#          
#   media = soma / 4   
#   escreva(soma)
#Fimdoalgoritmo

soma = 0 
for i in range(3):
    num = float(input("Digite as notas: "))
    soma += num 

media = soma / 4
print(f"A média das suas notas é: {media}")