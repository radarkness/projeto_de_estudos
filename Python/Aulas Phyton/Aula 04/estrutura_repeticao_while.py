opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n: ")) 

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por utilizar o nosso sistema bancário, tenha um bom dia.")