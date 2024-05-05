# 2. Elaborar um programa que leia o nome completo de um aluno. Valide o nome para que seja composto.
# Exiba apenas o primeiro nome do aluno em letras maiúsculas. 

nome = input("Digite seu nome completo: ")

while nome.find(" ") == -1:
    print("Ops... Por favor, digite o nome completo")
    nome = input("Digite seu nome completo: ")

partes = nome.split(" ")
print("Nome no Crachá: ", partes[0].upper())
