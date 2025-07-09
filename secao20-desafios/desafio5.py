num1=int(input("Digite um numero:"))
num2=int(input("Digite um numero:"))
cont=True

while cont==True:
    add=num1+num2
    print(f'Adição de {num1} e {num2}: {add}')
    sub=num1-num2
    print(f'Subtração de {num1} e {num2}: {sub}')
    mult=num1*num2
    print(f'Multiplicação de {num1} e {num2}: {mult}')
    div=num1-num2
    print(f'Divisão de {num1} e {num2}: {div}')
    exp=num1**num2
    print(f'Exponenciação de {num1} e {num2}: {exp}')
    cont=False