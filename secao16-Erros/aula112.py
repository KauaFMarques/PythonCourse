try:
    valor=int(input("digite o valor do seu produto:"))
    print(valor)
    print(type(valor))
except ValueError:
    print("Favor digitar valores do tipo int")

finally:
    print("código ok")
    
'''
else:
    print("Usuários digitou correto")
    resultado=valor*2
    print(resultado)
'''