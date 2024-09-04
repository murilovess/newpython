import os

os.system("cls || clear")

class Conta_bancaria: 
    def __init__(self, banco: str, agencia: str, numero: str, tipo: str, saldo: str, limite: str) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo
        self.limite = limite

    def __str__(self) -> str:
        return(
        f"Banco: {self.banco}"
        f"\nAgência: {self.agencia}"
        f"\nNumero: {self.numero}"
        f"\nTipo: {self.tipo}"
        f"\nSaldo: {self.saldo}"
        f"\nLimite: {self.limite}")

    def exibir_dados(self) -> str:
        return (
        f"Banco: {self.banco}"
        f"\nAgência: {self.agencia}"
        f"\nNumero: {self.numero}"
        f"\nTipo: {self.tipo}"
        f"\nSaldo: {self.saldo}"
        f"\nLimite: {self.limite}")



class Funcionario:
    def __init__(self, codigo_funcionario: str, nome: str, endereco: str, telefone: str, email: str, conta_bancaria: Conta_bancaria ) -> None:
        self.codigo_funcionario = codigo_funcionario
        self.nome = nome 
        self.endereco = endereco
        self.telefone = telefone 
        self.email = email 
        self.conta_bancaria = conta_bancaria      

    def __str__(self) -> str:
        return(
        f"codigo do funcionário: {self.codigo_funcionario}"
        f"\nNome: {self.nome}"
        f"\nEndereço: {self.endereco}"
        f"\nTelefone: {self.telefone}"
        f"\nEmail: {self.email}"
        f"\nConta Bancária: {self.conta_bancaria}")

    def exibir_dados(self) -> str:
        return(
        f"codigo do funcionário: {self.codigo_funcionario}"
        f"\nNome: {self.nome}"
        f"\nEndereço: {self.endereco}"
        f"\nTelefone: {self.telefone}"
        f"\nEmail: {self.email}"
        f"\nConta Bancária: {self.conta_bancaria}")




conta_bancaria = Conta_bancaria("Santander", "001", "786940221", "corrente", "1400", "3000")
funcionario  = Funcionario("008", "Márcio", "ondina", "71 98734272", "marcinho@gmail.com", conta_bancaria)


print(conta_bancaria.exibir_dados())
print(funcionario.exibir_dados())