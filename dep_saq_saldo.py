## Inicio da classe conta
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
    
    def imprimirExtrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
## Fim da classe        


menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

#Insctanciando classe conta
contaCorrente = Conta()

while True:
    opcao = input(menu)
    if opcao.upper() == "D":
        contaCorrente.depositar()
    elif opcao.upper() == "S":
        contaCorrente.sacar()
    elif opcao.upper() == "E":
        contaCorrente.imprimirExtrato()
    elif opcao.upper() == "Q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")