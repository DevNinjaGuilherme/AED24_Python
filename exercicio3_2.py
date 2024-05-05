# 3. Elaborar um programa que leia uma palavra. Exiba a letra inicial (e suas ocorrências) e "_" nas demais
# posições, conforme o exemplo.
# Palavra: Abacaxi
# Descubra: A _ A _ A _ _


palavra = input("Digite uma palavra: ")
letraInicial = palavra[0].upper()
palavraFinal = letraInicial + " "
for i in range(1, len(palavra)):
    if palavra[i].upper() == letraInicial:
        palavraFinal += palavra[i] + " "
    else:
        palavraFinal += "_ "
print(palavraFinal)

##Na parte de print(abc[3]) por exemplo imprime Pel de Pelotas mas ele imprime o caracter da posicao 0 até o caracter da posicao 3. Menos ele mesmo entao ao invés de Pelo fica Pel. porque anula o "O".