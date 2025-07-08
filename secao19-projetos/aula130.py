funcionarios=['ana','kaua','pamela','pedro']
turno_manha=['ana','pedro']
turno_noite=['kaua','pamela']
tem_carro=['kaua','ana']

lista1=set(tem_carro).intersection(turno_noite)
print(lista1)

lista2=set(tem_carro).intersection(turno_manha)
print(lista2)

lista3=set(funcionarios).difference(tem_carro)
print(lista3)