import os 
os.system("cls || clear")#Limpa terminal.

#Classe.
class Aluno:
    #construtor.
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} anos"

#Instanciar classe.
aluno = Aluno("Matheus", 9)

#print(aluno.nome)
#print(aluno.idade)

print(aluno.exibir_dados())