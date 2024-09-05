from enum import Enum

import os
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Homi"
    FEMININO = "Mulé"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSO_HUMANO = "Rh"
    VENDAS = "Vendas"
    MARKERTING = "Markenting"

class Funcionario: 
    def __init__(self, id: str, nome:str, salario:float, setor:Setor, sexo:Sexo, idade:int) -> None:
        self.id = id
        self.nome = nome
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
        self.idade = idade

    def __str__(self) -> str:
        return(
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nSalário: {self.salario}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
            f"\nIdade: {self.idade}"
        )

funcionario1 = Funcionario("57432", "Murilo", 2344, Setor.FINANCEIRO, Sexo.MASCULINO, 20
)
print(funcionario1)