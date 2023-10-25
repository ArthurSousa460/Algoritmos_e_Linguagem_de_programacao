#Faça um programa que leia varios n números, calcule e mostre:  
#(a) A soma dos numeros digitados  
#(b) A quantidade de numeros digitados  
#(c) A media dos numeros digitados  
#(d) O maior numero digitado  
#(e) O menor numero digitado  
#(f) A media dos números pares

#O programa deve terminar se o número 0 for digitado


def media(sum, cont):
    media = sum / cont
    if type(media) == float:
        return f"{media:.2f}"


sum = 0
cont = 0
cont_p =0
sum_p = 0
while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break
    
    elif num % 2 == 0:
        cont_p += 1
        sum_p += num


    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    sum += num
    cont += 1



print(f"A soma dos números digitados é: {sum}")
print(f"A quantidade dos números digitado é: {cont}")
print(f"A média dos valores digitados é: {media(sum,cont)}")
print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
print(f"A média entre os números parés são: {media(sum_p, cont_p)}")

