# AND = para ser True, tuda condição precisa ser True
# OR = Para ser True, apenas uma condição precisa ser True

#print(True and True)
#print(True and False)
#print(False and False)
#print(True or True)
#print(True or False)
#print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True


exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)