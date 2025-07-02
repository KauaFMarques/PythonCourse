# ==============================================================================
# SEÇÃO 1: INTRODUÇÃO A FUNÇÕES
# ==============================================================================

print("======== SEÇÃO 1: INTRODUÇÃO A FUNÇÕES ========\n")

# --- 77. Criando uma função de soma ---
# Explicação:
# A função 'somar_simples' é um bloco de código que executa uma tarefa específica (somar).
# Neste exemplo, os números são fixos dentro da função.
def somar_simples():
    num1 = 5
    num2 = 3
    soma = num1 + num2
    print(f"77. Criando uma função de soma:")
    print(f"   A soma fixa é: {soma}")

# Chamando a função para executá-la
somar_simples()
print("-" * 30)

# --- 78. Parâmetros e Argumentos em uma função ---
# Explicação:
# - Parâmetros: 'a' e 'b' são os parâmetros na definição da função.
# - Argumentos: São os valores reais que passamos (ex: 10, 5) quando chamamos a função.
# Isso torna a função flexível, permitindo somar números diferentes a cada chamada.
def somar_com_parametros(a, b):
    soma = a + b
    print(f"78. Parâmetros e Argumentos:")
    print(f"   A soma de {a} e {b} é: {soma}")

# Chamando a função e passando argumentos
somar_com_parametros(10, 5)
somar_com_parametros(7, 20)
print("-" * 30)

# --- 79. Argumentos Default e Non-default ---
# Explicação:
# - 'mensagem' é um argumento non-default (obrigatório).
# - 'nome' é um argumento default (opcional), com valor padrão "Usuário".
# Argumentos default SEMPRE vêm depois dos non-default na definição.
def saudar(mensagem, nome="Usuário"):
    print(f"79. Argumentos Default e Non-default:")
    print(f"   {mensagem}, {nome}!")

# Chamando a função sem fornecer o argumento 'nome' (usa o default)
saudar("Olá")
# Chamando a função fornecendo o argumento 'nome' (sobrescreve o default)
saudar("Bom dia", "Alice")

# Outro exemplo com valores numéricos e default
def calcular_desconto(valor_original, percentual_desconto=0.10): # 10% de desconto por padrão
    desconto = valor_original * percentual_desconto
    valor_final = valor_original - desconto
    print(f"   Valor original: R${valor_original:.2f}, Desconto ({percentual_desconto*100:.0f}%): R${desconto:.2f}, Valor final: R${valor_final:.2f}")

calcular_desconto(200) # Usa o desconto padrão de 10%
calcular_desconto(500, 0.05) # Usa 5% de desconto
print("-" * 30)

# --- 80. Print ou Return em Funções ---
# Explicação:
# - 'print()' apenas exibe algo na tela. A função não "devolve" um valor.
# - 'return' envia um valor de volta para o local onde a função foi chamada,
#   permitindo que o valor seja usado em outras operações ou armazenado.
def somar_e_imprimir(a, b):
    soma = a + b
    print(f"80. Print ou Return em Funções (com print):")
    print(f"   A soma (exibida por print) é: {soma}")

def somar_e_retornar(a, b):
    soma = a + b
    return soma # Retorna o valor da soma

# Usando a função com print
resultado_print = somar_e_imprimir(10, 2)
print(f"   Variável 'resultado_print' contém: {resultado_print} (None, pois não houve return)")

# Usando a função com return
print(f"80. Print ou Return em Funções (com return):")
resultado_return = somar_e_retornar(10, 2)
print(f"   Variável 'resultado_return' contém: {resultado_return}")

# O valor retornado pode ser usado em outras operações
dobro_da_soma = somar_e_retornar(5, 3) * 2
print(f"   O dobro da soma de 5 e 3 é: {dobro_da_soma}")
print("-" * 30)

# ==============================================================================
# SEÇÃO 2: ARGUMENTOS ESPECIAIS (*args e **kwargs)
# ==============================================================================

print("\n======== SEÇÃO 2: ARGUMENTOS ESPECIAIS (*args e **kwargs) ========\n")

# --- 81. Vários argumentos *args com números ---
# Explicação:
# O '*args' permite que uma função aceite um número variável de argumentos posicionais.
# Dentro da função, 'numeros' será uma tupla contendo todos os argumentos passados.
def somar_varios_numeros(*numeros):
    print(f"81. Vários argumentos *args com números:")
    print(f"   Tipo de 'numeros' dentro da função: {type(numeros)}")
    total = 0
    for num in numeros:
        total += num
    return total

print(f"   Soma de 1, 2, 3: {somar_varios_numeros(1, 2, 3)}")
print(f"   Soma de 10, 20: {somar_varios_numeros(10, 20)}")
print(f"   Soma de 5, 5, 5, 5: {somar_varios_numeros(5, 5, 5, 5)}")
print(f"   Soma de nenhum número: {somar_varios_numeros()}") # Também funciona!
print("-" * 30)

# --- 82. Vários argumentos **kwargs nomeando parâmetros ---
# Explicação:
# O '**kwargs' permite que uma função aceite um número variável de argumentos nomeados (chave=valor).
# Dentro da função, 'dados' será um dicionário contendo todos os pares chave-valor passados.
def exibir_detalhes(**dados):
    print(f"82. Vários argumentos **kwargs nomeando parâmetros:")
    print(f"   Tipo de 'dados' dentro da função: {type(dados)}")
    print("   Detalhes recebidos:")
    if not dados:
        print("      Nenhum detalhe fornecido.")
    else:
        for chave, valor in dados.items():
            print(f"      - {chave.replace('_', ' ').title()}: {valor}") # Formatação para melhor leitura

exibir_detalhes(nome="Ana", idade=25, cidade="Rio de Janeiro")
print() # Pula linha para separar a próxima chamada
exibir_detalhes(produto="Teclado", preco=150.00, em_estoque=True)
print()
exibir_detalhes() # Chamando sem argumentos nomeados
print("-" * 30)


# ==============================================================================
# SEÇÃO 3: MODULARIZAÇÃO
# ==============================================================================

print("\n======== SEÇÃO 3: MODULARIZAÇÃO ========\n")

# --- 83. Importando um Módulo ---
# Explicação:
# Módulos são arquivos .py que contêm código (funções, classes, variáveis).
# Podemos importar esses módulos para reutilizar o código em outros scripts.

# SIMULAÇÃO: Para este exemplo funcionar de verdade,
# você precisaria ter um arquivo chamado 'meu_modulo_util.py' no mesmo diretório, com o seguinte conteúdo:
#
# # Conteúdo de meu_modulo_util.py:
# def multiplicar(x, y):
#     return x * y
#
# def dividir(x, y):
#     if y == 0:
#         return "Erro: Divisão por zero!"
#     return x / y
#
# PI_CONSTANT = 3.14159

try:
    # Opção 1: Importar o módulo completo
    import meu_modulo_util # Supondo que 'meu_modulo_util.py' existe

    print("83. Importando um Módulo (import meu_modulo_util):")
    resultado_multi = meu_modulo_util.multiplicar(6, 4)
    print(f"   Multiplicação usando módulo: {resultado_multi}")

    valor_pi = meu_modulo_util.PI_CONSTANT
    print(f"   Valor de PI no módulo: {valor_pi}")

    # Opção 2: Importar funções específicas do módulo (recomendado para clareza)
    from meu_modulo_util import dividir, multiplicar as mult_func # Podemos até renomear

    print("\n83. Importando um Módulo (from meu_modulo_util import ...):")
    resultado_div = dividir(10, 2)
    print(f"   Divisão direta: {resultado_div}")

    # Usando a função renomeada
    resultado_multi_renomeada = mult_func(7, 3)
    print(f"   Multiplicação (renomeada): {resultado_multi_renomeada}")

except ImportError:
    print("83. Importando um Módulo:")
    print("   ERRO: Não foi possível importar 'meu_modulo_util.py'.")
    print("   Por favor, crie um arquivo chamado 'meu_modulo_util.py' no mesmo diretório")
    print("   com o conteúdo de exemplo fornecido nas explicações (dentro deste arquivo principal).")
except Exception as e:
    print(f"Ocorreu um erro ao executar a parte de importação: {e}")

print("-" * 30)

print("\n======== FIM DO ARQUIVO ========")