# 4. Digamos que o número de chinchilas de uma fazenda triplica a cada ano, após o primeiro ano.
# Elaborar um programa que leia o número inicial de chinchilas e anos e informe ano a ano o número
# médio previsto de chinchilas da fazenda. O número inicial de chinchilas deve ser maior ou igual a 2
# (um casal). 


numChinchilas = int(input("Nº de Chinchilas: "))

numAnos = int(input("Nº de Anos de Criação: "))

total = numChinchilas

if numChinchilas < 2:
    print("Deve iniciar com, no mínimo, 2 chinchilas")
else:
  for i in range(1, numAnos+1):
    print(f"{i}º ano: {total}")
    total = total * 3