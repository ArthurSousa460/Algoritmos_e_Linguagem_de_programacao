#enuciado:Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores  ́
#desse numero, com exceção dele próprio. Ex: a soma dos divisores do número 66 
#é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78


def soma_dos_divisores(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

print("---------------soma dos divisores de um número----------------")
n = int(input("Digite um numero: "))
print(soma_dos_divisores(n))