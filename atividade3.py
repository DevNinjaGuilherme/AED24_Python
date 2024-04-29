# 3. Elaborar um programa que leia o nome de um produto e o número de etiquetas a serem
# impressas desse produto. Exiba as etiquetas com o nome do produto, com no máximo 2 etiquetas
# por linha, conforme exemplo de execução do programa, demonstrado a seguir.


nomeProduto = input("Nome do Produto: ")
nEtiquetas = int(input("Nº de Etiquetas: "))

print(f"Nº de Etiquetas: ", nEtiquetas)

for i in range(1, nEtiquetas+1):
    print(f"{nomeProduto:15s}", end=" ")
    if i % 2 == 0:
        print()