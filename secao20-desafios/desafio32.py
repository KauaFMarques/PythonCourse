# Função lambda para calcular quadrado individual
quadrado = lambda x: x ** 2

# Função que processa uma lista inteira
def calcular_quadrados(lista):
    resultados = []
    for numero in lista:
        resultados.append(quadrado(numero))
    return resultados

# Exemplo de uso
numeros = [1, 2, 3, 4, 5]
quadrados = calcular_quadrados(numeros)

print(f"Lista original: {numeros}")
print(f"Quadrados: {quadrados}")