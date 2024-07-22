#while True:
#    opcao = int(input("Informe um número: ")) 

#    if opcao == 10:
#        print("Fim da execução")
#        break
        
for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")