from enum import Enum
import os
os.system("cls || clear")


class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta:int, agencia:int,) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 69 # Atributo protegido
    
    #semelhante ao GetSaldo()
    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor) -> str:
        try:
            self.__vereificar_sacar(valor) 
        except SaldoInsuficienteError as erro:
            return f"Erro: {erro}"

      
        return f"Saque Realizado com sucesso!"

    def __vereificar_sacar(self, valor) -> None:
          if valor > self._saldo:
              raise SaldoInsuficienteError("Saldo Insuficiente.")
            
          self._saldo -= valor
            
    def depositar(self, valor): 
        self._saldo += valor
        return self._saldo


class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

conta_corrente = ContaCorrente(222,333)
conta_corrente.sacar(100)
#print(f"Saldo da conta: {conta_corrente._saldo}")

print(f"NUmero da conta: {conta_corrente.numero_conta}")
print(f"Saldo da conta: {conta_corrente.saldo}")
valor_saque = float(input("Qual valor deseja sacar? "))
print(f"Saque: {conta_corrente.sacar(valor_saque)}")

