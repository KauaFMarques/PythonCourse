from datetime import datetime
#criar classe
class Funcionarios:
    def __init__(self,nome,sobrenome,ano_nascimento):
        self.nome=nome
        self.sobrenome=sobrenome
        self.ano_nascimento=ano_nascimento

    def imprimirNomeSobrenome(self):
        return self.nome+" "+self.sobrenome
    
    def calcula_Idade(self):
        ano_atual=datetime.now().year
        self.ano_nascimento=int(ano_atual-self.ano_nascimento)
        return self.ano_nascimento
#criar objeto
usuario1=Funcionarios('helena','cabral',2003)

print(usuario1.imprimirNomeSobrenome())
print(Funcionarios.imprimirNomeSobrenome(usuario1))
print(Funcionarios.calcula_Idade(usuario1))