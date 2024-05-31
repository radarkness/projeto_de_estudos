from datetime import date

class ContaBancaria:
    def __init__(self, titular, saldo=950):
        self.titular = titular
        self.saldo = saldo
        self.extratos = []
        self.saques_diarios = 0
        self.ultimo_saque_data = None
        self.limite_saques = 3
        self.limite_valor_saque = 500

    def atualizar_limite_saques(self):
        if self.ultimo_saque_data != date.today():
            self.saques_diarios = 0
            self.ultimo_saque_data = date.today()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extratos.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        self.atualizar_limite_saques()
        if self.saques_diarios >= self.limite_saques:
            print("Limite de saques diários atingido!")
        elif valor > self.limite_valor_saque:
            print(f"Valor do saque excede o limite de R${self.limite_valor_saque:.2f} por saque!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor <= 0:
            print("Valor de saque inválido!")
        else:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extratos.append(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def ver_extratos(self):
        print(f"Extratos da conta de {self.titular}:")
        if not self.extratos:
            print("Não há movimentações na conta.")
        else:
            for extrato in self.extratos:
                print(extrato)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.saques_diarios}/{self.limite_saques}")

def menu():
    conta = ContaBancaria(titular=input("Digite o nome do titular da conta: "))

    while True:
        print(f"\nBom dia, {conta.titular} escolha uma operação:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver extratos")
        print("4. Sair")
        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.ver_extratos()
        elif opcao == '4':
            print("Encerrando o sistema bancário. Obrigado por usar nossos serviços!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    menu()
