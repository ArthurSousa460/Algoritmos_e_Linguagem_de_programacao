#enuciado: Faça um programa que some os numeros primos existentes entre a e b, onde a e b  são números informados pelo usuário
def is_prime(n):
    for i in range(2, n):
        if n % i  == 0:
            return False
    return True



def maior(a, b):
    if a > b:
        return a 
    else:
        return b


def menor(a, b):
    if a < b:
        return a
    else:
        return b 


a = int(input("Digite o número a:"))
b = int(input("Digite o número b:"))

ma = maior(a, b)
me = menor(a, b)
sum = 0


for i in range(me, ma):
    if is_prime(i) == True:
        sum += i
    

print(f"A soma dos números primos entre os valores {a} e {b} é: {sum}")
