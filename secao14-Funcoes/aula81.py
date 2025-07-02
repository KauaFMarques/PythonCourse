def somar_numeros(*numeros):
    resultado=0
    for num in numeros:
        resultado+=num
    return resultado

x=somar_numeros(2,4,6,7)
print(x)