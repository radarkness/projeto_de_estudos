
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você está qualificado para tirar sua habilitação.")
else:
    print("Você ainda não atingiu a idade para tirar sua habilitação.")

if idade >= 18:
    print("Você está qualificado para tirar sua habilitação.")
elif idade == 17:
    print("Você fazer as aulas teóricas, mais não pode fazer as aulas práticas.")
else:
    print("Você ainda não atingiu a idade para tirar sua habilitação.")