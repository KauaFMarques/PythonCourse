frutas=[]
while len(frutas)<6:
    nova_fruta=str(input("digite um afruta:"))
    frutas.append(nova_fruta)
print(frutas)

cont=0
for fruta in frutas:
    if fruta=='maca':
        cont+=1
print(f'Quantidade de macas repetidas: {cont}')