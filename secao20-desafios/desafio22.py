lista_capitais={
    'brasil':'brasília',
    'eua':'new york',
    'argentina':'buenos aires',
    'chile':'santiago',
    'australia':'sydney',
    'canada':'ohawa'
}

pais_usuario=input("digite o nome do país:")

if pais_usuario in lista_capitais:
    print(f'a capital de {pais_usuario} é {lista_capitais[pais_usuario]}' )
else:
    print(f'sem informações')