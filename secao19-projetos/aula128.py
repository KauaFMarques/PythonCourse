'''
Programa qye calcula a quantidade de tinta necessária para pintar uma parede.
devemos fornecer informações:
redimento,altura,largura
print('vc necessita de x latas de tinta)
'''
redimento=int(input("Qual o rendimento:"))
altura=int(input("Qual a altura:"))
largura=int(input("Qual a largura:"))


def calculo():
    area=(altura*largura)/redimento
    print(f'Vc precisa de: {area}')

calculo()