#criar classe
class Funcionarios:
    def __init__(self,nome,sobrenome,data_nascimento):
        self.nome=nome
        self.sobrenome=sobrenome
        self.data_nascimento=data_nascimento
#criar objeto
usuario1=Funcionarios('helena','cabral','12/08/2004')

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)