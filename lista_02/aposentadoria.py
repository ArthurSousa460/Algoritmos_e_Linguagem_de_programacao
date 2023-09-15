#Enuciado: Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se  ̃
#aposentar. As condicoes para aposentadoria sao
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.


age_user = int(input("Digite a sua idade: "))
time_of_work = int(input("Digite a seu tempo de trabalho: "))

if age_user >= 65 or time_of_work == 30:
    print("Parábens, você esta apto para aposentar!")

elif age_user >= 60 and time_of_work >= 25:
    print("Parábens, você esta apto para aponsentar!")

else:
    print("Infelizmente você não esta apto para aposentar")
