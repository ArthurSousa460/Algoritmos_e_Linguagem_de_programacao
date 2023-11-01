import pandas as pd
from time import sleep


def print_aling_center(text):
    width = len(text)
    space = int(110 / width)
    print(" " * space, end="")
    print(text)


def print_line():
    print("=" * 45)


def menu():
    print_line()
    print_aling_center("AGENDA")
    print_line()
    print(" [1] - Adcionar um contato \n [2] - Listar contatos \n [3] - Editar contato(nome) \n [4] - Editar contato(numero) \n [5] - Pesquisar contato \n [6] - Deletar contato \n [7] - Sair")
    print_line()
    try:
        op = int(input("Digite uma opção: "))
        return op
    except:
        print_line()
        print("O valor digitado não é uma opção")
        print_line()
        sleep(1.8)


def post(name, number):
    contact["name"] = name
    contact["number"] = number
    if len(agenda) == 0:
        agenda.append(contact.copy())
        contact.clear()
        print("Adicionado com sucesso")
        print_line()
        sleep(3)
    else:
        for i in agenda:
            if (contact["name"] == i["name"] and contact["number"] == i["number"]) or (contact["number"] == i["number"]):
                print_line()
                print("Número já adcionado")
                sleep(2)
                print_line()
                break
            else:
                agenda.append(contact.copy())
                contact.clear()
                print("Adicionado com sucesso")
                print_line()
                sleep(3)
                break


def get_all():
    table = pd.DataFrame(agenda)
    print(table)


def get_contact(name):
    query = list()
    for c in agenda:
        if c["name"] == name:
            query.append(c)

    table = pd.DataFrame(query)
    print(table)



def put_contact_name(name, new_name):
    for c in agenda:
        if c["name"] == name:
            c["name"] = new_name
            print_line()
            print("nome autalizado com sucesso")
            sleep(2)
        else:
            print_line()
            print("Nome não se encotra na base de dados")
            print_line()
            sleep(2)


def put_contact_number(name, new_number):
    for c in agenda:
        if c["name"] == name:
            c["number"] = new_number
            print("Atualizado com sucesso")
            print_line()
            sleep(2)
        else:
            print("Numero não consta na base de dados")
            print_line()
            sleep(2)



def delete_contact_name(name):
    for c in agenda:
        if c["name"] == name:
            agenda.remove(c)
            print("Contato removido com sucesso")
            sleep(2)
            break
        else:
            print("Valor não localizado na base de dados")
            sleep(2)
            break
    
        

agenda = list()
contact = dict()

while True:
    op = menu()
    sleep(1)
    match op:
        case 1:
            print_line()
            name = str(input("Nome: "))
            sleep(0.5)
            print_line()
            number = int(input("Número: "))
            sleep(1)
            print_line()
            post(name, number)
        case 2:
            print_line()
            get_all()
            input("Enter para sair:")
            sleep(0.8)
        case 3: 
            print_line()
            name = str(input("Digite o nome:"))
            sleep(0.8)
            print_line()
            new_name = str(input("Digite o novo nome: "))
            sleep(0.8)
            put_contact_name(name, new_name)
        case 4:
            sleep(0.8)
            print_line()
            name = str(input("Digite o nome:"))
            print_line()
            sleep(0.8)
            new_number = int(input("Digite o novo número:"))
            put_contact_number(name, new_number) 
        case 5:
            print_line()
            name = str(input('Digite o nome: '))
            sleep(0.8)
            print_line()
            get_contact(name)
            input("Enter para conntinuar ")
        case 6:
            print_line()
            name = str(input("digite o nome: "))
            print_line()
            delete_contact_name(name)
        case 7:
            print("Saindo do Sistema...")
            print_line()
            sleep(0.8)
            break
        
    