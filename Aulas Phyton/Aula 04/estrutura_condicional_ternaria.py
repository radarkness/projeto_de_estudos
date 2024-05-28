saldo = 2000
saque = 200

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar saque!")