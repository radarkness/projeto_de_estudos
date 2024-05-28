def sacar(valor_saque):
    saldo = 5000
    valor = int(input("Digite um valor de saque! "))    
    if saldo >= valor:
        print("Você sacou R$", valor, "Reais, saldo disponível R$", saldo - valor,"Reais")
        print("Obrigado por utilizar nosso sistema, tenha um dia")
    else:
        print("Limite Indisponível, seu limite atual é R$", saldo,"Reais")
        print("Vamos tentar outra vez?")
    print("tenha um Bom dia")
    

valor_para_sacar = ()
sacar(valor_para_sacar)