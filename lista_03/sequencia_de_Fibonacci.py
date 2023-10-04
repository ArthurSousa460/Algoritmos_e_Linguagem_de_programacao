print("--------------Sequência de Fibonacci--------------")

num = int(input("Digite quantos termos quer mostrar: "))
list = list()

for i in range(0, num):
    if len(list) == 0:
        list.append(i)
    elif len(list) == 1:
        list.append(list[0] + i)
    else:
        list.append(list[i -1] + list[i - 2])


for i in list:
    print(f"{i} ", end=" ")
