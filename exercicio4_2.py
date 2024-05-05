# 4. Uma palavra é dita palíndrome quando pode ser lida nos 2 sentidos. Elabore um programa que leia
# uma palavra e informe se ela é ou não palíndrome.

palavra = input("PAlavra: ").upper()

inverso = ""

for letra in palavra:
    inverso = letra + inverso
    
if palavra == inverso:
    print(f"{palavra} é uma palíndrome")
else:
    print(f"Erro. Esta palavra não é uma palíndrome")