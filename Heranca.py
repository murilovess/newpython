from abc import ABC, abstractclassmethod
import os
os.system("cls || clear")

class Funcionario(ABC): 
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario


    @abstractclassmethod
    def salario_final

    def __str__(self) -> str:
    return(
    f"\nNome: {self.nome}"
    f"\nSalario: {self.salario}"
    f"\nSa"
        )


class Motoboy(Funcionario):
    def sal

motoboy_1 = Motoboy("Álvaro", 1000,)

print(motoboy_1)
    