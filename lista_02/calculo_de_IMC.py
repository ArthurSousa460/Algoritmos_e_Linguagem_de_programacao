#Enuciado: Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificacão de
#acordo com os dados a baixo:
#1- menor que 18.5 - abaixo do peso;
#2- entre 18.5 e 24.9 - saudável;
#3- entre 25.0 e 29.9 - peso em excesso;
#4- entre 30.0 e 34.9 - obsidade grau I;
#5- entre 35.0 e 39.9 - obsidade grau II(severa);
#6- maior ou igual a 40.0 - obsidade grau III(mórbida) 

print("-----------------Caluculo de IMC----------------")
weith = float(input("Digite seu peso:"))
height = float(input("Digite seu altura: "))
imc = weith / height ** 2

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}, esta abaixo do peso!")

elif imc > 18.5 and imc <= 24.9:
    print(f"Seu IMC é de {imc:.2f}, esta saudável!")

elif imc > 24.9 and imc <= 29.9:
    print(f"Seu IMC é de {imc:.2f}, esta com peso em excesso!")

elif imc > 29.9 and imc <= 34.9:
    print(f"Seu IMC é de {imc:.2f}, esta com obsidade grau I!")

elif imc > 34.9 and imc <= 39.9:
    print(f"Seu IMC é de {imc:.2f}, esta com obsidade grau II!")

else:
    print(f"Seu IMC é de {imc:.2f}, esta com obsidade grau III!")

