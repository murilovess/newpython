#biblioteca enum.
from enum import Enum 

import os
os.system("cls || clear")

class Sexo(Enum):
    MASCULNO = "Masculino"
    FEMININO = "Mulé"


#aplicação.
print(f"Sexo {Sexo.FEMININO}")
#Maiusculo.
print(f"Sexo: {Sexo.FEMININO.name}")
#valor atribuido.
print(f"Sexo: {Sexo.FEMININO.value}")
