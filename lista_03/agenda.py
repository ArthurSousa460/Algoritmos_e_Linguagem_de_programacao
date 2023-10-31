import pandas as pd

def menu():
    print(" [1] - Adcionar um contato \n [2] - Listar contatos \n [3] - Editar contato(nome) \n [4] - Editar contato(numero) \n [5] - Pesquisar contato \n [6] - Deletar contato \n [7] - Sair")
    op = int(input("Digite uma opção: "))
    return op


def post(name, number):
    contact["name"] = name
    contact["number"] = number
    agenda.append(contact.copy())
    print("Adcionado com sucesso")


def get_all():
    table = pd.DataFrame(agenda)
    print(table)


def get_contact(name):
    for c in agenda:
        if c["name"] == name:
            print("nome: {} numero: {}".format(c["name"], c["number"]))


def put_contact_name(name, new_name):
    for c in agenda:
        if c["name"] == name:
            c["name"] = new_name
            print("nome autalizado com sucesso")


def put_contact_number(name, new_number):
    for c in agenda:
        if c["name"] == name:
            c["number"] = new_number
            print("Atualizado com sucesso")


def delete_contact_name(name):
    for c in agenda:
        if c["name"] == name:
            agenda.remove(c)
            print("Contato removido com sucesso")

agenda = list()
contact = dict()

while True:
    op = menu()
    match op:
        case 1:
            name = str(input("Nome: "))
            number = int(input("Número: "))
            post(name, number)
        case 2:
            get_all()
        case 3: 
            name = str(input("Digite o nome:"))
            new_name = str(input("Digite o novo nome: "))
            put_contact_name(name, new_name)
        case 4:
            name = str(input("Digite o nome:"))
            new_number = int(input("Digite o novo número:"))
            put_contact_number(name, new_number) 
        case 5:
            name = str(input('Digite o nome: '))
            get_contact(name)
        case 6:
            name = str(input("digite o nome: "))
            delete_contact_name(name)
        case 7:
            break