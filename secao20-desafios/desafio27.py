def fatorial(num):
    cont = num
    resultado = 1
    while cont > 0:
        resultado *= cont  # Multiplica o resultado pelo contador atual
        cont -= 1          # Decrementa o contador
        print(f'Passo {num - cont}: {resultado}')  # Mostra o progresso
    print(f'\nFatorial de {num} é: {resultado}')

fatorial(5)