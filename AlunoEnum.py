from enum import Enum
#Limpa a tela do terminal
import os
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Aluno:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
        )

# Criação do objeto Aluno e exibição dos dados
aluno1 = Aluno("Murilo", 22, Sexo.FEMININO)
print(aluno1)