nome = "Rafael"
idade = 34
profissao = "programador"
linguagem = "Python"

print(f"Eu me chamo {nome}, tenho {idade} anos, gostaria muito de trabalhar como {profissao} atualmente estou estudando na D.I.O a linguagem {linguagem}")
print("Eu me chamo %s, tenho %d anos, gostaria muito de trabalhar como %s atualmente estou estudando na D.I.O a linguagem %s " % (nome, idade, profissao, linguagem))
print("Eu me chamo {}, tenho {} anos, gostaria muito de trabalhar como {} atualmente estou estudando na D.I.O a linguagem {}".format(nome, idade, profissao, linguagem))
print("Eu me chamo {3}, tenho {2} anos, gostaria muito de trabalhar como {1} atualmente estou estudando na D.I.O a linguagem {0}".format(linguagem, profissao, idade, nome))
print("Eu me chamo {nome}, tenho {idade} anos, gostaria muito de trabalhar como {profissao} atualmente estou estudando na D.I.O a linguagem {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

dados = {"nome": "Rafael", "idade": 34, "profissao": "Programador", "linguagem": "Python"}
print("Eu me chamo {nome}, tenho {idade} anos, gostaria muito de trabalhar como {profissao} atualmente estou estudando na D.I.O a linguagem {linguagem}".format(**dados))