"""
# Exemplo 1
class pessoa:
    Nome = input("Digite Seu nome ")
    Idade = input("Qual sua Idade? ")
    Peso = input("Quanto você pesa? ")

pessoa = pessoa()
print(f"Nome: {pessoa.Nome}") 
print(f"Idade: {pessoa.Idade}") 
print(f"Peso: {pessoa.Peso}")

# Exemplo 2
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

print("A soma é: ", (a+b))
print("A subtração é: ", (a-b))
print("A multiplicação é: ", (a*b))
print("A Divisão é: ", (a/b))
print("O resto da divisão é: ", (a%b))
print("A potencia é: ", (a**b))


# Exemplo 3
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
        
media = (a + b) /2 

if media <= 7:
    print("Parabéns, você está Reprovado Vagabundo")
else: 
    print("Parabéns, você passou de ano") 

print("Sua Média Final é:", media)


# Exemplo 4
import math

Num = float(input("Digite um Numero: "))
resultado = math.sqrt(Num)

print("A Raíz quadrada é:", resultado)


# Exemplo 5
import math

raio = float(input("Digite um raio circunferência em cm: "))
comprimento = 2 * math.pi * raio
area = math.pi * raio * raio
print("O Comprimento da circunferência é igual a %.2f cm" % (comprimento))
print("A área da circunferência é igual a %.2f cm²" % (area))  

"""

# Exemplo 6
import math

sombra = float(input("Digite o comprimento da sobra em m: "))
angulo = math.radians(float(input("Digite o ângulo em graus: ")))
altura = math.tan(angulo) * sombra

print("A Altura do Prédio é de %.2f m" %(altura))