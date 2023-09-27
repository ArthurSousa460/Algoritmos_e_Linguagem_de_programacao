#Enuciado:Faça um programa que receba um numero inteiro maior do que 1, e verifique se o numero  ́
#fornecido e primo ou nao.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número para saber se é primo: "))

if is_prime(n) == True:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")