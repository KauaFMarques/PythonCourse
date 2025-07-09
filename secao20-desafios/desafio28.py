def dobrar(num):
    resultado = num * 2
    print(f"Dobro: {resultado}")
    return resultado

def quadrado(num):
    resultado = dobrar(num) ** 2
    print(f"Quadrado do dobro: {resultado}")
    return resultado

try:
    user_answer = float(input("Digite um número: "))
    quadrado(user_answer)  # Isso já chama dobrar() internamente
except ValueError:
    print("Por favor, digite um número válido!")