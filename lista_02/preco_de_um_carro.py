#Enuciado:O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão
#do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo 
#de fabrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.

#CUSTO DE FABRICA            % DO DISTRIBUIDOR   % DOS IMPOSTOS
#ate R$12.000,00 ´                   5               isento
#entre R$12.000,00 e 25.000,00       10                 15
#acima de R$25.000,00                15                  2





print("---------------Custo do carro para o consumidor-----------------------")
fabrica = float(input("Digite o custo de fábrica: "))


if fabrica <= 12000:
    imposto_do_distribuidor = fabrica * 0.05
    print(f'O carro irá custar para o cliente: R${imposto_do_distribuidor + fabrica}')

elif fabrica > 12000 and fabrica <= 25000:
    imposto_do_distribuidor = fabrica * 0.10
    imposto = fabrica * 0.15
    print(f'O carro irá custar para o cliente: R${imposto_do_distribuidor + imposto + fabrica}')
    
else:
    imposto_do_distribuidor = fabrica * 0.15
    imposto = fabrica * 0.02
    print(f'O carro irá custar para o cliente: R${imposto_do_distribuidor + imposto + fabrica}')


    