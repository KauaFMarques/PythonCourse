valor=int(input('Digite o valor do seu produto:'))

while valor>20:
    valor=(valor*0.1)+valor
    print(f'o valor final do produto é R${valor}')
    break