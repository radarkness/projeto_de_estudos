def sacar(valor_saque):
    conta_normal = True
    conta_universitaria = False

saldo = 5000
cheque_especial = 2000

valor = int(input("Qual o valor do sacar? "))
if saldo >= valor:
    print("Saque realizado com Sucesso no valor de R$", valor, "Reais, restando valor total de R$", 
          saldo -  valor, "Reais, mais cheque especial limite de R$", cheque_especial, "Reais")
elif valor <= (saldo + cheque_especial):
    print("Saque realizado com sucesso com cheque especial no valor de R$", valor, 
          "Reais, restando um valor total de R$", (saldo + cheque_especial) - valor)
else:
    print("Saque Nâo Realizado, limite disponível é R$", saldo, "Reais + Cheque especial de R$", 
          cheque_especial, "Reais, totalizado R$", saldo + cheque_especial, "Reais")

valor_para_sacar = ()
sacar(valor_para_sacar)