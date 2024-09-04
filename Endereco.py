import os 
os.system("cls || clear")#Limpa terminal.

class Endereco:
    def __init__(self, logadouro: str, numero: str) -> None:
        self.logadouro
        self.numero

    def __str__(self) -> str:
        return(
            f"\nLogadouro: " {self.logadouro}
            f"\nNumero: " {self.numero}

        )


#Classe.
class Aluno:
    #construtor.
    def __init__(self, nome: str, idade: str, endereco: str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} anos, \nendereço {self.endereco}"

#Instanciar classe.
aluno = Aluno("Matheus", "9")
endereco1 = Endereco("Rua da Morte", "12")
#print(aluno.nome)
#print(aluno.idade)

print(aluno.exibir_dados())