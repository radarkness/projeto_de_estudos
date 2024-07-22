

texto = input("Digite um nome qualquer: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um literável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print("Executa no final do laço")


# Exemplo utilizando a  função built-in range
for numero in range(0, 91, 9):
    print(numero, end=" ")