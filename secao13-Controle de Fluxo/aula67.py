for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero1,numero2)

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print("--------------------")
print("Percorrendo a matriz")
for linha in matriz:
    for elemento in linha:
        print(elemento,end=' ')
    print()

print("-------------------")
frutas = ["Maçã", "Banana", "Uva"]
cores = ["Vermelho", "Amarelo", "Roxo"]

print("\nCombinações de frutas e cores:")
for fruta in frutas:
    print("-------")
    for cor in cores:
        print(f"{fruta} {cor}")

print("---------------------")
altura_triangulo = 5

print("\nTriângulo de asteriscos:")
for i in range(1, altura_triangulo + 1): # Controla as linhas (de 1 até a altura)
    for j in range(i): # Controla os asteriscos em cada linha (igual ao número da linha atual)
        print("*", end="") # Imprime um asterisco sem pular linha
    print() # Pula para a próxima linha

print("----------------------")
lista_numeros = [10, 2, 8, 5, 12, 3]
soma_alvo = 15

print(f"\nProcurando pares que somam {soma_alvo}:")
for i in range(len(lista_numeros)): # Pega o primeiro número
    for j in range(i + 1, len(lista_numeros)): # Pega o segundo número (garantindo que seja diferente do primeiro e à sua frente)
        if lista_numeros[i] + lista_numeros[j] == soma_alvo:
            print(f"Par encontrado: ({lista_numeros[i]}, {lista_numeros[j]})")