#O programa permite incluir, listar, listar em ordem alfabética e excluir compras. O programa é finalizado quando o usuário escolhe a opção 5. O programa é salvo no arquivo compras.txt e seu conteúdo pode ser retomado posteriormente.

import os

compras = []
precos = []

def titulo(texto, sublinhado="="):
    print()
    print(texto)
    print(sublinhado*40)

def incluir():
    titulo("Inclusão de Compra", "-")
    
    compra = input("Descrição da Compra: ")
    preco = float(input("Valor Previsto R$..: "))
    
    compras.append(compra)
    precos.append(preco)
    print("Ok. Compra Cadastrada com Sucesso!")
    
def listar():
    titulo("Compras Cadastradas", "-")
    
    print("Descrição da Compra..........: R$ Previsto:")
    print("-"*43)
    
    for compra, preco in zip(compras, precos):
        print(f"{compra:30s} {preco:12.2f}")
    print(f"O Total das Compras é: {total}.")
    print("-"*43)

def listar_ordem():
    titulo("Compras Cadastradas em Ordem", "-")
    
    print("Descrição da Compra..........: R$ Previsto:")
    print("-"*43)
    for compra, preco in sorted(zip(compras, precos)):
        
        print(f"{compra:30s} {preco:12.2f}")
    print(f"O Total das Compras é: {total}.")
    print("-"*43)
    
def excluir():
    titulo("Exclusão de Compra", "-",)
    descricao = input("Digite a descrição da compra a ser excluída: ").lower()
    descricao_lower = [desc.lower() for desc in compras]
    if descricao in descricao_lower:
        posicao = descricao_lower.index(descricao)
        compras.pop(posicao)
        precos.pop(posicao)
    else:
        print("Compra não encontrada.")

def grava_compras():
    with open("compras.txt", "w") as arq:
        for compra, preco in zip(compras, precos):
            arq.write(f"{compra};{preco}\n")

def le_compras():
    if not os.path.isfile("compras.txt"):
        return
    
    with open("compras.txt", "r") as arq:
        dados = arq.readlines()
        
        for linha in dados:
            partes = linha.split(";")
            compras.append(partes[0])
            precos.append(float(partes[1]))

# ------------------------------ Programa Principal

le_compras()
while True:
    total = sum(precos)
    titulo("Lista de Compras da Semana")
    print("1. Incluir Compra")
    print("2. Listar Compras")
    print("3. Listar Compras em Ordem")
    print("4. Excluir Compra")
    print("5. Finalizar")
    print("\n")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        listar_ordem()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        grava_compras()
        break