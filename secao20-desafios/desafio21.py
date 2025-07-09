list_tuple=('sp','rj','jp')

for cidade in list_tuple:
    nome_cidade=(input("Digite um nome de uma cidade:"))
    if nome_cidade.lower()==cidade:
        print(f'cidade {nome_cidade} encotrada na lista')
    else:
        print(f'a cidade {nome_cidade} n foi encontrada')