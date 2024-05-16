## Inicio da classe conta
class Cliente:
    def __init__(self, nome) -> None:
        self.conta = None
        self.nome = nome

    def cadastraConta(self):
        self.conta = Conta()
        print(f"Conta do cliente {self.nome} cadastrada!")

    def imprimeExtratoConta(self):
        self.conta.imprimirExtrato(self.nome)
    
    def sacar(self):
        self.conta.sacar()
    
    def depositar(self):
        self.conta.depositar()

class Conta:
    def __init__(self) -> None:
        self.saldo = float(0.0)
        self.extrato = str("")
        self.LIMITE_SAQUES = int(3)
        self.numero_saques = int(0)

    def sacar(self):
        valor = float(input("Informe o valor do saque: "))
        if( self.numero_saques < self.LIMITE_SAQUES and valor <=  self.saldo and valor <= 500):
            self.numero_saques += 1
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Operação realizada com sucesso.")
        elif(valor > self.saldo):
            print("Operação falhou! Você não possui saldo suficiente.")
        elif( self.numero_saques >= self.LIMITE_SAQUES):
            print(f"Operação falhou! Você atingiu o limite de {self.LIMITE_SAQUES} diários.")
        elif(valor > 500):
            print(f"Operação falhou! O valor máximo por saque é de R$ 500.00.")
        else:
            print(f"Operação falhou! O valor informado é inválido.")
    
    def depositar(self):
        valor = float(input("Informe o valor do depósito: "))
        if(valor > 0):
             self.saldo += valor
             self.extrato += f"Depósito: R$ {valor:.2f}\n"
             print(f"Operação realizada com sucesso.")
    
    def imprimirExtrato(self, nomeCliente):
        print("\n================ EXTRATO ================")
        print(f"Cliente: {nomeCliente}\n")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
## Fim da classe        


menu = """

[C] Cadastrar Cliente
[O] Registrar Conta
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

#Insctanciando classe conta
cliente = None

while True:
    opcao = input(menu)
    if opcao.upper() == "C":
        if(cliente == None):
            nome = input("Nome do cliente: ")
            cliente = Cliente(nome)
        else:
            print("Cliente já cadastrado!")
    elif opcao.upper() == "O":
        if(cliente == None):
            print("Cliente sem cadastrado!")
        else:
            cliente.cadastraConta()
    elif opcao.upper() == "D":
        if(cliente == None):
            print("Cliente sem cadastrado!")
        elif(cliente.conta == None ):
            print("Cliente sem conta cadastrada!")
        else:
            cliente.depositar()       
    elif opcao.upper() == "S":
        if(cliente == None):
            print("Cliente sem cadastrado!")
        elif(cliente.conta == None ):
            print("Cliente sem conta cadastrada!")
        else:
            cliente.sacar()
    elif opcao.upper() == "E":
        if(cliente == None):
            print("Cliente sem cadastrado!")
        elif(cliente.conta == None ):
            print("Cliente sem conta cadastrada!")
        else:
            cliente.imprimeExtratoConta()
    elif opcao.upper() == "Q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
