cores=['azul','amarelo','verde']
cor_cliente=input('Digite um cor:')

if cor_cliente.lower() in cores:
    print('cor disponível')
else:
    print('cor nao presente')